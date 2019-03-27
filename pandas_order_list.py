# 根据指定的 list 所包含元素比 Dataframe 中需要排序的列的元素的多或少，可以分为三种情况:
# • 相等的情况下，可以使用reorder_categories和set_categories方法;
# • list的元素比较多的情况下，可以使用set_categories方法;
# • list的元素比较少的情况下，也可以使用set_categories方法，但list中没有的元素会在DataFrame中以 NaN 表示。

# 将pandas中的Series类型转换按照某一个list进行排序
import pandas as pd

# 第一种情况，list元素与map一致
s = pd.Series({'a':1, 'b':2, 'c':3})
print(s)

# 将series转变为dataframe类型
list_custom = ['b', 'a', 'c']

df = pd.DataFrame(s)
df = df.reset_index()
df.columns = ['words', 'number']

df['words'] = df['words'].astype('category')

df['words'].cat.reorder_categories(list_custom, inplace=True)

df.sort_values('words', inplace=True)
print(df)

# 第二种情况，list元素比map多
# 第三种情况，list元素比map少,找不到的元素默认按照NAN展示，并展示在最后位置。
list_custom_new = ['d', 'c', 'a', 'e']
dict_new = {'e':1, 'b':2, 'c':3}

df_new = pd.DataFrame(list(dict_new.items()), columns=['words', 'value'])

print(list_custom_new)
df_new.sort_values('words', inplace=True)

df_new['words'] = df_new['words'].astype('category')
df_new['words'].cat.set_categories(list_custom_new, inplace=True)

print(df_new['words'])

df_new.sort_values('words', inplace=True, ascending=True)

print(df_new)

