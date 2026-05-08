import streamlit as st

st.set_page_config(page_title="แอป AI ของฉัน", layout="centered")
st.title("🤖 แอป AI ของฉัน")
st.write("แอปนี้รันบนโลกออนไลน์ 24 ชั่วโมงแล้วนะเพื่อน!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("ลองพิมพ์คุยกับ AI ดูสิ"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    response = f"AI: ได้รับข้อความ '{prompt}' แล้ว! ยินดีด้วยที่คุณสร้างแอปสำเร็จ"
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)
