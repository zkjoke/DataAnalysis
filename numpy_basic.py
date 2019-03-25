# numpy的基本用法
import numpy as np

# 基于list或者tuple创建数组
arr1 = np.array([1, 2, 3, 4])
print(arr1)

arr_tuple = np.array((1, 2, 3, 4))
print(arr_tuple)

# 创建二维数组
arr2 = np.array([[1, 2, 3, 4], [3, 4, 5, 6]])
print(arr2)

# 基于np.arange创建数组
arr1 = np.arange(5)
print(arr1)

arr2 = np.array([np.arange(3), np.arange(3)])
print(arr2)

# 创建多位数组
arr = np.arange(24).reshape(2, 3, 4)
print(arr)

# np的数据类型转换
print(np.int8(12.23))
print(np.float64(12))
print(np.float(True))
print(bool(1))

# 创建数组时指定数据类型
a = np.arange(5, dtype='float')
print(a)

b = np.arange(6, dtype='D')
print(b)

c = np.array([12.3, 433.324, 212.32], dtype='int16')
print(c)

# 数组相关的一些方法
a = np.array([[1, 2, 3], [7, 8, 9]])
# 数组数量
print(a.ndim)
# 数组尺度，矩阵类型
print(a.shape)
# 数组元素个数
print(a.size)
# 数组各元素所占字节数
print(a.itemsize)
# 数组总共用的字节数
print(a.nbytes)

# 数组的转置玩法
b = np.arange(24).reshape(4, 6)
print(b)
print(b.T)

# 虚数分别获取实部与虚部
d = np.array([1+2j, 3+4j])
print(d)
print(d.real)
print(d.imag)

c = d.flat
for item in c:
    print(item)

print(c[1:])

d.flat=7
print(d)

# 数组的切片与索引
a = np.arange(7)
print(a[1:4])
print(a[:6:2])

b = np.arange(12).reshape(3,4)
print(b[:3, :2])
print('----------')
# 改变数组形状, reshape不会改变数组形状，而resize会
print(b.reshape(4,3))
print(b)
b.resize(4,3)
print(b)

# 多维数组转换一维数组, ravel直接取得实际数组，flatten相当于返回数组的拷贝
b.ravel()[2]=10
print(b.ravel())
b.flatten()[2]=20
print(b.flatten())

# 修改数组形态进行改变
b.shape = (2, 6)
print(b)
# 数组转置，相当于b.T
print(b.transpose())

# 数组内元素统一变化
c = b*2
print(c)

# 数组横向拼接
print(np.hstack((b, c)).shape)
print(np.column_stack((b,c)))
# 数组的垂直拼接
print(np.vstack((b,c)).shape)
print(np.row_stack((b,c)))
print('----------')
# 通过参数设置方向
print(np.concatenate((b,c), axis=0))

# 深度叠加,
arr_dstack = np.dstack((b,c))
print(arr_dstack)

# 数组的拆分
print('----------------------')
print(b)
# 横向拆分，将数组横向拆分后分别放入不同的数组中
# print(np.hsplit(b, 2).shape())
print(np.split(b,2,axis=1))
# 纵向拆分，将数组纵向拆分后分别放入不同的数组中，拆分数目不能超过行数
# print(np.vsplit(b, 2).shape())
print(np.split(b,2,axis=0))


print(arr_dstack)
print(np.dsplit(arr_dstack, 2))
print(np.array([[[ 0],
        [ 1],
        [10],
        [ 3],
        [ 4],
        [ 5]],

       [[ 6],
        [ 7],
        [ 8],
        [ 9],
        [10],
        [11]]]).shape)
# 叠加与拆分的特殊
# 叠加是将多个数组进行拼接，其中的shape对比
# b          (2,6)
# 横向叠加后   (2,12)
# 纵向叠加后   (4,6)
# 深度叠加后   (2,6,2)

# 横向拆分    2个(2,3)数组组成的list
# 纵向拆分    2个(1,6)数组组成的list
# 深度叠加后  2个(2,6,1)数组组成的list

print('--------------')
# 数组转换list
print(b)
print(b.tolist())
# 数组指定数据类型
print(b.astype(float).tolist())

# 数组B
# [[ 0  1 10  3  4  5]
#  [ 6  7  8  9 10 11]]
print('数组最大值：', np.max(b))
print('数组最小值：', np.min(b))
# 返回的一维数组
print('指定数组的最大值：', np.max(b, axis=0))
print('数组的最大偏差值：', np.ptp(b))
print('数组在横向的最大偏值：', np.ptp(b, axis=1))

b.resize(4,3)
print(b)
# [[ 0  1 10]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]
# 每一位的数值为指定方向索引比他小的数值相加。
print('数组指定方向进行累加：', np.cumsum(b, axis=0))
print('数组指定方向进行累积：', np.cumprod(b, axis=0))

# 数组广播，即数组中每一个元素分别进行计算
print('数组广播：', b+2)