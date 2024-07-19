import constants

# Turns the lights on or off.
def state(value, my_devices):
  if "on" in value.lower() or "true" in value.lower():
    for x in my_devices:
      my_devices[x].writeAction(1, "01")

  if "off" in value.lower() or "false" in value.lower():
    for x in my_devices:
      my_devices[x].writeAction(1, "00")


# Changes the brightness of the lights.
def brightness(value, my_devices):
  value = hex(value)[2:]
  if len(value) == 1:
    value = "0" + value

  try:
    my_devices[constants.lights.light1].writeAction(2, value)

  except:
    print("Error.  " + value + " did not work.  Consult Jackson for help.")


# Changes the warmth of the light
def warmth(value, my_devices):
  try:
    my_devices[constants.lights.light1].writeAction(3, value)

  except:
    print("Error.  " + value + " did not work.  Consult Jackson for help.")


# Changes the color of the lights.
def color(value, my_devices):
  if "#" in value:
    value = value[1:]

  colors = {
    "red": "FF0000",
    "orange": "FF7E00",
    "yellow": "FFFF00",
    "green": "00FF00",
    "blue": "0000FF",
    "purple": "FF00FF",
    "white": "FFFFFF"
  }

  try:
    if value in colors:
      my_devices[constants.lights.light1].writeAction(4, colors[value])

    else:
      my_devices[constants.lights.light1].writeAction(4, value)

  except:
    print("Error.  " + value + " did not work.  Consult Jackson for help.")


def error():
  print("Please enter a valid input!")
