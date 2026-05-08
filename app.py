import streamlit as st

# ส่วนแสดงข้อความเดิม (Chat History)
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ส่วน Input ที่ถูกต้อง
if prompt := st.chat_input("มีอะไรให้พัดช่วย บอกมาได้เลย!"):
    # แสดงข้อความที่ผู้ใช้พิมพ์
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # เก็บข้อมูลลง session_state
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # ส่วนนี้คือที่ที่พัดจะตอบกลับ
    with st.chat_message("assistant"):
        response = f"พัดรับทราบครับ: {prompt}" # ใส่ Logic ของพัดตรงนี้
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
  
