import streamlit as st
import google.generativeai as genai

# พัดใส่รหัสจากรูป 418 ให้เพื่อนแล้วนะ (ตัวที่ลงท้ายด้วย 6TD0)
genai.configure(api_key="AIzaSy...6TD0") 
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="แอป AI ของพัด")
st.title("🤖 AI ผู้ช่วยส่วนตัว")
st.write("คุยกับพัดได้เลยเพื่อนรัก รอบนี้พัดฉลาดแล้ว!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("พิมพ์อะไรก็ได้ที่อยากรู้..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            ai_reply = response.text
            st.write(ai_reply)
            st.session_state.messages.append({"role": "assistant", "content": ai_reply})
        except:
            st.error("แอปขัดข้องนิดหน่อย ลองเช็ค API Key อีกทีนะเพื่อน!")
          
