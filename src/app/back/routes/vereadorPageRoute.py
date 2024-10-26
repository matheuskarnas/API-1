from flask import Blueprint, render_template
import mysql.connector
from config import Config
import os

vereadorPage = Blueprint('vereador', __name__)

my = {
    'user': Config.DBUSER,
    'password': Config.DBPASS,
    'host': Config.DBHOST,
    'database': Config.DBNAME  
}

@vereadorPage.route('/')  
def listar_vereadores():
    sql = 'SELECT * FROM tb_vereador'
    con = mysql.connector.connect(**my)
    cur = con.cursor()
    cur.execute(sql)
    vereadores = cur.fetchall() 
    print(vereadores)
    con.close()  
    return render_template('index.html', vereadores=vereadores)  
