from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from datetime import datetime
import os

# 載入.env的API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# 初始化LLM
llm = ChatOpenAI(api_key=api_key, temperature=0, model_name="gpt-3.5-turbo")

# 取得今天日期格式：2024.4.10）
today = datetime.now().strftime("%Y.%m.%d")

# 記帳格式化 prompt，將「今天」替換成實際日期
prompt = PromptTemplate.from_template(
    f"今天是 {today}，請幫我從這句話中分析記帳資料，並將「今天」替換成實際日期。\
輸出格式為三行純文字：\n時間：xxx\n類別：xxx\n金額：xxx\n\n句子：{{question}}\n\n輸出："
)

# 建立簡單的處理鏈
simple_chain = prompt | llm | StrOutputParser()

# 主函式：輸入一句話 → 回傳分析結果
def run_llm(user_prompt: str) -> str:
    return simple_chain.invoke({"question": user_prompt})
