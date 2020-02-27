# In[]:
# デコレータ


def deco(func):
    def wrapper(*args, **kwargs):
        print('--start--')
        func(*args, **kwargs)
        print('--end--')
    return wrapper


@deco
def test():
    print('Hello Decorator')


test()

# In[]:


def deco2(func):
    import os

    def wrapper(*args, **kwargs):
        res = '--start--' + os.linesep
        res += func(*args, **kwargs) + '!' + os.linesep
        res += '--end--'
        return res
    return wrapper


@deco2
def test2():
    return('Hello Decorator')


print(test2())

# In[]:


def deco_html(func):

    def wrapper(*args, **kwargs):
        res = '<html>'
        res = res + func(*args, **kwargs)
        res = res + '</html>'
        return res
    return wrapper


def deco_body(func):
    def wrapper(*args, **kwargs):
        res = '<body>'
        res = res + func(*args, **kwargs)
        res = res + '</body>'
        return res
    return wrapper


@deco_html
@deco_body
def test():
    return 'Hello Decorator'


print(test())
# In[]:


def deco_p(func):
    def wrapper(*args, **kwargs):
        res = '<p>'
        res = res + func(args[0], **kwargs)
        res = res + '</p>'
        return res
    return wrapper


@deco_p
def test(str):
    return str


print(test('Hello decorator!'))
# In[]:


def deco_tag(tag):
    def _deco_tag(func):
        def wrapper(*args, **kwargs):
            res = '<' + tag + '>'
            res = res + func(*args, **kwargs)
            res = res + '</' + tag + '>'
            return res
        return wrapper
    return _deco_tag


@deco_tag('html')
@deco_tag('body')
def test():
    return 'Hello Decorator!'


print(test())
# In[]:


def my_decorator(target_function):
    def wrapper_function(*args, **kwargs):
        kwargs['test_key'] = 'デコレータで書き換えられた値'
        return target_function(*args, **kwargs)
    return wrapper_function


@my_decorator
def my_method(*args, **kwargs):
    if 'test_key' in kwargs:
        print('test_keyの値は、[{}]'.format(kwargs['test_key']))
    else:
        print('test_keyに値は、入っていません。')


my_method()
my_method(test_key="テスト用の値")

# In[]:
# 引数無しデコレータでラッパー関数を返す場合


def args_logger(f):
    def wrapper(*args, **kwargs):
        f(*args, **kwargs)
        print('args:{}, kwargs:{}'.format(args, kwargs))
    return wrapper


@args_logger
def print_message(msg):
    print(msg)


# 以下と同じ
'''
def print_message(msg):
    print(msg)
print_message = args_logger(print_message)
'''

print_message('hello')
# In[]:
# 引数ありデコレータでラッパー関数を返さない場合
funcs = []


def appender(*args, **kwargs):
    def decorator(f):
        print(args)
        if kwargs.get('option1'):
            print('option1 is True')
        funcs.append(f)
    return decorator


@appender('arg1', option1=True)
def hoge():
    print('hoge')


@appender('arg2', option2=False)
def fuga():
    print('fuga')


# 以下と同じ
'''
def hoge():
    print('hoge')
appender('arg1', option1=True)(hoge)

def fuga():
    print('fuga')
appender('arg2', option2=False)(fuga)
'''

for f in funcs:
    f()

# In[]:
# 引数ありデコレータでラッパー関数を返す場合


def args_joiner(*dargs, **dkwargs):
    def decorator(f):
        def wrapper(*args, **kwargs):
            newargs = dargs + args
            newkwargs = {**kwargs, **dkwargs}
            f(*newargs, **newkwargs)
        return wrapper
    return decorator


@args_joiner('darg', dkwarg=True)
def print_args(*args, **kwargs):
    print('args:{}, kwargs:{}'.format(args, kwargs))


# 以下と等価
'''
def print_args(*args, **kwargs):
    print('args:{}, kwargs:{}'.format(args, kwargs))
print_args = args_joiner('darg', dwarg=True)(print_args)
'''

print_args('arg', kwarg=False)
# In[]:


def print_result(func):
    def new_func(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return result
    return new_func


def add_two_ints(a: int, b: int):
    return a + b


add_two_ints = print_result(add_two_ints)
add_two_ints(3, 5)
# In[]:


def print_result(func):
    def new_func(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return result
    return new_func


@print_result
def add_two_ints(a: int, b: int):
    return a + b


add_two_ints(3, 5)


# In[]:

def print_args(func):
    def new_func(*args, **kwargs):
        print(args)
        print(kwargs)
        return func(*args, **kwargs)
    return new_func


def print_result(func):
    def new_func(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return result
    return new_func


@print_args
@print_result
def add_two_ints(a: int, b: int):
    return a + b


add_two_ints(3, 5)
print()
add_two_ints(a=3, b=5)

# In[]:


def print_result2(func):
    def new_func(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return result
    return new_func


def print_message2(start_message, end_message):
    def _print_args(func):
        def new_function(*args, **kwargs):
            print(start_message)
            result = func(*args, **kwargs)
            print(end_message)
            return result
        return new_function
    return _print_args


@print_message2("処理開始", "処理終了")
@print_result2
def add_two_ints2(a: int, b: int):
    return a + b


add_two_ints2(3, 5)
# In[]:


def a():
    def b():
        return 'bです。'
    return b


print(a())  # b関数オブジェクトを出力
# <function a.<locals>.b at 0x00000176152BC950>
print(a()())  # b関数の実行結果を出力
# 'bです。'

# In[]:


def a(name):
    return 'hello!' + name


print(a('jobs'))  # a関数の実行結果を出力
# 'hello!jobs'

# In[]:
# 関数を引数にとる関数


def a(func):
    return func


def b(name):
    return 'hello' + name


print(a(b))
# <function b at 0x00000176152BCD90>

# In[]:


def a(func):
    return func


def b(name):
    return 'hello!' + name


print(a(b)('jobs'))
# hello!jobs

# In[]:
# デコレータの例


def a(func):
    def b():
        print('スタート')
        func()  # func() = c関数の実行
        print('おわり')
    return b


def c():
    print("c関数を実行しています。")


a(c)()  # b関数の実行(func = c)

# In[]:


def a(func):
    def b():
        print('スタート')
        func()
        print('おわり')
    return b


@a
def c():
    print('c関数を実行しています。')


c()
# In[]:


def adult(func):
    def checker(name, age):
        if age >= 20:
            print(f'{name}は大人')
            func(name, age)
            print('処理が完了しました。')
        else:
            print(f'{name}は未成年')
    return checker


@adult
def drink(name, age):
    print(f'{name}({age})「gokugoku」')


drink('Jobs', 21)

drink('Rola', 12)

# In[]:


def add(name):
    return name


print(add('Alice'))


# In[]:


def hello(func):  # デコレータ
    def wrapper(func):
        return print('Hello ' + func + '!')
    return wrapper


def add(name):  # 修飾される関数
    return name


hello(add)('Alice')

# In[]:


# @を使う
def hello(func):  # デコレータ
    def wrapper(func):
        return print('Hello ' + func + '!')
    return wrapper


@hello
def add(name):  # 修飾される関数
    return name


add('Alice')

# In[]:


class Test:
    num = 10

    def b(self):  # メソッド
        self.c('Hello')

    def c(self, msg):
        print("{0}".format(msg))
        print(("{0}".format(self.num)))


test = Test()  # オブジェクトの生成
test.b()
# In[]:


class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_test(self):
        sum_t = self.a + self.b
        print("{0}".format(sum_t))


# In[]:

# In[]:

# In[]:
