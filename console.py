#!/usr/bin/python3
"""
This module defines the command interpreter class.
"""
import cmd
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class.
    """
    prompt = "(hbnb) "

    def do_create(self, arg):
        """
        Creates a new instance of a specified class.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in [
                "BaseModel",
                "State",
                "City",
                "Amenity",
                "Place",
                "Review"
                ]:
            print("** class doesn't exist **")
            return
        new_obj = eval(class_name)()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, arg):
        """
        Prints str rep of an instance based on the class name and id.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        class_name = args[0]
        obj_id = args[1]
        if class_name not in [
                "BaseModel",
                "State",
                "City",
                "Amenity",
                "Place",
                "Review"
                ]:
            print("** class doesn't exist **")
            return
        key = "{}.{}".format(class_name, obj_id)
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_count(self, arg):
        """Retrieve the number of instances of a class."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        count = len(storage.all()[class_name])
        print(count)

    def do_quit(self, arg):
        """
        Exits the command interpreter.
        """
        return True

    def do_EOF(self, arg):
        """
        Handles EOF (Ctrl+D) to exit the command interpreter.
        """
        print("")
        return True

    def emptyline(self):
        """
        Handles empty lines.
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
