import os
import sys
import signal

def daemonize ( terminateFunc=lambda *args: None,
        showpid = True,
        stdin = '/dev/null',
        stdout = '/dev/null',
        stderr = '/dev/null'
    ):
    fork()
    pid = fork()
    
    if (showpid):
        sys.stdout.write('process daemonized with pid: %d\n' % (pid))

    pid = os.getpid()
    createPidFile(pid)
    signal.signal(signal.SIGTERM, lambda s, f, p=pid, t=terminateFunc : signalHandler(s,f,p,t))

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

def getPidFileName(pid):
    return "daemon.pid"

def signalHandler(signum, frame, pid, terminateFunc):
    try:
        os.remove(getPidFileName(pid))
    except OSError:
        pass
    terminateFunc()
    sys.exit(0)

def createPidFile(pid):
    with open(getPidFileName(pid), "w") as pidFile:
        pidFile.write(str(pid))