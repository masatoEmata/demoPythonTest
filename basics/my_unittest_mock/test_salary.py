import unittest
from unittest.mock import MagicMock
from unittest import mock
import salary


# currently salary.ThirdPartyBonusRestApi.bonus_price func is not working.


class TestSalary(unittest.TestCase):
    def test_cal_salary(self):
        s = salary.Salary()
        s.bonus_api.bonus_price = MagicMock(return_value=1)
        self.assertEqual(s.calc_salary(), 101)
        s.bonus_api.bonus_price.assert_called_once_with(year=2017)

    '''
    assert_not_called
    '''
    def test_cal_salary_no_bonus(self):
        s = salary.Salary(year=2050)
        s.bonus_api.bonus_price = MagicMock(return_value=1)
        self.assertEqual(s.calc_salary(), 100)
        s.bonus_api.bonus_price.assert_not_called()

    '''
    PATCH
    '''
    '''patch'''
    @mock.patch('salary.ThirdPartyBonusRestApi.bonus_price', return_value=1)
    def test_cal_salary_patch(self, mock_bonus):
        s = salary.Salary(year=2017)
        self.assertEqual(s.calc_salary(), 101)
        mock_bonus.assert_called()

    def test_cal_salary_patch_with(self):
        with mock.patch('salary.ThirdPartyBonusRestApi.bonus_price', return_value=1) as mock_bonus:
            s = salary.Salary(year=2017)
            self.assertEqual(s.calc_salary(), 101)
            mock_bonus.assert_called()

    '''Patcher'''
    def setUp(self) -> None:
        self.patcher = mock.patch('salary.ThirdPartyBonusRestApi.bonus_price', return_value=1)
        self.mock_bonus = self.patcher.start()

    def tearDown(self) -> None:
        self.patcher.stop()

    def test_cal_salary_patcher(self):
        # patcher = mock.patch('salary.ThirdPartyBonusRestApi.bonus_price', return_value=1)
        # mock_bonus = patcher.start()
        self.mock_bonus.return_value = 1

        s = salary.Salary(year=2017)
        self.assertEqual(s.calc_salary(), 101)
        self.mock_bonus.assert_called()
        # pather.stop()


    def test_cal_salary_patch_sied_effect_func(self):
        def f(year):
            return 1
        self.mock_bonus.side_effect = f
        s = salary.Salary(year=2017)
        self.assertEqual(s.calc_salary(), 101)
        self.mock_bonus.assert_called()

    def test_cal_salary_patch_sied_effect_list(self):
        self.mock_bonus.side_effect = [1, 2, 3]
        s = salary.Salary(year=2017)
        self.assertEqual(s.calc_salary(), 101)
        s = salary.Salary(year=2018)
        self.assertEqual(s.calc_salary(), 102)
        s = salary.Salary(year=2019)
        self.assertEqual(s.calc_salary(), 103)

    '''class mock'''
    @mock.patch('salary.ThirdPartyBonusRestApi', spce=True)
    @mock.patch('salary.Salary.get_from_boss')
    def test_cal_salary_patch_class(self, mock_boss, MockRest):
        mock_boss.return_value = 10

        mock_rest = MockRest.return_value # mock_rest = MockRest()
        mock_rest.bonus_price.return_value = 1
        mock_rest.bonus_price.get_api_name = 'Money'

        s = salary.Salary(year=2017)
        salary_price = s.calc_salary()

        self.assertEqual(salary_price, 111)
        mock_rest.bonus_price.assert_called()