import unittest

from back_system.common.es_ import *
from unittest import TestCase,TestSuite,TextTestRunner


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
    suit = TestSuite()
    suit.addTest(TestEs.test_a1_create_index)
    suit.addTest(TestEs.test_b0_add_doc)
    suit.addTest(TestUser.test_a0_login)
    suit.addTest(TestUser.test_b1_logout)

    runner = TextTestRunner()
    runner.run(suit)