'''
Develop a program that asks for 3 school grades, and if the average is higher or equal to 5 show a message "Approved Student"
'''
grade1 = int(input("Introduce the first note: "))
grade2 = int(input("Introduce the second note: "))
grade3 = int(input("Introduce the third note: "))

average = (grade1+grade2+grade3)/3
round(average,2)

if average>=5 :
    print(f"Yor average is: {average} , Approved Student ")
else:
    print(f"Yor average is: {average} , Not Approved Student ")
