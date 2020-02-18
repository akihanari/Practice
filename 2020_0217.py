# %% [markdown]
# **コンプリヘンション（comprehension）**<br>
# **リスト内包表記**<br>
# **[式 for 変数 in リスト if 条件]**<br>

# In[]:
sample_list1 = ['a', 'b', 'c', 'd', 'e']
print(sample_list1)
sample_list2 = [i*3 for i in sample_list1 if i >= 'c']
print(sample_list2)

# %% [markdown]
# **ディクショナリ内包表記**<br>
# **{式 : 式 for 変数 in リスト if 条件}**<br>

# In[]:
sample_dict1 = {'a': 100, 'b': 120, 'c': 200, 'd': 300, 'e': 400}
print(sample_dict1)
sample_dict2 = {i*3 for i in sample_dict1 if i >= 'c'}
print(sample_dict2)

# %% [markdown]
# **セット内包表記**<br>
# **{式 for 変数 in リスト if 条件}**<br>

# In[]:
sample_set1 = {'a', 'b', 'c', 'd', 'e'}
print(sample_set1)
sample_set2 = {i*3 for i in sample_set1 if i >= 'c'}
print(sample_set2)

# %% [markdown]
# **タプル**<br>

# In[]:
sample = ('a', 'b', 'c', 'd', 'e')
print("sample:", sample)
print("type:", type(sample))

# In[]:
sample = ()  # 中身が空
print("sample:", sample)
print("type:", type(sample))

# In[]:
sample = ('a')  # 要素が1つだけの場合は後ろに','をつけないとタプルにならない
print("sample:", sample)
print("type:", type(sample))

# In[]:
sample = ('a',)  # 要素が1つだけの場合は後ろに','をつける
print("sample:", sample)
print("type:", type(sample))

# In[]:
sample = 'a',  # ()を省略
print("sample:", sample)
print("type:", type(sample))

# In[]:
sample = list(['a', 'b', 'c'])  # タプル⇒リスト
print("sample:", sample)
print("type:", type(sample))

# In[]:
sample = tuple(['a', 'b', 'c'])  # リスト⇒タプル
print("sample:", sample)
print("type:", type(sample))

# In[]:
sample = ('a', 'b', 'c', 'd', 'e')
print("sample:", sample)
print("type:", type(sample))
print("sample[0]:", sample[0])  # インデックスを指定して要素を取り出す
print("type:", type(sample[0]))

# In[]:
sample = 'a', 'b', 'c'
print(type(sample))
for a in enumerate(sample):
    print("a:", a)


# In[]:
sample = ('a', 'b', 'c', 'd', 'e')
print(sample)
print(sample[2:5:2])  # タプル名[開始:終了:ステップ(間隔)]


# In[]:

# In[]:

# In[]:

# In[]:

# In[]:

# In[]:

# In[]:

# In[]:

# In[]:
