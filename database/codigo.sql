create database if not exists db_vereador;
-- drop database db_vereador;
use db_vereador;

create table if not exists tb_vereador
( 
vere_id int not null primary key auto_increment,
vere_nome varchar(30) not null,
vere_img_url varchar(150) unique,
vere_partido varchar(30) not null,
vere_reelegendo int default 1 not null,
vere_email varchar (100), 
vere_telefone char(11)
);

create table if not exists tb_histo_poli
(
id_histo_poli int not null auto_increment primary key,
hist_cargo varchar(80) not null,
hist_inicio_manda date not null,
hist_fim_manda date not null,
vere_id int,
foreign key (vere_id) references tb_vereador(vere_id)
);

create table if not exists tb_comentario
(
come_id int not null auto_increment primary key,
come_usuario varchar(60),
come_data datetime default current_timestamp,
come_texto longtext,
vere_id int, 
foreign key (vere_id) references tb_vereador(vere_id)
);

create table if not exists tb_comissao
(
comi_id int not null auto_increment primary key,
comi_cargo varchar(30) not null,
comi_nome varchar(40) not null,
comi_tipo varchar(12) not null,
vere_id int
);

create table if not exists tb_preposicoes
(
prep_id int not null auto_increment primary key,
prep_tema varchar(10) not null,
prep_data date,
prep_projetos varchar(45) not null
);

create table if not exists tb_chaves_estra
(
estr_id int not null auto_increment primary key,
vere_id int,
comi_id int,
prep_id int,
foreign key (comi_id) references tb_comissao(comi_id),
foreign key (vere_id) references tb_vereador(vere_id),
foreign key (prep_id) references tb_preposicoes(prep_id)
);

select*from tb_comissao;
select*from tb_preposicoes;
select* from tb_histo_poli;
show tables;

select * from tb_vereador;
select * from tb_comentario;


