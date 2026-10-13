# titulo
# campo de mensagem (input)
# quando o usuario enviar uma mensagem
    # mostrar a mensagem na conversa
    # mandar a mensagem pra IA responder
    # mostrar a reposta
# Elementos do sistema 
    # Titulo
    # Campo de mensagem/input
    # Funcionamento - 1 = Exiba a mensagem - 2 = Envie para a IA - 3 = Mostre a resposta da IA

# streamlit e openai
# streamlit run codigo.py
from openai import OpenAI
import streamlit as st 
modelo_ia = OpenAI(
    api_key=("SEGREDO"),  
    base_url=r"https://generativelanguage.googleapis.com/v1beta/openai/"
    ) # key e url da IA
    
    

# A cada nova mensagem o sistema roda tudo denovo loop

st.title(" ChatBot com IA") # titulo

if not "lista_mensagens" in st.session_state: # if = se not = não tiver lista de mensagem no armazenamento da sessão do usuario = st.session_state
    st.session_state["lista_mensagens"] = [] # Cria uma nova lista, se tiver, mantém

texto_usuario = st.chat_input("Digite sua mensagem ") # campo de mensagem (input)

for mensagem in st.session_state["lista_mensagens"]: # para cada mensagem em armazenamento de lista_mensagens
    role = mensagem["role"] # se a mensagem for do usuario = "user" se for da IA = "assistant"
    content = mensagem["content"] # se a mensagem for do usuario = mensagem_usuario se for da IA = mensagem_IA
    st.chat_message(role).write(content) # escreve cada mensagem na lista_mensagens do usuario e da IA na tela

if texto_usuario: # se houver texto digitado
    print(texto_usuario) # o conteudo sera exibido
    st.chat_message("user").write(texto_usuario) # st.chat_message = mensagem de chat + .write(texto_usuario) = texto que o cliente digitou, ou seja, historico de mensagens
    #"user" icone de pessoa "Name" primeira letra do nome "assistant" icone de robô
    mensagem_usuario = {"role": "user", "content": texto_usuario} # as IAs recebem mensagens nesse formato role: "user" e content: "" , ou seja, coloca "user" e a mensagem do usuario nesse formato
    st.session_state["lista_mensagens"].append(mensagem_usuario) # adiciona a mensagem_usuario a lista de mensagem ou armazenamento de mensagens
    
    resposta_ia = modelo_ia.chat.completions.create( # o codigo envia todo o historico de mensagens
        messages=st.session_state["lista_mensagens"], # lista de mensagens do chat, para que a IA responda com base no contexto
        model="gemini-flash-lite-latest"
     ) # modelo da openai
   
    
    texto_resposta_ia = resposta_ia.choices[0].message.content # extrai a resposta_ia sem dataframe tokens e etc.

    # resposta_ia = "Você perguntou: " + texto_usuario # simulação de resposta da IA
    
    st.chat_message("assistant").write(texto_resposta_ia) # em todas as perguntas apenas ira repetir a mensagem
    mensagem_IA = {"role": "assistant", "content": texto_resposta_ia} # mesma coisa la de cima , a IA devolve a resposta desse formato
    st.session_state["lista_mensagens"].append(mensagem_IA) # adicionar mensagem_IA na lista de mensagens ou armazenamento 
    
print(st.session_state["lista_mensagens"])
    

    
    
    
    
    
    
