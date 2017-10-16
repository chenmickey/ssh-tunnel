#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from multiprocessing import Process


class AutoSsh(object):
	def __init__(self):
		self.monitorPort = "7777"
		self.bridgePort = "10000"
		self.remoteUser = 'dysec'
		self.remoteIp = "47.92.160.84"
		self.process = None
	
	def _start(self):
		cmd = "/usr/bin/autossh -M 7777 -NR " + self.bridgePort + ":localhost:22 " + self.remoteUser + "@" + self.remoteIp + " -p22"
		os.system(cmd)
	
	def start(self):
		self.process = Process(target=self._start(), args=())
		self.process.start()
		return self
	
	def stop(self):
		self.process.terminate()
