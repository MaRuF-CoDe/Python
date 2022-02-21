student_height = (input("Input a list of student heights ")).split()
for n in range(0,len(student_height)):
    student_height[n] = int(student_height[n])
print(student_height)
count = 0
sum = 0
for student in student_height:
    sum += int(student) 
    count = count + 1

avg = round(sum/count)

print(avg)