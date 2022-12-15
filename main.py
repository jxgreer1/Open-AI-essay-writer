import pyautogui
import keyboard
import dis_key
import setting
import colorama
import os
import openai
import time
# pip install -r requirements.txt 
# Create a set to store the keys that have been pressed
keys_pressed = set()
openai.api_key="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"
print("write da prompt")

# Define a list to store the recorded keys

##################################################################################
# Define a list to store the recorded keys
recorded_keys = []

# Print a message to let the user know the script is running
print("Recording keyboard input. Press '=' to stop.")

# Define a callback function to handle key presses
def on_press(key):
  # Record the key pressed
  #if keyboard.is_pressed(' '):
  #  key = " "
  recorded_keys.append(key)

# Start listening for key presses
keyboard.on_press(on_press)

# Wait until the "*" key is pressed
while not keyboard.is_pressed("="):
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
recorded_keys_str = recorded_keys_str.replace("shift", "")
recorded_keys_str = recorded_keys_str.replace("enter", "")



print(recorded_keys_str)
prompt = recorded_keys_str
# Print a message to let the user know the script has stopped recording
print("Keyboard input recording stopped.")
######################################################################################
if os.path.exists("dist/myfile.txt"):
    print("there")
    os.remove("dist/myfile.txt")
    
else: 
    print("nothere")

f = open("dist/myfile.txt", "x")
f.write(prompt)
f.close()
# Print the generated essay
    
global word_count
global word
# Clear Terminal
os.system('cls' if os.name=='nt' else 'clear')
colorama.init(autoreset=True, convert=True)
# the letter for what to press
word_count = 0
# Grabbing Document
f=open("dist/myfile.txt", "r")
y = f.read()
f.close()
print(y)
# Use the GPT-3 model to generate the essay
completions = openai.Completion.create(
    engine="text-davinci-003",
    prompt=y,
    max_tokens=4060,
    temperature=0.01,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
f = open("dist/myfile.txt", "a")
f.write(completions.choices[0].text)
f.close()
print(type(completions.choices[0]))
word = setting.checkOPENAI()
# makes the comma typable / may need to check more symbols
for i in word:
    if i == '’':
        x = word.index(i)
        word = word[:x]+["'"]+word[x+1:]
    else:
        pass
#Block Key             
dis_key.blocked()
print(completions.choices[0].text)
while True:
    if keyboard.is_pressed(" ") or keyboard.is_pressed("!") or keyboard.is_pressed('"') or keyboard.is_pressed("#") or keyboard.is_pressed("$") or keyboard.is_pressed("%") or keyboard.is_pressed("&") or keyboard.is_pressed("'") or keyboard.is_pressed("(") or keyboard.is_pressed(")") or keyboard.is_pressed("*") or keyboard.is_pressed("+") or keyboard.is_pressed(",") or keyboard.is_pressed(".") or keyboard.is_pressed("/") or keyboard.is_pressed("0") or keyboard.is_pressed("1") or keyboard.is_pressed("2") or keyboard.is_pressed("3") or keyboard.is_pressed("4") or keyboard.is_pressed("5") or keyboard.is_pressed("6") or keyboard.is_pressed("7") or keyboard.is_pressed("8") or keyboard.is_pressed("9") or keyboard.is_pressed(":") or keyboard.is_pressed(";") or keyboard.is_pressed("<") or keyboard.is_pressed("=") or keyboard.is_pressed(">") or keyboard.is_pressed("?") or keyboard.is_pressed("@") or keyboard.is_pressed("[") or keyboard.is_pressed("]") or keyboard.is_pressed("^") or keyboard.is_pressed("_") or keyboard.is_pressed("`") or keyboard.is_pressed("a") or keyboard.is_pressed("b") or keyboard.is_pressed("c") or keyboard.is_pressed("d") or keyboard.is_pressed("e") or keyboard.is_pressed("f") or keyboard.is_pressed("g") or keyboard.is_pressed("h") or keyboard.is_pressed("i") or keyboard.is_pressed("j") or keyboard.is_pressed("k") or keyboard.is_pressed("l") or keyboard.is_pressed("m") or keyboard.is_pressed("n") or keyboard.is_pressed("o") or keyboard.is_pressed("p") or keyboard.is_pressed("q") or keyboard.is_pressed("r") or keyboard.is_pressed("s") or keyboard.is_pressed("t") or keyboard.is_pressed("u") or keyboard.is_pressed("v") or keyboard.is_pressed("w") or keyboard.is_pressed("x") or keyboard.is_pressed("y") or keyboard.is_pressed("z") or keyboard.is_pressed("{") or keyboard.is_pressed("|") or keyboard.is_pressed("}") or keyboard.is_pressed("~") or keyboard.is_pressed("capslock") or keyboard.is_pressed("ctrl") or keyboard.is_pressed("delete") or keyboard.is_pressed("down") or keyboard.is_pressed("end") or keyboard.is_pressed("enter") or keyboard.is_pressed("insert") or keyboard.is_pressed("left") or keyboard.is_pressed("numlock") or keyboard.is_pressed("pagedown") or keyboard.is_pressed("pageup") or keyboard.is_pressed("right") or keyboard.is_pressed("shift") or keyboard.is_pressed("tab") or keyboard.is_pressed("up") or keyboard.is_pressed("win"):
        if word_count == len(word):
            break
        keyboard.write(word[word_count])
        word_count += 1
    elif keyboard.is_pressed("backspace"):
        pyautogui.press("backspace")
        if word_count != 0:
            word_count -= 1
    elif keyboard.is_pressed("-"):
        dis_key.unblocked()
        keyboard.wait("-")
        dis_key.blocked()

    

