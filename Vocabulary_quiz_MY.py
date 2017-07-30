
parts_of_speech  = ["_1_", "_2_", "_3_", "_4_", "_5_"]


vocabularies=[
["_1_ means: the trait of sincere and steadfast fixity of purpose\n\
_2_means:\n\
\n\
\n\
\n"],
["\n\
\n\
\n\
\n\
\n"],
["\n\
\n\
\n\
\n\
\n"]
]
answers=[["commitment","b","c","d","e"],["f","g","h","i","j"],["k","l","m","n","o"]]

# Checks if a word in parts_of_speech is a substring of the word passed in.
def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None
        
"""
This code is designed to let a user take a vocabulary quiz:
first:choose the vocabulary type
second: type in the attempt answers
third: give feedback
"""

def play_game(parts_of_speech):  
    print 'Please select vocabulary type by typing it in!'
    print 'Possible choices include:\n1. BASIC\n2. TOEFL\n3. GRE\n'
    choices=raw_input('Choose vocabulary type:')  
    ml_string=difficulty(choices)
    choices=choices-1
    print ml_string
    replaced = []
    ml_string = ml_string.split()
    for word in ml_string:
        replacement = word_in_pos(word, parts_of_speech)
        if replacement != None:
            user_input = raw_input("Type in "+replacement+" word: ")
            answer=trials(user_input)
            word = word.replace(replacement, answer)
            replaced.append(word)
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    return replaced
#select difficulty
#I am trying to secure my code by making it only input the valid data
#I know how to do that in C but not in python
def difficulty(choices):
    if choices==1 | 'BASIC' | 'basic':

        print "You've chosen Basic!"
        strings=vocabularies[0]
    if choices==2 | 'TOEFL' | 'toefl':

        print "You've chosen TOEFL!"
        strings=vocabularies[1]
    if choices==3 | 'GRE' | 'gre':

        print "You've chosen GRE!"
        strings=vocabularies[2]
    return strings


#build a function and let user have several trials:
def trials(user_input):
    for index in range(0,4):
        trials_left=4-index
        while user_input!=answers[choices][index]:
            print "You have"+ trials_left+ "left!"
        answer=answers[choices][index]
        index+=1
    return answer




    
print play_game(parts_of_speech)   