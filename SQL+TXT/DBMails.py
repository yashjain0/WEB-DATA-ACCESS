simport sqlite3
import re

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
#creating a Table if didn't exist
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = re.findall('\S+@(\S+)',pieces[1])
    #its always email[0] because its changing every time
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (str(email[0]),))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (str(email[0]),))
    else:
      #if row is more than 0 then update and add increase one with adding email[0]
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (str(email[0]),))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 20'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
