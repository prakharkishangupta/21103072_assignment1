#(a) print a list and then remove 4th element from the list and let it print a new list
#(b) remove 'Black' and 'Pink' from the list and replace it with 'Purple'


list=['Red','Green','White','Black','Pink','Yellow']
#(a) part
print('(a)')
print(list)
list.remove('Black')
print(list)

list=['Red','Green','White','Black','Pink','Yellow']
#(b) part
print('(b)')
print(list)
list[3:5]=['Purple']
print(list)
