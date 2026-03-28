class Pakistan():
    def capital(self):
        print("Islamabad is the capital of Pakistan")
    def language(self):
        print("Urdu is the national language")
    def type(self):
        print("Pakistan is a developing nation")

class Germany():
    def capital(self):
        print("Berlin is the capital of Germany")
    def language(self):
        print("German is the national language")
    def type(self):
        print("Germany is a developed nation")

pk=Pakistan()
ger=Germany()

for country in (pk,ger):
    country.capital()
    country.language()
    country.type()