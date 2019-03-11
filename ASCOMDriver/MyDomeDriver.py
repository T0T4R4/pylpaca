from .DeviceInterfaces.IDomeV2 import IDomeV2
from .DeviceInterfaces.Enumerations import ShutterState
from .MyDeviceDriver import MyDeviceDriver


class MyDomeDriver(MyDeviceDriver, IDomeV2):
    """This is an example of how a driver could be implemented
    Ref: https://github.com/ASCOMInitiative/ASCOMPlatform/blob/master/DriverTemplates/TemplateSources/src/ASCOM%20Driver%20Template%20(CS)/DeviceDome.cs
    """

    def __init__(self):
        super().__init__("MyASCOMDomeDriver", "My driver description")

        self.__shutterstatus = ShutterState.shutterClosed
        pass

    #
    # IDomeV2
    #

    def CloseShutter(self):
        # Close shutter or otherwise shield telescope from the sky.

        self.__shutterstatus = ShutterState.shutterClosed  # TODO: Implement logic instead

        MyDeviceDriver.logger.info("Shutter is now closed")
        pass

    def OpenShutter(self):
        # Open shutter or otherwise expose telescope to the sky.

        self.__shutterstatus = ShutterState.shutterOpen  # TODO: Implement logic instead

        MyDeviceDriver.logger.info("Shutter is now open")
        pass

    @property
    def ShutterStatus(self):
        # Indicates whether the dome is in the home position. Raises an error if not supported.
        return self.__shutterstatus


if __name__ == "__main__":
    driver = MyDomeDriver()

    print("Initial status: %s" % driver.ShutterStatus)

    driver.OpenShutter()
    print(driver.ShutterStatus)

    driver.CloseShutter()
    print(driver.ShutterStatus)

    pass
