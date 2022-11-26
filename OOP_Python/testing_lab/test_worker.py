import unittest


class WorkerTests(unittest.TestCase):
    NAME = "Ivan"
    SALARY = 50
    ENERGY = 2
    MONEY = 0

    def setUp(self) -> None:
        self.worker = Worker(self.NAME, self.SALARY, self.ENERGY)

    def test_init__props__expect_correct_name(self):
        expected_name = self.NAME
        actual_name = self.worker.name
        self.assertEqual(expected_name, actual_name)
        self.assertEqual(self.worker.energy, self.ENERGY)
        self.assertEqual(self.worker.salary, self.SALARY)
        self.assertEqual(0, self.MONEY)

    def test_worker_energy__incremented__after_rest_correct(self):
        self.worker.rest()
        self.assertEqual(self.ENERGY + 1, self.worker.energy)

    def test_worker_with_0_energy__raise_error(self):
        self.worker.work()
        self.worker.work()
        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertIsNotNone(ex)
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_worker__increase_money_by_salary_correct(self):
        self.worker.work()
        self.worker.work()
        self.assertEqual(2 * self.SALARY, self.worker.money)

    def test_worker_energy__decrease_after_work(self):
        self.worker.work()
        self.assertEqual(self.ENERGY - 1, self.worker.energy)

    def test_method_get_info_correct_return(self):
        expected_value = f'{self.NAME} has saved {self.MONEY} money.'
        actual_value = self.worker.get_info()
        self.assertEqual(expected_value, actual_value)


if __name__ == "__main__":
    unittest.main()