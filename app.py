import streamlit as st
import google.generativeai as genai

# พัดใส่รหัสจริงที่เพื่อนส่งมาให้แล้วครับ (ห้ามแก้บรรทัดนี้นะ)
genai.configure(api_key="AIzaSyCUCnMrVu7-qboB6p-qLvue9R2LT2G6TD0") 
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="แอป AI ของพัด", page_icon="🤖")
st.title("🤖 AI ผู้ช่วยส่วนตัว")
st.write("คุยกับพัดได้เลยเพื่อนรัก รอบนี้พัดฟื้นคืนชีพ 100% แล้ว!")

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
            st.error(f"อุ๊ย! เกิดข้อผิดพลาด: {e}")
