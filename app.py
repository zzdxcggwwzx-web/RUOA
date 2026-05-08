import google.generativeai as genai
import streamlit as st

# 1. ตั้งค่า API Key (ตรวจสอบให้แน่ใจว่า Key ยังใช้งานได้)
genai.configure(api_key="ใส่_API_KEY_ของคุณที่นี่")

# 2. แก้จุดนี้: ใช้ชื่อ Model ให้ถูกต้องตามที่ระบบต้องการ
# บางครั้งต้องใช้ 'gemini-1.5-flash-latest' หรือแค่ 'gemini-1.5-flash'
model = genai.GenerativeModel('gemini-1.5-flash')

# ส่วนของ UI Streamlit
st.title("🤖 AI ผู้ช่วยส่วนตัว")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("มีอะไรให้พัดช่วย บอกมาได้เลย!"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        # 3. เรียกใช้งานการสร้างเนื้อหา
        response = model.generate_content(prompt)
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"เกิดข้อผิดพลาด: {e}")
      
# ส่วนที่เรียกใช้ AI
if prompt := st.chat_input("มีอะไรให้พัดช่วย บอกมาได้เลย!"):
    # 1. แสดงข้อความที่เราพิมพ์
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. ให้ AI คิดคำตอบ
    response = model.generate_content(prompt)

    # 3. จุดสำคัญ! ต้องสั่งให้มัน "แสดงคำตอบ" ออกมาด้วย
    with st.chat_message("assistant"):
        st.markdown(response.text)  # <--- บรรทัดนี้ต้องมีครับ!
