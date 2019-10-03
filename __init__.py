from flask import Flask, request, render_template, redirect, url_for, jsonify
import sqlite3
['(', ')', ',', "'", '"', '<', '>', '"""', "'''"]
class sec:
    def sanitize(listOfPoints,
     characters=[['backspace', '%08'],['tab', '%09'],['linefeed',  '%0A'],['creturn', '%0D'],['space', '  %20'],['!', '%21'],['"', '%22'],['#', '%23'],['$', '%24'],[' %', '%25'],['&', '%26'],["'", '%27'],['(', '%28'],[')', '%29'],['*', '%2A'],['+', '%2B'],[',', '%2C'],['-', '%2D'],['.', '%2E'],['/', '%2F'],['0', '%30'],['1', '%31'],['2', '%32'],['3', '%33'],['4', '%34'],['5', '%35'],['6', '%36'],['7', '%37'],['8', '%38'],['9', '%39'],[':', '%3A'],[';', '%3B'],['<', '%3C'],['=', '%3D'],['>', '%3E'],['?', '%3F'],['@', '%40'],['A', '%41'],['B', '%42'],['C', '%43'],['D', '%44'],['E', '%45'],['F', '%46'],['G', '%47'],['H', '%48'],['I', '%49'],['J', '%4A'],['K', '%4B'],['L', '%4C'],['M', '%4D'],['N', '%4E'],['O', '%4F'],['P', '%50'],['Q', '%51'],['R', '%52'],['S', '%53'],['T', '%54'],['U', '%55'],['V', '%56'],['W', '%57'],['X', '%58'],['Y', '%59'],['Z', '%5A'],['[', '%5B'],['\\', '%5C'],[']', '%5D'],['^', '%5E'],['_', '%5F'],['`', '%60'],['a', '%61'],['b', '%62'],['c', '%63'],['d', '%64'],['e', '%65'],['f', '%66'],['g', '%67'],['h', '%68'],['i', '%69'],['j', '%6A'],['k', '%6B'],['l', '%6C'],['m', '%6D'],['n', '%6E'],['o', '%6F'],['p', '%70'],['q', '%71'],['r', '%72'],['s', '%73'],['t', '%74'],['u', '%75'],['v', '%76'],['w', '%77'],['x', '%78'],['y', '%79'],['z', '%7A'],['{', '%7B'],['|', '%7C'],['}', '%7D'],['~', '%7E'],['¢', '%A2'],['£', '%A3'],['¥', '%A5'],['|', '%A6'],['§', '%A7'],['«', '%AB'],['¬', '%AC'],['¯', '%AD'],['º', '%B0'],['±', '%B1'],['ª', '%B2'],[',', '%B4'],['µ', '%B5'],['»', '%BB'],['¼', '%BC'],['½', '%BD'],['¿', '%BF'],['À', '%C0'],['Á', '%C1'],['Â', '%C2'],['Ã', '%C3'],['Ä', '%C4'],['Å', '%C5'],['Æ', '%C6'],['Ç', '%C7'],['È', '%C8'],['É', '%C9'],['Ê', '%CA'],['Ë', '%CB'],['Ì', '%CC'],['Í', '%CD'],['Î', '%CE'],['Ï', '%CF'],['Ð', '%D0'],['Ñ', '%D1'],['Ò', '%D2'],['Ó', '%D3'],['Ô', '%D4'],['Õ', '%D5'],['Ö', '%D6'],['Ø', '%D8'],['Ù', '%D9'],['Ú', '%DA'],['Û', '%DB'],['Ü', '%DC'],['Ý', '%DD'],['Þ', '%DE'],['ß', '%DF'],['à', '%E0'],['á', '%E1'],['â', '%E2'],['ã', '%E3'],['ä', '%E4'],['å', '%E5'],['æ', '%E6'],['ç', '%E7'],['è', '%E8'],['é', '%E9'],['ê', '%EA'],['ë', '%EB'],['ì', '%EC'],['í', '%ED'],['î', '%EE'],['ï', '%EF'],['ð', '%F0'],['ñ', '%F1'],['ò', '%F2'],['ó', '%F3'],['ô', '%F4'],['õ', '%F5'],['ö', '%F6'],['÷', '%F7'],['ø', '%F8'],['ù', '%F9'],['ú', '%FA'],['û', '%FB'],['ü', '%FC'],['ý', '%FD'],['þ', '%FE'],['ÿ', '%FF']]):
        refinedData = []
        for point in listOfPoints:
            for char in characters:
                point = str(point)
                point = point.replace(char[0], char[1])
            if point == '"':
                point = ''
            refinedData.append(point)
        return ''.join(refinedData)

    def deSanitize(listOfPoints,
     characters=[['backspace', '%08'],['tab', '%09'],['linefeed',  '%0A'],['creturn', '%0D'],['space', '  %20'],['!', '%21'],['"', '%22'],['#', '%23'],['$', '%24'],[' %', '%25'],['&', '%26'],["'", '%27'],['(', '%28'],[')', '%29'],['*', '%2A'],['+', '%2B'],[',', '%2C'],['-', '%2D'],['.', '%2E'],['/', '%2F'],['0', '%30'],['1', '%31'],['2', '%32'],['3', '%33'],['4', '%34'],['5', '%35'],['6', '%36'],['7', '%37'],['8', '%38'],['9', '%39'],[':', '%3A'],[';', '%3B'],['<', '%3C'],['=', '%3D'],['>', '%3E'],['?', '%3F'],['@', '%40'],['A', '%41'],['B', '%42'],['C', '%43'],['D', '%44'],['E', '%45'],['F', '%46'],['G', '%47'],['H', '%48'],['I', '%49'],['J', '%4A'],['K', '%4B'],['L', '%4C'],['M', '%4D'],['N', '%4E'],['O', '%4F'],['P', '%50'],['Q', '%51'],['R', '%52'],['S', '%53'],['T', '%54'],['U', '%55'],['V', '%56'],['W', '%57'],['X', '%58'],['Y', '%59'],['Z', '%5A'],['[', '%5B'],['\\', '%5C'],[']', '%5D'],['^', '%5E'],['_', '%5F'],['`', '%60'],['a', '%61'],['b', '%62'],['c', '%63'],['d', '%64'],['e', '%65'],['f', '%66'],['g', '%67'],['h', '%68'],['i', '%69'],['j', '%6A'],['k', '%6B'],['l', '%6C'],['m', '%6D'],['n', '%6E'],['o', '%6F'],['p', '%70'],['q', '%71'],['r', '%72'],['s', '%73'],['t', '%74'],['u', '%75'],['v', '%76'],['w', '%77'],['x', '%78'],['y', '%79'],['z', '%7A'],['{', '%7B'],['|', '%7C'],['}', '%7D'],['~', '%7E'],['¢', '%A2'],['£', '%A3'],['¥', '%A5'],['|', '%A6'],['§', '%A7'],['«', '%AB'],['¬', '%AC'],['¯', '%AD'],['º', '%B0'],['±', '%B1'],['ª', '%B2'],[',', '%B4'],['µ', '%B5'],['»', '%BB'],['¼', '%BC'],['½', '%BD'],['¿', '%BF'],['À', '%C0'],['Á', '%C1'],['Â', '%C2'],['Ã', '%C3'],['Ä', '%C4'],['Å', '%C5'],['Æ', '%C6'],['Ç', '%C7'],['È', '%C8'],['É', '%C9'],['Ê', '%CA'],['Ë', '%CB'],['Ì', '%CC'],['Í', '%CD'],['Î', '%CE'],['Ï', '%CF'],['Ð', '%D0'],['Ñ', '%D1'],['Ò', '%D2'],['Ó', '%D3'],['Ô', '%D4'],['Õ', '%D5'],['Ö', '%D6'],['Ø', '%D8'],['Ù', '%D9'],['Ú', '%DA'],['Û', '%DB'],['Ü', '%DC'],['Ý', '%DD'],['Þ', '%DE'],['ß', '%DF'],['à', '%E0'],['á', '%E1'],['â', '%E2'],['ã', '%E3'],['ä', '%E4'],['å', '%E5'],['æ', '%E6'],['ç', '%E7'],['è', '%E8'],['é', '%E9'],['ê', '%EA'],['ë', '%EB'],['ì', '%EC'],['í', '%ED'],['î', '%EE'],['ï', '%EF'],['ð', '%F0'],['ñ', '%F1'],['ò', '%F2'],['ó', '%F3'],['ô', '%F4'],['õ', '%F5'],['ö', '%F6'],['÷', '%F7'],['ø', '%F8'],['ù', '%F9'],['ú', '%FA'],['û', '%FB'],['ü', '%FC'],['ý', '%FD'],['þ', '%FE'],['ÿ', '%FF']]):
        refinedData = []
        for point in listOfPoints:
            for char in characters:
                point = str(point)
                point = point.replace(char[1], char[0])
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

def route(app, route, template):
    @app.route(route)
    def basic():
        return render_template(template)
    return True

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

@app.route('/data/', methods=["GET", "POST"])
def get_data():
    if request.method == "POST":
      comment = request.form.get("comment")
      comment = sec.sanitize(comment)
      database.submit("comments", [comment])
      return jsonify(str("Success!"))


if __name__ == '__main__':
    app.run(debug=True)

