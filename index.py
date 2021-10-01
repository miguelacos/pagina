from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app=Flask(__name__)

# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'prueba'
mysql = MySQL(app)

# settings
app.secret_key = "mysecretkey"

@app.route('/')
def principal():
    return render_template('Vulnerabilidad.html')

@app.route('/Temperatura.html')
def Temperatura():
    return render_template('Temperatura.html')

@app.route('/Precipitacion.html')
def Precipitacion():
    return render_template('Precipitacion.html')


@app.route('/Vulnerabilidad.html')
def vulnerabilidad():
    return render_template('Vulnerabilidad.html')

@app.route('/DescargaV.html')
def descargav():
    return render_template('DescargaV.html')

@app.route('/RS.html')
def RS():
    return render_template('RS.html')

@app.route('/EstacionesP.html')
def estacionesP():
    return render_template('EstacionesP.html')

@app.route('/EstacionesT.html')
def estacionesT():
    return render_template('EstacionesT.html')

@app.route('/Est1pre.html')
def est1pre():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts1p')
    data = cur.fetchall()
    cur.close()
    return render_template('Est1pre.html', contacts1p = data)

@app.route('/Est2pre.html')
def est2pre():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts2p')
    data = cur.fetchall()
    cur.close()
    return render_template('Est2pre.html', contacts2p = data)

@app.route('/Est3pre.html')
def est3pre():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts3p')
    data = cur.fetchall()
    cur.close()
    return render_template('Est3pre.html', contacts3p = data)

@app.route('/Est1tem.html')
def est1tem():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts1t')
    data = cur.fetchall()
    cur.close()
    return render_template('Est1tem.html', contacts1t = data)

@app.route('/Est2tem.html')
def est2tem():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts2t')
    data = cur.fetchall()
    cur.close()
    return render_template('Est2tem.html', contacts2t = data)

@app.route('/Est3tem.html')
def est3tem():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts3t')
    data = cur.fetchall()
    cur.close()
    return render_template('Est3tem.html', contacts3t = data)



if __name__ == '__main__':
    app.run(debug=True)
    

