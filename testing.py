import keyboard

# Define a list to store the recorded keys
recorded_keys = []

# Print a message to let the user know the script is running
print("Recording keyboard input. Press '*' to stop.")

# Define a callback function to handle key presses
def on_press(key):
  # Record the key pressed
  recorded_keys.append(key)

# Start listening for key presses
keyboard.on_press(on_press)

# Wait until the "*" key is pressed
while not keyboard.is_pressed("*"):
  pass

# Join the recorded keys into a single string
recorded_keys_str = "".join(str(key) for key in recorded_keys)

# Print the recorded keys string
print(f"Recorded keys: {recorded_keys_str}")

# Save the recorded keys string to a file called "pressed_string"
with open("pressed_string", "w") as file:
  file.write(recorded_keys_str)

# Print a message to let the user know the script has stopped recording
print("Keyboard input recording stopped.")
