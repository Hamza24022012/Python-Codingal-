class bird:
    def __init__(self):
        print("bird is ready")
    def whoisthis(self):
        print("bird")
    def swim(self):
        print("swim faster")
class penguin(bird):
    def __init__(self):
        super().__init__()
        print("penguin is ready")
    def whoisthis(self):
        super().whoisthis()
        print("penguin")
    def run(self):
        print("run faster")
p=penguin()
p.whoisthis()
p.swim()
p.run()