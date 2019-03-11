# ASCOM.Interface Telescope Enumerations
# ref: https://github.com/ASCOMInitiative/ASCOMPlatform/blob/master/ASCOM.DeviceInterface/Enumerations.vb

from enum import Enum, IntEnum


class AlignmentModes(IntEnum):
    algAltAz = 0
    algPolar = 1
    algGermanPolar = 2


class DriveRates(IntEnum):
    driveSidereal = 0
    driveLunar = 1
    driveSolar = 2
    driveKing = 3


class EquatorialCoordinateType(IntEnum):
    equOther = 0
    equTopocentric = 1
    equJ2000 = 2
    equJ2050 = 3
    equB1950 = 4


class GuideDirections(IntEnum):
    guideNorth = 0
    guideSouth = 1
    guideEast = 2
    guideWest = 3


class TelescopeAxes (IntEnum):
    axisPrimary = 0
    axisSecondary = 1
    axisTertiary = 2


class PierSide(IntEnum):
    pierEast = 0
    pierUnknown = -1
    pierWest = 1


class ShutterState (IntEnum):
    shutterOpen = 0
    shutterClosed = 1
    shutterOpening = 2
    shutterClosing = 3
    shutterError = 4


class CameraStates (IntEnum):
    cameraIdle = 0
    cameraWaiting = 1
    cameraExposing = 2
    cameraReading = 3
    cameraDownload = 4
    cameraError = 5


class SensorType(IntEnum):
    Monochrome = 0
    Color = 1
    RGGB = 2
    CMYG = 3
    CMYG2 = 4
    LRGB = 5
