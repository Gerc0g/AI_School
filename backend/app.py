from flask import Flask, render_template, request
from langchain_openai import ChatOpenAI
import time
#from backend.aiTools import get_embeddings
import components.aiTools as ait
from components.initialisateApp import create_app
#from backend.databaseManager import init_db
import database.databaseManager as dbm
from loguru import logger # Import logger
import httpx
from flask_bootstrap import Bootstrap
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv



#1 - осздать статический чат вебформу
#2 - Обработчик запросов = Граф - основная структура вопрос- ответ системы - 3 темы
#3 - осздать память чата в течение сесии
#4 - Создать общее хранилище всех чатов при инициализации локальное, когда нажимаешь и получаешь чат с возможностью продолжить общение
#5 - Создать инструменты для обработки первой темы - RAG план обучения
#6 - сделать CI/CD на сервер
#7 - рассписать документацию по деплою и самогу проекту

load_dotenv()
app = Flask(__name__)
CORS(app)  # Разрешает CORS для всех доменов. В продакшене настройте более строго.

'''
if not os.path.exists("Log"):
    os.makedirs("Log")
logging.basicConfig(
    filename="Log/st.log",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    filemode='a'
)
настроить логирование
'''

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_PROXY = os.getenv("OPENAI_PROXY")

llm = ChatOpenAI(
    model="gpt-4o",
    api_key=OPENAI_API_KEY,
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    openai_proxy=OPENAI_PROXY
)

logger.add("Log/st.log", format="{time} {level} {message}", level="DEBUG", rotation="100 KB", compression="zip")

embending = ait.get_embeddings()



FAISS_INDEX_PATH = "database/faiss_index_educ"

database = dbm.init_db(embending, FAISS_INDEX_PATH)


'''
Пути веб сервиса
'''

'''
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('msg')

    if not user_message:
        return jsonify({'error': 'Сообщение не предоставлено'}), 400

    messages = [
        {"role": "system", "content": "Ты должен общаться на Русском. Ты учитель биологии."},
        {"role": "user", "content": user_message},
    ]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            temperature=0,
            max_tokens=150,  # Установите подходящее значение
        )
        ai_response = response.choices[0].message['content'].strip()
        return jsonify({'response': ai_response})
    except Exception as e:
        logging.error(f"Ошибка при вызове модели: {str(e)}")
        return jsonify({'error': f"Ошибка: {str(e)}"}), 500
'''

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('msg', '')

    messages = [
        ("system", "Ты должен общаться на Русском. Ты учитель биологии."),
        ("human", user_message),
    ]

    try:
        ai_response = llm.invoke(messages)
        # Возвращаем ответ в JSON
        return jsonify({"response": ai_response.content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
