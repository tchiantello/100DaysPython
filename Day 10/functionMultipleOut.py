#Function with output

def format_name(f_name, l_name):
    #can put a return early so the rest of the function does not run
    #eg if no name is entered
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
    
    #print statement after return will not print. "return" tells the function to end
    print("This does not get printed")