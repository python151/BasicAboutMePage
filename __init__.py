from flask import Flask, request, render_template, redirect, url_for, jsonify
import sqlite3

class sec:
    def sanitize(listOfPoints, characters='''
    {}[];:<>,./?!@#$%^&*()-_=+\|'"`~
    '''):
        refinedData = []
        for point in listOfPoints:
            for char in characters:
                point = str(point)
                point = point.replace(char, "")
            if point == '"':
                point = ''
            refinedData.append(point)
        return ''.join(refinedData)

class database:
    def submit(tableName, variableList):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        str00 = '", "'.join(variableList)
        c.execute('INSERT INTO '+tableName+' VALUES("'+str00+'")')
        conn.commit()
        c.close()
        conn.close()

    def getTable(tableName):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("SELECT * FROM "+tableName)
        listOfRows = []
        for row in c.fetchall():
            listOfRows.append(row)
        listOfRows = database.dataRefiner(listOfRows)
        return sec.deSanitize(listOfRows)
        c.close()
        conn.close()

    def createTable(tableName, variableList):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        str00 = " TEXT,".join(variableList)
        sqlcode = 'CREATE TABLE IF NOT EXISTS '+tableName+' ('+str00+')'.replace(',)', ")")
        c.execute(sqlcode)
        conn.commit()
        c.close()
        conn.close()
    
    def rename(old, new):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('''A LTER TABLE "'''+old+'''" RENAME TO '''+new)
        conn.commit()
        c.execute('UPDATE lists SET name = "'+new+'" WHERE name = "'+old+'"')
        conn.commit()
        c.close()
        conn.close()

    def deleteItem(name, whereVar, var='email'):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('DELETE FROM '+name+' WHERE "'+var+'" = "'+whereVar+'"')
        conn.commit()
        c.close()
        conn.close()

    def get(var, whereVar, tableName, getting):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("SELECT "+getting+" FROM "+tableName+" WHERE '"+var+"' = '"+whereVar+"'")
        listOfRows = []
        for row in c.fetchall():
            listOfRows.append(row)
        listOfRows = database.dataRefiner(listOfRows)
        return sec.deSanitize(listOfRows)
        c.close()
        conn.close()

app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/Home')
def index():
   return render_template("index.htm")

@app.route('/Social Media')
def social():
   return render_template("social.htm")

@app.route('/About')
def about():
   return render_template("about.htm")

@app.route('/Comment')
def comment():
   return render_template("comment.htm")

@app.route('/data/', methods=["POST"])
def get_data():
    if request.method == "POST":
      comment = request.form.get("comment")
      comment = sec.sanitize(comment)
      database.submit("comments", [comment])
      return jsonify(str("Success!"))

if __name__ == '__main__':
    app.run()

