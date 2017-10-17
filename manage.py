#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf8')
from app import create_app
from config import Config

app = create_app(Config)

if __name__ == "__main__":
	app.run()

