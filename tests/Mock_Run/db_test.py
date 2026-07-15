#####
# File for testing the success of the database injection
#####




# Libraries
import sqlite3
import json
from pathlib import Path



# Establish connection to the database
con = sqlite3.connect("arbor.db")
cur = con.cursor()



#######
#  Run checks
#######

# Check if the papers table exists
cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='papers'")
if not cur.fetchone():
    print("Error: papers table does not exist")
else:
    print("Success: papers table exists")

# Check if the authors table exists
cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='authors'")
if not cur.fetchone():
    print("Error: authors table does not exist")
else:
    print("Success: authors table exists")

# Check if the citations table exists
cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='citations'")
if not cur.fetchone():
    print("Error: citations table does not exist")
else:
    print("Success: citations table exists")

############
# Run queries
############

cur.execute("SELECT COUNT(*) FROM papers")
print(f"Number of papers: {cur.fetchone()[0]}")

cur.execute("SELECT title FROM papers")
print(f"Titles of papers: {[row[0] for row in cur.fetchall()]}")

# Check abstracts
cur.execute("SELECT abstract FROM papers")
print(f"Abstracts of papers: {[row[0] for row in cur.fetchall()]}")
