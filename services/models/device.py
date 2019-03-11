import sys

# TODO ASCOMDriver should be in its proper package ?
from ASCOMDriver import *
sys.path.append("C:/ExtendedPartition/_Dev/pylpaca/ASCOMDriver")


class Device(object):

    def __init__(self, device_type, device_number, device_driver, driver_config):
        self.__device_type = device_type
        self.__device_number = device_number
        self.__driver = self._instanciateAscomDriver(
            device_driver, driver_config)

    def _instanciateAscomDriver(self,  device_driver, driver_config):
        driver = None

        if (self.__device_type == 'dome'):
            # TODO Ideally the available drivers would be registered on the system,
            # and we should perform a name lookup in that registry and dynamically instanciate it.
            #
            if (device_driver == 'MyASCOMDomeDriver'):
                # TODO the custom driver should be loaded dynamically, not hardcoded
                from ASCOMDriver.MyDomeDriver import MyDomeDriver
                driver = MyDomeDriver()  # Pass driver_config if required

        return driver

    @property
    def device_type(self):
        return self.__device_type

    @property
    def device_number(self):
        return self.__device_number

    @property
    def connected(self):
        if (self.__driver is None):
            return False

        return self.__driver.Connected

    # @connected.setter
    # def connected(self):
    #    return self.__connected
