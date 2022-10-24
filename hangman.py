import random
def hangman(word):
    counter=1
    old_geuss=""
    count=""
    testlist=list(range(len(word)))
    while (counter < 7):

        geuss=input("geuss a letter: ")
        i=0
        if (geuss in word):


            i=word.index(geuss)
            testlist[i] = geuss
            print(testlist)
        else:
            counter += 1
        if testlist == word:
            print("you win")
            break
    print("you lose")




words = ['ahmed', 'car', 'watch', 'mobile']
x = random.randrange(0,3)
name=input("enter your name: ")
word=words[x]
hangman(word)
