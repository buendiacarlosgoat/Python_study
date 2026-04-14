import numpy as np


#task 1
#note:random.random 生成的是 0 到 1 之间的均匀分布随机数。random.randn 生成的是围绕 0 上下波动的标准正态分布随机数。
#
a=np.random.randint(1,11,size=[3,2])
b = np.random.random((2, 3)) * 100
c = np.random.randn(3, 3)
d=np.random.randn(5, 3)*10+10                  #广播的方法调标准差和整均值
e = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
val_2_3 = e[2, 3]
val_0_0 = e[0, 0]
print(a)
print(b)
print(f"(3) 标准正态分布数组 c:\n{c}")
print(f"(4) 标准正态分布数组 d:\n{d}")
print(f"(5) 数组 e 下标 (2,3) 的值: {val_2_3}, 下标 (0,0) 的值: {val_0_0}")

arr_dos=np.arange(1,20)
print(f"(2) 索引 9 的元素: {arr_dos[9]}")
print(f"(3)  {arr_dos[4:9]}")
arr_dos[1:18:2] = 50
print(f"(5) 修改后的数组: {arr_dos}")

#task 2:boardcasting



