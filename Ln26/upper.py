class capital():
    def __init__(self):
        self.str1=" "
    def get_string(self):
        self.str1=input("enter string")
    def print_string(self):
        print("Upper case is ",self.str1.upper())

a=capital()
a.get_string()
a.print_string()