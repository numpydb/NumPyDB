import unittest

from NumPyDB.src.common.data import Data


class TestDataStructure(unittest.TestCase):
    def test_data_with_id(self):
        data_id = 100500
        data_vector = [1, 2, 3, 4, 5]  # TODO(поменть на np)
        data_value = "кот"
        data_expected = {
                'value': data_value,
                'vector': data_vector,
                'id': data_id
             }

        result = Data(data_vector, data_value, data_id)
        self.assertEqual(data_expected, result.get())

    def test_data_no_id(self):
        data_vector = [1, 2, 3, 4, 5]  # TODO(поменть на np)
        data_value = "кот"
        data_expected = {
                'value': data_value,
                'vector': data_vector,
                'id': -1
             }

        result = Data(data_vector, data_value)
        self.assertEqual(data_expected, result.get())

if __name__ == '__main__':
    unittest.main()
