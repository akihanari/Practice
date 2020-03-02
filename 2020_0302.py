# In[]:


class SampleClass:
    count = 0  # クラス変数

    def __init__(self, name, money):  # コンストラクタ
        SampleClass.count += 1
        self.name = name
        self.money = money

    def getName(self):  # インスタンスメソッド
        return self.name

    def getMoney(self):  # インスタンスメソッド
        return self.money

    @classmethod
    def getCount(cls):  # クラスメソッド
        return cls.count


p1 = SampleClass("Alice", 200)  # インスタンスの作成
print("名前は", p1.getName(), ", 所持金は", p1.getMoney(), "です。")
print("カウント:", SampleClass.getCount())

p2 = SampleClass("Tom", 220)  # インスタンスの作成
print("名前は", p2.getName(), ", 所持金は", p2.getMoney(), "です。")
print("カウント:", SampleClass.getCount())
# In[]:


class SampleClass:
    count = 0  # クラス変数

    def __init__(self, name, money):  # コンストラクタ
        SampleClass.count += 1
        self.name = name
        self.money = money

    def getName(self):  # インスタンスメソッド
        return self.name

    def getMoney(self):  # インスタンスメソッド
        return self.money

    @classmethod
    def getCount(cls):  # クラスメソッド
        return cls.count


p1 = SampleClass("Alice", 200)  # インスタンスの作成
print("名前は", p1.getName(), ", 所持金は", p1.getMoney(), "です。")
print("カウント:", SampleClass.count)
SampleClass.count = 10  # クラス変数を書き換える
print("カウント:", SampleClass.count)
p1.money = -100  # インスタンス変数を書き換える
print("名前は", p1.getName(), ", 所持金は", p1.getMoney(), "です。")

# In[]:


class SampleClass:
    _count = 0  # クラス変数

    def __init__(self, name, money):  # コンストラクタ
        SampleClass._count += 1
        self.name = name
        self._money = money

    def getName(self):  # インスタンスメソッド
        return self.name

    def getMoney(self):  # インスタンスメソッド
        return self._money

    @classmethod
    def getCount(cls):  # クラスメソッド
        return cls._count


p1 = SampleClass("Alice", 200)  # インスタンスの作成
print("名前は", p1.getName(), ", 所持金は", p1.getMoney(), "です。")
print("カウント:", SampleClass._count)
SampleClass._count = 10  # クラス変数を書き換える
print("カウント:", SampleClass._count)
p1.money = -100  # インスタンス変数を書き換える
print("名前は", p1.getName(), ", 所持金は", p1.getMoney(), "です。")

# In[]:


class SampleClass:
    __count = 0  # クラス変数

    def __init__(self, name, money):  # コンストラクタ
        SampleClass.__count += 1
        self.name = name
        self.__money = money

    def getName(self):  # インスタンスメソッド
        return self.name

    def getMoney(self):  # インスタンスメソッド
        return self.__money

    @classmethod
    def getCount(cls):  # クラスメソッド
        return cls.__count


p1 = SampleClass("Alice", 200)  # インスタンスの作成
print("名前は", p1.getName(), ", 所持金は", p1.getMoney(), "です。")
print("カウント:", SampleClass.__count)
SampleClass.__count = 10  # クラス変数を書き換える
print("カウント:", SampleClass.__count)
p1.money = -100  # インスタンス変数を書き換える
print("名前は", p1.getName(), ", 所持金は", p1.getMoney(), "です。")

# In[]:


class SampleClass:
    __count = 0  # クラス変数

    def __init__(self, name, money):  # コンストラクタ
        SampleClass.__count += 1
        self.name = name
        self.__money = money

    def getName(self):  # インスタンスメソッド
        return self.name

    def getMoney(self):  # インスタンスメソッド
        return self.__money

    @classmethod
    def getCount(cls):  # クラスメソッド
        return cls.__count


p1 = SampleClass("Alice", 200)  # インスタンスの作成
print("名前は", p1.getName(), ", 所持金は", p1.getMoney(), "です。")
print("カウント:", SampleClass.getCount())
p1._SampleClass__count = 10  # クラス変数を書き換える
print("カウント:", SampleClass.__count)
# p1.money = -100  # インスタンス変数を書き換える
# print("名前は", p1.getName(), ", 所持金は", p1.getMoney(), "です。")
# In[]:
