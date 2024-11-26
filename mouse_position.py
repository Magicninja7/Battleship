import pyautogui
import time
import openai

time.sleep(10)



def chatgptfun(message):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "The users prompt, will be a code snippet in python. You have to or find a bug within it, or make it faster in time, or so that it takes up less space. You can also add a comment to the code, or write a function that would be useful in the code. The possibilities are endless. But remember to add a comment '#chatgpt start', at the beggining of code you create/modify and '#chatgpt end' at the end of the code you create/modify. Think about your solution for a moment, if its a bug, how would you fix it? If its a speed issue, how would you make it faster? If its a space issue, how would you make it take up less space? If you think the code is perfect, what would you add to it? Only return code and comments, so that a compiler can run it."},
            {
                "role": "user",
                "content": message
            }  
        ]
    )
    return completion.choices[0].message


while True:
    i = 0
    with open("statki.py", "r") as file:
        complete_code = file.read()
        lines = file.readlines()
        if i < len(lines):
            code = lines[i]
            i += 1
    response = chatgptfun(complete_code)



    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You will receive two code snippets, divided by ':::' you have to merge them in a way that would make the program work."},
            {
                "role": "user",
                "content": f"{response}:::{complete_code}"
            }  
        ]
    )
    next_code = completion.choices[0].message
    lines = next_code.splitlines()



    pyautogui.moveTo(482, 309) 
    pyautogui.click() 
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')

    pyautogui.write(next_code)
    for line in lines:
        pyautogui.write(line)
        time.sleep(30)
        pyautogui.press('enter')
        pyautogui.hotkey('ctrl', 's')
