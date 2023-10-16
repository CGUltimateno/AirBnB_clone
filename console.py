#!/usr/bin/python3
"""
Module for the console
"""
import cmd

from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from models.city import City
from models.state import State
from models import storage
import re
import json


class Console(cmd.Cmd):
    """
    Console class
    """
    prompt = '(hbnb) '

    def default(self, line):
        """
        catches commands if nothing matches
        """
        self.precmd(line)

    def precmd(self, line):
        """
        intercepts commands to test
        """
        match = re.search(r'^(\w*)\.(\w+)(?:\(([^)]*)\))$', line)
        if not match:
            return line
        class_name = match.group(1)
        command = match.group(2)
        args = match.group(3)
        match_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_args:
            uid = match_args.group(1)
            attr = match_args.group(2)
        else:
            uid = args
            attr = False

        value = ""
        if command == "update" and attr:
            match_value = re.search('^"([^"]*)"$', attr)
            if match_value:
                self.update_dict(class_name, uid, match_value.group(1))
                return ""
            match_value = re.search('^(?:"([^"]*)")?(?:, (.*))?$', attr)
            if match_value:
                value = ((match_value.group(1) or "")
                         + (match_value.group(2) or ""))
        comm = command + " " + class_name + " " + uid + " " + value
        self.onecmd(comm)
        return comm

    def update_dict(self, class_name, uid, attr):
        """
        Updates the dictionary
        """
        x = attr.replace('"', '')
        y = json.loads(x)
        if not class_name:
            print("** class name missing **")
        elif class_name not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = class_name + "." + uid
            if key in storage.all():
                for key, value in y.items():
                    setattr(storage.all()[key], key, value)
                storage.all()[key].save()
            else:
                print("** no instance found **")

    def do_EOF(self, line):
        """
        exits the console
        """
        print()
        return True

    def do_quit(self, line):
        """
        exits the console
        """
        return True

    def emptyline(self):
        """
        empty line
        """
        pass

    def do_create(self, line):
        """
        Creates a new instance
        Command line:
        create <class name>
        examples:
        create City
        create Place
        create User
        create State
        create Amenity
        """
        class_mapping = {
            "city": City,
            "place": Place,
            "user": User,
            "state": State,
            "amenity": Amenity,
            "review": Review,
        }

        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            new_instance = storage.classes()[line]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args = line.split()
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args = line.split()
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    del storage.all()[key]
                    save()
                else:
                    print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances
        """
        if line != "":
            args = line.split('')
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                print([str(v) for k, v in
                       storage.all().items() if args[0] in k])
        else:
            print([str(v) for k, v in storage.all().items()])

    def do_count(self, line):
        """
        Counts the number of instances of a class
        """
        args = line.split()
        if not args:
            print("** missing class name **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            count = [k for k in storage.all().keys()
                     if k.startswith(args[0] + ".")]
            print(len(count))

    def do_update(self, line):
        """
        Updates an instance
        """
        if line == "" or line is None:
            print("** class name missing **")
            return

        r = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(r, line)
        class_name = match.group(1)
        uid = match.group(2)
        attr = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
        elif class_name not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = class_name + "." + uid
            if key in storage.all():
                if attr is None:
                    print("** attribute name missing **")
                elif value is None:
                    print("** value missing **")
                else:
                    cast = None
                    if not re.search(r'^"([^"]*)"$', value):
                        if '.' in value:
                            cast = float
                        else:
                            cast = int
                    else:
                        value = value.replace('"', '')
                    attrs = storage.attributes()[class_name]
                    if attr in attrs:
                        value = attrs[attr](value)
                    elif cast:
                        try:
                            value = cast(value)
                        except ValueError:
                            pass
                    setattr(storage.all()[key], attr, value)
                    storage.all()[key].save()


if __name__ == '__main__':
    Console().cmdloop()
