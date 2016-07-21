#!/usr/bin/env python

import sys
import threading
import subprocess
import time
import Queue

def main(args=None):
    s = args[1]
    q = Queue.Queue()
    e = threading.Event();
    args = (s,q,e)
    t = threading.Thread(target=_spawn, args=(args,))
    t.start()
    e.wait()
    while not q.empty():
        print "getting..."
        rc = q.get()
        print "got {}".format(rc)

def _spawn(args):
    s, q, e = args
    p = subprocess.Popen(["ls", s])
    rc = p.wait()
    q.put(rc)
    e.set()

if __name__ == "__main__":
    sys.exit(main(sys.argv))
