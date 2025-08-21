from app import app

def test_root_ok():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
    assert "message" in res.get_json()

def test_health_ok():
    client = app.test_client()
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json()["status"] == "ok"
