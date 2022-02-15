 # Queston 5

Word='ABCDEFGHIJK'
counter=1

  # First we identify the pattern which says that
  # Leave gaps equal to (counter-1) where counter tells
  # Then row no. and alphabets should decrease after every row

while(counter<7):
    print(" "*(counter-1),Word[0:11-((counter-1)*2)])
    counter=counter+1
print('Done!')
