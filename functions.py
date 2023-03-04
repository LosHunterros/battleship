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

def string_fill(string_original, lenght, align="center"):
    if len(string_original) > lenght:
        string_original = string_original[0:lenght]
    
    if align == "left":
        return string_original + ( lenght - len(string_original) ) * " "
    elif align == "right":
        return ( lenght - len(string_original) ) * " " + string_original
    else:
        return ( ( lenght - len(string_original) ) // 2 ) * " " + string_original + ( lenght - ( ( lenght - len(string_original) ) // 2 ) - len(string_original) ) * " "
