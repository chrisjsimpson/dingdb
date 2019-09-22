#!/usr/bin/env python
import sqlite3
import argparse


def up():
    con = sqlite3.connect(args.db)

    cur = con.cursor()
    cur.executescript(
        """
  CREATE TABLE IF NOT EXISTS thing (
    id text UNIQUE,
    name text,
    kind_id text
  );

  CREATE TABLE IF NOT EXISTS version (
    id text UNIQUE,
    thing_id text,
    creator text,
    creation_date text,
    comment text
  );

  CREATE TABLE IF NOT EXISTS data (
    thing_id text,
    version_id text,
    key text,
    value text
  );

    """
    )
    con.commit()


def down():
    con = sqlite3.connect(args.db)
    cur = con.cursor()
    cur.executescript(
    """
        DROP TABLE IF EXISTS thing;
        DROP TABLE IF EXISTS version;
        DROP TABLE IF EXISTS data;
    """
    )
    con.commit()


parser = argparse.ArgumentParser()
parser.add_argument(
    "-db",
    "-database",
    default="../../../../data.db",
    help="Path to the sqlite database",
)
group = parser.add_mutually_exclusive_group()
group.add_argument("-up", action="store_true", help="Run the 'up' migration.")
group.add_argument("-down", action="store_true", help="Run the 'down' migration.")

args = parser.parse_args()

if args.up:
    print("Running 'up' migration.")
    up()
elif args.down:
    print("Running 'down' migration.")
    down()
