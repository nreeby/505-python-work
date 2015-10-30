#download python-twitter from https://code.google.com/p/python-twitter/downloads/list
#cd into that folder and run the line (python setup.py install --user) in terminal.
import sqlite3
import time
import twitter, datetime
user = 4060620058
file = open("/Users/nreeby/Documents/505-python-work/Tweeting/keys.txt")
creds = file.readline().strip().split(',')
print(creds)
api = twitter.Api(creds[0],creds[1],creds[2],creds[3])
timestamp = datetime.datetime.utcnow()
console = sqlite3.connect("/Users/nreeby/Library/Application Support/Google/Chrome/Default/History")
cursor = console.cursor()
cursor.execute("SELECT * FROM urls")
Titleofpage=cursor.execute("SELECT title FROM urls limit 1")
rows = cursor.fetchall()
for row in rows:
    response = api.PostUpdate("I'm really liking " + row[0] +" and this was tweeted at "+str(timestamp))
    print("Status updated to: " + response.text)
console.close()