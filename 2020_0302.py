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

print("名前は", p1.getName(), ", 所持金は", p1.getMoney(), "です。")
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
# クラス変数をプライベートにする


class SampleClass:
    __count = 0  # プライベート変数

    def __init__(self, name, money):
        SampleClass.__count += 1
        self.name = name
        self.money = money

    def getName(self):
        return self.name

    def getMoney(self):
        return self.money

    @classmethod
    def getCount(cls):
        return cls.__count


p1 = SampleClass("Alice", 200)  # インスタンスの作成
print("名前は", p1.getName(), ", 所持金は", p1.getMoney(), "です。")
print("カウント:", SampleClass.__count)
SampleClass.__count = 10  # クラス変数を書き換えられない
print("カウント:", SampleClass.__count)

# In[]:
# インスタンス変数をプライベートにする


class SampleClass:
    count = 0

    def __init__(self, name, money):
        SampleClass.count += 1
        self.name = name
        self.__money = money  # プライベート変数

    def getName(self):
        return self.name

    def getMoney(self):
        return self.__money

    @classmethod
    def getCount(cls):
        return cls.count


p1 = SampleClass("Alice", 200)  # インスタンスの作成
print("名前は", p1.getName(), ", 所持金は", p1.getMoney(), "です。")
print(p1.name)
print(p1.__money)  # アクセス不可

# In[]:


class SampleClass:
    __count = 0

    def __init__(self, name, money):
        SampleClass.__count += 1
        self.name = name
        self.money = money

    def getName(self):
        return self.name

    def getMoney(self):
        return self.money

    def setMoney(self, money2):
        self.money = money2

    @classmethod
    def getCount(cls):
        return cls.__count


p1 = SampleClass("Alice", 200)
print("名前は", p1.getName(), ", 所持金は", p1.getMoney(), "です。")
p1.setMoney(300)
print("名前は", p1.getName(), ", 所持金は", p1.getMoney(), "です。")
print("カウント:", p1.getCount())

# In[]:


class SampleClass:
    count = 0

    def __init__(self, name, money):
        SampleClass.count += 1
        self.name = name
        self.__money = money

    def getName(self):
        return self.name

    def getMoney(self):
        return self.__money

    def setMoney(self, money2):
        self.__money = money2

    @classmethod
    def getCount(cls):
        return cls.count


p1 = SampleClass("Alice", 200)  # インスタンスの作成
print("名前は", p1.getName(), ", 所持金は", p1.getMoney(), "です。")
p1.setMoney(300)
print("名前は", p1.getName(), ", 所持金は", p1.getMoney(), "です。")


# In[]:
