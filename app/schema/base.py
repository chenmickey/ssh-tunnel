from tinydb import TinyDB


class Base(object):
	def __init__(self, file_path):
		self.db = TinyDB(file_path)
	
	def insert(self):
		return self.db.insert
	
	def all(self):
		return self.db.all
	
	def search(self):
		return self.db.search
	
	def update(self):
		return self.db.update
	
	def remove(self):
		return self.db.remove
	
	def purge(self):
		return self.db.purge
