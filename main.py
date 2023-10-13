#!/usr/bin/env python
# -*- coding: utf-8 -*-

# importando dependencias do Tkinter
from tkinter.ttk import *
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

# tk calendar
from tkcalendar import Calendar, DateEntry
from datetime import date

# importando pillow
from PIL import ImageTk, Image

#importando View
from view import *

#importando o screeninfo # para saber o tamanho da tela
from screeninfo import get_monitors

# Obtém as dimensões do monitor principal
monitor = get_monitors()[0]

# Calcula as coordenadas para o centro da tela
largura_janela = 850  # Largura da sua janela
altura_janela = 620   # Altura da sua janela
pos_x = (monitor.width - largura_janela) // 2
pos_y = (monitor.height - altura_janela) // 2


# cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # azul
co7 = "#ef5350"   # vermelha

co6 = "#038cfc"   # azul
co8 = "#263238"   # + preta
co9 = "#e9edf5"   # + grey

co10 = "#1b1464"   # azul escuro
co11 = "#0ff2c5"   # + verde
co12 = "#eb008c"   # pink

# Criando janela
janela = Tk()
janela.title("")
# Define a posição da janela
janela.geometry(f'{largura_janela}x{altura_janela}+{pos_x}+{pos_y}')
janela.configure(background=co1)
#janela.configure(background=co10)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

