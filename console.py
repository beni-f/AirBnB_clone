#!/usr/bin/python3
"""
console module
"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    HBNBComand class
    """
    prompt = "(hbnb) "


    def do_EOF(self, line):
        """handles EOF"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """an empty line"""
        pass
    
    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if arg is None or arg == "":
            print("** class name missing **")
        elif arg not in storage.classes():
            print("** class doesn't exist")
        else:
            new_instance = storage.classes()[arg]()
            print(new_instance.id)
            new_instance.save()
        
    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name"""
        if arg is None or arg == "":
            print ("** class name missing **")
        else:
            args = arg.split(' ')
            if args[0] not in storage.classes():
                print("** class doesn't exits **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])  
    
    def do_destroy(self, arg):
        if arg is None or arg == "":
            print("** class name missing **")
        else:
            args = arg.split(' ')
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key] 
                    storage.save()
    
    def do_all(self, arg):
        if arg is None or arg == "":
            obj = [str(v) for k, v in storage.all().items()]
            print(obj)
        else:
            args = arg.split(' ')
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                obj = [str(v) for k, v in storage.all().items()
                       if type(v).__name__ == args[0]
                      ]
                print(obj)

    def do_update(self, arg):
        if arg is None or arg == "":
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            elif len(args) < 3:
                key = "{}.{}".format(args[0], args[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                setattr(storage.all()[key], args[2], args[3])
                storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()