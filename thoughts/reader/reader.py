
import struct
from PIL import Image

from .formats import fmt
from .snapshot import Snapshot

class Reader():
    def __init__(self, path):
        self.path = path
        self.data_file = open(self.path, "rb")

        self.id, self.name_length = struct.unpack(fmt.ID_NAME_LENGTH_FORMAT, self.data_file.read(12))
            
        self.name = struct.unpack(fmt.BYTE_ARRAY_FORMAT(self.name_length), self.data_file.read(self.name_length))[0].decode("utf-8")

        self.birth, self.gender = struct.unpack(fmt.BIRTH_GENDER_FORMAT, self.data_file.read(5))

        self.gender = self.gender.decode("utf-8").replace('m', 'male').replace('f', 'female').replace('o', 'other')


    def __iter__(self):

        while 1:
            try:

                time =struct.unpack(fmt.TIME_FORMAT, self.data_file.read(8))[0]
            except:
                break

            tx, ty, tz =struct.unpack(fmt.TRNSL_FORMAT, self.data_file.read(24))

            rx, ry, rz, rw, hight, width =struct.unpack(fmt.ROTATE_IMWIDTH_IMHIGHT_FORMAT, self.data_file.read(40))
                
            img_color_array = struct.unpack(fmt.BYTE_ARRAY_FORMAT(hight*width*3), self.data_file.read(hight*width*3))[0]
                
            image = Image.frombytes("RGB",(width,hight),img_color_array, 'raw')

            dhight, dwidth = struct.unpack(fmt.DEPTH_IMWIDTH_IMHIGHT_FORMAT, self.data_file.read(8))

            img_depth_array = struct.unpack(fmt.BYTE_ARRAY_FORMAT(dhight*dwidth*4), self.data_file.read(dhight*dwidth*4))[0]

            dimage = Image.frombytes("I",(dwidth,dhight), img_depth_array, 'raw')

            hunger, thirst, exhaustion, happiness = struct.unpack(fmt.FEELING_FORMAT, self.data_file.read(16))
            
            snapshot = Snapshot(time)
            snapshot.set_location(tx, ty, tz)
            snapshot.set_rotation(rx, ry, rz, rw)
            snapshot.set_color_image(hight, width, img_color_array)
            snapshot.set_depth_image(dhight, dwidth, img_depth_array)
            snapshot.set_thoughts(hunger, thirst, exhaustion, happiness)

            yield snapshot
            
