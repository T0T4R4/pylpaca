import logging

from .DeviceInterfaces.IAscomDriver import IAscomDriver


class MyDeviceDriver(IAscomDriver):

    FORMAT = '%(asctime)-15s %(identifier)s %(message)s'
    logging.basicConfig(format=FORMAT)
    logger = logging.getLogger('MyASCOMDriver')

    def __init__(self, name, description):
        self.__connectedState = False
        self.__name = name
        self.__description = description
        self.__supportedActions = []

    #
    # IAscomDriver
    #

    @property
    def IsConnected(self):
        #  TODO check that the driver hardware connection exists and is connected to the hardware
        return self.__connectedState

    def CheckConnected(self, message):
        # Use this function to throw an exception if we aren't connected to the hardware
        if (not self.IsConnected):
            raise ValueError("Not Connected : %s" % message)
        pass

    @property
    def Connected(self):
        return self.IsConnected

    @Connected.setter
    def Connected(self, value):
        if (value == self.IsConnected):
            return

        if (value == True):
            self.__connectedState = True
            MyDeviceDriver.logger.info("Connecting to device %s" % self.__name)
            # TODO connect to the device
        else:
            self.__connectedState = False
            MyDeviceDriver.logger.info(
                "Disconnecting from device %s" % self.__name)
            # TODO disconnect from the device

        pass

    @property
    def Description(self):
            # TODO customise this device description
        return self.__description

    @property
    def Name(self):
        self.__name = "Short driver name - please customise"
        return self.__name

    #
    # IDeviceControl
    #

    def Action(self, actionName, actionParameters):
        raise NotImplementedError(
            "Action %s is not implemented by this driver" % actionName)

    @property
    def SupportedActions(self):
        return self.__supportedActions

    def CommandBlind(self, command, raw=False):
        self.CheckConnected("CommandBlind")
        # Call CommandString and return as soon as it finishes
        self.CommandString(command, raw)
        # or
        raise NotImplementedError("CommandBlind")
        # DO NOT have both these sections!  One or the other

    def CommandBool(self, command, raw=False):
        self.CheckConnected("CommandBool")
        ret = self.CommandString(command, raw)
        # TODO decode the return string and return true or false
        # or
        raise NotImplementedError("CommandBool")
        # DO NOT have both these sections!  One or the other

    def CommandString(self, command, raw=False):
        self.CheckConnected("CommandString")
        # it's a good idea to put all the low level communication with the device here,
        # then all communication calls this function
        # you need something to ensure that only one command is in progress at a time

        raise NotImplementedError("CommandString")

        return "the expected return value"


if __name__ == "__main__":
    d = MyDeviceDriver("Test name", "Test description")
    print(d.Connected)
    d.Connected = True
    print(d.Connected)
    pass
