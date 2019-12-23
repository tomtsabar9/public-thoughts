from thoughts import Snapshot
from datetime import datetime as dt


def test_snap():

    tx = 1
    tz = 2
    ty = 1
    rx = 3
    ry = 4
    rz = 5
    rw = 6
    hight = 7
    width = 8
    img_color_array = b'30'*hight*width
    dhight = 9
    dwidth = 10
    img_depth_array = b'30'*dhight*dwidth
    hunger = 1
    thirst = 2
    exhaustion = 3
    happiness = 4

    now = dt.now().timestamp()
    snap = Snapshot(now)

    snap.set_location(tx, ty, tz)
    snap.set_rotation(rx, ry, rz, rw)
    snap.set_color_image(hight, width, img_color_array)
    snap.set_depth_image(dhight, dwidth, img_depth_array)
    snap.set_thoughts(hunger, thirst, exhaustion, happiness)

    assert snap.tx == tx 
    assert snap.tz == tz 
    assert snap.ty == ty
    assert snap.rx == rx 
    assert snap.ry == ry 
    assert snap.rz == rz 
    assert snap.rw == rw 
    assert snap.chight == hight 
    assert snap.cwidth == width 
    assert snap.cimage == img_color_array 
    assert snap.dhight == dhight 
    assert snap.dwidth == dwidth 
    assert snap.dimage == img_depth_array 
    assert snap.hunger == hunger 
    assert snap.thirst == thirst 
    assert snap.exhaustion == exhaustion 
    assert snap.happiness == happiness 
