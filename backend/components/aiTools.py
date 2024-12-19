import time
from langchain_huggingface import HuggingFaceEmbeddings
from loguru import logger # Import logger

#Функция для запроса к ЛЛМ
def generate_response():
    pass

# Функция для разделения (splitting) документов

# Функция для получения embeddings model from HuggingFace
def get_embeddings(type='cpu'):
    logger.debug('get_embeddings............')
    start_time = time.time()
    model_id = 'intfloat/multilingual-e5-large' # <-- Это имя используемой embeddings модели
    if type=='cpu':
        model_kwargs = {'device': 'cpu'}
    else:
        model_kwargs = {'device': 'cuda'}
    embeddings = HuggingFaceEmbeddings(
        model_name=model_id,
        model_kwargs=model_kwargs
    )
    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.debug(f'get_embeddings elapsed_time = {elapsed_time} sec')
    return embeddings

#Функция сплит текста