import os
import sys

def daemonize (
        showpid = True,
        stdin = '/dev/null',
        stdout = '/dev/null',
        stderr = '/dev/null'
    ):
    fork()
    pid = fork()

    if (showpid):
        sys.stdout.write('process daemonized with pid: %d\n' % (pid))


    # Redirect standard file descriptors.
    si = open(stdin, 'r')
    so = open(stdout, 'a+')
    se = open(stderr, 'a+')
    os.dup2(si.fileno(), sys.stdin.fileno())
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(), sys.stderr.fileno())

    return pid


def fork ():
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
    except OSError as e:
        sys.stderr.write('fork failed: (%d) %s\n' % (e.errno, e.strerror))
        sys.exit(1)

    # Decouple from parent environment.
    os.umask(0)
    os.setsid()
    return os.getpid()
