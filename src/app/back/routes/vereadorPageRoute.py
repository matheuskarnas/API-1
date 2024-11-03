from flask import Blueprint, render_template
import mysql.connector
from config import Config, datacfg
import os

vereadorPage = Blueprint('vereador', __name__)

@vereadorPage.route('/')  
def listar_vereadores():
    sql = 'SELECT * FROM tb_vereador order by vere_nome asc'
    con = mysql.connector.connect(**datacfg)
    cur = con.cursor()
    cur.execute(sql)
    vereadores = cur.fetchall() 
    print(vereadores)
    con.close()  
    return render_template('index.html', vereadores=vereadores)

@vereadorPage.route('/detalhes/<int:id>')
def detalhes_vereador(id):
    sql = 'SELECT * FROM tb_vereador WHERE vere_id = %s'
    con = mysql.connector.connect(**datacfg)
    cur = con.cursor()
    cur.execute(sql, (id,))
    vereador = cur.fetchone()
    con.close()
    if vereador:
        return render_template('informationPage.html', vereador=vereador)
    else:
        return "Vereador não encontrado!", 404
    
@vereadorPage.route('/compPage')
def comparationPage():
    # sql = 'SELECT * FROM tb_vereador WHERE vere_id = %s'
    # con = mysql.connector.connect(**datacfg)
    # cur = con.cursor()
    # cur.execute(sql, (id,))
    # vereador = cur.fetchone()
    # con.close()
    return render_template('comparationPage.html')


