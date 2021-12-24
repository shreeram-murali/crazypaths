import asyncio
import math
import time
import xml.etree.cElementTree as ET
from threading import Thread
import logging

import qtm

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
from cflib.utils.multiranger import Multiranger

X_FENCE, Y_FENCE, Z_FENCE = (-2, 2), (-1.5, 1.5), (0, 1.5) # meters
FLYING = True
CF_URI = 'radio://0/80/2M'
QUALISYS_IP = '192.168.0.106'
CF_NAME = 'cf1'

def sqrt(x):
    return 0.0 if (x < 0.0) else math.sqrt(x)

class fence:
    def __init__(self, x_range, y_range, z_range) -> None:
        self.xmin = x_range[0]
        self.xmax = x_range[1]
        self.ymin = y_range[0]
        self.ymax = y_range[1]
        self.zmin = z_range[0]
        self.zmax = z_range[1]
    
    def astray(self, ) -> bool:
        #check if it has gone out of bounds
        """text"""

if __name__ == '__main__':
    with SyncCrazyflie(CF_URI, cf=Crazyflie(rw_cache='./cache')) as scf:
            cf = scf.cf