#!/usr/bin/python3
<<<<<<< HEAD
"""
Module Console
"""
import cmd
import shlex
import sys
import models
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """HBNB Class """
    prompt = '(hbnb) '

    classes = {'BaseModel': BaseModel, 'Amenity': Amenity,
               'State': State, 'Place': Place, 'Review': Review,
               'User': User, 'City': City}

    def do_quit(self, argument):
        """ Defines quit option"""
        return True

    def do_EOF(self, argument):
        """ Defines EOF option"""
        print()
        return True

    def emptyline(self):
        """ Defines Empty option"""
        pass

    def do_create(self, argument):
        """Creates an instance of BaseModel"""
        if argument:
            if argument in self.classes:
                # instance = models.base_model.BaseModel()
                get_class = getattr(sys.modules[__name__], argument)
                instance = get_class()
                print(instance.id)
                models.storage.save()
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
        return

    def do_show(self, argument):
        """string representation based on the class name and id"""
        tokens = shlex.split(argument)
        if len(tokens) == 0:
            print("** class name missing **")
        elif len(tokens) == 1:
            print("** instance id missing **")
        elif tokens[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            dic = models.storage.all()
            # Key has format <className>.id
            keyU = tokens[0] + '.' + str(tokens[1])
            if keyU in dic:
                print(dic[keyU])
            else:
                print("** no instance found **")
        return

    def do_destroy(self, argument):
        """Deletes an instance based on the class name and id"""
        tokensD = shlex.split(argument)
        if len(tokensD) == 0:
            print("** class name missing **")
            return
        elif len(tokensD) == 1:
            print("** instance id missing **")
            return
        elif tokensD[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            dic = models.storage.all()
            # Key has format <className>.id
            key = tokensD[0] + '.' + tokensD[1]
            if key in dic:
                del dic[key]
                models.storage.save()
            else:
                print("** no instance found **")

            # for i in dic.values():
            #     if i.__class__.__name__ == tokensD[0] and i.id == tokensD[1]:
            #         del i
            #         models.storage.save()
            #         return
            # print("** instance id missing **")
            # models.storage.save()

    def do_all(self, argument):
        """all string representation of all instances"""
        tokensA = shlex.split(argument)
        listI = []
        dic = models.storage.all()
        # show all if no class is passed
        if len(tokensA) == 0:
            for key in dic:
                representation_Class = str(dic[key])
                listI.append(representation_Class)
            # if listI:
            print(listI)
            return

        if tokensA[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            # Representation for a specific class
            representation_Class = ""
            for key in dic:
                className = key.split('.')
                if className[0] == tokensA[0]:
                    # This form doesn't work
                    # listI.append(dic[key])
                    representation_Class = str(dic[key])
                    listI.append(representation_Class)
            # if listI:
            print(listI)

    def do_update(self, argument):
        """Updates an instance based on the class name and id """
        tokensU = shlex.split(argument)
        if len(tokensU) == 0:
            print("** class name missing **")
            return
        elif len(tokensU) == 1:
            print("** instance id missing **")
            return
        elif len(tokensU) == 2:
            print("** attribute name missing **")
            return
        elif len(tokensU) == 3:
            print("** value missing **")
            return
        elif tokensU[0] not in self.classes:
            print("** class doesn't exist **")
            return
        keyI = tokensU[0] + "." + tokensU[1]
        dicI = models.storage.all()
        try:
            instanceU = dicI[keyI]
        except KeyError:
            print("** no instance found **")
            return
        try:
            typeA = type(getattr(instanceU, tokensU[2]))
            tokensU[3] = typeA(tokensU[3])
        except AttributeError:
            pass
        setattr(instanceU, tokensU[2], tokensU[3])
        models.storage.save()

    def do_count(self, argument):
        """  retrieve the number of instances of a class """
        tokensA = shlex.split(argument)
        dic = models.storage.all()
        num_instances = 0
        if tokensA[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            for key in dic:
                className = key.split('.')
                if className[0] == tokensA[0]:
                    num_instances += 1

            print(num_instances)

    def precmd(self, argument):
        """ executed just before the command line line is interpreted """
        args = argument.split('.', 1)
        if len(args) == 2:
            _class = args[0]
            args = args[1].split('(', 1)
            command = args[0]
            if len(args) == 2:
                args = args[1].split(')', 1)
                if len(args) == 2:
                    _id = args[0]
                    other_arguments = args[1]
            line = command + " " + _class + " " + _id + " " + other_arguments
            return line
        else:
            return argument
=======

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
        return True

    def emptyline(self):
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
        if line:
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
>>>>>>> ed699e272ad6c29fe2a9b2e2d739b45c2c9ceda6


if __name__ == '__main__':
    """infinite loop"""
    HBNBCommand().cmdloop()
