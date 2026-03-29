# Source - https://stackoverflow.com/a/187701
# Posted by Florian Bösch
# Retrieved 2026-03-29, License - CC BY-SA 2.5

import cmd

addresses = [
    'yogurt', 'chicken', 'peas'
]

class MyCmd(cmd.Cmd):
    def do_send(self, line):
        pass

    def complete_send(self, text, line, start_index, end_index):
        if text:
            return [
                address for address in addresses
                if address.startswith(text)
            ]
        else:
            return addresses

if __name__ == '__main__':
    my_cmd = MyCmd()
    my_cmd.cmdloop()
