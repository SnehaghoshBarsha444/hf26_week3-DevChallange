import app as app_module

def test_home_page():
    client = app_module.app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Small steps" in response.data

def test_health_endpoint():
    client = app_module.app.test_client()
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json["provider"] == "local Ollama"

def test_goal_required():
    client = app_module.app.test_client()
    response = client.post("/api/plan", json={"goal": "   "})
    assert response.status_code == 400
    assert "error" in response.json

def test_goal_length_limit():
    client = app_module.app.test_client()
    response = client.post("/api/plan", json={"goal": "x" * 501})
    assert response.status_code == 400
