# Importing files + workspaces
import pytz
from datetime import datetime as dtdt
from hubspace import Hubspace
import constants

# Logging into hubspace
hubspace = Hubspace(constants.login.username, constants.login.password)

# Collects the device names and IDs and puts them into an array.
my_devices = {}
devices = hubspace.getDevices()
for device in devices:
  my_devices[device.getName()] = hubspace.getDevice(device.getID())

# Removes first device and its ID because it is not a valid device.
del my_devices[""]

light1 = hubspace.getDevice("8abd5443b23562ea")
"""
Many of the inputs will be changed when I make an interface.

Note: Hubspace does not like single-character inputs!  If you have one character, put a 0 before it.

Jax Light 1 ID: 8abd5443b23562ea
Jax Light 2 ID: 80fa5443b237b9de

Action 1 is On/Off.  Values are "00"(off) and "01"(on)

Action 2 is Brightness.  Note: Lowest is 1%

Action 3 is Warmth.  IDK how it scales yet.  I only have specific temperature values.
  AC0D = 3500 K
  AC0C = 3244 K
  6419 = 6500 K
  9808 = 2200 K

Action 4 is Color.  Use strings such as "FFFFFF"

Action 5 switches between white, RGB, and preset modes.  Vales are "00" (white), "01" (RGB), "02" (presets)

Action 6 is unknown.  Didn't let me change it.

Action 11 is ???

Action 100 is ???

Action 200 is ???

Action 300 is ???

Action 400 is brightness for mode 2 (unneccessary)

Action 65004 is wifi signal name
"""
"""
Turns the lights on or off.
Inputs: True or False
ID: 1
"""


def state(value, name=""):
  if name == "":
    for x in my_devices:
      my_devices[x].writeAction(1, "01") if value else my_devices[x].writeAction(1, "00")

  else:
    my_devices[name].writeAction(
      1, "01") if value else my_devices[name].writeAction(1, "00")


"""
Changes the brightness of the lights.
Inputs: 1 to 100 (0 defaults to 1.  If you want the lights off, run state(False))
ID: 2
"""


def brightness(value, name=""):
  value = hex(value)[2:]
  if len(value) == 1:
    value = "0" + value

  if name == "":
    for x in my_devices:
      my_devices[x].writeAction(2, value)

  else:
    my_devices[name].writeAction(2, value)


"""
Changes the warmth of the light.  If it is any color other than white, it changes the color to white.
Input: Unknown scaling, but I have some set values.  They are as follows.
  AC0D = 3500 K = 44045
  AC0C = 3244 K
  6419 = 6500 K
  9808 = 2200 K
ID: 3
"""


def warmth(value, name=""):
  if name == "":
    for x in my_devices:
      my_devices[x].writeAction(3, value)

  else:
    my_devices[name].writeAction(3, value)


"""
Changes the color of the lights.
Input: The 6 colors of the rainbow or a hex code.
ID: 4
"""


def color(value, name=""):
  colors = {
    "red": "FF0000",
    "orange": "FF7E00",
    "yellow": "FFFF00",
    "green": "00FF00",
    "blue": "0000FF",
    "purple": "FF00FF",
    "white": "FFFFFF"
  }

  if name == "":
    if value.lower() in colors:
      for x in my_devices:
        my_devices[x].writeAction(4, colors[value])

    else:
      for x in my_devices:
        my_devices[x].writeAction(4, value)

  else:
    my_devices[name].writeAction(
      4, colors[value]) if value in colors else my_devices[name].writeAction(
        4, value)