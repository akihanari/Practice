# In[]:
# クラスの勉強


class Monster:

    def __init__(self, name, luck):
        self.name = name
        self.luck = luck

    def display(self):
        print("Name:", self.name)
        print("Luck:", self.luck)


monster = Monster("アイウ", 12)
monster.display()
# In[]:


class Monster:
    # クラス内で定義した変数...クラス変数（どこからでもアクセスして書き換えられてしまう）
    LUCK_LIMIT = 99

    def __init__(self, name, luck):
        self.name = name
        if(luck > Monster.LUCK_LIMIT):
            print(str(Monster.LUCK_LIMIT) + "より上は指定できません。"
                  + str(Monster.LUCK_LIMIT) + "に設定します。")
            self.luck = Monster.LUCK_LIMIT
        else:
            self.luck = luck

    def display(self):
        print("Name:", self.name)
        print("Luck:", self.luck)


print(Monster.LUCK_LIMIT)
Monster.LUCK_LIMIT = 10  # クラス変数の書き換えができてしまう
monster = Monster("aaa", 122)
monster.display()
print(Monster.LUCK_LIMIT)

# In[]:


class Monster:
    # マングリング
    __LUCK_LIMIT = 99

    def __init__(self, name, luck):
        self.name = name
        if(luck > Monster.__LUCK_LIMIT):
            print(str(Monster.__LUCK_LIMIT) + "より上は指定できません。"
                  + str(Monster.__LUCK_LIMIT) + "に設定します。")
            self.luck = Monster.__LUCK_LIMIT
        else:
            self.luck = luck

    def display(self):
        print("Name:", self.name)
        print("Luck:", self.luck)


monster = Monster("aaa", 122)
monster.display()
monster.luck = 120  # インスタンス変数を直接書き直すことができてしまう
monster.display()
# クラス変数...すべてのインスタンスで使用する変数
# インスタンス変数...インスタンス毎に値が管理されている
# プロパティ...データの参照や設定をするものを制御するときに使う
# In[]:
# ジェネレータ


def fc_sum(n):
    while n < 5:
        yield n
        n += 1


n = fc_sum(0)
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
# print(next(n)) # StopIterationエラーになる
# In[]:
# リストと連携させる


def fc_sum(n):
    while n < 5:
        yield n
        n += 1


print(list(fc_sum(2)))
print([i * i for i in fc_sum(1)])

# In[]:

# In[]:
