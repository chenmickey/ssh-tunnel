#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import g

from . import deploy
from .. import AutoSsh
from .. import Msg


@deploy.route('/auto/ssh/query', methods=['get'])
def query():
	if g.ssh_tunnel_holder:
		return Msg().msg('成功')()
	else:
		return Msg().msg('成功')()


@deploy.route('/auto/ssh/start', methods=['get'])
def start():
	ssh_tunnel = AutoSsh()
	g.ssh_tunnel_holder = ssh_tunnel.start()
	return Msg().msg('成功').send()


@deploy.route('/auto/ssh/stop', methods=['get'])
def stop():
	try:
		g.ssh_tunnel_holder.stop()
	except BaseException, e:
		return Msg().fail('').msg('成功').send()
	finally:
		g.ssh_tunnel_holder = None
		return Msg().msg('成功').send()
