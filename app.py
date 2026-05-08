import streamlit as st
import google.generativeai as genai

# 1. ตั้งค่า API Key ของคุณ
genai.configure(api_key="ใส่_API_KEY_ของคุณตรงนี้")
model = genai.GenerativeModel('gemini-pro')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("มีอะไรให้พัดช่วย บอกมาได้เลย!"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2. ส่วนที่ทำให้พัดตอบฉลาดขึ้น (เรียก AI จริงๆ มาตอบ)
    with st.chat_message("assistant"):
        with st.spinner("พัดกำลังคิดแป๊บนึงนะ..."):
            try:
                # ส่งข้อความไปให้ AI ประมวลผล
                response = model.generate_content(prompt)
                full_response = response.text
                st.markdown(full_response)
            except Exception as e:
                full_response = "ขออภัยครับ พัดเกิดข้อผิดพลาดนิดหน่อย ลองใหม่อีกทีนะ"
                st.error(str(e))
        
    st.session_state.messages.append({"role": "assistant", "content": full_response})
  
