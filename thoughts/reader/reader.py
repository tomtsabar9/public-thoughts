# from PIL import Image

from .formats import Unpack
from .snapshot import Snapshot


class Reader():

    def __init__(self, path):
        self.path = path
        self.data = open(self.path, "rb")
        self.unpacker = Unpack(self.data)

        self.id = self.unpacker.id()

        self.name_l = self.unpacker.name_length()

        self.name = self.unpacker.name(self.name_l)

        self.birth = self.unpacker.birth()

        self.gender = self.unpacker.gender()

    def __iter__(self):

        while 1:
            try:
                time = self.unpacker.time()
            except Exception:
                break

            tx, ty, tz = self.unpacker.transform()

            rx, ry, rz, rw = self.unpacker.rotation()

            hight, width = self.unpacker.image_size()

            img_color_array = self.unpacker.arr(hight*width*3)

            # image = Image.frombytes("RGB", (width, hight), img_color_array, 'raw')

            dhight, dwidth = self.unpacker.image_size()

            img_depth_array = self.unpacker.arr(dhight*dwidth*4)

            # dimage = Image.frombytes("I", (dwidth, dhight), img_depth_array, 'raw')

            hunger, thirst, exhaustion, happiness = self.unpacker.feeling()

            snapshot = Snapshot(time)
            snapshot.set_location(tx, ty, tz)
            snapshot.set_rotation(rx, ry, rz, rw)
            snapshot.set_color_image(hight, width, img_color_array)
            snapshot.set_depth_image(dhight, dwidth, img_depth_array)
            snapshot.set_thoughts(hunger, thirst, exhaustion, happiness)

            yield snapshot
