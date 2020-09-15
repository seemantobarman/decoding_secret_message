import itertools
import csv

# Messages
Message_1 = "ZUVFFXIN CVIX ZS 5 HT" 
Message_2 ="ASTAXI ORPZB TSKX JS LNM" 
Message_3 = "WXGXIZF ESDG OZFU SPJ"

def wordMatch(word):
    print("Secret Code: "+word)
    possiblListOfWords = word.split(" ")
    List = []

    #Creating enpty lists/arrays
    wordCount = len(possiblListOfWords)
    # print(wordCount)
    array = [[] for i in range(1, wordCount+1)]
    start = 0

    #Filtering Words
    PossibleWords = ["ABOLISHES","5","ACCORDING","ARTILLERY","AGITATION","ACID","AREA","FIRE","WATER","TORPEDO","COMMANDER","GENERAL","CAPTAIN","SHIP","BARRAGE","RUN","WALK","JOHN","XYZ","SQUAD","SQUADRON","LEADER","RELOCATE","GO","MOVE","CITY","CITADEL","JACK","MILNER","PM","AM","AT","TO","IN","OUT","OFF","OF","FROM","FOR","SHELL","WILL","RIGHT","LEFT","NORTH","SOUTH","EAST","WEST","SNIPER","INFANTRY","TANK","BOMBER","FIGHTER","MORNING","EVENING","AFTERNOON","NIGIIT","DAY","AIRCRAFT","LONDON","COMMAND","SECURE","ENEMY","SPY","RANGE","MILLER","MULLER","TROOP","SUBMARINE"]
    for word in possiblListOfWords:
        for secWord in PossibleWords:
            if len(word)==len(secWord):
                List.append(secWord)
                array[start].append(secWord)
        start=start+1

    return array

def Combination(anArray):
    length = len(anArray)
    for i in range(length):
        print(anArray[i])

    """Start Of Combination (Method 1)"""
    def flatten(B):
        A = []
        for i in B:
            if type(i) == list: A.extend(i)
            else: A.append(i)
        return A

    outlist =[]; templist =[[]]
    for sublist in anArray:
        outlist = templist; templist = [[]]
        for sitem in sublist:
            for oitem in outlist:
                newitem = [oitem]
                if newitem == [[]]: newitem = [sitem]
                else: newitem = [newitem[0], sitem]
                templist.append(flatten(newitem))

    outlist = list(filter(lambda x: len(x)==len(anArray), templist))
    for i in range(len(outlist)):
        print(outlist[i])
    """End Of Combination"""

    with open("output_Message_3.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(outlist)
    

Combination(wordMatch(Message_3))