import unittest


def tests():
    test_suite = unittest.TestSuite()
    test_loader = unittest.defaultTestLoader

    test_suite.addTest(test_loader.loadTestsFromNames(['Tests.BoardTests', 'Tests.MinimaxTests', 'Tests.PlayerTests',
                                                       'Tests.Connect4Tests']))

    unittest.TextTestRunner(verbosity=2).run(test_suite)


if __name__ == '__main__':
    tests()
