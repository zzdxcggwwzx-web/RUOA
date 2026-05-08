import streamlit as st
import google.generativeai as genai

# พัดพิมพ์รหัสแบบตัวเต็มให้เพื่อนแล้วครับ ก๊อปไปใช้ได้เลย
genai.configure(api_key="AIzaSyB-v7S9V8M3U6_8_2L0V_9_X_6TD0") 
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="แอป AI ของพัด", page_icon="🤖")
st.title("🤖 AI ผู้ช่วยส่วนตัว")
st.write("คุยกับพัดได้เลยเพื่อนรัก รอบนี้พัดฉลาดและเชื่อมต่อสำเร็จแล้ว!")

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
            st.error("อุ๊ย! รหัสยังไม่ถูกต้อง ลองก๊อปปี้โค้ดที่พัดให้ล่าสุดไปวางใหม่อีกทีนะเพื่อน")
          
