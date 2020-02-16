# %% [markdown]
# **リスト**<br>

# In[]:
sample_list = [1, 2, 3, 4, 5]
print("sample_list:", sample_list)
print("type:", type(sample_list))
print("sample_list[0]:", sample_list[0])

# %% [markdown]
# **タプル**<br>

# In[]:
sample_tuple = (1, 2, 3, 4, 5)
print("sample_tuple:", sample_tuple)
print("type:", type(sample_tuple))
print("sample_tuple[4]:", sample_tuple[4])

# %% [markdown]
# **ディクショナリ**<br>

# In[]:
sample_dict = {100:"apple:", 200:"orange", 300:"strawberry"}
print("sample_dict:", sample_dict)
print("type:", type(sample_dict))
print("sample_dict[200]:", sample_dict[200])
# In[]:
# **セット**<br>

# In[]:
sample_set = {1, 2, 2, 3, 4, 5, 5, 5, 4}
print("sample_set:", sample_set)
print("type:", type(sample_set))
# In[]:

# %% [markdown]
# **リスト**<br>

# In[]:
sample_list1 = []
print("sample_list1:", sample_list1, "type:",type(sample_list1))
# In[]:
sample_list1.append(1)
sample_list1.append(2)
sample_list1.append(3)
print("sample_list1:", sample_list1)
# In[]:
sample_list1.insert(0,0)
print("sample_list1:", sample_list1)
# In[]:
sample_list1.remove(3)
print("sample_list1:", sample_list1)
# In[]:
sample_list2 = sample_list1.copy() #新しいリストにコピー
# print("sample_list2:", sample_list2)
print("sample_list1 is sample_list2:", sample_list1 is sample_list2) #False
# In[]:
sample_list3 = sample_list1 #リストの情報をコピー
# print("sample_list3:", sample_list3)
print("sample_list1 is sample_list3:", sample_list1 is sample_list3) #True
# In[]:
sample_list4 = list(sample_list1) #新しいリストにコピー
# print("sample_list4:", sample_list4)
print("sample_list1 is sample_list4:", sample_list1 is sample_list4) #False
# In[]:
#del sample_list1


# In[]:

# In[]:
