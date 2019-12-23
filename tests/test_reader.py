from reader import Reader
from datetime import datetime as dt
import pytest

@pytest.fixture
def tmp_mind(tmp_path):

    data = open('thoughts/reader/tests/tmp.mind', 'rb').read()
    
    f = tmp_path / 'tmp.mind'
    f.write_bytes(data)
    return f.absolute()

def test_reader_init(tmp_mind):
    reader = Reader(tmp_mind)

    assert reader.id == 42
    assert reader.name_length ==10
    assert reader.name == 'Dan Gittik'
    assert reader.birth == 699746400
    assert reader.gender == 'mail'

def test_reader_read1(tmp_mind):
    pass

def test_reader_fail():
    pass