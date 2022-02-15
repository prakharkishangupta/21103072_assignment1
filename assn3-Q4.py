 # Question 4
 # Here we create if else statements

Grade_points=int(input('Give a no. between 4 and 10 including them:'))
if(Grade_points==4):
    print('Performance=Poor')
    print('Letter Grade=D')
elif(Grade_points==5):
    print('Performance=Below Average')
    print('Letter Grade=C')
elif(Grade_points==6):
    print('Performance=Average')
    print('Letter Grade=C+')
elif(Grade_points==7):
    print('Performance=Good')
    print('Letter Grade=B')
elif(Grade_points==8):
    print('Performance=Very Good')
    print('Letter Grade=B+')
elif(Grade_points==9):
    print('Performance=Excellent')
    print('Letter Grade=A')
elif(Grade_points==10):
    print('Performance=Outstanding')
    print('Letter Grade=A+')
else:
    print('Error')
print('Done!')
