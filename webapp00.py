# MEU PRIMEIRO WEB APP
import streamlit as st
from ACTlib01 import *
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT0U488MF4q5_1rWyEXTZ1OE3t_ACIylHTirxkI3-7usaYpu4KGjpnh4e7kIEjtahEJLKg8xrSQNhSx/pub?output=csv"
db = Ler_GooglePlanilha(url)    
Escrever(db)
Configurar_Pagina("Exemplo 1", 
                    "amplo", 
                    "auto", 
                    "https://docs.streamlit.io", 
                    "mailto:informacoes.actsp@gmail.com", 
                    "ACT - Soluções para Pessoas. Você pode usar formatação Markdown para adicionar informações neste espaço. Para mais informações acesse *https://www.markdownguide.org*",
                    "©️")

# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("MEU 1º WEB APP STREAMLIT")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("PANDAS")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("NOTÍCIAS PYTON ")

# Use st.write("") para adicionar um texto ao seu Web app
st.write("Como já deve ter percebido, o método st.write() é usado para escrita de texto e informações gerais!")
Divisor()
    
coluna1 = Colunas(3)
with coluna1[0]:
  Escrever("")
with coluna1[1]:
  Escrever("ACTlib Versão 0.1", "titulo")
  nome = Ler(rotulo = "Nome:", nmax=30, tipo="padrao", info="Inserção de Nome", autocompletar=None, na_mudanca=None, args=None, kwargs=None, placeholder="Não esqueça de preencher seu nome", desabilitada="falso", visibilidade="visivel")
  if nome:     
    Escrever("Seja Bem vinda(o), " + nome + "!")
with coluna1[2]:
  Escrever("")
