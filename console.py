#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """This class defines the command interpreter"""

    prompt = "(hbnb) "

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
