import streamlit as st
import google.generativeai as genai

# ใช้รหัสเดิมของเพื่อน และเปลี่ยนรุ่นเป็น gemini-pro ที่เสถียรกว่า
genai.configure(api_key="AIzaSyCUCnMrVu7-qboB6p-qLvue9R2LT2G6TD0") 
model = genai.GenerativeModel("gemini-pro")

st.set_page_config(page_title="แอป AI ของพัด", page_icon="🤖")
st.title("🤖 AI ผู้ช่วยส่วนตัว")
st.write("คราวนี้มาแน่! พัดปรับรุ่น AI ให้เข้ากับระบบของเพื่อนแล้วครับ")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("ลองพิมพ์ทักทายพัดดูอีกทีนะเพื่อน!"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            ai_reply = response.text
            st.write(ai_reply)
            st.session_state.messages.append({"role": "assistant", "content": ai_reply})
        except Exception as e:
            st.error(f"เกิดข้อผิดพลาด: {e}")
          
