from .reader import Reader
import sys
from datetime import  datetime as dt


def main():
    if len(sys.argv) !=3:
        print ('Usage: python -m thoughts <command> <arg>')
        return

    if sys.argv[1] == 'read':
        reader = Reader(sys.argv[2])

        print (f'user {reader.id}: {reader.name}, born {dt.fromtimestamp(reader.birth)} ({reader.gender})')
        for sn in reader:
            print (f'Snapshot from {dt.fromtimestamp(sn.time / 1000)} on ({sn.tx}, {sn.ty}, {sn.tz}) / ({sn.rx}, {sn.ry}, {sn.rz}, {sn.rw}) with {sn.cwidth}X{sn.chight} color image and a {sn.dwidth}X{sn.dhight} depth image')
if __name__ == '__main__':
    main()