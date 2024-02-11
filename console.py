#!/usr/bin/python3
"""
    Console module for Airbnb project
"""


import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import cmd
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
        Define HBNBCommand class for console
    """
    prompt = "(hbnb) "
    all_classes = ['BaseModel', 'User', 'Place', 'State',
                   'City', 'Amenity', 'Review']

    def do_quit(self, args):
        """
            Command to quit from the command interpreter
        """
        return True

    def do_EOF(self, args):
        """
            Command to exit from the command interpreter
        """
        return True

    def help_quit(self):
        """
            Command to show quit documentation
        """
        print("Quit command to exit the program\n")

    def emptyline(self):
        """
            Command do nothing when emptyline appears
        """
        pass

    def do_create(self, args):
        """Creates a new instance in all_classes, saves it to the JSON file
            and prints the id
        """
        argu_list = args.split()
        if len(argu_list) == 0:
            print('** class name missing **')
            return
        try:
            result = eval(argu_list[0] + '()')
            result.save()
            print(result.id)
        except:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance based
            on the class name and id
        """
        argu_list = args.split()

        if Checker(argu_list):
            reference = Checker(argu_list)
            all_instances = models.storage.all()

            if reference in all_instances.keys():
                reference = all_instances[reference]
                print(reference)
            else:
                print("** no instance found **")
                return

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id,
            save the change into the JSON file
        """
        argu_list = args.split()
        if Checker(argu_list):
            obj_reference = Checker(argu_list)
            all_instances = models.storage.all()

            if obj_reference in all_instances.keys():
                del all_instances[obj_reference]
                models.storage.save()
            else:
                print("** no instance found **")
                return

    def do_all(self, args):
        """Prints all string representation of all instances
            based or not on the class name
        """
        instances = models.storage.all()
        if args:
            arg_list = args.split()
            print(arg_list[0])
            if arg_list[0] not in self.all_classes:
                print("** class doesn't exist **")
            else:
                new_list = [str(instances[obj]) for obj in instances.keys()
                            if arg_list[0] in obj]
                print(new_list)
        else:
            new_list = [str(instances[obj]) for obj in instances.keys()]
            print(new_list)

    def do_update(self, args):
        """Update an specific dictionary based in the class name
            and the id reference
        """
        argu_list = args.split()
        if Checker(argu_list):
            reference = Checker(argu_list)
            all_instances = models.storage.all()

            if reference in all_instances.keys():
                obj = all_instances[reference]
                len_arg_list = len(argu_list)

                if len_arg_list < 3:
                    print("** attribute name missing **")
                    return
                elif len_arg_list < 4:
                    print("** value missing **")
                    return
                else:
                    try:
                        value = int(argu_list[3].replace('"', ""))
                    except:
                        try:
                            value = float(argu_list[3].replace('"', ""))
                        except:
                            try:
                                value = str(argu_list[3].replace('"', ""))
                            except:
                                pass
                    obj.__dict__[argu_list[2]] = value
                    models.storage.save()
                    return
            else:
                print("** no instance found **")
                return

def Checker(list_args):
    """Function to Checker content in list or arguments
    """
    if list:
        len_list = len(list_args)
        if len_list < 1:
            print("** class name missing **")
            return None

        if (list_args[0] not in HBNBCommand.all_classes):
            print("** class doesn't exist **")
            return None

        if len_list < 2:
            print("** instance id missing **")
            return None

        reference = list_args[0] + '.' + list_args[1]
        return reference

if __name__ == '__main__':
    HBNBCommand().cmdloop()


