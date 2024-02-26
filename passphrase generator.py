#generates a passphrase of 5 random words from a list and combines them together,separating them with hyphens
import random

def genpass(wordsread=5): #change the 5 to however many words you want
    with open('list.txt', 'r') as file: #replace the name
        listofwords = file.readlines()
    words = [word.strip() for word in listofwords]
    words4phrase = random.sample(words, wordsread)
    return '-'.join(words4phrase)

passphrase = genpass()
print(passphrase)
