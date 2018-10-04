import sqlite3
import os
from getl.extractors.location_history  import LocationHistory

class GetlError(Exception):
    pass


class Getl(object):
  def __init__(self, path):
    if not isinstance(path, str):
      raise GetlError('path should be string')

    self.db   = sqlite3.connect(':memory:')
    self.path = os.path.abspath(path)

  def load_location_history(self):
    LocationHistory(self.db, self.path)

  def load_all(self):
    self.load_location_history()

  def sql(self, query):
    return self.db.execute(query).fetchall()

  def save(self, path):
    disk_db = sqlite3.connect(path)
    with disk_db:
      for line in self.db.iterdump():
        if line not in ('BEGIN;', 'COMMIT;'): # let python handle the transactions
          disk_db.execute(line)
    disk_db.commit()
