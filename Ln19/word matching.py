def match_words(words):
    count=0
    list=[]
    for word in words:
        if len(word)>1 and word[0] == word[-1]:
            count=count+1
            list.append(word)
    print("list of words with same first and last letter",list)
    return count

count=match_words(["oppo","rtg","tht","13241"])
print("number of words with same first and last letter",count)

