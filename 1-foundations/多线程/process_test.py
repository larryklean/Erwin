from multiprocessing import Process
import os


def run_proc(*args):
    print("Run child process %s (%s)..." % (args, os.getpid()))


if __name__ == '__main__':
    print('Parent process is %s.' % os.getpid())
    p = Process(target=run_proc, args=('test'))
    print('Child process will start')
    p.start()
    p.join()
    print('Child process end.')

# import os
#
# print("Process (%s) start..." % os.getpid())
#
# pid = os.fork()
# if pid == 0:
#     print("Child process (%s),and my parent thread is (%s)" % (os.getpid(),os.getppid()))
