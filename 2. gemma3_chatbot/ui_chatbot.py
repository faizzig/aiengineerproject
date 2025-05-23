import streamlit as st
import requests

#Fungsi untuk mengirim prompt ke Ollama
def send_to_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "gemma3:1b",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json().get("response", "Tidak ada respons dari AI.")
    except Exception as e:
        return f"Terjadi error: {e}"

#Konfigurasi halaman
st.set_page_config(page_title="Chat Gemma", layout="centered")
st.title("Chat dengan AI Gemma 3B")

#Inisialisasi riwayat percakapan
if "messages" not in st.session_state:
    st.session_state.messages = []

#Menampilkan seluruh chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ketik pertanyaan Anda..."):                               #Input chat berada di posisi bawah layar
    st.session_state.messages.append({"role": "user", "content": prompt})             #Menyimpan riwayat chat user
    with st.chat_message("user"):                                                     #Tampilkan pesan user
        st.markdown(prompt)

    response = send_to_ollama(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})      #Menyimpan riwayat chat balasan AI
    with st.chat_message("assistant"):                                                #Tampilkan pesan balasan AI
        st.markdown(response)
