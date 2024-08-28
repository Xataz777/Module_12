import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class Runner_test(unittest.TestCase):
    def test_walk(self):
        test_obj = Runner('AAA')
        for i in range(10):
            test_obj.walk()
        self.assertEqual(test_obj.distance, 50)

    def test_run(self):
        test_obj = Runner('BBB')
        for i in range(10):
            test_obj.run()
        self.assertEqual(test_obj.distance, 100)

    def test_challenge(self):
        test_obj1 = Runner('A1')
        test_obj2 = Runner('B2')
        for i in range(10):
            test_obj1.run()
            test_obj2.walk()
        self.assertNotEqual(test_obj1.distance, test_obj2.distance)