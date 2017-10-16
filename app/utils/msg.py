# -*- coding: utf-8 -*-

import json


class Msg(object):
	def __init__(self):
		self.message = {
			'meta': {
				'page': {
					'total': 0
				}
			},
			'user': {},
			'configure': {},
			'dictionary': {},
			'result': None,
			'status': True,
			'module': '',
			'message': ''
		}
	
	def to_json(self):
		return json.dumps(
				self.message,
				ensure_ascii=False,
				check_circular=True,
				indent=4,
				encoding="utf-8",
				sort_keys=True)
	
	def page(self, number):
		self.message['meta']['page']['total'] = number
		return self
	
	def succeed(self):
		self.message['status'] = True
		return self
	
	def fail(self):
		self.message['status'] = False
		return self
	
	def msg(self, msg):
		self.message['message'] = msg
		return self
	
	def result(self, result):
		self.message['result'] = result
		return self
	
	def send(self):
		return self.to_json()
	
	def __call__(self):
		return self.to_json()
