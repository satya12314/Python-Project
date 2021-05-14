import random
words=['rainbow','computer','geeks','programming','board']
word=random.choice(words)
# print(word)
print('guess the character ')
guessed_word=''
chance=13
while chance>0:
    failed=0
    for i in word:
        if i in guessed_word:
            print(i)
        else:
            print('-')
            failed+=1
    if failed==0:
        print('I win')
        print('Word is : ',word)
        break
    guess=input('Enter the character : ')
    guessed_word+=guess
    if guess not in word:
        chance-=1
        print('Wrong Prediction')
        print('Remaining chances : ',chance)
        if chance==0:
            print('I Loose')

