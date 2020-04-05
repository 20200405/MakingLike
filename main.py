"""

实现文件加载热更新

"""

import os
import sys
import time
import subprocess
import threading


def main():
    print('three step: Hello 123')


def file_change():
    print("file detect has run 1")
    mtimes = {}
    while 1:
        filename = __file__
        mtime = os.stat(filename).st_mtime
        old_time = mtimes.get(filename)
        if old_time is None:
            mtimes[filename] = mtime
            continue
        elif mtime > old_time:
            print(' * Detected change in {}, reloading'.format(filename))
            os._exit(3)
        time.sleep(1)


if os.environ.get('secord_process'):
    print("this is the seconde step 2")
    threading.Thread(target=main, args=()).start()
    file_change()

# else中的代码无法被改变
else:
    while 1:
        print("this is the first step ")
        env = os.environ.copy()
        env['secord_process'] = 'true'
        exit_code = subprocess.call([sys.executable] + sys.argv, env=env)
