from app import app

client = app.test_client()

def test_items():
    r = client.get("/items")
    assert r.status_code == 200