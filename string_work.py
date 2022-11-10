class PrintString:
    def __init__(self):
        self.user_string = ''
        
    def get_String(self):
        sin = input("What would you like to scream into the void? ")
        self.print_String(sin)
    
    def print_String(self, string):
        print(string.upper())

up_string = PrintString()

up_string.get_String()