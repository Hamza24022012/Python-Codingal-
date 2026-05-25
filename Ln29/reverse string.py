class reversestring:
    def __init__(self,sentence):
        self.sentence=sentence

    def reverse_words(self):
        word=self.sentence.split()
        reversedwords=word [::-1]
        return ' '.join(reversedwords)
    def __str__(self):
        return self.reversedwords()
    def __str__(self):
        return self.reversedwords()
text=reversestring("this is python")
print(text.reverse_words())
        
        