# pandas日期相关使用

import pandas as pd

df = pd.read_csv('date.csv', header=None)

# print(df.tail(2))
# 设定各行表头
df.columns = ['date', 'number', 'sign']
# 转换日期格式
df['date'] = pd.to_datetime(df['date'])
# 将date设为index
df = df.set_index('date')
print(df.head(2))
print(df.shape)

print(type(df))
print(df.index)
print(type(df.index))

# 构造series数据
s = pd.Series(df['sign'], index=df.index)
print(type(s))
print(s.head(2))

# 获取某一年的数据
print('------------获取2013年的数据---------')
print(df['2013'].head(2))

# 获取某个时间段的数据
print('------------获取2013年到2014年的数据---------')
print(df['2013':'2014'].head(2))
print(df['2013':'2014'].tail(2))

# 获取某月的数据
print('------------获取某月的数据---------')
print(df['2013-10'].tail(2))

# 获取某天的数据
print('------------获取某天的数据---------')
print(s['2013-10-30'])
print(df['2013-10-30':'2013-10-30'])

# 以某个时间点来获取数据
# 注意，数据之前的时间是201510，所以取2015-10之后的数据
print('-------------获取某个时间之前或者之后的数据--------------')
print('------after--------')
print(df.truncate(before='2015-04'))
print('-----------before------------')
print(df.truncate(after='2015-04'))

# pandas日期处理函数to_period
df_period = df.to_period('M')
print(df_period.head(2))
print(df.to_period('Q').head(2))
print(df.to_period('Y').head(2))

# 按照频率展示
# A默认是A-DEC,不要末尾年份，A-JAN不要开始年份。
print(df_period.index.asfreq('A'))
print(df_period.index.asfreq('A-JAN'))
#Q、Q-SEP、Q-JAN分别为不要末尾、不要开始、不要开始和末尾。
print(df_period.index.asfreq('Q'))
print(df_period.index.asfreq('Q-SEP'))
print(df_period.index.asfreq('Q-JAN'))
# 按月和日展示
print(df_period.index.asfreq('M'))
print(df_period.index.asfreq('B', how='start'))
print(df_period.index.asfreq('B', how='end'))

# 按时间维度汇总数据
print(df.resample('w').sum().head())
print(df.resample('M').sum().to_period('M'))
print(df.resample('Q').sum().to_period('Q'))
print(df.resample('AS').sum().to_period('A'))



