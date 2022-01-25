# Question-6

# Define the sides of a triangle with variables a,b and c.
side1=int(input('Enter the length of side a:'))
side2=int(input('Enter the length of side b:'))
side3=int(input('Enter the length of side c:'))
# using conditional statement
# any of three sides shouldn't greater than the sum of the other two sides
if ((side3)<((side1)+(side2))) and ((side2)<((side1)+(side3))) and ((side1)<((side2)+(side3))):
    print('Yes')
else:
    print('No')
