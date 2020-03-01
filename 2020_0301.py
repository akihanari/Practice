# In[]:
class Person:  # クラス

    def __init__(self, name="aaa", blood="x"):  # コンストラクタ
        self.name = name
        self.blood = blood

    def getName(self):  # メソッド
        return self.name

    def getBlood(self):
        return self.blood

p1 = Person("Alice", "A型")  # インスタンスを作成
print("名前は", p1.getName(), ", 血液型は", p1.getBlood(), "です。")


# In[]:
class A:
    def test(self, test):  # メソッド
        self.test = test
        return self.test

a = A()  # インスタンス
print(a.test("test"))

# In[]:
