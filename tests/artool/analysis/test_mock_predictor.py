from unittest.mock import MagicMock

import unittest
import __init__
from artool.analysis.predictor import Predictor
from artool.error.custom import PredictorError


class TestMockPredictorModule(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """

    def setUp(self):
        self.fj_predictor = Predictor("salary", "JDU-SS")

    def test_mock_predict_salary_called(self):
        """_summary_
        """
        self.fj_predictor.predict_salary = MagicMock(return_value=10000)
        self.fj_predictor.predict_salary(4000, "F8")
        self.fj_predictor.predict_salary.assert_called_with(4000, "F8")
        self.assertEqual(self.fj_predictor.predict_salary.return_value, 10000)

    def test_predict_salary(self):
        """_summary_
        """
        self.assertEqual(self.fj_predictor.predict_salary(4000, "F8"), 4200)

    def tearDown(self):
        del self.fj_predictor


if __name__ == '__main__':
    unittest.main()
