#!/usr/bin/python3
"""
this file is for calling the cmd class for interpreter functionalities
for our AirBnB project
"""
from cmd import Cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(Cmd):
    """
    this class will not be implementing all cmd commands only
    a select few like quit, EOF, prompt and  help.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """This is the quit help command."""
        print("Quit command to exit the program")

    def emptyline(self):
        pass

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        return True

    def do_create(self, arg):
        """creation of instances from BaseModel..."""
        if not arg:
            print("** class name missing **")
        else:
            try:
                obj = eval(arg)()
                obj.save()
                print(obj.id)
            except Exception as e:
                print("** class doesn' t exist **")

    def do_show(self, arg):
        """ this shows saved instances of a class BaseModel """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
