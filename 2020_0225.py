# 関数について
# In[]:
# 戻り値のある関数


def fc_print_name(name):
    return print("名前は", name, "です。")


fc_print_name("test")

# In[]:
# 戻り値のない関数


def fc_print_end():
    print("終了しました。")
    return


fc_print_end()

# In[]:
# 複数の戻り値をもつ関数


def fc_price():
    price = 399
    num = 13
    tax = int(price * num * 0.08)
    total = price * num + tax
    print("単価は", price, "円、売上個数は", num, "個、\n消費税は",
                        tax, "円、合計金額は", total, "円です。")
    return price, num, tax, total


p, n, t, total = fc_price()
print("複数の戻り値：", p, n, t, total)

# In[]:
# デフォルト引数


def fc_price(price=100, num=5):
    tax = int(price * num * 0.08)
    total = price * num + tax
    print("単価は", price, "円、売上個数は", num, "個、\n消費税は",
                        tax, "円、合計金額は", total, "円です。")
    return


price = 399
num = 13
print(fc_price())
print(fc_price(price, num))
# In[]:
# 可変長引数


def func(*args):
    print(args)


func("こんにちは", "Hello", "Bonjour")
func("Hello")
func()

# In[]:
# 可変長引数（辞書型）


def func(**kwargs):
    print(kwargs)


func(JPN="こんにちは", GBR="Hello", FRA="Bonjour")
func(JPN="こんにちは")
func()

# In[]:
# クラスの勉強


class Monster:

    def __init__(self, name, luck):
        self.name = name
        self.luck = luck

    def display(self):
        print("Name:", self.name)
        print("Luck:", self.luck)


monster = Monster("アアア", 12)
# monster.name = "クイバタ"
# monster.luck = 99
monster.display()
# In[]:
