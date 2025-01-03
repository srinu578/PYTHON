import numpy as np
# 1 slicing and indexing
arr = np.random.randint(0,100,(4,4))
print("original array:\n",arr)
print("first 2 rows:\n",arr[:2])
print("last 2 colums:\n",arr[:,-2:])
arr[arr>50] =-1
print("modified array:\n",arr)


# 2 stastical operations

arr = np.array([[10,20,30],[40,50,60]])
print("mean:",np.mean(arr))
print("standard division",np.std(arr))
print("row-wise sum",np.sum(arr,axis=1))
print("column-wise sum",np.sum(arr,axis=0))

# 3 random numbers and normalization

rand_arr = np.random.random((2,5))
print("random array:\n",rand_arr)
norm_arr=(rand_arr-rand_arr.min())/(rand_arr.max()-rand_arr.min())
print("normalized array:\n",norm_arr)


# 4 matrix operations

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print("dot product:\n",np.dot(A,B))
print("transpose of a:\n",A.T)
print("transpose of a:\n",B.T)


# 5 sorting and searching

arr= np.random.randint(0,100,10)
print("original array:\n",arr)
print("sorting array:\n",np.sort(arr))
value=50
print("indices of value 50:",np.where(arr==value))


# 6 solving linear equations

A=np.array([[3,1],[1,2]])
B=np.array([9,8])
x=np.linalg.solve(A,B)
print("soluton x:",x)

# # 7 checkeboard pattern

checkeboard=np.zeros((6,6),dtype=int)
checkeboard[1::2,::2]=1
checkeboard[::2,1::2]=1
print("checkeboard pattern:\n",checkeboard)
