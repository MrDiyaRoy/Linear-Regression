import numpy as np

#Training Data
data = np.array([(17,94),(13,73),(12,59),(15,80),(16,93),(14,85),(16,66),(16,79),(18,77),(19,91)])

print("  X  Y  ")

print(data)

n = data.shape[0] #returns tuple

mean = data.sum(axis = 0)/n #returns array

diff = data - mean #array subtraction

mul_diff = np.multiply(diff[:, 0], diff[:, 1])

diff_squ = diff**2

r1 = mul_diff.sum(axis = 0)

r2 = diff_squ.sum(axis = 0)

r3 = np.multiply(r2[0], r2[1])

r4 = np.sqrt(r3)

r = r1/r4

sy = ((r2[1])/(n-1))**(1/2)

sx = ((r2[0])/(n-1))**(1/2)

m = r*(sy/sx)

c = mean[1]  - m*mean[0]

#User Input or Test data
x = int(input("Enter the value of X :- "))

y = m*x + c

#Prediction
print(y)