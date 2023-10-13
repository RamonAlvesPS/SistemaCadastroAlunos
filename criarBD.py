#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importações
#import os
import sqlite3
#from datetime import datetime, timedelta, date

# Conectando ao BD
try:
    con = sqlite3.connect('cadastro_alunos.db')
    print('Conexao com banco de dados realizado com sucesso!!')
except sqlite3.Error as e:
    print("Erro ao conectar com o Banco de Dados!!", e)

cursor = con.cursor()

# Criando tabela de cursos
try:
    with con:
        cursor = con.cursor()
        cursor.execute(""" CREATE TABLE IF NOT EXISTS cursos(
                       id INTEGER PRIMARY KEY AUTOINCREMENT, 
                       nome TEXT,
                       duracao TEXT
        )""")
        print("Tabela 'cursos' criada com sucesso!")
except sqlite3.Error as e:
    print("Erro ao criar a tabela 'cursos':", e)

# Criando tabela de turmas
try:
    with con:
        cursor = con.cursor()
        cursor.execute(""" CREATE TABLE IF NOT EXISTS turmas(
                       id INTEGER PRIMARY KEY AUTOINCREMENT, 
                       nome TEXT,
                       curso_nome TEXT,
                       data_inicio DATE,
                       FOREIGN KEY (curso_nome) REFERENCES cursos (nome) ON UPDATE CASCADE ON DELETE CASCADE
        )""")
        print("Tabela 'turmas' criada com sucesso!")
except sqlite3.Error as e:
    print("Erro ao criar a tabela 'turmas':", e)

# Criando tabela de alunos
try:
    with con:
        cursor = con.cursor()
        cursor.execute(""" CREATE TABLE IF NOT EXISTS alunos(
                       id INTEGER PRIMARY KEY AUTOINCREMENT, 
                       nome TEXT,
                       email TEXT,
                       telefone TEXT,
                       sexo TEXT,
                       imagem TEXT,
                       data_nascimento DATE,
                       cpf TEXT,
                       turma_nome TEXT,
                       FOREIGN KEY (turma_nome) REFERENCES turmas (nome) ON DELETE CASCADE
        )""")
        print("Tabela 'alunos' criada com sucesso!")
except sqlite3.Error as e:
    print("Erro ao criar a tabela 'alunos':", e)

# Criando tabela de alunos
try:
    with con:
        cursor = con.cursor()
        cursor.execute(""" CREATE TABLE IF NOT EXISTS professores(
                       id INTEGER PRIMARY KEY AUTOINCREMENT, 
                       nome TEXT,
                       email TEXT,
                       telefone TEXT,
                       sexo TEXT,
                       imagem TEXT,
                       data_nascimento DATE,
                       cpf TEXT,
                       turma_nome TEXT,
                       FOREIGN KEY (turma_nome) REFERENCES turmas (nome) ON DELETE CASCADE
        )""")
        print("Tabela 'professores' criada com sucesso!")
except sqlite3.Error as e:
    print("Erro ao criar a tabela 'professores':", e)