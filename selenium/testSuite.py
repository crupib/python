import unittest
from test_homePage import Testing
from test_CreateNewProfile import Testing
from selenium import webdriver
from selenium.webdriver.common.by import By
test_homePage = unittest.TestLoader().loadTestsFromTestCase(Testing)
test_CreatePage = unittest.TestLoader().loadTestsFromTestCase(Testing)
test_suite = unittest.TestSuite([test_homePage, test_CreatePage])
unittest.TextTestRunner().run(test_suite)
