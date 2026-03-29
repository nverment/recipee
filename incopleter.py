import cmd

ingredients = [
    'yogurt', 'chicken', 'peas'
]

class MyCmd(cmd.Cmd):
    def do_send(self, line):
        pass

    def complete_send(self, text, line, start_index, end_index):
        if text:
            return [
                ing for ing in ingredients
                if ing.startswith(text)
            ]
        else:
            return ingredients

if __name__ == '__main__':
    my_cmd = MyCmd()
    my_cmd.cmdloop()
