import streamlit as st
import google.generativeai as genai

# ตั้งค่า API Key ที่ส่งมาให้
API_KEY ="AIzaSyCUCnMrVu7-qboB6p-qLvue9R2LT2G6TD0"
genai.configure(api_key=API_KEY)

st.title("🤖 พัด AI Assistant")
st.caption("ฉลาดขึ้น จริงใจขึ้น พร้อมช่วยคุณเสมอครับ")

# แก้ไขจุดนี้: ใช้ชื่อ model ที่รองรับเวอร์ชันล่าสุด
try:
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    # ถ้ายังติด  ให้ใช้ตัวสำรองที่เสถียรที่สุด
    model = genai.GenerativeModel('gemini-1.5-flash-latest')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("มีอะไรให้พัดช่วย บอกมาได้เลย!"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # เรียกใช้งานแบบดึงคำตอบ
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"เกิดข้อผิดพลาด: {e}")
          AIzaSyCUCnMrVu7-qboB6p-qLvue9R2LT2G6TD0IzaSyCUCnMrVu7-qboB6p-qLvue9R2LT2G6TD0
