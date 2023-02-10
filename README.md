We started work on our AirBnB clone. The project is being done in phases.
In this current phase, we're:
1. Creating a class Basemodel which will be the super class for other classes we create;
2. Creating a class Filestorage that will enable us store our data in a file first before we implement a database Our objects are pulled from/inserted into the file storage using JSON serialization/deserialization
3. Building the console. The console is a command line interface through which we can interact with our model and manipulate the data in the file stirage or databse. The console will have these commands: 'quit'; 'EOF'; 'help'; 'create'; 'show'; 'destroy'; 'all'; 'update'
