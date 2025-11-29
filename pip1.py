import numpy as np
a=np.array([1,2,3,4,5])
print(a)
print(a[2])
b=np.array([[1,2,3],[4,5,6]])
print(b)
#ndarray.ndim     #gives dimension
#ndarray.shape
#ndarray.size
#ndarray.dtype
print(b.shape)
zeros_arr=np.zeros((3,3))
print(zeros_arr)
range_arr=np.arange(1,10)
print(range_arr)
linspace_arr=np.linspace(0,1,5)
print(linspace_arr)
print("Hello")
matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix)
print(matrix[1,2])
print(matrix[0:1])
print(range_arr[2:5])
data=np.array([10,20,30,40,50])
condition=data>25
print("Condition:",condition)
print("Selected elements:",data[condition])       #or data[data>25]
scores=np.array([88,92,75,95,64,85,92])
print(np.max(scores))
print(min(scores))
print(np.max(matrix))
print(np.mean(scores))
std_dev=np.std(scores)      #standard deviation
print(f"standard deviation:{std_dev:.2f}")
#np.median()
#np.var() -calculates variance which is square of std deviation
print(np.prod(scores))
c=a+data
print(c)
print(a*data)
print(data**a)