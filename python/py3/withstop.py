#!/usr/bin/python3
# -*-coding:utf8-*-
'''
学习asyncio 之 KeyboardInterrupt 是否触发 context exit
'''


class A:
    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")


with A() as a:
    ii = input("use input to hang the process:\n")
    print(ii)

"""
result:
enter
use input to hang the process:
exit
Traceback (most recent call last):
  File "./withstop.py", line 16, in <module>
    ii = input("use input to hang the process:\n")
KeyboardInterrupt
"""
