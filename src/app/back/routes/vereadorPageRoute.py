from flask import Blueprint, render_template, request, url_for, redirect
import mysql.connector
from config import Config, datacfg
import os
import json

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
    

    sql_proposicoes = 'select * from tb_proposicoes where vere_id = %s'
    cur = con.cursor()
    cur.execute(sql_proposicoes,(id,))
    proposicoes = cur.fetchall()

        
    sql = 'SELECT * FROM tb_frequencia_plenario where vere_id = %s'
    con = mysql.connector.connect(**datacfg)
    cur = con.cursor()
    cur.execute(sql,(id,))
    presenca = cur.fetchall()

    print(f"Total de registros retornados: {len(presenca)}")

    presenca_list = [{'freq_id': row[0], 'freq_situacao': row[1], 'freq_ano': row[2],'freq_quantidade': row[3], 'vere_id': row[4]} for row in presenca]
    folder_path = 'front\static\scripts'
    file_path = os.path.join(folder_path, 'presenca.json')

    with open(file_path, 'w') as json_file:
        json.dump(presenca_list, json_file,indent = 4)

    con.close()
    if vereador:
        return render_template('informationPage.html', vereador=vereador, comentarios=comentarios,  proposicoes = proposicoes)
    else:
        return "Vereador não encontrado!", 404
    
@vereadorPage.route('/compPage/<int:id>',  methods=['GET','POST'])
def comparationPage(id):
    
    #Primeiro vereador
    sql_principal = 'SELECT vere_nome, vere_id, vere_foto FROM tb_vereador WHERE vere_id = %s'
    con = mysql.connector.connect(**datacfg)
    cur = con.cursor()
    cur.execute(sql_principal, (id,))
    vereador1 = cur.fetchone()
    
    #Busca todos os vereadores
    sql = 'SELECT vere_nome, vere_id, vere_foto FROM db_vereadores.tb_vereador'
    con = mysql.connector.connect(**datacfg)
    cur = con.cursor()
    cur.execute(sql)
    vereadores = cur.fetchall()
    
    # Processa a seleção do vereador secundário
    vereador2 = None
    if request.method == 'POST':
        vereador2_id = request.form.get('vereador2')
        sql_secundario = 'SELECT vere_nome, vere_id, vere_foto FROM tb_vereador WHERE vere_id = %s'
        cur.execute(sql_secundario, (vereador2_id,))
        vereador2 = cur.fetchone()
    
    con.close()
    
    return render_template(
        'comparationPage.html',
        vereador1=vereador1,
        vereador2=vereador2,
        vereadores=vereadores
    )


