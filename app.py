import streamlit as st
import google.generativeai as genai

# Configuration
# ติดตั้ง API Key ที่ได้รับมาเรียบร้อยครับ
API_KEY = "AIzaSyCUCnMrVu7-qboB6p-qLvue9R2LT2G6TD0"
genai.configure(api_key=API_KEY)

# Initializing Gemini Model
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="พัด AI Assistant", page_icon="🤖")

st.title("🤖 พัด AI Assistant")
st.caption("ฉลาดขึ้น จริงใจขึ้น พร้อมช่วยคุณเสมอครับ")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("มีอะไรให้พัดช่วย บอกมาได้เลย!", key="pad_main_input"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        with st.spinner("พัดกำลังประมวลผลคำตอบ..."):
            try:
                # Get response from Gemini
                response = model.generate_content(prompt)
                full_response = response.text
                message_placeholder.markdown(full_response)
            except Exception as e:
                full_response = f"ขออภัยครับเพื่อนรัก พัดขัดข้องนิดหน่อย: {str(e)}"
                message_placeholder.error(full_response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
  
