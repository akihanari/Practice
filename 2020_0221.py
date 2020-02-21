# In[]:
# numpyをimport
import numpy as np

# N枚の円形の餅がある。整数で入力
N = int(input())
# print("N:", N)
# 各餅の直径を整数で入力、N個の要素を持つリストdに格納
d = np.array([int(input()) for i in range(N)])
# print("d:", d)

# リストdから重複を削除、昇順にソート
d_uni = np.unique(d)

# 鏡餅の最大の段数を出力（d_uniに重複した要素はないので、len()で要素数を出せばよい）
print(len(d_uni))

# %% [markdown]
# セット（集合）

# %% [markdown]
# 【セットの作成】
#  セット名 = {値1, 値2, ...}

# In[]:
sample = {"札幌", "東京", "大阪", "那覇"}
print(sample, type(sample))

# In[]:
sample = {"札幌", "東京", "大阪", "那覇", "東京", "那覇", "那覇"}
print(sample, type(sample))

# %% [markdown]
# 【リストからセットを作成】
#  set()

# In[]:
sample1 = ["札幌", "東京", "大阪", "那覇"]
print("sample1:", sample1, type(sample1))
sample2 = set(sample1)
print("sample2:", sample2, type(sample2))

# %% [markdown]
# 【中身が空のセットを作成】
#  セット名 = set()

# In[]:
sample = set()
print(sample, type(sample))

# %% [markdown]
# 組み込み関数のenumerate()でインデックスと要素を組み合わせる
# In[]:
sample = {"札幌", "東京", "大阪", "那覇"}
for a in enumerate(sample):
    print(a)
# 取り出される値はタプルになる

# %% [markdown]
# 【要素の変更】
# ⇒できない

# In[]:

# %% [markdown]
# 【要素の追加】
# セット名.add(値)

# In[]:
sample = {"札幌", "東京", "大阪", "那覇"}
print("sample:", sample)
sample.add("福岡")
print("sample:", sample)

# %% [markdown]
# 【要素を削除】
# セット名.remove(値)

# In[]:
sample = {"札幌", "東京", "大阪", "那覇"}
print("sample:", sample)
sample.remove("東京")
print("sample:", sample)


# %% [markdown]
# 【集合演算】

# %% [markdown]
# 【和集合：A∪B】
#  演算子... A | B
#  メソッド... A.union(B)
# AとBのすべての要素

# In[]:
A = {1, 2, 3, 4, 5}
print("A:", A)
B = {4, 5, 6, 7, 8}
print("B:", B)
print("A | B:", A | B)
print("A.union(B):", A.union(B))

# %% [markdown]
# 【共通部分：A∩B】
#  演算子... A & B
#  メソッド... A.intersection(B)
# AとBの共通要素
# In[]:

A = {1, 2, 3, 4, 5}
print("A:", A)
B = {4, 5, 6, 7, 8}
print("B:", B)
print("A & B:", A & B)
print("A.intersection(B):", A.intersection(B))

# %% [markdown]
# 【差集合：A-B】
#  演算子... A - B
#  メソッド... A.difference(B)
# AにあってBにない要素

# In[]:
A = {1, 2, 3, 4, 5}
print("A:", A)
B = {4, 5, 6, 7, 8}
print("B:", B)
print("A - B:", A - B)
print("A.difference(B):", A.difference(B))

# %% [markdown]
# 【対象差：A△B】
#  演算子... A ^ B
#  メソッド... A.symmetric_difference(B)
# AとBどちらかのみに含まれる要素

# In[]:
A = {1, 2, 3, 4, 5}
print("A:", A)
B = {4, 5, 6, 7, 8}
print("B:", B)
print("A ^ B:", A ^ B)
print("A.symmetric_difference(B):", A.symmetric_difference(B))

# In[]:
# {式 : 式 for 変数名 in イテレート可能なオブジェクト if 条件式}
fruits = ["apple", "grape", "lemon"]
print("fruits:", fruits)
colors = ["red", "purple", "yellow"]
print("colors:", colors)
fruits_dic = {f: c for (f, c) in zip(fruits, colors)}
print("fruits_dic:", fruits_dic)

# In[]:
# {式 for 変数名 in イテレート可能なオブジェクト if 条件式}
num_list = [0, 1, 1, 2, 3, 4, 5, 5, 5]
print("num_list:", num_list)
num_set = {i * 2 for i in num_list if i >= 2}
print("num_set:", num_set)

# In[]:
# (式 for 変数名 in イテレート可能なオブジェクト if 条件式)
num_gene = (i*i for i in range(10) if i % 3 == 0)

print(next(num_gene))
print(next(num_gene))
print(next(num_gene))
print(next(num_gene))

# In[]:
sample_list = ["a", "p", "p", "l", "e"]
for i in sample_list:
    print(i)

# In[]:
sample_tuple = (1, 2, 3, 4, 5)
for i in sample_tuple:
    print(i)

# In[]:
for i in range(5):
    print(i)

# In[]:
sample_list = ["a", "b", "c"]
print("sample_list:", sample_list, "type:", type(sample_list))
sample_iter = iter(sample_list)
print("sample_iter:", sample_iter, "\ntype:", type(sample_iter))
print(next(sample_iter))
print(next(sample_iter))
print(next(sample_iter))
# StopIteration
print(next(sample_iter))
# In[]:
sample_list = ["a", "b", "c"]
print("sample_list:", sample_list, "type:", type(sample_list))
sample_iter = iter(sample_list)
print("sample_iter:", sample_iter, "\ntype:", type(sample_iter))
for i in sample_iter:
    print(i)

# In[]:
sample_list = ["a", "b", "c"]
print("sample_list:", sample_list, "type:", type(sample_list))
# イテレータ
sample_iter = iter(sample_list)
print(next(sample_iter))
# イテレータでない（イテラブルなオブジェクトではある）
print(next(sample_list))

# In[]:
sample_list = ["a", "b", "c"]
print("sample_list:", sample_list)
sample_iter = iter(sample_list)
print(next(sample_iter))

print("--for文--")
for i in sample_list:
    print(i)
print("----")

print(next(sample_iter))  # 取り出された状態を保持
print(next(sample_iter))
# In[]:
sample_list = ["a", "b", "c"]
print("sample_list:", sample_list)
sample_iter = iter(sample_list)

print("--1回目--")
for i in sample_iter:
    print(i)

print("--2回目--")
for i in sample_iter:
    print(i)

# In[]:

# In[]:

# In[]:
