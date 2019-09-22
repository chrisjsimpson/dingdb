import sqlite3

class thingdb():

  def __init__(self, database='./data.db'):
    """Initalise connection
    :args: database - full path to sqlite database
    """
    self.database = database


  def getdb(self):
    """Return database connection"""
    conn = sqlite3.connect(self.database)
    conn.row_factory = sqlite3.Row
    return conn

  def help():
    print("""Usage: 
      - getThing(id)
      - putThing(7, 'person', 'person', data=[{'key':'name', 'value': 'Sam'}, {'key':'age', 'value':30}])
      - getThingsByType(kind_id)
      
    """)

  def getThing(self, id):
    db = self.getdb()
    c = db.cursor()
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
    db.close()
    # Build a thing
    rawThing = {
    'id': result[0]['id'],
    'kind': result[0]['kind_id'],
    'name': result[0]['name'],
    'data': {}
    }
    for row in result:
      rawThing['data'][row['key']] = row['value']
    # Return thing
    return thing(rawThing)

  def getThingsByType(self, kind_id):
    """Return list of things of a given type"""
    db = self.getdb()
    c = db.cursor()
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
    db.close()
    # Build things list
    things = {} #Dict
    for row in result:
      currentId = row['id']
      if currentId not in things:
        things[currentId] = {}
      things[currentId]['kind'] = row['kind_id']
      if 'data' not in things[currentId]:
        things[currentId]['data'] = {}
      # Apply attributes
      things[currentId]['data'][row['key']] = row['value']
   
    return things

  def putThing(self, thing_id, name, kind_id, data=None, creator=None, creation_date=None, comment=None):
    db = self.getdb()
    c = db.cursor()
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
    db.commit()

  def deleteThing(self, thing_id):
    db = self.getdb()
    c = db.cursor()
    c.execute(
    """
    DELETE FROM thing WHERE id=?
    """, (thing_id,))

    c.execute(
    """ 
    DELETE FROM version WHERE thing_id = ?;
    """, (thing_id,))
    db.commit()

class thing(thingdb):
  def __init__(self, rawThing):
    super().__init__()
    self.thing = rawThing
  
  def load(self):
    """Return thing object"""
    return self.thing

  def save(self):
    """Persist latest thing to the database"""
    # Refresh attributes - if an attribute never gets explicitly set, its not available
      # TODO understand why we need to refesh them...
    for key in self.thing['data'].keys():
      try:
        self.thing['data'][key] = self.__getattribute__(key) 
      except AttributeError:
        self.__setattr__(key, self.thing['data'][key])

    for key in self.thing['data'].keys():
      db = self.getdb()
      c = db.cursor()
      c.execute(
      """
      INSERT INTO data (thing_id, version_id, key, value)
      VALUES (?, ?, ?, ?)
      """,(self.thing['id'], 0, key, self.__getattribute__(key)))
      db.commit()

  def __getattr__(self, attribute):
    return self.__dict__['thing']['data'][attribute]
    

