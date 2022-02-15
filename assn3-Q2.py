 # Question 2

month=int(input('Give month:'))

if(month in[1,3,5,7,8,10,12]):
    day=int(input('Give day:'))
    if(1<=day<=31):
        year=int(input('Give year:'))
        if(1800<=year<=2025):
            print('Date:',day,'/',month,'/',year)
            if(month==12 and day==31):
                print('Next Date:','1/1',year+1)
            elif(day==31):
                print('Next Date:','1/',month+1,'/',year)
            else:
                print('Next Date:',day+1,'/',month,'/',year)
        else:
            print('Invalid year')
    else:
        print('Invalid date')
elif(month in[4,6,9,11]):
     day=int(input('Give day:'))
     if(1<=day<=30):
         year=int(input('Give year:'))
         if(1800<=year<=2025):
            print('Date:',day,'/',month,'/',year)
            if(day==30):
               print('Date:',day,'/',month,'/',year)
         else:
             print('Invalid year')
     else:
         print('Invalid date')
elif(month==2):
    year=int(input('Give year:'))
    if(1800<=year<=2025):
         day=int(input('Give day:'))
         if(year%4==0):
             if(1<=day<=29):
                 print('Date:',day,'/',month,'/',year)
                 if(day==29):
                     print('Next Date:','1/',month+1,'/',year)
                 else:
                     print('Next Date:',day+1,'/',month,'/',year)
             else:
                     print('Invalid day')
         else:
             if(1<=day<=28):
                 print('Date:',day,'/',month,'/',year)
                 if(day==28):
                     print('Next Date:','1/',month+1,'/',year)
                 else:
                     print('Next Date:',day+1,'/',month,'/',year)
             else:
                 print('Invalide day')
    else:
             print('Invalid year')
else:
    print('Invalid month')
print('Done!')
