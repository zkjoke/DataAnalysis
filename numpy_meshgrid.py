# 向量与矩阵的使用

# 加载数据
import numpy as np
import matplotlib.pyplot as plt

m, n = (5, 3)
x = np.linspace(0, 1, m)
y = np.linspace(0, 1, n)
X, Y = np.meshgrid(x, y)

print('输出向量x和y')
print(x)
print(y)

print('输出矩阵X和Y')
print(X)
print(Y)

print('矩阵的大小')
print(X.shape)
print(Y.shape)

plt.plot(X, Y, marker='.', color='blue', linestyle='none')
plt.show()

# 坐标点数据
z = [i for i in zip(X.flat, Y.flat)]
print(z)