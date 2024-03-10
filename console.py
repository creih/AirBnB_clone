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

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return
        try:
            args = arg.split()
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            args = arg.split()
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            if key in models.storage.all():
                del models.storage.all()[key]
                models.storage.save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if not arg:
            print([str(obj) for obj in models.storage.all().values()])
        else:
            try:
                print([str(obj) for obj in models.storage.all().values() if obj.__class__.__name__ == arg])
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            args = arg.split()
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            attribute_name = args[2]
            attribute_value = args[3]
            key = "{}.{}".format(class_name, instance_id)
            if key in models.storage.all():
                instance = models.storage.all()[key]
                setattr(instance, attribute_name, attribute_value)
                instance.save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()
