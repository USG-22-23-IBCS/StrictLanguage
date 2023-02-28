import random
# define a generating line that has parameters as syllable and value
# value is the number of syllable for each line
def genLine(syl, val, exclude, include):
# create an empty string so that we can add word 
    line = ""
# use indefinite loop because there are no limited words
    while True:
        v = random.randint(1,4)
# val is the number of syllables in one line
        if val - v >= 0:
# get the list of syllables, get(v) is get the key
            myList = syl.get(v).split()
# choose a random word from the list
            word = random.choice(myList)
# if word is in the letter that user want to exclude, then use words that do not have that letter
# if word is in the letter that user want to include, then use words that have that letter
            if exclude not in word and include in word:
                line = line + word + " "
                val = val - v
#if value is 0, break the loop
        if val == 0:
            break
    
    return line
       




def main():
    f1 = open("one syllable.txt")
    f2 = open("two syllables.txt")
    f3 = open("three syllables.txt")
    f4 = open("four syllables.txt")
    readOne = f1.read()
    readTwo = f2.read()
    readThree = f3.read()
    readFour = f4.read()
    syl = {1 : readOne,
           2 : readTwo,
           3 : readThree,
           4 : readFour}
    mulHaiku = int(input("How many Haiku do you want to make?\n"))
    include = input("What letter do you want to include in the Haiku?\n")
    exclude = input("What letter do you want to exclude in the Haiku?\n")
# the number of Haiku is the number that user wants
    for i in range(mulHaiku):
        print(genLine(syl, 5, exclude, include))
        print(genLine(syl, 7, exclude, include))
        print(genLine(syl, 5, exclude, include))
        
    
if __name__ == "__main__":
    main()
