#!/usr/bin/env python2

import sys, redis, os, re

REDIS_IP = "127.0.0.1"
REDIS_PORT = 6379
REDIS_DB = 4

r = redis.StrictRedis(host=REDIS_IP, port=REDIS_PORT, db=REDIS_DB)
path = sys.argv[1]

def index_dir(path, r):
    path = os.path.abspath(os.path.expandvars(os.path.expanduser(path)))
    path = re.sub(os.path.sep + '$', '', path)
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    for f in files:
        key, val = f, os.path.split(path)[-1]
        print "set", key, val
        r.set(key, val)

index_dir(path, r)


