from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

op = os.getenv("OPENAI_API_KEY")

template_mensagem = ChatPromptTemplate.from_messages([
    ("system", """Você é um assistente que ajuda a registrar novos usuários. 
    Colete as seguintes informações:
    1. Número de telefone (obrigatório e válido no formato internacional, exemplo: +5511999999999).
    2. Tipo de usuário (opções: professor, personal trainer, atendente, aluno).

    Se o usuário não fornecer informações completas ou válidas, peça gentilmente que ele forneça. 
    Não prossiga até que todas as informações estejam corretas.
    Resuma os dados ao final da interação no formato JSON, apenas json."""),
    ("user", "{texto}"),
])

modelo = ChatOpenAI(model="gpt-4o")
parser = StrOutputParser()
chain = template_mensagem | modelo | parser
