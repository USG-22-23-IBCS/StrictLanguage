import random
# define a generating line that has parameters as syllable and value
# value is the number of syllable for each line
def genLine(syl, val, exclude, include):
# create an empty string so that we can add word 
    line = ""
# use indefinite loop because there are no limited words
    while True:
        v = random.randint(1,4)
        if val - v >= 0:
            myList = syl.get(v).split()
            word = random.choice(myList)
            if exclude not in word and include in word:
                line = line + word + " "
                val = val - v
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
    for i in range(mulHaiku):
        print(genLine(syl, 5, exclude, include))
        print(genLine(syl, 7, exclude, include))
        print(genLine(syl, 5, exclude, include))
        
    
if __name__ == "__main__":
    main()
