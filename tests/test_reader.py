from thoughts import Reader
from thoughts import Snapshot
from datetime import datetime as dt
import pytest

@pytest.fixture
def tmp_mind(tmp_path):

    data = open('tests/Utils/tmp.mind', 'rb').read()
    
    f = tmp_path / 'tmp.mind'
    f.write_bytes(data)
    return f.absolute()

def test_reader_init(tmp_mind):
    reader = Reader(tmp_mind)

    assert reader.id == 42
    assert reader.name_length ==10
    assert reader.name == 'Dan Gittik'
    assert reader.birth == 699746400
    assert reader.gender == 'male'

def test_reader_read1(tmp_mind):

    reader = Reader(tmp_mind)

    snapshot = Snapshot(1575446887339)
    snapshot.set_location(0.4873843491077423, 0.007090016733855009, -1.1306129693984985)
    snapshot.set_rotation(-0.10888676356214629, -0.26755994585035286, -0.021271118915446748, 0.9571326384559261)
    snapshot.set_color_image(1080, 1920, b'')
    snapshot.set_depth_image(172, 224, b'')
    snapshot.set_thoughts(0, 0, 0, 0)

    snapts = list(reader)
    assert len(snapts) == 1

    s = snapts[0]

    assert s.time == snapshot.time
    assert s.tx == snapshot.tx 
    assert s.tz == snapshot.tz 
    assert s.ty == snapshot.ty
    assert s.rx == snapshot.rx 
    assert s.ry == snapshot.ry 
    assert s.rz == snapshot.rz 
    assert s.rw == snapshot.rw 
    assert s.chight == snapshot.chight 
    assert s.cwidth == snapshot.cwidth 
    assert s.dhight == snapshot.dhight 
    assert s.dwidth == snapshot.dwidth  
    assert s.hunger == snapshot.hunger 
    assert s.thirst == snapshot.thirst 
    assert s.exhaustion == snapshot.exhaustion 
    assert s.happiness == snapshot.happiness 
