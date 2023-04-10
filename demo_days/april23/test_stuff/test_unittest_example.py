import unittest_examples as ue

def test_foo():
   assert ue.foo(5,2) == 9
   assert ue.foo(5) == 7
def test_foo_string():
   assert ue.foo_string("abc","def") == "abcdef"
def test_boo():
   assert ue.boo(12,2) == 3
   assert ue.boo(12) == 6
