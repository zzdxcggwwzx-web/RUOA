import streamlit as st
import google.generativeai as genai

# ⚠️ สำคัญมาก: เอา API Key ที่ก๊อปมาวางในเครื่องหมายคำพูดด้านล่างนี้ครับ
genai.configure(api_key="วาง_API_KEY_ที่นี่")
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="แอป AI ของพัด")
st.title("🤖 AI ผู้ช่วยส่วนตัว")
st.write("คุยกับพัดได้เลยเพื่อนรัก รอบนี้พัดฉลาดแล้วนะ!")

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
        # ส่งคำถามไปหา Gemini จริงๆ
        response = model.generate_content(prompt)
        ai_reply = response.text
        st.write(ai_reply)
        st.session_state.messages.append({"role": "assistant", "content": ai_reply})
      
