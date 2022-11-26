import unittest

from testing_lab.List.extended_list import IntegerList


class IntegerListTests(unittest.TestCase):
    LIST = [1.5, 2, 3, False, "A"]

    def setUp(self) -> None:
        self.list = IntegerList(*[1.5, 2, 3, False, "A"])

    def test_init_work_correct(self):
        self.assertEqual([2, 3], self.list._IntegerList__data)

    def test_get_data_correct(self):
        self.assertEqual([2, 3], self.list.get_data())

    def test_element_to_add_not_int__raise_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.list.add("1")
        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_element_append_correct(self):
        self.assertEqual([2, 3, 4], self.list.add(4))

    def test__element_index__raise_exception(self):
        with self.assertRaises(IndexError) as ie:
            self.list.remove_index(5)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test__return_value__correct(self):
        self.assertEqual(2, self.list.remove_index(0))

    def test_remove_value__correct(self):
        self.list.remove_index(0)
        self.assertNotIn(2, self.list._IntegerList__data)

    def test_get__element_index_raise_exception(self):
        with self.assertRaises(IndexError) as ie:
            self.list.get(5)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_element_correct(self):
        self.assertEqual(2, self.list.get(0))

    def test_insert_element_index_raise_exception(self):
        with self.assertRaises(IndexError) as ie:
            self.list.insert(5, 4)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_element_type_raise_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.list.insert(0, '4')
        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert__element_correct(self):
        self.list.insert(0, 1)
        self.assertEqual([1, 2, 3], self.list._IntegerList__data)

    def test_get_biggest_num_correct(self):
        self.assertEqual(3, self.list.get_biggest())

    def test_get_element_index_correct(self):
        self.assertEqual(0, self.list.get_index(2))


if __name__ == "__main__":
    unittest.main()
