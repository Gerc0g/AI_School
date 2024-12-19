from langchain_community.vectorstores import FAISS # Import FAISS module
from loguru import logger # Import logger
import time
import os

def create_db(source_chunks,embeddings,db_file_name):
    start_time = time.time()
    logger.debug('create_db............')
    db = FAISS.from_texts(source_chunks, embeddings)
    db.save_local(db_file_name)
    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.debug(f'create_db elapsed_time = {elapsed_time} sec')
    return db


# Функция для загрузки существующей векторной базы знаний
def load_db(embeddings, db_file_name):
    start_time = time.time()
    new_db = FAISS.load_local(db_file_name, embeddings, allow_dangerous_deserialization=True)
    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.debug(f'load_db elapsed_time = {elapsed_time} sec')
    return new_db

def init_db(embedding, faiss_idx, source_chunks = ["NULL"]):
    # Проверяем, существует ли сохранённый индекс
    if os.path.exists(faiss_idx) and os.path.isdir(faiss_idx):
        logger.debug('Найдена существующая база данных, выполняется загрузка...')
        db = load_db(embedding,faiss_idx)
    else:
        logger.debug('База данных не найдена, создаём новую...')
        db = create_db(source_chunks, embedding, faiss_idx)
    return db