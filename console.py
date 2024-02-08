import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program by pressing Ctrl+D (EOF)"""
        print("")  
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
