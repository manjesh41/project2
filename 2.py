'''
WAP which accepts marks of four subjects and display total marks, percentage and grade.
Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail
'''
WPA=int(input('enter the percentage:'))
if  WPA>=70:
    print(f"distinction")
elif WPA>=60:
    print (f"firts")
elif WPA>=40:
    print (f"pass")
else:
    print (f"fail")