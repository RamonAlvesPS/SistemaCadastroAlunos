#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importações
import sqlite3

# ========== Conectando ao BD ==========
try:
    con = sqlite3.connect('cadastro_alunos.db')
    print('Conexao com banco de dados realizado com sucesso!!')
except sqlite3.Error as e:
    print("Erro ao conectar com o Banco de Dados!!", e)


# ========== Tabela de cursos ==========
# Inserindo Cursos
def criar_curso(i):
    try:
        with con:
            cursor = con.cursor()
            query = "INSERT INTO cursos (nome, duracao) VALUES (?,?)"

            cursor.execute(query, i)
        print("Curso criado com sucesso!")
    except sqlite3.Error as e:
        print("Erro ao criar o Curso:", e)
#criar_cursos(['ADS', '3 anos'])

# Consultar Cursos
def consultar_cursos():
    lista = []
    try:
        with con:
            cursor = con.cursor()
            query = "SELECT * FROM cursos"
            cursor.execute(query)
            linha = cursor.fetchall()

            for i in linha :
                lista.append(i)

        print("Consulta a tabela Cursos realizada com sucesso!")
        return lista
    except sqlite3.Error as e:
        print("Erro ao consultar a tabela Cursos:", e)
#print(consultar_cursos())

# Atualizar Curso
def atualizar_curso(i):
    try:
        with con:
            cursor = con.cursor()
            query = "UPDATE cursos SET nome=?, duracao=? WHERE id=?"
            cursor.execute(query, i)
        print("Curso atualizado com sucesso!")
    except sqlite3.Error as e:
        print("Erro ao atualizar o Curso:", e)
#atualizar_curso(['ADS', '3 anos', 1])

# Deletar Curso
def deletar_curso(i):
    try:
        with con:
            cursor = con.cursor()
            query = "DELETE FROM cursos WHERE id=?"
            cursor.execute(query, i)
        print("Curso deletado com sucesso!")
    except sqlite3.Error as e:
        print("Erro ao deletar o Curso:", e)
#deletar_curso([1])

# ========== Tabela de Turmas ==========
# Inserindo Cursos
def criar_turma(i):
    try:
        with con:
            cursor = con.cursor()
            query = "INSERT INTO turmas (nome, curso_nome, data_inicio) VALUES (?,?,?)"

            cursor.execute(query, i)
        print("Turma criada com sucesso!")
    except sqlite3.Error as e:
        print("Erro ao criar a Turma:", e)
#criar_turma([])

# Consultar Turmas
def consultar_turmas():
    lista = []
    try:
        with con:
            cursor = con.cursor()
            query = "SELECT * FROM turmas"
            cursor.execute(query)
            linha = cursor.fetchall()

            for i in linha :
                lista.append(i)

        print("Consulta a tabela Turmas realizada com sucesso!")
        return lista
    except sqlite3.Error as e:
        print("Erro ao consultar a tabela Turmas:", e)
#print(consultar_turmas())

# Atualizar Turma
def atualizar_turma(i):
    try:
        with con:
            cursor = con.cursor()
            query = "UPDATE turmas SET nome=?, curso_nome=?, data_inicio=? WHERE id=?"
            cursor.execute(query, i)
        print("Turma atualizada com sucesso!")
    except sqlite3.Error as e:
        print("Erro ao atualizar a Turma:", e)
#atualizar_turma([])

# Deletar Turma
def deletar_turma(i):
    try:
        with con:
            cursor = con.cursor()
            query = "DELETE FROM turmas WHERE id=?"
            cursor.execute(query, i)
        print("Turma deletada com sucesso!")
    except sqlite3.Error as e:
        print("Erro ao deletar o Turma:", e)
#deletar_turma([])

# ========== Tabela de Alunos ==========
# Inserindo Alunos
def criar_aluno(i):
    try:
        with con:
            cursor = con.cursor()
            query = "INSERT INTO alunos (nome, email, telefone, sexo, imagem, data_nascimento, cpf, turma_nome) VALUES (?,?,?,?,?,?,?,?)"
            cursor.execute(query, i)

        print("Aluno criado com sucesso!")
    except sqlite3.Error as e:
        print("Erro ao criar a Aluno:", e)
#criar_aluno([])

# Consultar Alunos
def consultar_alunos():
    lista = []
    try:
        with con:
            cursor = con.cursor()
            query = "SELECT * FROM alunos"
            cursor.execute(query)
            linha = cursor.fetchall()

            for i in linha :
                lista.append(i)

        print("Consulta a tabela Alunos realizada com sucesso!")
        return lista
    except sqlite3.Error as e:
        print("Erro ao consultar a tabela Alunos:", e)
#print(consultar_alunos())

# Atualizar Alunos
def atualizar_aluno(i):
    try:
        with con:
            cursor = con.cursor()
            query = "UPDATE alunos SET nome=?, email=?, telefone=?, sexo=?, imagem=?, data_nascimento=?, cpf=?, turma_nome=? WHERE id=?"
            cursor.execute(query, i)
        print("Aluno atualizado com sucesso!")
    except sqlite3.Error as e:
        print("Erro ao atualizar a Aluno:", e)
#atualizar_aluno([])

# Deletar Aluno
def deletar_aluno(i):
    try:
        with con:
            cursor = con.cursor()
            query = "DELETE FROM alunos WHERE id=?"
            cursor.execute(query, i)
        print("Aluno deletado com sucesso!")
    except sqlite3.Error as e:
        print("Erro ao deletar o Aluno:", e)
#deletar_aluno([])

