import keyboard

# Define a list to store the recorded keys
#recorded_keys = []
prompt = ""

# Print a message to let the user know the script is running
print("Recording keyboard input. Press '*' to stop.")

# Define a callback function to handle key presses
def on_press(key):
  global prompt
  # Record the key pressed
  keyRefined = str(key)
  keyRefined = keyRefined[14:15]
  if keyboard.is_pressed(' '):
    keyRefined = " "
  prompt += keyRefined
  #recorded_keys.append(key)

# Start listening for key presses
keyboard.on_press(on_press)

# Wait until the "*" key is pressed
while not keyboard.is_pressed("*"):
  pass
# Print a message to let the user know the script has stopped recording
print(prompt[:-1])
print("Keyboard input recording stopped.")
