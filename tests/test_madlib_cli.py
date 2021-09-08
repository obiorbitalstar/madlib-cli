from madlib_cli import __version__
from madlib_cli.madlib_cli import readFile,write,inputs


def test_version():
    assert __version__ == '0.1.0'


def test_read_function():
    expected = open('./assets/story.txt','r').read()
    actual = readFile()
    assert expected == actual

def test_parse_function():
    expected = ["my name","your name"]
    actual = inputs("Hello am {my name} and you are? {your name}")
    assert expected == actual

def test_merge_function():
    inputs = ['jump', 'jump']
    madlibs = ['name', 'age', 'language']
    text = 'i got the sound to make you %s %s'
    actual = write(text, inputs,madlibs)
    expected = 'i got the sound to make you jump jump'
    assert expected == actual
