from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_search_basic():
    """Проверяем базовый поиск по ключевому слову"""
    resp = client.get("/search", params={"q": "FastAPI"})
    assert resp.status_code == 200
    data = resp.json()
    assert "results" in data
    assert len(data["results"]) > 0

def test_search_with_param_k():
    """Проверяем, что параметр k корректно влияет на результат"""
    resp = client.get("/search", params={"q": "LLM", "k": 3})
    data = resp.json()
    assert len(data["results"]) == 3
