import pytest
import os

@pytest.fixture
def csv_file(tmpdir):
    # return 'csv file!!!'
    path = os.path.join(tmpdir, 'test.csv')
    with open(path, 'w+') as c:
        print('before test')
        yield c
        print('after test')

def pytest_addoption(parser):
    parser.addoption('--os-name', default='linux', help='os name')
