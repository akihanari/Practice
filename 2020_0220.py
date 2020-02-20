# %% [markdown]
# ディクショナリ

# In[]:
# 【ディクショナリの作成】
#  {キー1, 値1, キー2, 値2,...}
# sample = {"札幌": "晴れ", "新潟": "曇り", "仙台": "曇り", "東京": "晴れ",
#                 "金沢": "雨", "名古屋": "晴れ", "大阪": "晴れ", "広島": "曇り",
#                 "高知": "曇り", "福岡": "晴れ", "那覇": "曇り"}
# In[]:
sample = {"札幌": "雨", "東京": "晴", "大阪": "晴", "那覇": "曇"}
print(sample)

# %% [markdown]
# 【中身が空の辞書を作成】

# %% [markdown]
# ・その1... {}

# In[]:
sample = {}
print(sample, type(sample))

# %% [markdown]
# ・その2... dict()

# In[]:
sample = dict()
print(sample, type(sample))

# %% [markdown]
# 【要素を取り出す】
#  辞書名[キー]
# In[]:
sample = {"札幌": "雨", "東京": "晴", "大阪": "晴", "那覇": "曇"}
print("sample:", sample)
print("sample[札幌]:", sample["札幌"])

# %% [markdown]
# ・組み込み関数のenumerate()でインデックスとキーの値を組み合わせる
# In[]:
sample = {"札幌": "雨", "東京": "晴", "大阪": "晴", "那覇": "曇"}
for a in enumerate(sample):
    print(a)
# 取り出される値はタプルになる

# %% [markdown]
# 【要素（キーと値）を変更】
# 辞書名[キー] = 値 ※キーが存在する場合

# In[]:
sample = {"札幌": "雨", "東京": "晴", "大阪": "晴", "那覇": "曇"}
print("sample:", sample)
sample["札幌"] = "晴"
print("sample:", sample)

# %% [markdown]
# 【要素（キーと値）を追加】
# 辞書名[キー] = 値 ※キーが存在しない場合

# In[]:
sample = {"札幌": "雨", "東京": "晴", "大阪": "晴", "那覇": "曇"}
print("sample:", sample)
sample["福岡"] = "晴"
print("sample:", sample)

# %% [markdown]
# 【要素（キーと値）を削除】
# del 辞書名[キー]

# In[]:
sample = {"札幌": "雨", "東京": "晴", "大阪": "晴", "那覇": "曇"}
print("sample:", sample)
del sample["大阪"]
print("sample:", sample)


# %% [markdown]
# 【辞書内のすべてのキーを取り出す】
#  辞書名.keys()

# In[]:
sample = {"札幌": "雨", "東京": "晴", "大阪": "晴", "那覇": "曇"}
print("sample:", sample)
print(list(sample.keys()))

# In[]:
sample = {"札幌": "雨", "東京": "晴", "大阪": "晴", "那覇": "曇"}
print("sample:", sample)
for i in sample.keys():
    print(i)

# %% [markdown]
# 【辞書内のすべての値を取り出す】
#  辞書名.values()

# In[]:
sample = {"札幌": "雨", "東京": "晴", "大阪": "晴", "那覇": "曇"}
print("sample:", sample)
print(list(sample.values()))

# In[]:
sample = {"札幌": "雨", "東京": "晴", "大阪": "晴", "那覇": "曇"}
print("sample:", sample)
for i in sample.values():
    print(i)

# %% [markdown]
# 【辞書内のすべてのキーと値を取り出す】
#  辞書名.items()

# In[]:
sample = {"札幌": "雨", "東京": "晴", "大阪": "晴", "那覇": "曇"}
print("sample:", sample)
print(list(sample.items()))

# In[]:
sample = {"札幌": "雨", "東京": "晴", "大阪": "晴", "那覇": "曇"}
print("sample:", sample)
for i in sample.items():
    print(i)
# In[]:

# In[]:
