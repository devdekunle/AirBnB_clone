#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models

class HBNBCommand(cmd.Cmd):
    """This class defines the command interpreter"""

    prompt = "(hbnb) "

    def do_create(self, class_name):
        """Creates a new instance, saves it and prints the id"""
        if len(class_name) == 0:
            print("** class name missing **")
        elif class_name != "BaseModel":
            if not issubclass(type(class_name), BaseModel):
                print("** class doesn't exist **")
        else:
            new_inst = eval(class_name)()
            models.storage.new(new_inst)
            models.storage.save()
            print(new_inst.id)

    def do_show(self, class_name, id_num):
        """command to print the string representation of an instance"""
        if len(class_name) == 0:
            print("** class name missing **")
        elif class_name != "BaseModel":
            if not issubclass(type(class_name), BaseModel):
                print("** class doesn't exist **")
        if len(id_num) == 0:
            print("** instance id missing ** ")
        elif 

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        exit()

    def do_EOF(self, line):
        """exit the interpreter by pressing ^D"""
        return True

    def emptyline(self):
        """prints an empty line if not command is passed + ENTER"""
        return


if __name__ == "__main__":
    HBNBCommand().cmdloop()
