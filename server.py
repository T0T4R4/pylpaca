import tornado
import pyrestful
import services
import sys

from services.dome_service import DomeService
from services.config import ascomConfig, initConfig, getConfig

Services = []

def instanciateDriver(config):

    if not('driver_instance' in config):
        config['driver_instance'] = None
    
    driver = config['driver_instance']
    if (driver is None):
        if (config['device_type'] == 'dome'):
            # TODO  dynamically instanciate the drivers
        
            if (config['device_driver'] == 'MyASCOMDomeDriver'):
                from ASCOMDriver.MyDomeDriver import MyDomeDriver
                driver = MyDomeDriver()  # TODO pass driver_config as well ?

            config['driver_instance'] = driver

    return driver


def instanciateRestHandler(config):

    if (config['device_type'] == 'dome'):
        return DomeService

    return None


def getRestHandlers():
    # instanciate all necessary services defined in the config file
    
    handlers = []
    for config in services.config.ascomConfig['drivers']:

        instanciateDriver(config)

        handler = instanciateRestHandler(config)

        if (not(handler is None)):
            handlers.append(handler)

    return handlers


if __name__ == '__main__':
    try:
        
        initConfig()

        handlers = getRestHandlers()
        print("Start the service")
        app = pyrestful.rest.RestService(handlers)
        http_server = tornado.httpserver.HTTPServer(app)
        http_server.listen(11111)
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        print("\nStop the service")
