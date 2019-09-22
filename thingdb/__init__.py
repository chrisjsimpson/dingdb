import sqlite3

def getThing(id):
  conn = sqlite3.connect('./data.db')
  conn.row_factory = sqlite3.Row
  c = conn.cursor()
  c.execute(
  """
  SELECT DISTINCT
  thing.id, thing.name, thing.kind_id,
  data.version_id, data.key, data.value
  from data
   join version on 
    data.thing_id = version.thing_id
   join thing on
    version.thing_id = thing.id
  where data.thing_id = ?
  """, (id,))
  result = c.fetchall()
  conn.close()
  # Build thing
  thing = {
  'id': result[0]['id'],
  'kind': result[0]['kind_id'],
  'name': result[0]['name'],
  'data': {}
  }
  for row in result:
    thing['data'][row['key']] = row['value']
  # Return thing
  return thing

def getThingsByType(kind_id):
  """Return list of things of a given type"""
  conn = sqlite3.connect('./data.db')
  conn.row_factory = sqlite3.Row
  c = conn.cursor()
  c.execute(
    """
    SELECT DISTINCT
    thing.id, thing.name, thing.kind_id,
    data.version_id, data.key, data.value
    FROM data
     JOIN version ON
      data.thing_id = version.thing_id
     JOIN thing ON
      version.thing_id = thing.id
    WHERE thing.kind_id = ?
    GROUP BY data.thing_id, data.key
    ORDER BY thing.id

  """, (kind_id,))
  result = c.fetchall()
  conn.close()
  # Build things list
  things = {} #Dict
  for row in result:
    currentId = int(row['id'])
    if currentId not in things:
      things[currentId] = {}
    things[currentId]['kind'] = row['kind_id']
    if 'data' not in things[currentId]:
      things[currentId]['data'] = {}
    # Apply attributes
    things[currentId]['data'][row['key']] = row['value']
 
  return things

def putThing(thing_id, name, kind_id, data=None, creator=None, creation_date=None, comment=None):
  conn = sqlite3.connect('./data.db')
  c = conn.cursor()
  
  c.execute(
  """
  INSERT INTO thing (id, name, kind_id) VALUES (?, ?, ?)
  """, (thing_id, name, kind_id))

  c.execute(
  """
  INSERT INTO version (id, thing_id, creator, creation_date,comment) VALUES (?, ?, ?, ?, ?)
  """, (0, thing_id, creator, creation_date, comment))
  
  for attribute in data:
    c.execute(
    """
    INSERT INTO data (version_id, thing_id, key, value) VALUES(?, ?, ?, ?)
    """, (0, thing_id, attribute['key'], attribute['value']))
  # Commit all 
  conn.commit()

def deleteThing(thing_id):
  conn = sqlite3.connect('./data.db')
  c = conn.cursor()
  c.execute(
  """
  DELETE FROM thing WHERE id=?
  """, (thing_id,))

  c.execute(
  """ 
  DELETE FROM version WHERE thing_id = ?;
  """, (thing_id,))
  conn.commit()