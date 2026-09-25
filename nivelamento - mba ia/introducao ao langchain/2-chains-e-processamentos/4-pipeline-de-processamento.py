from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

template_translate = PromptTemplate(
    input_variables=["initial_text"],
    template="Translate the following text to English: {initial_text}"
)

template_summarize = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following text in 4 words: {text}"
)

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

translate = template_translate | llm | StrOutputParser()
pipeline = {"text": translate} | template_summarize | llm | StrOutputParser()

result = pipeline.invoke({"initial_text": "LangChain é um framework para desenvolvimento de aplicações de IA"})

print(result)