# Criando Frames
frame_logo = Frame(janela, width=850, height=52, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

frame_dados = Frame(janela, width=850, height=65, bg=co1)
#frame_dados = Frame(janela, width=850, height=65, bg=co10)
frame_dados.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

frame_detalhes = Frame(janela, width=850, height=200, bg=co1)
#frame_detalhes = Frame(janela, width=850, height=200, bg=co10)
frame_detalhes.grid(row=4, column=0, pady=0, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=850, height=200, bg=co1)
#frame_tabela = Frame(janela, width=850, height=200, bg=co10)
frame_tabela.grid(row=5, column=0, pady=0, padx=10, sticky=NSEW)

# ========== Frame Logo =========
app_lg = Image.open('education_icon.png')
app_lg = app_lg.resize((50, 50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text="Cadastro de Alunos", width=850, compound=LEFT, relief=RAISED, anchor=NW, font=('Ivy 15 bold'), bg=co6, fg=co1)
app_logo.place(x=0, y=0)

# ========== Função para cadastrar alunos ==========
def alunos():
    #funcão novo aluno
    def new_aluno():
        global imagem, imagem_string, l_imagem
        
        nome = e_nome.get()
        email = e_email.get()
        telefone = e_tell.get()
        sexo = c_sexo.get()
        imagem = imagem_string
        data = d_nascimento.get()
        cpf = e_cpf.get()
        turma = c_turma.get()

        lista = [nome, email, telefone, sexo, imagem, data, cpf, turma]

        for i in lista:
            if i == "":
                messagebox.showerror('Erro', 'Preencha todos os campos!')
                return
        
        criar_aluno(lista)

        e_nome.delete(0,END)
        e_email.delete(0,END)
        e_tell.delete(0,END)
        c_sexo.delete(0,END)
        #imagem_string.delete(0,END)
        d_nascimento.delete(0,END)
        e_cpf.delete(0,END)
        c_turma.delete(0,END)

        mostrar_alunos()
    
    #funcão atualizar aluno
    def update_aluno():
        global imagem, imagem_string, l_imagem
        try:
            tree_itens = tree_aluno.focus()
            tree_dicionario = tree_aluno.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            e_nome.insert(0,tree_lista[1])
            e_email.insert(0,tree_lista[2])
            e_tell.insert(0,tree_lista[3])
            c_sexo.insert(0,tree_lista[4])
            imagem = tree_lista[5]
            d_nascimento.delete(0,END)
            d_nascimento.insert(0,tree_lista[6])
            e_cpf.insert(0,tree_lista[7])
            c_turma.insert(0,tree_lista[8])

            #Abrindo a imagem
            imagem_string = imagem
            imagem = Image.open(imagem)
            imagem = imagem.resize((130, 135))
            imagem = ImageTk.PhotoImage(imagem)
            l_imagem = Label(frame_detalhes, image=imagem, bg=co1, fg=co4)
            l_imagem.place(x=294, y=10)

            def update():
                nome = e_nome.get()
                email = e_email.get()
                telefone = e_tell.get()
                sexo = c_sexo.get()
                imagem = imagem_string
                data = d_nascimento.get()
                cpf = e_cpf.get()
                turma = c_turma.get()

                lista = [nome, email, telefone, sexo, imagem, data, cpf, turma, valor_id]

                for i in lista:
                    if i == "":
                        messagebox.showerror('Erro', 'Preencha todos os campos!')
                        return
                
                atualizar_aluno(lista)

                e_nome.delete(0,END)
                e_email.delete(0,END)
                e_tell.delete(0,END)
                c_sexo.delete(0,END)
                #imagem.delete()
                #imagem = ""
                d_nascimento.delete(0,END)
                e_cpf.delete(0,END)
                c_turma.delete(0,END)

                mostrar_alunos()

                botao_confirmar_aluno.destroy()

            botao_confirmar_aluno = Button(frame_detalhes, width=10, command=update, anchor=CENTER, text='Confirmar', overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
            botao_confirmar_aluno.place(x=727, y=130)
        except ImportError:
            messagebox.showerror('Erro', 'Selecione um dos alunos na tabela!')
    
    #funcão Deletar aluno
    def delete_aluno():
        try:
            tree_itens = tree_aluno.focus()
            tree_dicionario = tree_aluno.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            deletar_aluno([valor_id])

            mostrar_alunos()
        
        except ImportError:
            messagebox.showerror('Erro', 'Selecione um aluno na tabela!')

    #funcão pesquisar aluno
    def select_aluno():
        global imagem, imagem_string, l_imagem
        
        try:
            nome_procurado = e_nome_procurar.get()
            alunos = consultar_alunos()

            for aluno in alunos:
                if aluno[1].lower() == nome_procurado.lower():
                    e_nome.insert(0,aluno[1])
                    e_email.insert(0,aluno[2])
                    e_tell.insert(0,aluno[3])
                    c_sexo.insert(0,aluno[4])
                    imagem = aluno[5]
                    d_nascimento.delete(0,END)
                    d_nascimento.insert(0,aluno[6])
                    e_cpf.insert(0,aluno[7])
                    c_turma.insert(0,aluno[8])

                    #Abrindo a imagem
                    imagem_string = imagem
                    imagem = Image.open(imagem)
                    imagem = imagem.resize((130, 135))
                    imagem = ImageTk.PhotoImage(imagem)
                    l_imagem = Label(frame_detalhes, image=imagem, bg=co1, fg=co4)
                    l_imagem.place(x=294, y=10)

                    return
                
        except ImportError:
            messagebox.showerror('Erro', 'Aluno não encontrado!')

        mostrar_alunos()
    
    #funcão visualizar aluno
    def view_aluno():
        global imagem, imagem_string, l_imagem
        try:
            tree_itens = tree_aluno.focus()
            tree_dicionario = tree_aluno.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            e_nome.insert(0,tree_lista[1])
            e_email.insert(0,tree_lista[2])
            e_tell.insert(0,tree_lista[3])
            c_sexo.insert(0,tree_lista[4])
            imagem = tree_lista[5]
            d_nascimento.delete(0,END)
            d_nascimento.insert(0,tree_lista[6])
            e_cpf.insert(0,tree_lista[7])
            c_turma.insert(0,tree_lista[8])

            #Abrindo a imagem
            imagem_string = imagem
            imagem = Image.open(imagem)
            imagem = imagem.resize((130, 135))
            imagem = ImageTk.PhotoImage(imagem)
            l_imagem = Label(frame_detalhes, image=imagem, bg=co1, fg=co4)
            l_imagem.place(x=294, y=10)
            
        except ImportError:
            messagebox.showerror('Erro', 'Selecione um dos alunos na tabela!')

    # Criando campos de entrada
    l_nome = Label(frame_detalhes, text="Nome do Aluno *", height=1, anchor=NW, font=('Ivy 10 '), bg=co1, fg=co4)
    l_nome.place(x=3, y=10)
    e_nome = Entry(frame_detalhes, width=34, justify='left', relief='solid')
    e_nome.place(x=6, y=40)
    
    #Email
    l_email = Label(frame_detalhes, text="Email *", height=1, anchor=NW, font=('Ivy 10 '), bg=co1, fg=co4)
    l_email.place(x=3, y=70)
    e_email = Entry(frame_detalhes, width=34, justify='left', relief='solid')
    e_email.place(x=6, y=100)

    #Telefone
    l_tell = Label(frame_detalhes, text="Telefone *", height=1, anchor=NW, font=('Ivy 10 '), bg=co1, fg=co4)
    l_tell.place(x=3, y=130)
    e_tell = Entry(frame_detalhes, width=20, justify='left', relief='solid')
    e_tell.place(x=6, y=160)

    #sexo
    sexo = ['Masculino', 'Feminino', 'Outro']
    l_sexo = Label(frame_detalhes, text="Sexo *", height=1, anchor=NW, font=('Ivy 10 '), bg=co1, fg=co4)
    l_sexo.place(x=183, y=130)
    c_sexo = ttk.Combobox(frame_detalhes, width=12, font=('Ivy 8 bold'))
    c_sexo['values'] = (sexo)
    c_sexo.place(x=183, y=160)

    #data de nascimento
    l_nascimento = Label(frame_detalhes, text="Data de Nascimento *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_nascimento.place(x=443, y=10)
    d_nascimento = DateEntry(frame_detalhes, width=16, backgroud='darkblue', foreground='white', bordewidth=2, year=2023)
    d_nascimento.place(x=446, y=40)

    #CPF
    l_cpf = Label(frame_detalhes, text="CPF *", height=1, anchor=NW, font=('Ivy 10 '), bg=co1, fg=co4)
    l_cpf.place(x=446, y=70)
    e_cpf = Entry(frame_detalhes, width=18, justify='left', relief='solid')
    e_cpf.place(x=449, y=100)

    #pegando os cursos
    turmas = consultar_turmas()
    turma = []
    for i in turmas:
        turma.append(i[1])

    l_turma = Label(frame_detalhes, text="Turma *", height=1, anchor=NW, font=('Ivy 10 '), bg=co1, fg=co4)
    l_turma.place(x=446, y=130)
    c_turma = ttk.Combobox(frame_detalhes, width=18, font=('Ivy 8 bold'))
    c_turma['values'] = (turma)
    c_turma.place(x=450, y=160)

    #funcao para escolher imagem
    global imagem, imagem_string, l_imagem
    def escolher_imagem():
        global imagem, imagem_string, l_imagem

        imagem = fd.askopenfilename()
        imagem_string = imagem

        #Abrindo a imagem
        imagem = Image.open(imagem)
        imagem = imagem.resize((130, 135))
        imagem = ImageTk.PhotoImage(imagem)
        l_imagem = Label(frame_detalhes, image=imagem, bg=co1, fg=co4)
        l_imagem.place(x=294, y=10)

        botao_carregar['text'] = 'Trocar de Foto'

    #Botão Escolher carregar imagem
    botao_carregar = Button(frame_detalhes, command=escolher_imagem, text=" Carregar Foto".upper(), width=20, anchor=CENTER, compound=CENTER, overrelief=RIDGE, font=('Ivy 7'), bg=co1, fg=co0)
    botao_carregar.place(x=290, y=155)

    # Linha separatória
    l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
    l_linha.place(x=610, y=10)
    l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
    l_linha.place(x=608, y=10)

    #Procurar Aluno
    l_nome = Label(frame_detalhes, text="Procurar Aluno", height=1, anchor=NW, font=('Ivy 10 '), bg=co1, fg=co4)
    l_nome.place(x=617, y=10)
    e_nome_procurar = Entry(frame_detalhes, width=16, justify='left', relief='solid')
    e_nome_procurar.place(x=620, y=35)

    botao_procurar = Button(frame_detalhes, anchor=CENTER, command=select_aluno, text='Procurar', width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
    botao_procurar.place(x=757, y=35)

    #Botões
    botao_salvar = Button(frame_detalhes, anchor=CENTER, command=new_aluno, text='Salvar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
    botao_salvar.place(x=627, y=100)

    botao_atualizar = Button(frame_detalhes, anchor=CENTER, command=update_aluno, text='Atualizar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co6, fg=co1)
    botao_atualizar.place(x=627, y=130)

    botao_deletar = Button(frame_detalhes, anchor=CENTER, command=delete_aluno, text='Deletar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1)
    botao_deletar.place(x=627, y=160)

    botao_ver = Button(frame_detalhes, anchor=CENTER, command=view_aluno, text='Ver'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
    botao_ver.place(x=727, y=160)

    # Tabela Alunos
    def mostrar_alunos():
        app_nome = Label(frame_tabela, text="Tabela de estudantes", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        # creating a treeview with dual scrollbars
        list_header = ['id','Nome','email',  'Telefone','sexo', 'imagem', 'Data', 'CPF','Curso']

        df_list = consultar_alunos()

        global tree_aluno

        tree_aluno = ttk.Treeview(frame_tabela, selectmode="extended",columns=list_header, show="headings")

        # vertical scrollbar
        vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_aluno.yview)
        # horizontal scrollbar
        hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_aluno.xview)

        tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_aluno.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tabela.grid_rowconfigure(0, weight=12)

        hd=["nw","nw","nw","center","center","center","center","center","center"]
        h=[30,150,150,70,70,70,90,80,100]
        n=0

        for col in list_header:
            tree_aluno.heading(col, text=col.title(), anchor=NW)
            # adjust the column's width to the header string
            tree_aluno.column(col, width=h[n],anchor=hd[n])

            n+=1

        for item in df_list:
            tree_aluno.insert('', 'end', values=item)

    mostrar_alunos()

# =========== Função para adicionar cursos e turmas ==========
def adicionar():
    # Criando frames para tabelas
    frame_tabela_curso = Frame(frame_tabela, width=300, height=200, bg=co1)
    frame_tabela_curso.grid(row=0, column=0, pady=0, padx=10, sticky=NSEW)

    frame_tabela_linha = Frame(frame_tabela, width=30, height=200, bg=co1)
    frame_tabela_linha.grid(row=0, column=1, pady=0, padx=10, sticky=NSEW)

    frame_tabela_turma = Frame(frame_tabela, width=300, height=200, bg=co1)
    frame_tabela_turma.grid(row=0, column=2, pady=0, padx=10, sticky=NSEW)

    botao_carregar = Button(frame_detalhes, anchor=CENTER, text='Salvar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
    botao_carregar.place(x=7, y=160)

    botao_atualizar = Button(frame_detalhes, anchor=CENTER, text='Atualizar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co6, fg=co1)
    botao_atualizar.place(x=87, y=160)

    botao_deletar = Button(frame_detalhes, anchor=CENTER, text='Deletar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1)
    botao_deletar.place(x=167, y=160)

    # Detalhes do Curso

    #funcão novo curso
    def new_curso():
        nome = e_nomecurso.get()
        duracao = e_duracao.get()

        lista = [nome, duracao]

        for i in lista:
            if i == "":
                messagebox.showerror('Erro', 'Preencha todos os campos!')
                return
        criar_curso(lista)
 
        e_nomecurso.delete(0, END)
        e_duracao.delete(0, END)

        mostrar_cursos()
    
    #funcão atualizar curso
    def update_curso():
        try:
            tree_itens = tree_curso.focus()
            tree_dicionario = tree_curso.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]
        
            e_nomecurso.insert(0,tree_lista[1])
            e_duracao.insert(0, tree_lista[2])

            def update():
                nome = e_nomecurso.get()
                duracao = e_duracao.get()

                lista = [nome, duracao, valor_id]

                for i in lista:
                    if i == "":
                        messagebox.showerror('Erro', 'Preencha todos os campos!')
                        return
                atualizar_curso(lista)

                e_nomecurso.delete(0, END)
                e_duracao.delete(0, END)

                mostrar_cursos()

                botao_confirmar.destroy()

            botao_confirmar = Button(frame_detalhes, command=update, anchor=CENTER, text='Confirmar Atualização', overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
            botao_confirmar.place(x=227, y=130)
        except ImportError:
            messagebox.showerror('Erro', 'Selecione um dos cursos na tabela!')
    
    #funcão Deletar curso
    def delete_curso():
        try:
            tree_itens = tree_curso.focus()
            tree_dicionario = tree_curso.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            deletar_curso([valor_id])

            mostrar_cursos()
        
        except ImportError:
            messagebox.showerror('Erro', 'Selecione um dos cursos na tabela!')

    l_nomecurso = Label(frame_detalhes, text="Nome do curso", height=1, anchor=NW, font=('Ivy 10 '), bg=co1, fg=co4)
    l_nomecurso.place(x=4, y=10)
    e_nomecurso = Entry(frame_detalhes, width=35, justify='left', relief='solid')
    e_nomecurso.place(x=7, y=40)

    l_duracao = Label(frame_detalhes, text="Duração *", height=1, anchor=NW, font=('Ivy 10 '), bg=co1, fg=co4)
    l_duracao.place(x=4, y=70)
    e_duracao = Entry(frame_detalhes, width=20, justify='left', relief='solid')
    e_duracao.place(x=7, y=100)

    botao_carregar = Button(frame_detalhes, command=new_curso, anchor=CENTER, text='Salvar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
    botao_carregar.place(x=7, y=160)

    botao_atualizar = Button(frame_detalhes, command=update_curso, anchor=CENTER, text='Atualizar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co6, fg=co1)
    botao_atualizar.place(x=87, y=160)

    botao_deletar = Button(frame_detalhes, command=delete_curso, anchor=CENTER, text='Deletar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1)
    botao_deletar.place(x=167, y=160)

    # Tabela Cursos
    def mostrar_cursos():
        app_nome = Label(frame_tabela_curso, text="Tabela de Cursos", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        # creating a treeview with dual scrollbars
        list_header = [' ID ',' Curso ',' Duração ']

        df_list = consultar_cursos()

        global tree_curso

        tree_curso = ttk.Treeview(frame_tabela_curso, selectmode="extended",columns=list_header, show="headings")

        # vertical scrollbar
        vsb = ttk.Scrollbar(frame_tabela_curso, orient="vertical", command=tree_curso.yview)
        # horizontal scrollbar
        hsb = ttk.Scrollbar(frame_tabela_curso, orient="horizontal", command=tree_curso.xview)

        tree_curso.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_curso.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tabela_curso.grid_rowconfigure(0, weight=12)

        hd=["nw","nw","e"]
        #hd=["nw","nw","e","e"]
        #h=[30,150,80,60]
        h=[50,170,100]
        n=0

        for col in list_header:
            tree_curso.heading(col, text=col.title(), anchor=NW)
            # adjust the column's width to the header string
            tree_curso.column(col, width=h[n],anchor=hd[n])
            n+=1

        for item in df_list:
            tree_curso.insert('', 'end', values=item)

    mostrar_cursos()

    # Linha separatória
    l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
    l_linha.place(x=374, y=10)
    l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
    l_linha.place(x=372, y=10)

    # Linha separatória da tabelas
    l_linha = Label(frame_tabela_linha, relief=GROOVE, text='h', width=1, height=140, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
    l_linha.place(x=6, y=10)
    l_linha = Label(frame_tabela_linha, relief=GROOVE, text='h', width=1, height=140, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
    l_linha.place(x=4, y=10)

    # Detalhes da Turma
    #funcão novo curso
    def new_turma():
        nome = e_nometurma.get()
        curso = c_curso.get()
        data = e_data_inicio.get()

        lista = [nome, curso, data]

        for i in lista:
            if i == "":
                messagebox.showerror('Erro', 'Preencha todos os campos!')
                return
        
        criar_turma(lista)
 
        e_nometurma.delete(0, END)
        c_curso.delete(0, END)
        e_data_inicio.delete(0,END)

        mostrar_turmas()
    
    #funcão atualizar curso
    def update_turma():
        try:
            tree_itens = tree_turma.focus()
            tree_dicionario = tree_turma.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]
        
            e_nometurma.insert(0,tree_lista[1])
            c_curso.insert(0, tree_lista[2])
            e_data_inicio.insert(0, tree_lista[3])

            def update():
                nome = e_nometurma.get()
                curso = c_curso.get()
                data_inicio = e_data_inicio.get()

                lista = [nome, curso, data_inicio, valor_id]

                for i in lista:
                    if i == "":
                        messagebox.showerror('Erro', 'Preencha todos os campos!')
                        return
                    
                atualizar_turma(lista)

                e_nometurma.delete(0, END)
                c_curso.delete(0, END)
                e_data_inicio.delete(0,END)

                mostrar_turmas()

                botao_confirmar.destroy()

            botao_confirmar = Button(frame_detalhes, command=update, anchor=CENTER, text='Confirmar Atualização', overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
            botao_confirmar.place(x=407, y=130)
        except ImportError:
            messagebox.showerror('Erro', 'Selecione uma das turmas na tabela!')
    
    #funcão Deletar curso
    def delete_turma():
        try:
            tree_itens = tree_turma.focus()
            tree_dicionario = tree_turma.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            deletar_turma([valor_id])

            mostrar_turmas()
        
        except ImportError:
            messagebox.showerror('Erro', 'Selecione uma das turmas na tabela!')

    l_nometurma = Label(frame_detalhes, text="Nome da Turma", height=1, anchor=NW, font=('Ivy 10 '), bg=co1, fg=co4)
    l_nometurma.place(x=404, y=10)
    e_nometurma = Entry(frame_detalhes, width=35, justify='left', relief='solid')
    e_nometurma.place(x=407, y=40)

    l_Curso = Label(frame_detalhes, text="Curso *", height=1, anchor=NW, font=('Ivy 10 '), bg=co1, fg=co4)
    l_Curso.place(x=404, y=70)
    #pegando os cursos
    cursos = consultar_cursos()
    curso = []
    for i in cursos:
        curso.append(i[1])
    c_curso = ttk.Combobox(frame_detalhes, width=20, font=('Ivy 8 bold'))
    c_curso['values'] = (curso)
    c_curso.place(x=404, y=100)

    l_datainicio = Label(frame_detalhes, text="Data de Inicio *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_datainicio.place(x=406, y=130)
    e_data_inicio = DateEntry(frame_detalhes, width=10, backgroud='darkblue', foreground='white', bordewidth=2, year=2023)
    e_data_inicio.place(x=407, y=160)

    botao_carregar = Button(frame_detalhes, command=new_turma, anchor=CENTER, text='Salvar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
    botao_carregar.place(x=510, y=160)

    botao_atualizar = Button(frame_detalhes, command=update_turma, anchor=CENTER, text='Atualizar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co6, fg=co1)
    botao_atualizar.place(x=590, y=160)

    botao_deletar = Button(frame_detalhes, command=delete_turma, anchor=CENTER, text='Deletar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1)
    botao_deletar.place(x=670, y=160)

    # Tabela Turmas
    def mostrar_turmas():
        app_nome = Label(frame_tabela_turma, text="Tabela de Turmas", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        # creating a treeview with dual scrollbars
        list_header = [' ID ',' Nome da Turma ',' Curso ', ' Inicio ']

        df_list = consultar_turmas()

        global tree_turma

        tree_turma = ttk.Treeview(frame_tabela_turma, selectmode="extended",columns=list_header, show="headings")

        # vertical scrollbar
        vsb = ttk.Scrollbar(frame_tabela_turma, orient="vertical", command=tree_turma.yview)
        # horizontal scrollbar
        hsb = ttk.Scrollbar(frame_tabela_turma, orient="horizontal", command=tree_turma.xview)

        tree_turma.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_turma.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tabela_turma.grid_rowconfigure(0, weight=12)

        hd=["nw","nw","e","e"]
        h=[30,130,150,80]
        n=0

        for col in list_header:
            tree_turma.heading(col, text=col.title(), anchor=NW)
            # adjust the column's width to the header string
            tree_turma.column(col, width=h[n],anchor=hd[n])
            n+=1

        for item in df_list:
            tree_turma.insert('', 'end', values=item)

    mostrar_turmas()

# =========== Função para salvar ==========
def salvar():
    print("Salvo!")

# ========== Função de controle ==========
def controle(i):
    if i == "Cadastrar":
        for widget in frame_detalhes.winfo_children():
            widget.destroy()
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        alunos() # Chamando a função alunos

    if i == "Adicionar":
        for widget in frame_detalhes.winfo_children():
            widget.destroy()
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        adicionar() # Chamando a função alunos

    if i == "Salvar":
        for widget in frame_detalhes.winfo_children():
            widget.destroy()
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        salvar() # Chamando a função alunos

# ========== Funções para botões ==========
# Função para realçar o botão quando o mouse passa sobre ele
def mouse_enter(event):
    app_cadastro.config(relief=SUNKEN)  # Mude para o efeito de realce desejado, como SUNKEN

# Função para remover o realce quando o mouse sai do botão
def mouse_leave(event):
    app_cadastro.config(relief=RAISED)  # Volte ao relevo original, como RAISED

# ========== Criando Botões ==========
#Botão CADASTRO
app_img_cadastro = Image.open('cad.png')
app_img_cadastro = app_img_cadastro.resize((18, 18))
app_img_cadastro = ImageTk.PhotoImage(app_img_cadastro)
app_cadastro = Button(frame_dados, command=lambda:controle('Cadastrar'), image=app_img_cadastro, text=" Cadastrar", width=100, compound=LEFT, relief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_cadastro.place(x=10, y=20)
app_cadastro.bind("<Enter>", app_cadastro.config(relief=SUNKEN))
app_cadastro.bind("<Leave>", app_cadastro.config(relief=RAISED))

#Botão ADICIONAR
app_img_adicionar = Image.open('add.png')
app_img_adicionar = app_img_adicionar.resize((18, 18))
app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)
app_adicionar = Button(frame_dados, command=lambda:controle('Adicionar'), image=app_img_adicionar, text=" Adicionar", width=100, compound=LEFT, relief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_adicionar.place(x=123, y=20)
app_adicionar.bind("<Enter>", app_adicionar.config(relief=SUNKEN))
app_adicionar.bind("<Leave>", app_adicionar.config(relief=RAISED))

#Botão SALVAR
app_img_salvar = Image.open('save.png')
app_img_salvar = app_img_salvar.resize((18, 18))
app_img_salvar = ImageTk.PhotoImage(app_img_salvar)
app_salvar = Button(frame_dados, command=lambda:controle('Salvar'), image=app_img_salvar, text=" Salvar", width=100, compound=LEFT, relief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_salvar.place(x=236, y=20)
app_salvar.bind("<Enter>", app_salvar.config(relief=SUNKEN))
app_salvar.bind("<Leave>", app_salvar.config(relief=RAISED))

alunos()

# Executando a janela
janela.mainloop()