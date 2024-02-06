from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Get default audio device
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
   IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Control the volume
currentVolumeDb = volume.GetMasterVolumeLevel()
print(currentVolumeDb)

# set volume
volume.SetMasterVolumeLevel(250.0, None) # -20.0 dB
