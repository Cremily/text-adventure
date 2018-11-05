import io
import os
import random
files = os.listdir('bored')
text = []
for file in files:
    try:
        file_type = file.split('.')[1]
        if file_type == 'txt':
            text.append(file)
    except IndexError as e:
        print(file,e)
def select_options():
    global text
    print("Choose from:")
    for txt_file in text:
        print(txt_file.split('.')[0])
    print('\n' + "Type all choices, then type end to finish!")
    choices = []
    choice_select = ""
    while choice_select != "end" and len(choices) < len(text):
        choice_select = input().lower()
        choices.append(choice_select)
    if choice_select == "end":
        choices = choices[:-1]
    string_list = "You selected: "
    for choice in choices:
        string_list += choice + ", "
    string_list = string_list[:-2]
    print(string_list)
    if input("Is this correct? Y/N ").lower() == "n":
        choices = select_options()
    else:
        return choices
choices = select_options()
answers = []
for choice in choices:
    choice = choice.capitalize()
    choice_path = 'bored/' + choice + '.txt'
    try:
        f = open(choice_path,'r')
        for line in f:
            line = line[:-1]
            answers.append(line)
    except Exception as e:
        print("sorry, couldn't find %s!" % choice)
print(answers)