# Question 6

   # Inputing a word from the first friend
word = input('Enter the word:')
word = word.lower()

   # Inputing the meaningfull word with exact same letter
testword = input('Enter the new meaningfull word with exact same letters to test your friendship:')
testword = testword.lower()
   # Defining dictionary
def count_in_dict(word):
    count = {}
    list1 = list(word)

    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count
   # Shopkeeper's input to verify the word's meaning
def userinput():
    if count_in_dict(word) != count_in_dict(testword):
        print("The letters aren't exact, friendship is fake")
        return
    ans = input('Does the word make sense?(y/Y or n/N)')

    if ans == 'y' or ans == 'Y':
        print('The friends pass the friendship test')
    elif ans == 'n' or ans == 'N':
        print("The word doesn't have a meaning, friendsip is fake")
    else:
        print('Invalid input, try again with y/Y or n/N')
        userinput()
userinput()
