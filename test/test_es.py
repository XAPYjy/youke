import unittest

from back_system.common.es_ import *
from unittest import TestCase, TestSuite, TextTestRunner, TestLoader


class TestEs(TestCase):
    def test_a1_create_index(self):
        print('------test_a1_create_index------')

    def test_b0_add_doc(self):
        print('------test_b0_add_doc------')

    def test_del_doc(self):
        print('------test_del_doc------')

    def test_del_index(self):
        print('------test_del_index------')


class TestUser(TestCase):
    def test_a0_login(self):
        print('-----test_a0_login----')

    def test_b1_logout(self):
        print('-----test_b1_logout----')


if __name__ == '__main__':
    suit = TestSuite()  # 测试套件
    suit.addTest(TestEs.test_a1_create_index)
    suit.addTest(TestEs.test_b0_add_doc)
    suit.addTest(TestUser.test_a0_login)
    suit.addTest(TestUser.test_b1_logout)

    # 将整个测试类添加到套件中
    suit = TestSuite(TestLoader().loadTestsFromTestCase(TestEs))

    runner = TextTestRunner()
    runner.run(suit)

    from sys import argv
    # 将 -o -c 参数转换成 {'o':'abc.txt','c':123}
    params = argv[1:]
    params2 = filter(lambda item:item.startswith('--'),params)

    data = {}
    for i in range(len(params)//2):
        name = params[i*2][1:]
        value = params[i*2+1]

    for p in params2:
        name,value = p[2:].split('=')
        data[name] = value

