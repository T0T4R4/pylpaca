import tornado
import pyrestful
import services
import json
import sys

from services.dome_service import DomeService

Services = []


def loadConfig():
    global ascomConfig

    with open('config.json') as json_data_file:
        ascomConfig = json.load(json_data_file)

    pass


def instanciateDriver(config):

    if config['instance'] is None:
        driver = None

        if (config['device_type'] == 'dome'):
            # TODO  dynamically instanciate the drivers
            if (config['device_driver'] == 'MyASCOMDomeDriver'):
                from ASCOMDriver.MyDomeDriver import MyDomeDriver
                driver = MyDomeDriver()  # TODO pass driver_config as well ?

        config['instance'] = driver

    pass


def instanciateRestHandler(config):

    if (config['device_type'] == 'dome'):
        return DomeService

    return None


def getRestHandlers():
    # instanciate all necessary services defined in the config file
    global ascomConfig

    handlers = []
    for config in ascomConfig['drivers']:

        instanciateDriver(config)

        handler = instanciateRestHandler(config)

        if (not(handler is None)):
            handlers.append(handler)

    return handlers


if __name__ == '__main__':
    try:
        loadConfig()
        handlers = getRestHandlers()
        print("Start the service")
        app = pyrestful.rest.RestService(handlers)
        http_server = tornado.httpserver.HTTPServer(app)
        http_server.listen(8080)
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        print("\nStop the service")
