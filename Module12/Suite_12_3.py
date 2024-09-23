import unittest
import test_12_1
import test_12_2

testST = unittest.TestSuite()
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_1.RunnerTest))
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(testST)
