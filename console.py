#!/usr/bin/python3
<<<<<<< HEAD

"""A command-line interface for managing instances of BaseModel.

This module supply a command-line interpreter managing instances of BaseModel.
It defines commands for creating, displaying, updating, and deleting instances.

"""

import cmd
import re
import json
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command-line interpreter class."""

    prompt = "(hbnb) "

    def default(self, line):
        """Intercepts commands and executes them."""
        self._precmd(line)

    def _precmd(self, line):
        """Intercepts and parses commands before execution."""
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line

        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(
                    1) or "") + " " + (match_attr_and_value.group(2) or "")
        command = method + " " + classname + " " + uid + " " + attr_and_value
        self.onecmd(command)
        return command

    def update_dict(self, classname, uid, s_dict):
        """Updates an instance with a dictionary."""
        s = s_dict.replace("'", '"')
        d = json.loads(s)
        if not classname:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[classname]
                for attribute, value in d.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def do_EOF(self, line):
        """Handles End Of File character."""
        print()
        return True

    def do_quit(self, line):
        """Exits the command-line interface."""
=======
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
>>>>>>> 07d301bcc0720ce90bcdb7669deb9c857fd9da91
        return True

    def help_quit(self):
        """
            Command to show quit documentation
        """
        print("Quit command to exit the program\n")

    def emptyline(self):
<<<<<<< HEAD
        """Does nothing when the user hits 'Enter' with an empty line."""
        pass

    def do_create(self, line):
        """Creates a new instance and saves it to the JSON file."""
        if not line:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            instance = storage.classes()[line]()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance."""
        if not line:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id."""
        if not line:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """Prints the string representation of all instances."""
        if line != "":
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                instances = [str(obj) for key, obj in storage.all().items()
                             if type(obj).__name__ == words[0]]
                print(instances)
        else:
            instances = [str(obj) for key, obj in storage.all().items()]
            print(instances)

    def do_count(self, line):
        """Counts the instances of a specified class."""
        if not line:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            instances = [k for k in storage.all() if k.startswith(line + '.')]
            print(len(instances))

    def do_update(self, line):
        """Updates an instance."""
        if not line:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)
        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[classname]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

=======
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
>>>>>>> 07d301bcc0720ce90bcdb7669deb9c857fd9da91

if __name__ == '__main__':
    HBNBCommand().cmdloop()


