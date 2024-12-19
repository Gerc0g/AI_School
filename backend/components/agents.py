'''
==================
Агенты Q&A системы
1. Функциональные описания агентов
2.
==================
'''
###################################
# ТУЛЗЫ
###################################
from langchain_core.tools import tool

@tool
def educ_plane_api(city: str) -> str:
    """Возвращает информацию об образовательных планах в указанном городе."""
    return f"Weather in {city}: Sunny, 22°C"


@tool
def presentation_api(query: str) -> str:
    """Возвращает актуальную информацию о стоимости акций."""
    return "AAPL stock price is 150 USD"


# Интегрируем инструменты с моделью
#llm_with_tools = llm.bind_tools([educ_plane_api, presentation_api])

tool_mapping = {
    "educ_plane_api": educ_plane_api,
    "presentation_api": presentation_api
}


