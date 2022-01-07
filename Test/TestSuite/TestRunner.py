# TestRunner.py
import sys
import os
from unittest import TestLoader, TestSuite, TextTestRunner
from Test.Scripts.test_Factorial_Links import Factorial_Links
from Test.Scripts.test_Home_Page import Factorial_HomePage
from Test.Scripts.test_Factorial_Input import Factorial_Input
import testtools as testtools

sys.path.append(sys.path[0] + "/...")
# Uncomment if the above example gives you a relative path error
sys.path.append(os.getcwd())

if __name__ == "__main__":
    test_loader = TestLoader()
    # Test Suite is used since there are multiple test cases
    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(Factorial_HomePage),
        test_loader.loadTestsFromTestCase(Factorial_Input),
        test_loader.loadTestsFromTestCase(Factorial_Links),
    ))

    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)

    # Refer https://testtools.readthedocs.io/en/latest/api.html for more information
    parallel_suite = testtools.ConcurrentStreamTestSuite(
        lambda: ((case, None) for case in test_suite))
    parallel_suite.run(testtools.StreamResult())
