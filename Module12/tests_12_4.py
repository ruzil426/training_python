import logging
from rt_with_exceptions import Runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner1 = Runner('Bob', -5)
            logging.info(f'{self.test_walk} выполнен успешно')
            for i in range(10):
                runner1.walk()
            self.assertEqual(runner1.distance, 50)
        except:
            logging.warning('Неверная скорость для Runner', exc_info=True)
            print(f'Скорость не может быть отрицательной, сейчас {self.speed}')


    def test_run(self):
        try:
            runner2 = Runner(2)
            logging.info(f'{self.test_run} выполнен успешно')
            for i in range(10):
                runner2.run()
            self.assertEqual(runner2.distance, 100)
        except:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)
            print('Имя не может быть только числом, передано int')

    def test_challenge(self):
        runner3 = Runner('Alex')
        runner4 = Runner('Mike')
        for i in range(10):
            runner3.run()
            runner4.walk()
        self.assertNotEqual(runner3.distance, runner4.distance)

if __name__ ==  "__main__":
    unittest.main()


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')
