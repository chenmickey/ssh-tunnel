#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import g

from ...router import deploy
from ...model.auth import Auth
from ...utils.msg import Msg


@deploy.route('/query', methods=['get'])
def query():
	ssh_tunnel = AutoSsh()
	g.ssh_tunnel_holder = ssh_tunnel.start()
	return Msg().msg('成功').send()


@deploy.route('/start', methods=['get'])
def start():
	ssh_tunnel = AutoSsh()
	g.ssh_tunnel_holder = ssh_tunnel.start()
	return Msg().msg('成功').send()


@deploy.route('/stop', methods=['get'])
def stop():
	g.ssh_tunnel_holder.stop()
	return Msg().msg('成功').send()
