# MGDOS2.5-PLUGINSYS
In this UPDATED MG-DOS version (2.5) you can make youre own plugins and add new features to ORIGINAL MG-DOS SYSTEM
example to make a plugin you need to add "<Py> Newplugin.py" and put it in
"<DIR> Plugins"->
```
$NewPlugin.py example$
def command():
    print("Test plugin presents")
REGISTERED_FUNCTIONS=[("command",command)]
def join_command():
    print("It's a new function")
def register_commands(register_command):
    register_command("join", join_command) 
```
# Practice
For starting develop plugins for MG-DOS you can use this example
and study for "programming"
