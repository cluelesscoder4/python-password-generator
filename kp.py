import random

def generate_passphrase(num_words=8):
    with open('output.txt', 'r') as file:
        word_list = file.readlines()
    words = [word.strip() for word in word_list]
    passphrase_words = random.sample(words, num_words)
    return '-'.join(passphrase_words)

passphrase = generate_passphrase()
print(passphrase)
