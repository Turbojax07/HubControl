# Importing files + workspaces
import constants
import functions
from hubspace import Hubspace

# Logging into hubspace
hubspace = Hubspace(constants.login.username, constants.login.password)

# Collects the device names and IDs and puts them into an array.
my_devices = {}
devices = hubspace.getDevices()
print(hubspace.getDevices()[0].getAttributes())
for device in devices:
  my_devices[device.getName()] = hubspace.getDevice(device.getID())

# Removes first device and its ID because it is not a valid device.
del my_devices[""]

print("Welcome to Jackson's Hubspace Lighting!")

while (True):
  command = input(constants.prompts.init)
  print(hubspace.getDevices()[0].getAttributes())
  """
  if command == "1":
    value = input(constants.prompts.state)
    functions.state(value, my_devices)

  elif command == "2":
    value = input(constants.prompts.brightness)
    functions.brightness(value, my_devices)

  elif command == "3":
    value = input(constants.prompts.color)
    functions.color(value, my_devices)

  elif command == "4":
    value = input(constants.prompts.warmth)

    try:
      functions.warmth(constants.values[value], my_devices)

    except:
      functions.error()

  elif command == "exit":
    print("Goodbye!")
    exit(0)

  else:
    functions.error
  """