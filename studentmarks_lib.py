import numpy as np
data = [20,30,60,99,88,41,33,22,33,78,99,65,43,23,11,88,66,44,55,66,77,55,44,33,
                22,11,89,67,54,34,23,12,34,67,55,44,33,22,11,66,77,88,99,100,99,88,77,65,43,21]

data =np.sort(data)
mean = np.mean(data)
median = np.median(data)
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
iqr = q3 - q1

print("Mean =", mean)
print("Median =", median)
print("Q1 =", q1)
print("Q3 =", q3)
print("Interquartile Range (IQR) =", iqr)