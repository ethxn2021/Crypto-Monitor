import sys
sys.dont_write_bytecode = True
from lib.monitors.ADAMonitor import ADAMonitor

class Main:
    def __init__(self):
        ADAMonitor().monitor()


Main()