#!/usr/bin/env python3
from threading import Thread
from dottalk   import DotTalk
from dotserver import DotServer


PROCESSES = (DotTalk, DotServer)

for process in PROCESSES:
    Thread(target=process().run).start()
