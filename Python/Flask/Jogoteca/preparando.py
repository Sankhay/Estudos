import mysql.connector
from mysql.connector import errorcode

print('Conectando')
try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='4093'
    )
except mysql.connecot.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Existe algo errado no nome de usuário ou senha')
    else:
        print(err)

cursor = conn.cursor()

cursor.execute("drop database if exists `jogoteca`;")

cursor.execute("create database `jogoteca`;")

cursor.execute("use `jogoteca`;")

tables = {}
tables['jogos'] = ('''
    create table `jogos` (
    `id` int(11) not null auto_increment,
    `nome` varchar(50) not null,
    `categoria` varchar(40) not null,
    `console` varchar(20) not null,
    primary key (`id`)
    ) engine=InnoDB default charset=utf8 collate=utf8_bin;
''')

tables['usuarios'] = ('''
    create table `usuarios` (
    `nome` varchar(20) not null,
    `nickname` varchar(8) not null,
    `senha` varchar(100) not null,
    primary key (`nickname`)
    ) engine = InnoDB default charset=utf8 collate=utf8_bin;
''')
print('ola')

for tabela_nome in tables:
    tabela_sql = tables[tabela_nome]
    try:
        print('Criando tabela {}:'.format(tabela_nome), end=' ')
        cursor.execute(tabela_sql)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print('ja existe')
        else:
            print(err.msg)
    else:
        print('OK')
    
usuario_sql = 'insert into usuarios (nome, nickname, senha) values (%s, %s, %s)'
usuarios = [
    ('Bruno Divino', 'BD', 'alohomora'),
    ('Camila Ferreira', 'Mila', 'paozinho'),
    ('Guilherme Louro', 'Cake', 'python_eh_vida'),
]

cursor.executemany(usuario_sql, usuarios)

cursor.execute('select * from jogoteca.usuarios')
print('------------- Usuários: -----------')
for user in cursor.fetchall():
    print(user[1])

jogos_sql = 'insert into jogos (nome, categoria, console) values (%s, %s, %s)'
jogos = [
    ('Tetris', 'Puzzle', 'Atari'),
    ('God of War', 'Hack n Slash', 'PS2'),
    ('Mortal Kombat', 'Luta', 'PS2'),
    ('Valorant', 'FPS', 'PC'),
    ('Crash Bandicoot', 'Hack n Slash', 'PS2'),
    ('Need for Speed', 'Corrida', 'PS2'),
]

cursor.executemany(jogos_sql, jogos)

cursor.execute('select * from jogoteca.jogos')
print(' ------------ Jogos: -----------')
for jogo in cursor.fetchall():
    print(jogo[1])