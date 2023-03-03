from os import system, name

def clear():
 
    if name=='nt':
        _ = system('cls')
    else:
        _ = system('clear')

def input_with_quit(question = ""):
    answer = input(question)
    if answer.lower() == "quit":
        exit()
    return answer