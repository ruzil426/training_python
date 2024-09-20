import inspect
from pprint import pprint


class Number:
    def introspection_info(self, obj):
        self.obj = obj
        res = obj +10
        print(res)


num1 =Number()
num1.introspection_info(42)

type_ = type(num1)
dir_ = dir(num1)
isins_ = isinstance(num1,Number)
get_m = inspect.getmodule(num1)

res_ = [type_, dir_, isins_, get_m]
for i in res_:
    pprint(res_)