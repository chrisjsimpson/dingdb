# Dingdb, a thingdb like storage & retrieval Python API 

                                                                                                        
```                                                                                                        
DDDDDDDDDDDDD          iiii                                      DDDDDDDDDDDDD      BBBBBBBBBBBBBBBBB   
D::::::::::::DDD      i::::i                                     D::::::::::::DDD   B::::::::::::::::B  
D:::::::::::::::DD     iiii                                      D:::::::::::::::DD B::::::BBBBBB:::::B 
DDD:::::DDDDD:::::D                                              DDD:::::DDDDD:::::DBB:::::B     B:::::B
  D:::::D    D:::::D iiiiiiinnnn  nnnnnnnn       ggggggggg   ggggg D:::::D    D:::::D B::::B     B:::::B
  D:::::D     D:::::Di:::::in:::nn::::::::nn    g:::::::::ggg::::g D:::::D     D:::::DB::::B     B:::::B
  D:::::D     D:::::D i::::in::::::::::::::nn  g:::::::::::::::::g D:::::D     D:::::DB::::BBBBBB:::::B 
  D:::::D     D:::::D i::::inn:::::::::::::::ng::::::ggggg::::::gg D:::::D     D:::::DB:::::::::::::BB  
  D:::::D     D:::::D i::::i  n:::::nnnn:::::ng:::::g     g:::::g  D:::::D     D:::::DB::::BBBBBB:::::B 
  D:::::D     D:::::D i::::i  n::::n    n::::ng:::::g     g:::::g  D:::::D     D:::::DB::::B     B:::::B
  D:::::D     D:::::D i::::i  n::::n    n::::ng:::::g     g:::::g  D:::::D     D:::::DB::::B     B:::::B
  D:::::D    D:::::D  i::::i  n::::n    n::::ng::::::g    g:::::g  D:::::D    D:::::D B::::B     B:::::B
DDD:::::DDDDD:::::D  i::::::i n::::n    n::::ng:::::::ggggg:::::gDDD:::::DDDDD:::::DBB:::::BBBBBB::::::B
D:::::::::::::::DD   i::::::i n::::n    n::::n g::::::::::::::::gD:::::::::::::::DD B:::::::::::::::::B 
D::::::::::::DDD     i::::::i n::::n    n::::n  gg::::::::::::::gD::::::::::::DDD   B::::::::::::::::B  
DDDDDDDDDDDDD        iiiiiiii nnnnnn    nnnnnn    gggggggg::::::gDDDDDDDDDDDDD      BBBBBBBBBBBBBBBBB   
                                                          g:::::g                                       
                                              gggggg      g:::::g                                       
                                              g:::::gg   gg:::::g                                       
                                               g::::::ggg:::::::g                                       
                                                gg:::::::::::::g                                        
                                                  ggg::::::ggg                                          
                                                     gggggg                                             

Put things. Get things.
```
Simple implementation of **Thingdb**, called **Dingdb** (German for *'thing'*)
Currently expects a sqlite3 database.

Inspired by: 

- http://web.archive.org/web/20080109204022/http://pharos.infogami.com/tdb
- https://github.com/reddit-archive/reddit/blob/master/r2/r2/lib/db/ding.py
- https://github.com/itslukej/ding/tree/master/dingdb
- https://www.reddit.com/r/webdev/comments/30ycc1/has_anyone_built_a_reddit_clone_if_so_any_tips_on/
  - http://www.reddit.com/r/webdev/.json
- https://www.youtube.com/watch?v=hB-M8oH4K4w

# Installation

```
git clone git@github.com:chrisjsimpson/dingdb.git
cd dingdb/
pip3 install ./
python3 dingdb/migrations/1-create-dingdb-schema.py -up -db ./data.db
```

# Usage

```
from dingdb import dingdb
from uuid import uuid4

# Connect and insert data
tdb = dingdb(database='./data.db')
# Put things
tdb.putDing(1, 'person', 'person', data=[{'key':'name', 'value': 'Sam'}, {'key':'age', 'value':30}])
# Get a thing
person = tdb.getDing(1)
person.name 
'Sam'
person.age
'30'
person.age = 31
person.save()

# Get things by type
tdb.getDingsByType('person')

# More..

# Use a uuid for ids:
tdb.putDing(str(uuid4()), 'person', 'person', data=[{'key':'name', 'value': 'Sam'}, {'key':'age', 'value':30}])
```
