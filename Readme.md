# RAG Prototype

Небольшой прототип **Retrieval-Augmented Generation (RAG)**, демонстрирующий работу простого поискового движка на эмбеддингах.

## 🚀 Функциональность
- API на **FastAPI**
- Векторный поиск по документам через **FAISS**
- Эмбеддинги с помощью **sentence-transformers**
- Мини-тесты с **pytest**

## 🧩 Установка и запуск

```bash
# 1. Клонируем репозиторий
git clone https://github.com/yourusername/rag-prototype.git
cd rag-prototype

# 2. Создаём виртуальное окружение
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Устанавливаем зависимости
pip install -r requirements.txt

# 4. Запускаем сервер
uvicorn app.main:app --reload
