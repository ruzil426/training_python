from runner_and_tournament import Runner, Tournament
import unittest

def skip_if_frozen(func):
    def wrapper(self, *args, **kwargs):
        if getattr(self.__class__, 'is_frozen', False):
            self.skipTest("Тесты в этом кейсе заморожены")
        else:
            return func(self, *args, **kwargs)
    return wrapper

class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.r1 = Runner('Усейн', 10)
        self.r2 = Runner('Андрей', 9)
        self.r3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    @skip_if_frozen
    def test_run1(self):
        tourn_1 = Tournament(90, self.r1, self.r3)
        result = tourn_1.start()
        formatted_result = {place: runner.name for place, runner in result.items()}
        TournamentTest.all_results['test_run1'] = formatted_result
        self.assertTrue(result[max(result.keys())].name == self.r3.name)

    @skip_if_frozen
    def test_run2(self):
        tourn_2 = Tournament(90, self.r2, self.r3)
        result = tourn_2.start()
        formatted_result = {place: runner.name for place, runner in result.items()}
        TournamentTest.all_results['test_run2'] = formatted_result
        self.assertTrue(result[max(result.keys())].name == self.r3.name)

    @skip_if_frozen
    def test_run3(self):
        tourn_3 = Tournament(90, self.r1, self.r2, self.r3)
        result = tourn_3.start()
        formatted_result = {place: runner.name for place, runner in result.items()}
        TournamentTest.all_results['test_run3'] = formatted_result
        self.assertTrue(result[max(result.keys())].name == self.r3.name)

