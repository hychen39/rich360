# Task1---導入模組
import streamlit as st

# from random_response import generate_ai_response
from core import run_llm  #回答core定義的函式

# Task2---初始化對話紀錄,創建一個空的聊天紀錄
if "messages" not in st.session_state:
    st.session_state.messages = []

# Task3---設定頁面標題
st.set_page_config(page_title="記帳機器人", layout="centered")
st.title("記帳機器人 💰🤖")

# Task4---CSS設定背景白底、字體黑色
st.markdown(
    """
    <style>
    body {
        background-color: #ffffff !important;
        color: #000000 !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# CSS
st.markdown(
    """
<style>
    .stChatMessage:has([data-testid="stChatMessageAvatarAssistant"]) {
        flex-direction: row-reverse;
        text-align: right;
    }
</style>
""",
    unsafe_allow_html=True,
)


# Task5---顯示聊天紀錄：用 st.chat_message() 決定左右分邊
# st.session_state.messages()是Streamlit API允許對話期間儲存資料
# assistant助理預設→左側,則user→右側
# st.chat_message(角色)是Streamlit API用來顯示訊息內容
for msg in st.session_state.messages:
    role = "assistant" if msg["role"] == "bot" else "user"
    with st.chat_message(role):
        st.write(msg["content"])

# Task6---User輸入並更新對話紀錄
# st.text_input()是API用來顯示文字輸入框
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("請輸入你的記帳內容（例如：'今天吃了拉麵 120 元'）", "")
    submitted = st.form_submit_button("送出")
    if submitted and user_input:
        # 使用者訊息：加到對話紀錄API
        st.session_state.messages.append({"role": "user", "content": user_input})
        # 呼叫core.py給出回覆
        response = run_llm(user_input)
        # response = generate_ai_response()
        # 機器人助理加進對話紀錄
        st.session_state.messages.append({"role": "bot", "content": response})
        st.rerun()
