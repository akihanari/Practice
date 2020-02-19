# %% [markdown]
# リスト

# In[]:
# ・リストの作成
sample = ['a', 'b', 'c', 'd', 'e']
print(sample)

# %% [markdown]
# ・中身が空のリストを作成_1

# In[]:
sample = []
print(sample)

# %% [markdown]
# ・中身が空のリストを作成_2

# In[]:
sample = list()
print(sample)

# %% [markdown]
# ・インデックスを指定して要素を取り出す（リスト名[インデックス]）
# In[]:
sample = ['a', 'b', 'c', 'd', 'e']
print("sample:", sample, "\ntype:", type(sample))
print("sample[0]:", sample[0], "\ntype:", type(sample[0]))

# %% [markdown]
# ・組み込み関数のenumerate()でインデックスと要素の値を組み合わせる
# In[]:
sample = ['a', 'b', 'c']
for a in enumerate(sample):
    print(a)
# 取り出される値はタプルになる

# %% [markdown]
# ・リストのスライス（リスト名[開始:終了:ステップ（間隔）]）
# In[]:
sample = ['a', 'b', 'c', 'd', 'e']
print("sample:", sample)
print("sample[:2:]:", sample[:2:])
print("sample[2::]:", sample[2::])
print("sample[::2]:", sample[::2])
print("sample[1:5:2]:", sample[1:5:2])
# %% [markdown]
# ・リストを逆順にする_1
sample = ['a', 'b', 'c', 'd', 'e']
print("sample:", sample)
print("sample[::-1]:", sample[::-1])

# %% [markdown]
# ・リストを逆順にする_2
sample1 = ['a', 'b', 'c', 'd', 'e']
print("sample1:", sample1)
sample2 = list(reversed(sample1))
print("sample2:", sample2)

# print("sample2:", next(sample2))

# %% [markdown]
# ・末尾に要素を追加

# In[]:
sample = ['a', 'b', 'c', 'd', 'e']
print("sample:", sample, "len:", len(sample))
sample.append('f')
print("sample:", sample, "len:", len(sample))

# %% [markdown]
# ・値の挿入

# In[]:
sample = ['a', 'b', 'c', 'd', 'e']
print("sample:", sample, "len:", len(sample))
sample.insert(3, 'r')
print("sample:", sample, "len:", len(sample))

# %% [markdown]
# ・値の削除_値を指定

# In[]:
sample = ['a', 'b', 'c', 'r', 'd', 'e']
print("sample:", sample, "len:", len(sample))
print("sample.remove('r')を実行")
sample.remove('r')
print("sample:", sample, "len:", len(sample))

# %% [markdown]
# ・値の削除_インデックスを指定

# In[]:
sample = ['a', 'b', 'c', 'r', 'd', 'e']
print("sample:", sample, "len:", len(sample))
print("del sample[3]を実行")
del sample[3]
print("sample:", sample, "len:", len(sample))

# %% [markdown]
# ・コピー_1

# In[]:
sample1 = ['a', 'b', 'c', 'r', 'd', 'e']
sample2 = sample1
print("sample1:", sample1)
print("sample2:", sample2)
del sample1[3]
print("sample1:", sample1)
print("sample2:", sample2)

# %% [markdown]
# ・コピー_2

# In[]:
sample1 = ['a', 'b', 'c', 'r', 'd', 'e']
sample2 = list(sample1)
print("sample1:", sample1)
print("sample2:", sample2)
del sample1[3]
print("sample1:", sample1)
print("sample2:", sample2)

# %% [markdown]
# ・コピー_3

# In[]:
sample1 = ['a', 'b', 'c', 'r', 'd', 'e']
sample2 = sample1.copy()
print("sample:", sample1)
print("sample2:", sample2)
del sample1[3]
print("sample1:", sample1)
print("sample2:", sample2)

# %% [markdown]
# ・連結_1

# In[]:
sample1 = ['a', 'b', 'c']
sample2 = ['d', 'e', 'f']
print("sample1:", sample1)
print("sample2:", sample2)
sample3 = sample1 + sample2
print("sample1:", sample1)
print("sample2:", sample2)
print("sample3:", sample3)

# %% [markdown]
# ・連結_2

# In[]:
sample1 = ['a', 'b', 'c']
sample2 = ['d', 'e', 'f']
print("sample1:", sample1)
print("sample2:", sample2)
sample1 += sample2
print("sample1:", sample1)
print("sample2:", sample2)

# %% [markdown]
# ・連結_3

# In[]:
sample1 = ['a', 'b', 'c']
sample2 = ['d', 'e', 'f']
print("sample1:", sample1)
print("sample2:", sample2)
sample1.extend(sample2)
print("sample1:", sample1)
print("sample2:", sample2)

# %% [markdown]
# ・複数のリストの要素を組み合わせる
# ※タプルとして出力される

# In[]:
sample1 = ['a', 'b', 'c']
sample2 = ['d', 'e', 'f']
print("sample1:", sample1)
print("sample2:", sample2)
for i in zip(sample1, sample2):
    print(i)

# %% [markdown]
# ・アンパック（展開）

# In[]:
sample1 = ['a', 'b', 'c']
sample2 = ['d', 'e', 'f']
print("sample1:", sample1)
print("sample2:", sample2)
for i, j in zip(sample1, sample2):
    print("i:", i, "j:", j)
# In[]:
import numpy as np

sample1 = np.array([1, 2, 3, 4, 5])
print(sample1)

sample2 = np.where(sample1 >= 3)
print(sample2[0])
# In[]:
sample1 = np.array([1, 2, 3])
print(sample1)

sample2 = np.append(sample1, [4, 5])
print(sample2)

# In[]:

# In[]:

# In[]:
