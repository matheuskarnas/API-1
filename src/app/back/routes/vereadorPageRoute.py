from flask import Blueprint, render_template, request, url_for, redirect
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

@vereadorPage.route('/detalhes/<int:id>', methods=['GET', 'POST'])
def detalhes_vereador(id):
    sql = 'SELECT * FROM tb_vereador WHERE vere_id = %s'
    con = mysql.connector.connect(**datacfg)
    cur = con.cursor()
    cur.execute(sql, (id,))
    vereador = cur.fetchone()

    sql_comentarios = 'SELECT * from tb_comentario WHERE vere_id = %s'
    cur.execute(sql_comentarios,(id,))
    comentarios = cur.fetchall()

    if request.method == 'POST':
        come_usuario = request.form ['come_usuario']
        come_texto = request.form ['come_texto']
        come_avaliacao = request.form ['come_avaliacao']

        if not come_avaliacao:
            return "Avaliação não fornecida", 400

        sql_comentarios = 'INSERT INTO tb_comentario (vere_id, come_usuario, come_texto, come_avaliacao) VALUES (%s, %s, %s, %s)'
        cur.execute(sql_comentarios, (id, come_usuario, come_texto, come_avaliacao))
        con.commit()

        return redirect(url_for('vereador.detalhes_vereador', id=id))

    con.close()
    if vereador:
        return render_template('informationPage.html', vereador=vereador, comentarios=comentarios)
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


