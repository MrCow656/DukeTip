def passOrNot(grade):
    #TODO: Print whether or not Student has passed based on Grading Criteria
    raise NotImplementedError
def grade(N):
    if (N > 70):
        print ("Congratulations You passed")
    else:
        print("Sorry. You must have at least 70% to pass. See you next semester.")

def modulusFour(start):
    #TODO: Determine whether given number is divisible by 4
    raise NotImplementedError
def thing(dang):
    end = 0
    print(dang)
    while (end < 1):
        if (dang - 4 > -1):
            dang = dang -4
            print (dang)
        else:
            print ("the remainder is the number shown above")
            end = 2


def letterSpace(userString):
    # TODO: Remove all letters or  numbers from the string "userString"
    """
    Reccommendation using the command bool(re.match('^[a-zA-Z0-9]', string))
    Example
        bool(re.match('^[a-zA-Z0-9]', '123abc'))
        >>> True
        bool(re.match('^[a-zA-Z0-9]', '123abc#'))
        >>> False

    """
    raise NotImplementedError
import string
import re
def letters(no):
    no =  str(input("write text"))
    yes = re.sub('[^ a-zA-Z]', ' ', no)
    print(yes)



def complimentMaker(answer1, answer2, answer3, answer4):
     #TODO: Print a string with some combination of adjectives  "super" "nice" "smart" and "cool"
           #based on the boolean values of the answer parameters
    if (answer1 == True):
        test1 = "super "
    else:
        test1 = ""
    if (answer2 == True):
        test2 = "nice "
    else:
        test2 = ""
    if (answer3 == True):
        test3 = "smart "
    else:
        test3 = ""
    if (answer4 == True):
        test4 = "cool "
    else:
        test4 = ""
    if (test1 == "super " or test2 == "nice " or test3 == "smart " or test4 == "cool "):
        print("you are " + test1  + test2  + test3  + test4)
    else:
        print ("no comment")
(False, False, False, False)

def wordMesh(a, b):
    #TODO: Overlap each letter of the strings. Assume that a and b will be of equal length.
    """
    Reccommend using the format
        newString = ""
        for(i in range(len(currentString)):
            newString = newString + currentString[i]
    - where currentString should be replaced with a reference to a string

    """


def replaceWord(str, b, letter):
    """
    TODO: Every time the string (a) occurs in the sentence string (letter) replace with (a) with (b)
    Reccomend Using string.replace() : https://www.tutorialspoint.com/python/string_replace.htm
    """

    print str.replace(letter,b)

replaceWord("do you play minecraft","why","m")
def print10table(i):
    """
    Reccomendation: Using Nested Loops: https://www.tutorialspoint.com/python/python_nested_loops.htm
    """
    raise NotImplementedError

######################################################################
##########################    TESTS     ##############################
######################################################################
