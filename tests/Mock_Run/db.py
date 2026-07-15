###############
# df.py uses sqlite3 to create a database with the validated json data
# out of test_data.json
###############

# Libraries

import sqlite3
import json
from pathlib import Path


# Setting up json file

json_file = Path("tests/test_data.json")


if not json_file.exists():
    raise FileNotFoundError(f"File was not found: {json_file}")




########## Creating database
con = sqlite3.connect("arbor.db")

######### Establish connection
cur = con.cursor()


######### Creating tables

# paper table
cur.execute("CREATE TABLE IF NOT EXISTS papers (paper_id TEXT PRIMARY KEY, title TEXT, abstract TEXT, year INTEGER)")

#author table
cur.execute("CREATE TABLE IF NOT EXISTS authors (id INTEGER PRIMARY KEY, paper_id INTEGER NOT NULL, name TEXT, FOREIGN KEY (paper_id) REFERENCES papers (paper_id))")

# does delete cascade and update cascade make sense?

#citations table
cur.execute("CREATE TABLE IF NOT EXISTS citations (id INTEGER PRIMARY KEY, paper_id INTEGER NOT NULL, cited_paper_id TEXT, FOREIGN KEY (paper_id) REFERENCES papers (papers_id))")



######### Inserting data into database tables

# for papers
traffic = json.load(json_file.open(encoding="utf-8"))
columns = ["paperId", "title", "abstract", "year"]

params = [tuple(row[c] for c in columns) for row in traffic]
cur.executemany("INSERT INTO papers VALUES (?, ?, ?, ?)", params)



##### Closing connection
con.commit()
con.close()




