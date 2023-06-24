import os
import json
import base64
from glob import glob


class FileInterface:
    def __init__(self):
        os.chdir('files/')

    def list(self, params=[]):
        try:
            filelist = glob('*.*')
            return dict(status='OK', data=filelist)
        except Exception as e:
            return dict(status='ERROR', data=str(e))

    def get(self, params=[]):
        try:
            filename = params[0]
            if (filename == ''):
                return None
            fp = open(f"{filename}", 'rb')
            isifile = base64.b64encode(fp.read()).decode()
            return dict(status='OK', data_namafile=filename, data_file=isifile)
        except Exception as e:
            return dict(status='ERROR', data=str(e))

    def upload(self,params=[]):
        try:
            filename = params[0]
            isifile = params[1]
            if (filename == '' or isifile == ''):
                return None
            fp = open(f"{filename}",'wb')
            fp.write(base64.b64decode(isifile))
            fp.close()
            return dict(status='OK', data=f"file {filename} berhasil diupload")
        except Exception as e:
            return dict(status='ERROR',data=str(e))

    def delete(self,params=[]):
        try:
            filename = params[0]
            if (filename == ''):
                return None
            if os.path.exists(filename):
                os.remove(filename)
                return dict(status='OK', data=f"file {filename} berhasil dihapus")
            else:
                return dict(status='ERROR', data=f"file {filename} tidak ditemukan")
        except Exception as e:
            return dict(status='ERROR',data=str(e))


if __name__ == '__main__':
    f = FileInterface()
    print(f.list())
    print(f.get(['pokijan.jpg']))