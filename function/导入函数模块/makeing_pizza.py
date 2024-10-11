"""
#导入整个模块
import pizza

pizza.make_pizza(16,"pepperoni")
pizza.make_pizza(12,"mushrooms","green peppers","extra cheese")
"""

"""
#导入特定函数
from pizza import make_pizza

make_pizza(16,"pepperoni")
make_pizza(12,"mushrooms","green peppers")
"""

"""
#使用as给函数指定别名
from pizza import make_pizza as mkp
mkp(16,"pepperoni")
mkp(12,"mushrooms","green peppers")
"""

#使用as给模块指定别名
import pizza as pz
pz.make_pizza(16,"pepperoni")
pz.make_pizza(12,"mushrooms","green peppers")

"""
#模块中导入所有函数写法(不常用)
from pizza import *
"""
