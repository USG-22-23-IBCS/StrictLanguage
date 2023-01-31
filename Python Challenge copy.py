from graphics import *
def Mablib(self, noun1, noun2, verb, adjective, exclamation):
    self.noun1 = noun1
    self.noun2 = noun2
    self.verb = verb
    self.adjective = adjective
    self.exclamation = exclamation
def noun1():
    return noun1
def noun2():
    return noun2
def verb():
    return verb
def adjective():
    return adjective
def exclamation():
    return exclamation    




noun1 = input('enter a noun: ')
noun2 = input('enter a noun: ')
verb = input('enter a verb: ')
adjective = input('enter an adjective: ')
exclamation = input('enter an exclamtion: ')


def main():
    story = "This morning, my " + noun1 + " woke me up. I woke up, " + verb + ", and ready to go to school. " + noun2 + " was still sleeping. He is so " + adjective + exclamation
    print(story)


if __name__ == "__main__":
    main()
