data = [20,30,60,99,88,41,33,22,33,78,99,65,43,23,11,88,66,44,55,66,77,55,44,33,
                22,11,89,67,54,34,23,12,34,67,55,44,33,22,11,66,77,88,99,100,99,88,77,65,43,21]

data.sort()
n = len(data)

#mean
mean = sum(data) / n

#median
if n% 2 == 0:
    median = (data[n//2 - 1] + data[n//2]) / 2
else:
    median = data[n//2]

#Q1
lower_half = data[:n//2]
if len(lower_half) % 2 == 0:
    q1 = (lower_half[len(lower_half)//2 - 1] + lower_half[len(lower_half)//2]) / 2
else:
    q1 = lower_half[len(lower_half)//2]

# Q3 
upper_half = data[n//2:]
if len(upper_half) % 2 == 0:
    q3 = (upper_half[len(upper_half)//2 - 1] + upper_half[len(upper_half)//2]) / 2
else:
    q3 = upper_half[len(upper_half)//2]

#IQR
iqr = q3 - q1

print("Mean:", mean)
print("Median (Q2):", median)
print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)
