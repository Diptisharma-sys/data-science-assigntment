students_data=[90,100,44.5,66,77,88,44,55,33,32,45,6,78,22,87,66,77,56,78,54,43,23,45,78,
               99,88,77,65,43,22,33,44,55,33.9,45,67,89,98,76,54,32,11,22,33,99.5,44,96,88,55,66]
count = len(students_data)
total=0
for i in students_data:
    total+=i
mean = total/count
print("Mean=",mean)

students_data.sort()
if count % 2 == 0:         
    median = (students_data[count//2 - 1] + students_data[count//2]) / 2
else:                 
    median = students_data[count//2]

print("Median =", median)