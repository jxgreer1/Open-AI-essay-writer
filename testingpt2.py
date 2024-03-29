import keyboard

# Define a list to store the recorded keys
recorded_keys = []

# Print a message to let the user know the script is running
print("Recording keyboard input. Press '*' to stop.")

# Define a callback function to handle key presses
def on_press(key):
  # Record the key pressed
  #if keyboard.is_pressed(' '):
  #  key = " "
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

#KeyboardEvent(backspace
while "KeyboardEvent(backspace" in recorded_keys_str:
    if recorded_keys_str.find("KeyboardEvent(backspace") != 0:
        before = 21
        after = 29
        pos = recorded_keys_str.find("KeyboardEvent(backspace")
        #11
        if recorded_keys_str[pos-11:pos-6] == "space":
            before = 25
        if recorded_keys_str[pos+20:pos+25] == "space":
            after = 28
        recorded_keys_str = recorded_keys_str[:pos-before] + recorded_keys_str[pos+after:]
        print("\n" +recorded_keys_str)
        
recorded_keys_str = recorded_keys_str.replace("KeyboardEvent(", "")
recorded_keys_str = recorded_keys_str.replace(" down)", "")
recorded_keys_str = recorded_keys_str.replace("space", " ")


print(recorded_keys_str)
# Print a message to let the user know the script has stopped recording
print("Keyboard input recording stopped.")