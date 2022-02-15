 # Question 8

set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}

 # (a)
print('*(a)*')
required_set=set1^set2
print(required_set)
print('Done!')

 # (b)
print('*(b)*')
required_set=set1^(set2^set3)
print(required_set)
print('Done!')

 # (c)
print('*(c)*')
required_set=(set1&set2)|(set2&set3)|(set1&set3)
print(required_set)
print('Done!')

 # (d)
print('*(d)*')
new_set={1,2,3,4,5,6,7,8,9,10}
required_set=new_set-set1
print(required_set)
print('Done!')

 # (e)
print('*(e)*')
required_set=new_set-(set1|set2|set3)
print(required_set)
print('Done!')
