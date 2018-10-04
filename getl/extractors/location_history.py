from getl.extractors.extractor import Extractor
import json

class LocationHistory(Extractor):
  def __init__(self, db, path):
    super().__init__(db, path)

  def create_table(self):
    self.sql('''
      CREATE TABLE locations(
        latitude          FLOAT NOT NULL,
        longitude         FLOAT NOT NULL,
        accuracy          FLOAT,
        altitude          FLOAT,
        vertical_accuracy FLOAT,
        activity          JSON,
        timestamp         DATETIME NOT NULL
      );
    ''')

  def load(self):
    data = self.load_json('/Location History/Location History.json')

    for raw_location in data['locations']:
      location = self.shape_location(raw_location)

      self.sql(f'''
        INSERT INTO locations (
          latitude,
          longitude,
          accuracy,
          altitude,
          vertical_accuracy,
          activity,
          timestamp
        ) VALUES (
          {location['latitude']},
          {location['longitude']},
          {'NULL' if location['accuracy'] == None else location['accuracy']},
          {'NULL' if location['altitude'] == None else location['altitude']},
          {'NULL' if location['vertical_accuracy'] == None else location['vertical_accuracy']},
          {'NULL' if location['activity'] == None else "'" + json.dumps(location['activity']) + "'"},
          '{location['timestamp']}'
        );
      ''')

    self.db.commit()

  def shape_location(self, raw_location):
    return {
      'timestamp':         self.extract_time(raw_location['timestampMs']),
      'latitude':          raw_location['latitudeE7']/1e7,
      'longitude':         raw_location['longitudeE7']/1e7,
      'accuracy':          raw_location.get('accuracy'),
      'altitude':          raw_location.get('altitude'),
      'vertical_accuracy': raw_location.get('verticalAccuracy'),
      'activity':          raw_location.get('activity')
    }
