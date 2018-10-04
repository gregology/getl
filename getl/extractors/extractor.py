from os import path
from datetime import datetime
import json

class ExtractorError(Exception):
    pass


class Extractor(object):
  def __init__(self, db, path):
    self.db = db
    self.path = path
    self.create_table()
    self.load()

  def load_json(self, uri):
    asset_path = self.path + uri
    if not path.isfile(asset_path):
      raise ExtractorError(f'file not found at {asset_path}')

    with open(asset_path) as f:
      data = json.load(f)

    return data

  def extract_time(self, unix_epoch_time):
    unix_epoch_time = float(unix_epoch_time)
    if unix_epoch_time > 10000000000:
      unix_epoch_time = unix_epoch_time/1000
    return datetime.fromtimestamp(unix_epoch_time).strftime('%Y-%m-%d %H:%M:%S')

  def sql_safe(self, text):
    return text.replace("'","''")

  def sql(self, query):
    return self.db.execute(query).fetchall()
