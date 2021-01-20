#!/usr/bin/env python

import logging
import datetime
import psutil
from influxdb import InfluxDBClient


class SystemStats:
    def __init__(self):
        logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.DEBUG, datefmt="%H:%M:%S")
        # influx configuration - edit these
        self.ifuser = "grafana"
        self.ifpass = "ca61ADC302"
        self.ifdb   = "home"
        self.ifhost = "127.0.0.1"
        self.ifport = 8086
        self.measurement_name = "system"

        # take a timestamp for this measurement
        self.time = datetime.datetime.utcnow()

        # collect some stats from psutil
        self.disk = psutil.disk_usage('/')
        self.mem = psutil.virtual_memory()
        self.load = psutil.getloadavg()

        # format the data as a single measurement for influx
        self.body = [
            {
                "measurement": self.measurement_name,
                "time": self.time,
                "fields": {
                    "load_1": self.load[0],
                    "load_5": self.load[1],
                    "load_15": self.load[2],
                    "disk_percent": self.disk.percent,
                    "disk_free": self.disk.free,
                    "disk_used": self.disk.used,
                    "mem_percent": self.mem.percent,
                    "mem_free": self.mem.free,
                    "mem_used": self.mem.used
                }
            }
        ]

        # connect to influx
        self.ifclient = InfluxDBClient(self.ifhost,self.ifport,self.ifuser,self.ifpass,self.ifdb)

    def grab_sysinfo(self):
        # write the measurement
        self.ifclient.write_points(self.body)
