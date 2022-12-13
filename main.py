import pyautogui
import keyboard
import dis_key
import setting
import colorama
import os
import openai

openai.api_key="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"
prompt = ""
print("write da prompt")
while True:
    if keyboard.is_pressed("a"):
        prompt += "a"
    if keyboard.is_pressed("b"):
        prompt += "b"
    if keyboard.is_pressed("c"):
        prompt += "c"
    if keyboard.is_pressed("d"):
        prompt += "d"
    if keyboard.is_pressed("e"):
        prompt += "e"
    if keyboard.is_pressed("f"):
        prompt += "f"
    if keyboard.is_pressed("g"):
        prompt += "g"
    if keyboard.is_pressed("h"):
        prompt += "h"
    if keyboard.is_pressed("i"):
        prompt += "i"
    if keyboard.is_pressed("j"):
        prompt += "j"
    if keyboard.is_pressed("k"):
        prompt += "k"
    if keyboard.is_pressed("l"):
        prompt += "l"
    if keyboard.is_pressed("m"):
        prompt += "m"
    if keyboard.is_pressed("n"):
        prompt += "n"
    if keyboard.is_pressed("o"):
        prompt += "o"
    if keyboard.is_pressed("p"):
        prompt += "p"
    if keyboard.is_pressed("q"):
        prompt += "q"
    if keyboard.is_pressed("r"):
        prompt += "r"
    if keyboard.is_pressed("s"):
        prompt += "s"
    if keyboard.is_pressed("t"):
        prompt += "t"
    if keyboard.is_pressed("u"):
        prompt += "u"
    if keyboard.is_pressed("v"):
        prompt += "v"
    if keyboard.is_pressed("w"):
        prompt += "w"
    if keyboard.is_pressed("x"):
        prompt += "x"
    if keyboard.is_pressed("y"):
        prompt += "y"
    if keyboard.is_pressed("z"):
        prompt += "z"
    if keyboard.is_pressed("-"):
        break


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
    engine="text-davinci-002",
    prompt=y,
    max_tokens=4080,
    temperature=0.5,
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

    

