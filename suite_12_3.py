import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        pass

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        pass

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        pass

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test1(self):
        pass

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test2(self):
        pass

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test3(self):
        pass

suite_12_3 = unittest.TestSuite()
suite_12_3.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
suite_12_3.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

TextTestRunner = unittest.TextTestRunner(verbosity=2)
TextTestRunner.run(suite_12_3)
