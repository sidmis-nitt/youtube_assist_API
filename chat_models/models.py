from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from schema.output_schema import SummarizerOutput

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.5)
Summarizer_model = llm.with_structured_output(SummarizerOutput)

quiz_model = llm

chat_model = llm