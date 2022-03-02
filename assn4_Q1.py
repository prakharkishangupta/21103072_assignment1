# Question 1

def TowerOfHanoi(n , from_rod , to_rod , middle_rod):
    if n==0:
           return
    TowerOfHanoi(n-1 ,from_rod , to_rod , middle_rod)
    print('Move disk',n,'from rod',from_rod,'to rod',to_rod)
    TowerOfHanoi(n-1 , middle_rod, to_rod, from_rod)
n=3
TowerOfHanoi(n, 'A', 'C', 'B')
print('\n')
