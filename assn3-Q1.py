 # Question 1

string=input('Give a string:')
list1=[]
list2=string.split()
y=len(list2)
d=dict()
t=dict()
if len(list2)==1:         #it is for one word
    for i in string:      #here i is creating a list with the characters
        list1.append(i)
    for j in list1:       #here i is creating a condition where all unique keys
        if j in d:        #get value 1 and when a key repeats it increases
          d[j]=d[j]+1     #value by 1
        else:
            d[j]=1
    print(d)

else:
    for i in list2:       #this is for multiple words
        if i in t:
            t[i]=t[i]+1
        else:
            t[i]=1
    print(t)
print('Done!')


             
    
