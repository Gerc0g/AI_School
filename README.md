# AI_School

- Сделать работу на агентах
- Использовать LangGraph для сложной логике работы в графах

Приложение представляет собой веб сервис.

Функционал:
1. Загрузка видео/аудио записи собеседования, на основе которого ИИ выделяет сущности:
    - Полный список вопросов по интервью
    - Вопросы на которые кандидат не смог ответить
    На основе этих данных строится статистика по всем вопросам и словарь, где для каждой технологии постепенно дополняется пулл вопросов.
    ИИ система автоматически обезличивает запсиси собеседований, отчего информация о ФИО, компании и зарплатных ожиданиях не хранится в БД.


    Таким образом существует база данных с общим списком вопросов и технологий по стекам.


2. Загрузка учебных материалов и формирование общей библиотеки знаний.


3. Просмотр всех вопросов которые попадаются на собеседованиях:
    - Как бы GPT ответил на этот вопрос.
    - Ответить на вопрос относительно информации из учебных материалов.

4. Гибкий фильтр по технологиям и грейдам для подготовки на позицию.



НОВОЕ:
- скинуть список вопросов - получаем список вопросов - по списку вопросов сформировать план обучения - по плану обучения дополнить информацией из учебных материалов которые загружены из книг - на выходе получаем документ с планом и по каждому пункту с информацией для изучения / по этому плану уже ребята сформируют презентации