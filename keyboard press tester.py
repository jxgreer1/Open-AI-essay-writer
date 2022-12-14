import pyautogui
import keyboard
import dis_key
import setting
import colorama
import os
import openai

openai.api_key="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"

print("write da prompt")
prompt=input()


# Use the GPT-3 model to generate the essay
completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    temperature=0.5,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
if os.path.exists("dist/myfile.txt"):
    print("there")
    os.remove("dist/myfile.txt")
    
else: 
    print("nothere")

f = open("dist/myfile.txt", "x")
f.write(prompt)
f.close
# Print the generated essay
    