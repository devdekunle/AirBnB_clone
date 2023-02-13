#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
import models
import shlex


class HBNBCommand(cmd.Cmd):
    """This class defines the command interpreter"""

    __classes = \
        ['BaseModel', 'User', 'State', 'Amenity', 'Place', 'Review', 'City']
    prompt = "(hbnb) "

    def do_create(self, class_name):
        """Creates a new instance, saves it and prints the id"""

        if len(class_name) == 0:
            print("** class name missing **")
            return
        if class_name in HBNBCommand.__classes:
            new_inst = eval(class_name)()
            models.storage.new(new_inst)
            models.storage.save()
            print(new_inst.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """command to print the string representation of an instance"""
        args = shlex.split(line)
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        else:
            all_obj = models.storage.all()
            obj_ids = all_obj.keys()
            obj_id = f"{args[0]}.{args[1]}"
            if obj_id in obj_ids:
                print(all_obj[obj_id])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """command to destroy an instance of the class name and id
        and save changes to the JSON file"""
        args = shlex.split(line)
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** Class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        else:
            all_obj = models.storage.all()
            obj_ids = all_obj.keys()
            obj_id = f"{args[0]}.{args[1]}"
            if obj_id in obj_ids:
                del all_obj[obj_id]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, class_name):
        """ Prints all string representation
        of all instances based or not on the class name"""

        all_obj = models.storage.all()
        list_obj = []
        if len(class_name) == 0:
            for keys in all_obj:
                list_obj.append(str(all_obj[keys]))
            print(list_obj)
        elif class_name and class_name in HBNBCommand.__classes:
            for key in all_obj:
                if key.split(".")[0] == class_name:
                    list_obj.append(str(all_obj[key]))
            print(list_obj)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """ updates the attributes of an instance and saves it"""
        args = shlex.split(line)
        all_objs = models.storage.all()
        obj_keys = all_objs.keys()
        ids = []
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        for model_id in obj_keys:
            ids.append(model_id.split(".")[1])
        if args[1] not in ids:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        else:
            try:
                value = eval(args[3])
            except Exception as e:
                value = str(args[3])
            obj_key = f"{args[0]}.{args[1]}"
            setattr(all_objs[obj_key], args[2], value)
            models.storage.save()

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
