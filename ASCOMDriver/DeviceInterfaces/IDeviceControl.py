import abc


class IDeviceControl(abc.ABC):
    """This interface is intended for use in any current or future device type and to avoid name clashes, management of action names is important from day  1. 
      Ref: https://github.com/ASCOMInitiative/ASCOMPlatform/blob/master/ASCOM.DeviceInterface/IDeviceControl.vb
    """

    @abc.abstractmethod
    def Action(self, actionName, actionParameters):
      # Invokes the specified device-specific action.
        pass

    @abc.abstractproperty
    def SupportedActions(self):
      # Gets the supported actions.
        pass

    @abc.abstractmethod
    def CommandBlind(self, command, raw=False):
      # Transmits an arbitrary string to the device and does not wait for a response.
        pass

    @abc.abstractmethod
    def CommandBool(self, command, raw=False):
      # Transmits an arbitrary string to the device and does not wait for a response.
        pass

    @abc.abstractmethod
    def CommandString(self, command, raw=False):
      # Transmits an arbitrary string to the device and does not wait for a response.
        pass
