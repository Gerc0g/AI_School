'''
==================
Графовые структуры взаимодействия Q&A действий и агентстких систем
1. Построение обучающего плана на основе списка вопрсоов
2. Создание презентации на основе обучающего плана
==================
'''
from typing import TypedDict, Sequence
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import ToolMessage
from langgraph.graph import StateGraph, END

# Определяем состояние агента
class AgentState(TypedDict):
    messages: Sequence[BaseMessage]
    category: str
    api_call_count: int


###################################
# ФУНКЦИИ ДЛЯ ВЫЗОВОВ В ГРАФЕ
###################################

def call_classifier(state: AgentState):
    """
    Узел классификации:
    Использует LLM для классификации последнего запроса пользователя на категории: weather, finance или general.
    """
    messages = state["messages"]
    user_msg = messages[-1].content

    prompt = SystemMessage(content=(
            '''Классифицируй обращения пользователя в подходящую категорию.
            Категории:
            {'presentation' : 'Пользователь просит создать презентацию',
            'leasson_create' : 'Пользователь просит дополнить пункты плана обучения учебным материалом',
            'general' : 'Остальное'}
            В ответе укажи только категорию, ключ.'''
        ))
    query = HumanMessage(content=user_msg)

    response = llm.invoke([prompt, query])
    category = response.content.strip().lower()
    if category not in ["presentation", "leasson_create"]:
        category = "general"

    return {"messages": state["messages"], "category": category, "api_call_count": state["api_call_count"]}

def route_by_category(state: AgentState):
    """
    Функция для определения следующего шага в зависимости от категории.
    """
    category = state["category"]
    if category == "presentation":
        return "presentation_agent"
    elif category == "leasson_create":
        return "leasson_create_agent"
    else:
        return "general_agent"

def call_presentation_agent(state: AgentState):
    """
    Узел для обработки запросов на создание презентации.

    Агент попробует вызвать ...
    """
    messages = state["messages"]
    user_query = messages[-1].content

    # Извлекаем город (на примере — упрощенная логика)
    #city = "Munich" if "munich" in user_query.lower() else "Unknown city"
    
    # Вызываем инструмент
    #tool_output = presentation_api.invoke({"city": city})
    state["api_call_count"] += 1
    
    # Возвращаем ToolMessage
    return {
        "messages": [ToolMessage(content='Презентации')],#[ToolMessage(content=tool_output)],
        "api_call_count": state["api_call_count"]
    }

def call_leasson_create_agent(state: AgentState):
    """
    Узел для обработки дополнения учебного плана.
    """
    messages = state["messages"]
    user_query = messages[-1].content
    
    # Простой вызов
    #tool_output = educ_plane_api.invoke({"query": user_query})
    state["api_call_count"] += 1

    return {
        "messages": [ToolMessage(content='Урок')],#[ToolMessage(content=tool_output)],
        "api_call_count": state["api_call_count"]
    }

def call_general_agent(state: AgentState):
    """
    Узел для обработки 'общих' запросов, без специализированных инструментов.
    Здесь просто дергаем модель для ответа.
    """
    messages = state["messages"]
    response = llm.invoke(messages)
    return {
        "messages": [response],
        "api_call_count": state["api_call_count"]}
#Главынй классификатор запроса



###################################
# ПОСТРОЕНИЕ ГРАФА
###################################

workflow = StateGraph(AgentState)

# Добавляем узлы
workflow.add_node("classifier", call_classifier)
workflow.add_node("leasson_create_agent", call_leasson_create_agent)
workflow.add_node("presentation_agent", call_presentation_agent)
workflow.add_node("general_agent", call_general_agent)

# Начинаем с классификатора
workflow.set_entry_point("classifier")

# Добавляем ветвление в зависимости от категории
workflow.add_conditional_edges(
    "classifier",
    route_by_category,
    {
        "leasson_create_agent": "leasson_create_agent",
        "presentation_agent": "presentation_agent",
        "general_agent": "general_agent"
    }
)

workflow.add_edge("leasson_create_agent", END)
workflow.add_edge("presentation_agent", END)
workflow.add_edge("general_agent", END)

