
import unittest


def eval_TestCase(TestCase, verbosity=2):
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    r = unittest.TextTestRunner(verbosity=verbosity).run(suite)
    if r.errors or r.failures:
        raise Exception('YOUR TEST FAILED')
    else:
        return True
