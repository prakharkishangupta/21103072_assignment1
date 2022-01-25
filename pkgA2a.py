# Assignment-2
# Question-1

# take input "Python is case sensitive language"
input_string = input('Enter the string:')
# (a)
print('Part A:')
print('Length of string is:',len(input_string))

# (b)
print('Part B:')
print('Reverse of string is;',"'",input_string[::-1],"'")

# (c)
print('Part C:')
# "a case sensitive " has index value 9 to 26
new_string = input_string[slice(9,26)]
print('New string is:',"'",new_string,"'")

# (d)
print('Part D:')
replaced_string = input_string.replace('a case sensitive ','object oriented ')
print(replaced_string)

# (e)
print('Part E:')
print('Index of (a) in given input string is:',input_string.index('a'))

# (f)
print('Part F:')
print(input_string.replace(' ',''))
