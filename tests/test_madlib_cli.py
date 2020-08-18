from madlib_cli import __version__
from madlib_cli.madlib_cli import readFile,write,inputs


def test_version():
    assert __version__ == '0.1.0'


def test_read():
    actual = type(readFile())
    expected ="type(<class 'str'>)"
    assert type(actual)== expected
