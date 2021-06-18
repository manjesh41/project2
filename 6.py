'''

Given a positive real number, print its fractional part.
'''
a=int(input('enter the frational number:'))
b=int(a)
c=1
for i in range(a):
    c=b*c
    c-=1
print(f'the fractional of real num {a} is = {c}')