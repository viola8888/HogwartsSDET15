from frame.main import Main


class TestMain:

    def test_main(self):
        Main().goto_market().goto_search().search()



# 打印a，并在a前后分别打印before after的方法

# 第一种方法：直接在函数前后添加 print

# def a():
#     print('before')
#     print('a')
#     print('after')

# def test_a():
#     a()

# 第二种方法:创建一个函数，加强函数
# def a():
#     print("a")
#
# def enhance(func):
#     print('before')
#     func()
#     print('after')
#
# def test_a():
#     enhance(a)

# 第三种方法：装饰器
# def tmp(func):
#     def wrapper(*args, **kwargs):
#         print('before')
#         func(*args, **kwargs)
#         print('after')
#     return wrapper
#
# @tmp
# def a(a1):
#     print("a")
#     print(a1)
#
# def test_a():
#     a('哈哈')
#
