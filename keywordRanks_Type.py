#Say we have a list/set of 10 - 15 course description and a dictionary of the 10 keywords and their ranking. 
#Which 3-5 course should we recommend?

import re
from nltk.stem import WordNetLemmatizer


#Assumption: lowest ranking is the best
def rank(courseDescrs, keywordRanking, k, type):

    ranked = []

    for course in courseDescrs:

        score = 0

        #replace all punctuation stuff with spaces
        replace = re.sub(r"[,.;@#-?!&$]+", ' ', course)
        
        splitCourse = replace.split(" ")
        splitCourse = list(set(splitCourse))
        print(splitCourse)

        containsType = False
        for word in splitCourse:
            if(word in keywordRanking):
                score += keywordRanking[word]
                if(word == type):
                    containsType = True

        print(score)
        if(score > 0 and containsType):
            ranked += [(score, course)]

    print(ranked)
    ranked.sort(key=lambda x: x[0])
    print(ranked)

    selected = ranked[:k]
    print("selected")
    print(selected)
    return selected



d = dict()
d["yes"] = 3
d["Hey"] = 6
rank(["Hey there! yes,", "Hey", "yes-yes"], d, 2)
