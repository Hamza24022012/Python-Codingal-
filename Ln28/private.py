class myclass:
    __privatevar = 27
    def __privmeth(self):
        print("I'm in 'myclass'")
    def hello(self):
        print("private var value:-", myclass.__privatevar)

obj=myclass()
obj.hello()
obj.__privmeth()