import time
import re  # Import the re module for regular expressions
def command():
    print("Test plugin presents")
REGISTERED_FUNCTIONS=[("command",command)]

def join_command():
    print("It's a new function")

def onedef():
    try:    
        regex = "e! ([\s\S]+)"
        if match := re.match(regex, word):
            txt = match.groups()[0]
            print("!~>", txt)
    except Exception as e:
        print(f"Error: {e}")

def register_commands(register_command):
    # Регистрация команд в MG-DOS
    register_command("join", join_command)
    register_command(onedef, onedef)
