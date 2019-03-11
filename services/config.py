import json

global ascomConfig
ascomConfig = None

def initConfig():
    global ascomConfig

    with open('config.json') as json_data_file:
        ascomConfig = json.load(json_data_file)

    pass

def getConfig(device_type, device_number):
    global ascomConfig

    for config in ascomConfig['drivers']:
        if (config['device_type'] == device_type) and (config['device_number'] == int(device_number)):
            return config

    return None

def getDriverInstance(device_type, device_number):
    config = getConfig(device_type, device_number)
    if not(config is None):
        return config['driver_instance']
    else:
        raise ValueError("No configuration found for device_type '%s' #%s" % (device_type, device_number))