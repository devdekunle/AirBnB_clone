We started work on our AirBnB clone. The project is being done in phases.
In this current phase, we're:
1. Creating a class Basemodel which will be the super class for other classes we create;
2. Creating a class Filestorage that will enable us store our data in a file first before we implement a database Our objects are pulled from/inserted into the file storage using JSON serialization/deserialization
3. Building the console. The console is a command line interface through which we can interact with our model and manipulate the data in the file stirage or databse. The console will have these commands: 'quit'; 'EOF'; 'help'; 'create'; 'show'; 'destroy'; 'all'; and  'update'

HOW TO START THE COMMAND INTERPRETER:
The command interpreter can be started in interactive mode using the command "./console.py" The interpreter can also process commands in non-interactive mode. For instance, to use the command "help" in non-interactive mode, we enter the command "echo 'help' | ./console.py"

HOW TO USE THE INTERPRETER:
a. start the interpreter with the command "./console.py"
b. enter the command "help" to see a list of all documented commands. 
you could pass a command as argument to help to get help about that specific command. For instance, by entering "help create" you get help on how to use the "create" command of the interpreter.
c. The "EOF" or "quit" command is used to exit the interpreter. By typing the word "quit" or pressing the keys "ctrl + D", the interpreter in exited.

THE COMMANDS AVAILABLE IN THE INTERPRETER:
