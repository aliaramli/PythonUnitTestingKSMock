from unittest import TestCase, main
from unittest.mock import patch, create_autospec
import __init__
from artool.analysis.holiday import Holiday

side_effect_holidays = [
    {'date': '2024-01-01', 'localName': '元日', 'name': "New Year's Day", 'countryCode': 'JP',
     'fixed': False, 'global': True, 'counties': None, 'launchYear': None, 'types': ['Public']},
    {'date': '2024-01-08', 'localName': '成人の日', 'name': 'Coming of Age Day', 'countryCode': 'JP',
     'fixed': False, 'global': True, 'counties': None, 'launchYear': None, 'types': ['Public']},
    {'date': '2024-02-12', 'localName': '建国記念の日', 'name': 'Foundation Day', 'countryCode': 'JP',
     'fixed': False, 'global': True, 'counties': None, 'launchYear': None, 'types': ['Public']}
]


class TestMockHolidayModule(TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """

    def setUp(self):
        self.holiday = Holiday()

    @patch('artool.analysis.holiday.Holiday')
    def test_mock_side_effect_holiday(self, mock_holiday):
        """_summary_
        """
        def side_effect(year, country_code):
            return side_effect_holidays

        mock_holiday_instance = mock_holiday.return_value
        mock_holiday_instance.get_holiday.side_effect = side_effect
        holidays = mock_holiday_instance.get_holiday("2024", "JP")
        self.assertEqual(len(holidays), 3)

    def test_get_holiday(self):
        """_summary_
        """
        print(self.holiday.get_holiday("2024", "JP"),
              len(self.holiday.get_holiday("2024", "JP")))

    def test_mock_as_patch_context_manager(self):
        """_summary_
        """
        ret = [{
            'date': '2024-01-01', 'localName': '元日',
            'name': "New Year's Day", 'countryCode': 'JP',
            'fixed': False, 'global': True, 'counties': None, 'launchYear': None, 'types': ['Public']
        }]
        with patch.object(Holiday, 'get_holiday', return_value=ret) as mock_method:
            thing = Holiday
            # patching mock / creating mock function does not validate the passed parameter.
            thing.get_holiday("2024", "MY", 1)
            thing.get_holiday("2024", "JP")
            # QUIZ
            # b = Holiday
            # b.get_holiday("2024", "MY")

        mock_method.assert_called_with("2024", "JP")
        self.assertEqual(mock_method.return_value, ret)

    def test_mock_as_patch_dict(self):
        """_summary_
        """
        foo = {'key': 'value'}
        original = foo.copy()
        with patch.dict(foo, {'newkey': 'newvalue'}, clear=True):
            assert foo == {'newkey': 'newvalue'}
        assert foo == original

    def test_mock_create_autospec_valid(self):
        """_summary_
        """
        mock_function = create_autospec(
            self.holiday.get_holiday, return_value="No holiday")
        mock_function("2024", "JP")
        mock_function.assert_called_once_with("2024", "JP")

    def test_mock_create_autospec_invalid(self):
        """_summary_
        """
        mock_function = create_autospec(
            self.holiday.get_holiday, return_value="No holiday")
        mock_function("tiputipu")

    def tearDown(self):
        del self.holiday


if __name__ == '__main__':
    main()
