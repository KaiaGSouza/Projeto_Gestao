import customtkinter
from tkinter import ttk
import customtkinter as ctk
import sqlite3


# VETORES
vetor_P=[]
vetor_Q=[]


# def
# CRIAR BANCO DE DADOS
def criar_banco_dados():
    conexao = sqlite3.connect("produtos.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute("CREATE TABLE IF NOT EXISTS produtos(nome text, "
                         "quantidade interger, "
                         "preco REAL, "
                         "desc text)")
    conexao.commit()
    conexao.close()


# SALVAR INFORMAÇÕES CADASTRAR
def salvar_dados():
    conexao = sqlite3.connect("produtos.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute("insert into produtos (nome, preco, desc) values(?, ?, ?)", (nome_entry.get(),
                                                                                      preco_entry.get(),
                                                                                      descricao_entry.get("1.0", "end"))
                         )
    conexao.commit()
    conexao.close()
    nome_entry.delete(0, "end")
    preco_entry.delete(0, "end")
    descricao_entry.delete("1.0", "end")


# LER DADOS TABELA
def ler_dados():
    conexao = sqlite3.connect("produtos.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute("SELECT * FROM produtos")
    recebe_dados = terminal_sql.fetchall()

    for objetos in tabela_relatorio_estoque.get_children():
        tabela_relatorio_estoque.delete(objetos)
    for objetos in tabela_saida_estoque.get_children():
        tabela_saida_estoque.delete(objetos)
    for objetos in tabela_entrada_estoque.get_children():
        tabela_entrada_estoque.delete(objetos)

    for i in recebe_dados:
        nome_entry = str(i[0])
        qtd = str(i[1])
        preco_entry = str(i[2])
        descricao_entry = str(i[3])
        tabela_relatorio_estoque.insert("", "end", values=(nome_entry, qtd, preco_entry, descricao_entry))


# CADASTRAR PRODUTOS
def cadastrar_produtos():
    # Fechar Frames
    frame_editar.grid_forget()
    frame_saida.grid_forget()
    frame_entrada.grid_forget()
    frame_relatorio_estoque.grid_forget()
    frame_relatorio_saida.grid_forget()
    frame_relatorio_entrada.grid_forget()
    frame_tela_inicial.grid_forget()

    # Cor Botão
    button_cadastrar.configure(fg_color="#E6AD4E")
    button_editar.configure(fg_color="red")
    button_saida.configure(fg_color="red")
    button_entrada.configure(fg_color="red")
    button_relatorio.configure(fg_color="red")

    # Abertura Frame
    frame_cadastrar.grid(row=0, column=1, padx=5, pady=10)
    frame_cadastrar.grid_propagate(False)


# EDITAR PRODUTOS
def editar_produtos():
    # Fechar Frames
    frame_cadastrar.grid_forget()
    frame_entrada.grid_forget()
    frame_saida.grid_forget()
    frame_relatorio_estoque.grid_forget()
    frame_relatorio_saida.grid_forget()
    frame_relatorio_entrada.grid_forget()
    frame_tela_inicial.grid_forget()

    # Cor Botão
    button_cadastrar.configure(fg_color="red")
    button_editar.configure(fg_color="#E6AD4E")
    button_saida.configure(fg_color="red")
    button_entrada.configure(fg_color="red")
    button_relatorio.configure(fg_color="red")

    frame_editar.grid(row=0, column=1, padx=5, pady=10)
    frame_editar.grid_propagate(False)
    lista_produtos_telas()


# APAGAR PRODUTOS DE EDITAR
def apagar_produtos():
    editar_nome.delete(0, "end")
    editar_preco.delete(0, "end")
    alterar_descricao.delete("1.0", "end")


# EXCLUIR PRODUTOS EDIÇÃO
def deletar_produtos(nome_produto):
    conexao = sqlite3.connect("produtos.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute(f"DELETE FROM produtos WHERE nome = '{nome_produto}'")
    conexao.commit()
    conexao.close()
    editar_nome.delete(0, "end")
    editar_preco.delete(0, "end")
    alterar_descricao.delete(0.0, "end")
    lista_produtos_telas()


# SALVAR EDIÇÃO
def salvar_edicao_produtos(nome_produto, preco_produto, descricao_produto):
    conexao = sqlite3.connect("produtos.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute(f"UPDATE produtos SET nome = '{nome_produto}', preco = '{preco_produto}', "
                         f"desc = '{descricao_produto}' WHERE nome = '{valor_checkbox_nome}'")
    conexao.commit()
    conexao.close()
    editar_nome.delete(0, "end")
    editar_preco.delete(0, "end")
    alterar_descricao.delete(0.0, "end")
    lista_produtos_telas()


# SAIDA DE PRODUTOS
def saida_produtos():
    frame_cadastrar.grid_forget()
    frame_entrada.grid_forget()
    frame_editar.grid_forget()
    frame_relatorio_estoque.grid_forget()
    frame_relatorio_saida.grid_forget()
    frame_relatorio_entrada.grid_forget()
    frame_tela_inicial.grid_forget()

    button_cadastrar.configure(fg_color="red")
    button_editar.configure(fg_color="red")
    button_saida.configure(fg_color="#E6AD4E")
    button_entrada.configure(fg_color="red")
    button_relatorio.configure(fg_color="red")

    frame_saida.grid(row=0, column=1, padx=5, pady=10)
    frame_saida.grid_propagate(False)
    lista_produtos_telas()


# PRODUTOS SELECIONADOS NA TABELA SAIDA E ENTRADA
def lista_selecionados(nome_entry):
    global valor_checkbox_Saida
    valor_checkbox_Saida = nome_entry.get().strip("(),'\"")


def botao_lista_selecionados():
    checkbox_selecionada= ctk.CTkLabel(produtos_selecionado, text=f"{valor_checkbox_Saida:<20} {qtd_retirar_itens.get()}", font=("Courier", 14))
    checkbox_selecionada.pack(pady=3, padx=3, anchor="w")
    vetor_P.append(valor_checkbox_Saida)
    vetor_Q.append(qtd_retirar_itens.get())
    print(vetor_P, vetor_Q)


# ENTRADA DE PRODUTOS
def entrada_produtos():
    frame_cadastrar.grid_forget()
    frame_editar.grid_forget()
    frame_saida.grid_forget()
    frame_relatorio_estoque.grid_forget()
    frame_relatorio_saida.grid_forget()
    frame_relatorio_entrada.grid_forget()
    frame_tela_inicial.grid_forget()

    button_cadastrar.configure(fg_color="red")
    button_editar.configure(fg_color="red")
    button_saida.configure(fg_color="red")
    button_entrada.configure(fg_color="#E6AD4E")
    button_relatorio.configure(fg_color="red")

    frame_entrada.grid(row=0, column=1, padx=5, pady=10)
    frame_entrada.grid_propagate(False)
    lista_produtos_telas()


# TABELA RELATORIO DE ESTOQUE DE PRODUTOS
def relatorio_estoque_produtos():
    frame_cadastrar.grid_forget()
    frame_entrada.grid_forget()
    frame_saida.grid_forget()
    frame_editar.grid_forget()
    frame_tela_inicial.grid_forget()
    frame_relatorio_saida.grid_forget()
    frame_relatorio_entrada.grid_forget()

    button_cadastrar.configure(fg_color="red")
    button_editar.configure(fg_color="red")
    button_saida.configure(fg_color="red")
    button_entrada.configure(fg_color="red")
    button_relatorio.configure(fg_color="#E6AD4E")

    frame_relatorio_estoque.grid(row=0, column=1, padx=5, pady=10)
    frame_relatorio_estoque.grid_propagate(False)
    ler_dados()


# TABELA RELATORIO DE SAiDA DE PRODUTOS
def relatorio_saida_produtos():
    frame_cadastrar.grid_forget()
    frame_entrada.grid_forget()
    frame_saida.grid_forget()
    frame_editar.grid_forget()
    frame_tela_inicial.grid_forget()
    frame_relatorio_estoque.grid_forget()
    frame_relatorio_entrada.grid_forget()

    frame_relatorio_saida.grid(row=0, column=1, padx=5, pady=10)
    frame_relatorio_saida.grid_propagate(False)
    ler_dados()


# TABELA RELATORIO DE ENTRADA DE PRODUTOS
def relatorio_entrada_produtos():
    frame_cadastrar.grid_forget()
    frame_entrada.grid_forget()
    frame_saida.grid_forget()
    frame_editar.grid_forget()
    frame_tela_inicial.grid_forget()
    frame_relatorio_estoque.grid_forget()
    frame_relatorio_saida.grid_forget()

    frame_relatorio_entrada.grid(row=0, column=1, padx=5, pady=10)
    frame_relatorio_entrada.grid_propagate(False)
    ler_dados()


# JANELA EXPORTAR DAS TABELAS DE ESTOQUE, SAIDA E ENTRADA
def miniwindow_exportar():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    mwindow = ctk.CTk()
    mwindow.geometry("400x200")
    mwindow.title("Exportar")

    titulo1 = ctk.CTkLabel(mwindow, text="Escolher Relatorio(s):", font=("Arial", 15, "bold"))
    titulo1.grid(row=0, column=0, pady=5, padx=5)

    relaframe = ctk.CTkFrame(mwindow, height=130, fg_color="black", border_color="red", border_width=2)
    relaframe.grid_propagate(False)
    relaframe.grid(row=1, column=0)
    # CHECK BOX 1
    box1_1 = ctk.CTkCheckBox(relaframe, text="Exportar Estoque", font=("Arial", 15), border_color="red",
                             hover_color="#E6AD4E", fg_color="red")
    box1_1.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    box2_1 = ctk.CTkCheckBox(relaframe, text="Exportar Saida", font=("Arial", 15), border_color="red",
                             hover_color="#E6AD4E", fg_color="red")
    box2_1.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    box3_1 = ctk.CTkCheckBox(relaframe, text="Exportar Entrada", font=("Arial", 15), border_color="red",
                             hover_color="#E6AD4E", fg_color="red")
    box3_1.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    # CHECK BOX 1 FIM

    titulo2 = ctk.CTkLabel(mwindow, text="Escolher Extensão:", font=("Arial", 15, "bold"))
    titulo2.grid(row=0, column=1, pady=5, padx=5)

    relaframe2 = ctk.CTkFrame(mwindow, height=130, fg_color="black", border_color="red", border_width=2)
    relaframe2.grid_propagate(False)
    relaframe2.grid(row=1, column=1)
    # CHECK BOX 2
    box1_2 = ctk.CTkCheckBox(relaframe2, text="Word", font=("Arial", 15), border_color="red", hover_color="#E6AD4E",
                             fg_color="red")
    box1_2.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    box2_2 = ctk.CTkCheckBox(relaframe2, text="PDF", font=("Arial", 15), border_color="red", hover_color="#E6AD4E",
                             fg_color="red")
    box2_2.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    box3_2 = ctk.CTkCheckBox(relaframe2, text="Excel", font=("Arial", 15), border_color="red", hover_color="#E6AD4E",
                             fg_color="red")
    box3_2.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    # CHECK BOX 2 FIM

    button_salvar = ctk.CTkButton(mwindow, text="salvar", width=80, fg_color="#E6AD4E", border_width=2,
                                  border_color="red", hover_color="red", command=mwindow.destroy)
    button_salvar.grid(row=3, column=1, sticky="e")
    button_cancelar = ctk.CTkButton(mwindow, text="cancelar", width=80, fg_color="red", border_color="#E6AD4E",
                                    border_width=2, hover_color="#E6AD4E")
    button_cancelar.grid(row=3, column=1, sticky="w")

    mwindow.mainloop()


# PRODUTOS EM CADA TABELA LISTADOS
def lista_produtos_telas():
    global produtos
    conexao = sqlite3.connect("produtos.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute("SELECT nome FROM produtos")
    receber_todos_dados = terminal_sql.fetchall()

    for i in mostrar_lista_editar.winfo_children():
        i.destroy()
    check_var = customtkinter.StringVar()
    for i in receber_todos_dados:
        nome_entry = str(i[0])
        produtos = customtkinter.CTkCheckBox(mostrar_lista_editar, text=nome_entry, onvalue=nome_entry, offvalue="",
                                             variable=check_var,
                                             command=lambda: seleciona_item(check_var) if check_var.get() else apagar_produtos())
        produtos.pack(pady=3, anchor="w")

    for i in mostrar_lista_saida.winfo_children():
        i.destroy()

    for i in receber_todos_dados:
        nome_entry = str(i[0])
        produtos = customtkinter.CTkCheckBox(mostrar_lista_saida, text=nome_entry, onvalue=nome_entry, offvalue="",
                                             variable=check_var,
                                             command=lambda: lista_selecionados(check_var) if check_var.get() else apagar_produtos())
        produtos.pack(pady=3, anchor="w")

    for i in mostrar_lista_entrada.winfo_children():
        i.destroy()
    for i in receber_todos_dados:
        nome_entry = str(i[0])
        produtos = customtkinter.CTkCheckBox(mostrar_lista_entrada, text=nome_entry, onvalue=nome_entry, offvalue="",
                                             variable=check_var,
                                             command=lambda: lista_selecionados(check_var) if check_var.get() else apagar_produtos())
        produtos.pack(pady=3, anchor="w")


# SELECIONAR PRODUTOS
def seleciona_item(nome_entry):
    global valor_checkbox_nome
    valor_checkbox_nome = nome_entry.get().strip("(),'\"{}")

    conexao = sqlite3.connect("produtos.db")
    terminal_sql_nome = conexao.cursor()
    terminal_sql_nome.execute(f"SELECT * FROM produtos WHERE nome = '{valor_checkbox_nome}'")
    receber_dados_produto = terminal_sql_nome.fetchall()
    print(valor_checkbox_nome)

    editar_nome.delete(0, "end")
    editar_nome.insert(0, receber_dados_produto[0][0])

    editar_preco.delete(0, "end")
    editar_preco.insert(0, receber_dados_produto[0][2])

    alterar_descricao.delete("1.0", "end")
    alterar_descricao.insert("1.0", receber_dados_produto[0][3])


criar_banco_dados()

# Abertura da Tela
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
window = ctk.CTk()
window.geometry("800x400")
window.title("Sistema")

# Frames Menu
frame_menu = ctk.CTkFrame(window, height=380, width=190, border_color="red", border_width=2, fg_color="black")
frame_menu.propagate(False)
frame_menu.grid(row=0, column=0, padx=5, pady=10)

# Frames Inicial
frame_tela_inicial = ctk.CTkFrame(window, height=380, width=590, border_color="red", border_width=2, fg_color="black")
frame_tela_inicial.propagate(False)
frame_tela_inicial.grid(row=0, column=1, padx=5, pady=10)

# Frames Tela
frame_cadastrar = ctk.CTkFrame(window, height=380, width=590, border_color="red", border_width=2, fg_color="black")
frame_cadastrar.grid_propagate(False)

frame_editar = ctk.CTkFrame(window, height=380, width=590, border_color="red", border_width=2, fg_color="black")
frame_editar.grid_propagate(False)

frame_saida = ctk.CTkFrame(window, height=380, width=590, border_color="red", border_width=2, fg_color="black")
frame_saida.grid_propagate(False)

frame_entrada = ctk.CTkFrame(window, height=380, width=590, border_color="red", border_width=2, fg_color="black")
frame_entrada.grid_propagate(False)

frame_relatorio_estoque = ctk.CTkFrame(window, height=380, width=590, border_color="red", border_width=2,
                                       fg_color="black")
frame_relatorio_estoque.grid_propagate(False)

frame_relatorio_saida = ctk.CTkFrame(window, height=380, width=590, border_color="red", border_width=2,
                                     fg_color="black")
frame_relatorio_saida.grid_propagate(False)

frame_relatorio_entrada = ctk.CTkFrame(window, height=380, width=590, border_color="red", border_width=2,
                                       fg_color="black")
frame_relatorio_entrada.grid_propagate(False)
# titulo
titulo = ctk.CTkLabel(frame_menu, text="Nome do\n Sistema", font=("Arial", 20, "bold"))
titulo.pack(pady=30)

# ______________________________________________Botão Cadastro__________________________________________________________
button_cadastrar = ctk.CTkButton(frame_menu, text="Cadastrar", command=cadastrar_produtos, fg_color="red",
                                 border_color="#E65349", border_width=3, hover_color="#E6AD4E")
button_cadastrar.pack()

# Funções Cadastro______________________________________________________________________________________________________
titulo_abertura = ctk.CTkLabel(frame_cadastrar, text="Cadastro Do Produto", font=("Arial", 20, "bold"))
titulo_abertura.grid(row=0, column=1, pady=20, padx=0)

# LABEL_________________________________________________________________________________________________________________

nome_produto = ctk.CTkLabel(frame_cadastrar, text=f"{'Nome do Produto:'}")
nome_produto.grid(row=1, column=0, pady=5, padx=2, sticky="e")

preco_produto = ctk.CTkLabel(frame_cadastrar, text=f"{'Preço(R$):'}")
preco_produto.grid(row=2, column=0, pady=5, padx=0, sticky="e")

descricao_produto = ctk.CTkLabel(frame_cadastrar, text=f"{'Descrição:'}")
descricao_produto.grid(row=3, column=0, pady=5, padx=0, sticky="en")

# ENTRY_________________________________________________________________________________________________________________
nome_entry = ctk.CTkEntry(frame_cadastrar, placeholder_text=f"{'Digite o nome do produto'}", width=300)
nome_entry.grid(row=1, column=1, pady=5, padx=5)

preco_entry = ctk.CTkEntry(frame_cadastrar, placeholder_text=f"{'0.00'}", width=80)
preco_entry.grid(row=2, column=1, pady=5, padx=5, sticky="w")

descricao_entry = ctk.CTkTextbox(frame_cadastrar, height=80, width=300)
descricao_entry.grid(row=3, column=1, pady=5, padx=5)

# BOTÕES________________________________________________________________________________________________________________
salvar = ctk.CTkButton(frame_cadastrar, text="Salvar!", width=80, fg_color="#E6AD4E", border_color="red",
                       border_width=2, hover_color="red", command=salvar_dados)
salvar.grid(row=4, column=1, pady=5, sticky="e")
# ______________________________________________________________________________________________________________________

# ______________________________________________Botão Editar____________________________________________________________
button_editar = ctk.CTkButton(frame_menu, text="Editar", command=editar_produtos, fg_color="red", border_color="#E65349",
                              border_width=3, hover_color="#E6AD4E")
button_editar.pack(pady=10)

# Funções Editar LABEL__________________________________________________________________________________________________
titulo_editar = ctk.CTkLabel(frame_editar, text="Editar Produto Cadastrado", font=("", 20, "bold"))
titulo_editar.grid(row=0, column=0, padx=5, pady=20, columnspan=5)

# TABElA________________________________________________________________________________________________________________
mostrar_lista_editar = ctk.CTkScrollableFrame(frame_editar, height=200, width=160)
mostrar_lista_editar.grid(row=2, column=0, pady=10, padx=20, rowspan=4, )

alterar_descricao = ctk.CTkTextbox(frame_editar, height=100, width=300)
alterar_descricao.grid(row=4, column=1, padx=5, pady=0, sticky="n", columnspan=3)

# ENTRY_________________________________________________________________________________________________________________
buscar_produto = ctk.CTkEntry(frame_editar, placeholder_text="Buscar Produto:", width=300)
buscar_produto.grid(row=1, column=0, padx=5, pady=10, columnspan=2, sticky="w")

editar_nome = ctk.CTkEntry(frame_editar, placeholder_text="Nome do Produto", width=300)
editar_nome.grid(row=2, column=1, padx=5, pady=0, sticky="n", columnspan=3)

editar_preco = ctk.CTkEntry(frame_editar, placeholder_text="0.00", width=80)
editar_preco.grid(row=3, column=1, padx=5, pady=0, sticky="wn")

# BOTÂO_________________________________________________________________________________________________________________
botao_excluir = ctk.CTkButton(frame_editar, text="Excluir", fg_color="red", border_color="#E6AD4E", border_width=2,
                              width=80, hover_color="#E6AD4E", command=lambda: deletar_produtos(editar_nome.get()))
botao_excluir.grid(row=5, column=1, padx=5, pady=0, sticky="w")

botao_cancelar = ctk.CTkButton(frame_editar, text="Cancelar", width=80, fg_color="#E6AD4E", border_color="red",
                               border_width=2, hover_color="red")
botao_cancelar.grid(row=5, column=2, padx=5, pady=0)

botao_salvar = ctk.CTkButton(frame_editar, text="Salvar", width=80, fg_color="#E6AD4E", border_color="red",
                             border_width=2, hover_color="red", command=lambda: salvar_edicao_produtos(editar_nome.get(),
                                                                                              editar_preco.get(),
                                                                                              alterar_descricao.get(0.0,
                                                                                                                    "end")))
botao_salvar.grid(row=5, column=3, padx=5, pady=0, sticky="e")

# ______________________________________________________________________________________________________________________


# ______________________________________________Botão Saida_____________________________________________________________
button_saida = ctk.CTkButton(frame_menu, text="Saida", command=saida_produtos, fg_color="red", border_color="#E65349",
                             border_width=3, hover_color="#E6AD4E")
button_saida.pack()

# Funções Saida LABEL___________________________________________________________________________________________________
titulo_saida = ctk.CTkLabel(frame_saida, text="Saida do Produto:", font=("Arial", 20, "bold"))
titulo_saida.grid(row=0, column=0, pady=5, padx=0, columnspan=4)

quantidade_produtos = ctk.CTkLabel(frame_saida, text="Quantidade em Estoque:20", font=("Arial", 15, "bold"))
quantidade_produtos.grid(row=1, column=1, pady=0, padx=0, columnspan=2)

# ENTRY_________________________________________________________________________________________________________________
pesquisar_produto = ctk.CTkEntry(frame_saida, placeholder_text="pesquisar", border_color="red")
pesquisar_produto.grid(row=2, column=0, pady=0, padx=0)

qtd_retirar_itens = ctk.CTkEntry(frame_saida, placeholder_text="Quantidade", width=90, border_color="red")
qtd_retirar_itens.grid(row=2, column=1, pady=0, padx=0)

# TABELA1_______________________________________________________________________________________________________________
mostrar_lista_saida = ctk.CTkScrollableFrame(frame_saida, fg_color="black", border_color="red", border_width=2)
mostrar_lista_saida.grid(row=3, column=0, pady=20, padx=20, rowspan=2)

produtos_selecionado = ctk.CTkScrollableFrame(frame_saida, fg_color="black", border_color="red", border_width=2)
produtos_selecionado.grid(row=3, column=1, pady=20, padx=20, columnspan=2, rowspan=2)
# TABELA2_______________________________________________________________________________________________________________

# ??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????

# BOTÂO_________________________________________________________________________________________________________________
retirar_itens = ctk.CTkButton(frame_saida, text="Adicionar Item", fg_color="#E6AD4E", border_color="red",
                              border_width=2, hover_color="red", command= botao_lista_selecionados)
retirar_itens.grid(row=2, column=2)

cancelar_alteracao = ctk.CTkButton(frame_saida, text="Cancelar", fg_color="red", width=80, border_color="#E6AD4E",
                                   border_width=2,
                                   hover_color="#E6AD4E")
cancelar_alteracao.grid(row=5, column=1)

salvar_alteracao = ctk.CTkButton(frame_saida, text="Salvar", width=80, fg_color="#E6AD4E", border_color="red",
                                 border_width=2,
                                 hover_color="red")
salvar_alteracao.grid(row=5, column=2)

# ______________________________________________Botão Entrada___________________________________________________________
button_entrada = ctk.CTkButton(frame_menu, text="Entrada", command=entrada_produtos, fg_color="red", border_color="#E65349",
                               border_width=3, hover_color="#E6AD4E")
button_entrada.pack(pady=10)

# Funções Entrada LABEL_________________________________________________________________________________________________
titulo_entrada = ctk.CTkLabel(frame_entrada, text="Entrada do Produto:", font=("Arial", 20, "bold"))
titulo_entrada.grid(row=0, column=0, pady=5, padx=0, columnspan=4)

quantidade_produtos = ctk.CTkLabel(frame_entrada, text="Quantidade em Estoque:20", font=("Arial", 15, "bold"))
quantidade_produtos.grid(row=1, column=1, pady=0, padx=0, columnspan=2)
# ENTRY_________________________________________________________________________________________________________________
pesquisar_produto = ctk.CTkEntry(frame_entrada, placeholder_text="pesquisar", border_color="red")
pesquisar_produto.grid(row=2, column=0, pady=0, padx=0)

adicionar_item = ctk.CTkEntry(frame_entrada, placeholder_text="Quantidade", width=90, border_color="red")
adicionar_item.grid(row=2, column=1, pady=0, padx=0)
# BOTÂO_________________________________________________________________________________________________________________
adicionar_itens = ctk.CTkButton(frame_entrada, text="Adicionar quantidade", fg_color="#E6AD4E", border_color="red",
                                border_width=2, hover_color="#E6AD4E")
adicionar_itens.grid(row=2, column=2)

cancelar_alteracao = ctk.CTkButton(frame_entrada, text="Cancelar", width=80, fg_color="red", border_color="#E6AD4E",
                                   border_width=2, hover_color="#E6AD4E")
cancelar_alteracao.grid(row=5, column=1)

salvar_alteracao = ctk.CTkButton(frame_entrada, text="Salvar", width=80, fg_color="#E6AD4E", border_color="red",
                                 border_width=2, hover_color="red")
salvar_alteracao.grid(row=5, column=2)

# TABELA1_______________________________________________________________________________________________________________
mostrar_lista_entrada = ctk.CTkScrollableFrame(frame_entrada, fg_color="black", border_color="red", border_width=2)
mostrar_lista_entrada.grid(row=3, column=0, pady=20, padx=20, rowspan=2)

# TABELA2_______________________________________________________________________________________________________________
produtos_selecionados = ctk.CTkScrollableFrame(frame_entrada, fg_color="black", border_color="red", border_width=2)
produtos_selecionados.grid(row=3, column=1, pady=20, padx=20, columnspan=2, rowspan=2)

# ?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????

# ______________________________________________________________________________________________________________________


# ______________________________________________Botão Relatorio_________________________________________________________
button_relatorio = ctk.CTkButton(frame_menu, text="Relatorio", command=relatorio_estoque_produtos, fg_color="red",
                                 border_color="#E65349", border_width=3, hover_color="#E6AD4E")
button_relatorio.pack()
# Funções Relatorio de Estoque LABEL ___________________________________________________________________________________

titulo_relatorio = ctk.CTkLabel(frame_relatorio_estoque, text="Relatorio Estoque", font=("Arial", 20, "bold"))
titulo_relatorio.grid(row=0, column=0, columnspan=5, pady=5)

# ENTRY ________________________________________________________________________________________________________________
barra_pesquisa = ctk.CTkEntry(frame_relatorio_estoque, placeholder_text="Barra de Pesquisa:", width=150,
                              border_color="red", border_width=2)
barra_pesquisa.grid(row=1, column=0, pady=5, padx=20)
# BOTÃO_________________________________________________________________________________________________________________
# EXPORTAR
exportar_relatorio = ctk.CTkButton(frame_relatorio_estoque, text="Exportar", width=80, fg_color="purple",
                                   border_color="purple", border_width=2, hover_color="#9E6EF0", command=miniwindow_exportar)
exportar_relatorio.grid(row=1, column=4, sticky="w")

# ESTOQUE
estoque_botao_relatorio = ctk.CTkButton(frame_relatorio_estoque, text="Estoque", width=80, fg_color="red",
                                        border_color="red",
                                        border_width=2, hover_color="red")
estoque_botao_relatorio.grid(row=3, column=2, sticky="e")

# SAIDA
saida_botao_relatorio = ctk.CTkButton(frame_relatorio_estoque, text="Saida", width=80, fg_color="red",
                                      border_color="#E6AD4E",
                                      border_width=2, hover_color="#E6AD4E", command=relatorio_saida_produtos)
saida_botao_relatorio.grid(row=3, column=3)

# ENTRADA
entrada_botao_relatorio = ctk.CTkButton(frame_relatorio_estoque, text="Entrada", width=80, fg_color="red",
                                        border_color="#E6AD4E",
                                        border_width=2, hover_color="#E6AD4E", command=relatorio_entrada_produtos)
entrada_botao_relatorio.grid(row=3, column=4, sticky="w")

# TABELA________________________________________________________________________________________________________________
frame_tabela_relatorio_estoque = ctk.CTkFrame(frame_relatorio_estoque)
frame_tabela_relatorio_estoque.grid(row=2, column=0, padx=30, pady=5, columnspan=5)

colunas_relatorio_estoque = ("Nome", "Quantidade", "Preço", "Descrição")
tabela_relatorio_estoque = ttk.Treeview(frame_tabela_relatorio_estoque, columns=colunas_relatorio_estoque,
                                        show="headings", height=10)

for coluna_relatorio_estoque in colunas_relatorio_estoque:
    tabela_relatorio_estoque.heading(coluna_relatorio_estoque, text=coluna_relatorio_estoque)

tabela_relatorio_estoque.column("Nome", width=132)
tabela_relatorio_estoque.column("Quantidade", width=132)
tabela_relatorio_estoque.column("Preço", width=132)
tabela_relatorio_estoque.column("Descrição", width=132)

estilo_relatorio_estoque = ttk.Style()
estilo_relatorio_estoque.configure("Custom.Treeview",
                                   background="#D3D3D3",
                                   foreground="black",
                                   fieldbackground="#D3D3D3",
                                   font=("Arial", 10))

estilo_relatorio_estoque.configure("Custom.Treeview.Heading",
                                   background="Blue",
                                   foreground="Black",
                                   font=("Arial", 12, "bold"))

tabela_relatorio_estoque.tag_configure("oddrow", background="#F0F0F0")
tabela_relatorio_estoque.tag_configure("evenrow", background="#FFFFFF")

tabela_relatorio_estoque.configure(style="Custom.Treeview")

tabela_relatorio_estoque.pack(pady=0)
tabela_relatorio_estoque.grid_propagate(False)
# ______________________________________________________________________________________________________________________

# Relatorio Saida_______________________________________________________________________________________________________
# Funções Saida Relatorio LABEL_________________________________________________________________________________________
titulo_relatorio_saida = ctk.CTkLabel(frame_relatorio_saida, text="Relatorio Saida", font=("Arial", 20, "bold"))
titulo_relatorio_saida.grid(row=0, column=0, columnspan=5, pady=5)
# ENTRY_________________________________________________________________________________________________________________
barra_pesquisa_Rsaida = ctk.CTkEntry(frame_relatorio_saida, placeholder_text="Barra de Pesquisa:", width=150,
                                     border_color="red",
                                     border_width=2)
barra_pesquisa_Rsaida.grid(row=1, column=0, pady=5, padx=20)
# BOTÃO_________________________________________________________________________________________________________________
exportar_relatorio_saida = ctk.CTkButton(frame_relatorio_saida, text="Exportar", width=80, fg_color="purple",
                                         border_color="purple",
                                         border_width=2, hover_color="#9E6EF0", command=miniwindow_exportar)
exportar_relatorio_saida.grid(row=1, column=4, sticky="w")

estoque_botao_relatorio = ctk.CTkButton(frame_relatorio_saida, text="Estoque", width=80, fg_color="red",
                                        border_color="#E6AD4E", border_width=2, hover_color="#E6AD4E",
                                        command=relatorio_estoque_produtos)
estoque_botao_relatorio.grid(row=3, column=2, sticky="e")

saida_botao_relatorio = ctk.CTkButton(frame_relatorio_saida, text="Saida", width=80, fg_color="red",
                                      border_color="red",
                                      border_width=2, hover_color="red")
saida_botao_relatorio.grid(row=3, column=3)

entrada_botao_relatorio = ctk.CTkButton(frame_relatorio_saida, text="Entrada", width=80, fg_color="red",
                                        border_color="#E6AD4E", border_width=2, hover_color="#E6AD4E",
                                        command=relatorio_entrada_produtos)
entrada_botao_relatorio.grid(row=3, column=4, sticky="w")

# TABELA________________________________________________________________________________________________________________
frame_tabela_saida_estoque = ctk.CTkFrame(frame_relatorio_saida)
frame_tabela_saida_estoque.grid(row=2, column=0, padx=30, pady=5, columnspan=5)

colunas_Saida_estoque = ("Nome", "Quantidade", "Preço", "Descrição")
tabela_saida_estoque = ttk.Treeview(frame_tabela_saida_estoque, columns=colunas_Saida_estoque, show="headings",
                                    height=10)

for coluna_saida_estoque in colunas_Saida_estoque:
    tabela_saida_estoque.heading(coluna_saida_estoque, text=coluna_saida_estoque)

tabela_saida_estoque.column("Nome", width=132)
tabela_saida_estoque.column("Quantidade", width=132)
tabela_saida_estoque.column("Preço", width=132)
tabela_saida_estoque.column("Descrição", width=132)

dados_saida_estoque = []

for item_saida_estoque in dados_saida_estoque:
    tabela_saida_estoque.insert("", "end", values=item_saida_estoque)

estilo_saida_estoque = ttk.Style()
estilo_saida_estoque.configure("Custom.Treeview",
                               background="#D3D3D3",
                               foreground="black",
                               fieldbackground="#D3D3D3",
                               font=("Arial", 10))

estilo_saida_estoque.configure("Custom.Treeview.Heading",
                               background="Blue",
                               foreground="Black",
                               font=("Arial", 12, "bold"))

tabela_saida_estoque.tag_configure("oddrow", background="#F0F0F0")
tabela_saida_estoque.tag_configure("evenrow", background="#FFFFFF")

tabela_saida_estoque.configure(style="Custom.Treeview")

tabela_saida_estoque.pack(pady=0)
tabela_saida_estoque.grid_propagate(False)

# ______________________________________________________________________________________________________________________

# Relatorio Entrada_____________________________________________________________________________________________________
# Funções Entrada Relatorio LABEL_______________________________________________________________________________________
titulo_relatorio_entrada = ctk.CTkLabel(frame_relatorio_entrada, text="Relatorio Entrada", font=("Arial", 20, "bold"))
titulo_relatorio_entrada.grid(row=0, column=0, columnspan=5, pady=5)
# ENTRY
pesquisa_relatorio_entrada = ctk.CTkEntry(frame_relatorio_entrada, placeholder_text="Barra de Pesquisa:", width=150,
                                          border_color="red", border_width=2)
pesquisa_relatorio_entrada.grid(row=1, column=0, pady=5, padx=20)
# BOTÃO
exportar_relatorio_entrada = ctk.CTkButton(frame_relatorio_entrada, text="Exportar", width=80, fg_color="purple",
                                           border_color="purple", border_width=2, hover_color="#9E6EF0",
                                           command=miniwindow_exportar)
exportar_relatorio_entrada.grid(row=1, column=4, sticky="w")
estoque_button = ctk.CTkButton(frame_relatorio_entrada, text="Estoque", width=80, fg_color="red",
                               border_color="#E6AD4E",
                               border_width=2, hover_color="#E6AD4E", command=relatorio_estoque_produtos)
estoque_button.grid(row=3, column=2, sticky="e")

saida_button = ctk.CTkButton(frame_relatorio_entrada, text="Saida", width=80, fg_color="red", border_color="#E6AD4E",
                             border_width=2, hover_color="#E6AD4E", command=relatorio_saida_produtos)
saida_button.grid(row=3, column=3)

entrada_button = ctk.CTkButton(frame_relatorio_entrada, text="Entrada", width=80, fg_color="red", border_color="red",
                               border_width=2, hover_color="red", )
entrada_button.grid(row=3, column=4, sticky="w")
# TABELA
frame_tabela_entrada_estoque = ctk.CTkFrame(frame_relatorio_entrada)
frame_tabela_entrada_estoque.grid(row=2, column=0, padx=30, pady=5, columnspan=5)

colunas_entrada_estoque = ("Nome", "Quantidade", "Preço", "Descrição")
tabela_entrada_estoque = ttk.Treeview(frame_tabela_entrada_estoque, columns=colunas_entrada_estoque,
                                      show="headings", height=10)

for coluna_Restoque in colunas_entrada_estoque:
    tabela_entrada_estoque.heading(coluna_Restoque, text=coluna_Restoque)

tabela_entrada_estoque.column("Nome", width=132)
tabela_entrada_estoque.column("Quantidade", width=132)
tabela_entrada_estoque.column("Preço", width=132)
tabela_entrada_estoque.column("Descrição", width=132)

dados_entrada_estoque = []

for item_entrada_estoque in dados_entrada_estoque:
    tabela_entrada_estoque.insert("", "end", values=item_entrada_estoque)

estilo_entrada_estoque = ttk.Style()
estilo_entrada_estoque.configure("Custom.Treeview",
                                 background="#D3D3D3",
                                 foreground="black",
                                 fieldbackground="#D3D3D3",
                                 font=("Arial", 10))

estilo_entrada_estoque.configure("Custom.Treeview.Heading",
                                 background="Blue",
                                 foreground="Black",
                                 font=("Arial", 12, "bold"))

tabela_entrada_estoque.tag_configure("oddrow", background="#F0F0F0")
tabela_entrada_estoque.tag_configure("evenrow", background="#FFFFFF")

tabela_entrada_estoque.configure(style="Custom.Treeview")

tabela_entrada_estoque.pack(pady=0)
tabela_entrada_estoque.grid_propagate(False)
# ______________________________________________________________________________________________________________________
window.mainloop()
