# Thingdb

Simple implementation of thingdb.
Currently expects a sqlite3 database.

Inspired by: 

- http://web.archive.org/web/20080109204022/http://pharos.infogami.com/tdb
- https://github.com/reddit-archive/reddit/blob/master/r2/r2/lib/db/thing.py
- https://github.com/itslukej/thing/tree/master/thingdb
- https://www.reddit.com/r/webdev/comments/30ycc1/has_anyone_built_a_reddit_clone_if_so_any_tips_on/
  - http://www.reddit.com/r/webdev/.json
- https://www.youtube.com/watch?v=hB-M8oH4K4w

# Installation

```
git clone git@github.com:chrisjsimpson/thingdb.git
cd thingdb/
pip3 install ./
python3 thingdb/migrations/1-create-thingdb-schema.py -up -db ./data.db
```

# Usage

```
from thingdb import thingdb
from uuid import uuid4

thingdb.help() # See help

# Connect and insert data
tdb = thingdb(database='./data.db')
# Put things
tdb.putThing(1, 'person', 'person', data=[{'key':'name', 'value': 'Sam'}, {'key':'age', 'value':30}])
# Get a thing
person = tdb.getThing(1)
person.name 
'Sam'
person.age
'30'
person.age = 31
person.save()

# Get things by type
tdb.getThingsByType('person')

# More..

# Use a uuid for ids:
tdb.putThing(str(uuid4()), 'person', 'person', data=[{'key':'name', 'value': 'Sam'}, {'key':'age', 'value':30}])
```
