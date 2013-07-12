import sqlite3

db=sqlite3.connect("Task.db")

with db:
	cur=db.cursor()
	db.execute('DROP TABLE IF EXISTS tasktable')
	db.execute('CREATE TABLE tasktable(task_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL,due_date TEXT NOT NULL,priority INTEGER NOT NULL, status INTEGER NOT NULL)')
	db.execute('INSERT INTO tasktable (name,due_date,priority,status) VALUES("Setting the Database","12/07/2013",10,1)')

db.close()	         
