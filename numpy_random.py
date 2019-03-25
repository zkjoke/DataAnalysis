# numpy的随机函数用法

import numpy as np

# 随机生成0～1的多维数组rand
print(np.random.rand(4, 3))

# 返回符合标准正态分布的多维数组
# 标准正态分布：standardnormaldistribution， 标准正态分布又称为u分布，是以0为均值、以1为标准差的正态分布，记为N(0，1)。
snd = np.random.randn(2, 4)
print('符合标准正态分布：', snd)

# 随机整数
print(np.random.randint(1, 10, 5, 'int8'))
print('随机多维数组：', np.random.randint(1, 10, (3, 4)))

# 生成[0,1)之间的浮点数
print('----------random_sample------------')
print(np.random.random_sample((2, 3)))
print('----------random------------')
print(np.random.random((2, 3)))
print('----------ranf------------')
print(np.random.ranf((2, 3)))
print('----------sample------------')
print(np.random.sample((2, 3)))

# 从指定一维数组之中生成随机数
print('-------从指定一维数组中生成随机数----------')
print(np.random.choice(5, (3, 2), replace=True))
# 从人员中进行随机呢？
demo_list = ['a', 'b', 'c', 'd']
print(np.random.choice(demo_list,size=(2,2), replace=False))

# random_seed，类似于加上一个密钥指向。相同密钥打开的东西相通
np.random.seed(1)
print(np.random.rand(5))

np.random.seed(1995)
print(np.random.rand(5))

np.random.seed(1995)
print(np.random.rand(5))