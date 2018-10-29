from pathlib import Path

from pytest import fixture


@fixture
def datadir() -> Path:
    '''
    Fixture that gives the path of the data directory
    '''
    return Path(__file__).absolute().parent / 'tests-data'

