 # Question 6
 # Run the whole 6th quiz in one go
student_info=dict()
n='y'
alistsid=[]
listsid=[]

 # (a)
 # here i have used the if statement so that i can exit the loop whenever i want
 # I am making a list along with the dictionary which will help us in further parts 
print('    (a)    ')
while(n=='y'):
    sid=int(input('Give the sid:'))
    if sid in listsid:
        print('Error!run the code again and enter a different sid!')
        break
    listsid.append(sid)
    name=input('Enter your name:')
    student_info[sid]=name
    n=input('Give a letter y or n:')
    alistsid.append((sid,name))
print('The required dictionary:',student_info)
print('The list will be used in furder parts:')
print('The required list:',alistsid)
print('Done!')    

 # (b)
 # to sort our dictionary based to names we iterate dict.items() twice each
 # time inversing the key value pair and we will form a list which can be sorted
 # and converted back to dictionary hence we get the required dictionary
print('    (b)    ')
print('The dictionary we had:')
print(student_info)
   # here we exchange the key value pair and make a new dictionary and a new list
newdict=dict()
alistname=[]
   # here we iterate
for (k,v) in student_info.items():
    newdict[v]=k
    alistname.append((v,k))
print('now we have exchanged the key value pair but its not sorted:')
   # our dict and list are both not sorted
print(newdict)
print('The unsorted list:')
print(alistname)
alistname.sort()
   # sorted list
print('The sorted list:')
print(alistname)
   # here we create a sorted dictionary from our sorted list
print('The sorted dictionary:')
sorted_dict=dict(alistname)
print(sorted_dict)
   # now we need to exchange the key value pair of the sorted_dict to get our required dictionary
required_dict_name=dict()
for (k,v) in sorted_dict.items():
    required_dict_name[v]=k
print('This is the dictionary sorted on the basis of name:')
print(required_dict_name)
print('Done!')

 # (c)
 # sort the dictionary on the basis of sid
 # first we sort the list and then convert it in to dictionary
print('    (c)   ')
print('The list we made before will be used now:')
print(alistsid)
alistsid.sort()
print('now the list is sorted:')
print(alistsid)
sorted_student_info_sid=dict(alistsid)
print('Sorted dictionary based on sid:',sorted_student_info_sid)
print('Done!')

 # (d)
 # here i search the name of the student with key value or sid as 21103072
print('    (d)    ')
entered_sid=int(input('Enter one of the sids you entered before:'))
print('Name of the student with the entered sid:')
print(student_info[entered_sid])
print('Done!')
    
