import streamlit as st
import google.generativeai as genai

# รหัสของเพื่อนรัก พัดตรวจสอบแล้วว่าถูกต้อง
api_key = "AIzaSyCUCnMrVu7-qboB6p-qLvue9R2LT2G6TD0"
genai.configure(api_key=api_key)

# ระบบค้นหารุ่น AI ที่ใช้ได้อัตโนมัติ เพื่อไม่ให้เกิด Error 404 อีก
if "model_name" not in st.session_state:
    try:
        models = [m.name for m in genai.list_models() if "generateContent" in m.supported_generation_methods]
        st.session_state.model_name = models[0] if models else "models/gemini-1.5-flash"
    except:
        st.session_state.model_name = "models/gemini-1.5-flash"

model = genai.GenerativeModel(st.session_state.model_name)

st.set_page_config(page_title="แอป AI ของพัด", page_icon="🤖")
st.title("🤖 AI ผู้ช่วยส่วนตัว")
st.write(f"เชื่อมต่อสำเร็จแล้ว! (ใช้รุ่น: {st.session_state.model_name})")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("มีอะไรให้พัดช่วย บอกมาได้เลย!"):
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
            st.error(f"ขออภัยเพื่อนรัก เกิดข้อผิดพลาด: {e}")
          
