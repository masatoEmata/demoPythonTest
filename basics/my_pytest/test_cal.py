import os
import pytest
from cal import Cal
# def test_add_num_double():
#     cal = Cal()
#     assert cal.add_num_and_double(1, 1) == 4

is_release = True

class TestCal(object):
    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = Cal()
        cls.test_file_name = 'test.txt'

    @classmethod
    def teardown_class(cls):
        print('end')
        cls.cal = Cal()

    def setup_method(self, method) -> None:
        print(f'setup method={method}\n')
        # self.cal = Cal()

    def teardown_method(self, method) -> None:
        print(f'teardown method={method}\n')
        # del self.cal

    def test_add_num_double(self, request):
        os_name = request.config.getoption('--os-name')
        if os_name == 'mac':
            print('ls')
        elif os_name == 'windows':
            print('dir')
        assert self.cal.add_num_and_double(1, 1) == 4


    @pytest.mark.skipif(is_release==True, reason='lesson')
    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
                self.cal.add_num_and_double('1', '1')


    '''
    fixture demo
    '''
    def test_add_num_double_ft(self, tmpdir):
        print('tmpdir: ', tmpdir)
        assert self.cal.add_num_and_double(1, 1) == 4

    def test_save(self, tmpdir):
        self.cal.save(tmpdir, self.test_file_name)
        test_file_path = os.path.join(tmpdir, self.test_file_name)
        assert os.path.exists(test_file_path) is True       