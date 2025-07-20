import requests
from datetime import datetime

def test_items_endpoint():
    resp = requests.get("http://localhost:8000/v1/items")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert all('id' in item and 'name' in item and 'created_at' in item for item in data)
    # Validate ISO-8601 format
    for item in data:
        try:
            dt = datetime.fromisoformat(item['created_at'].replace('Z', '+00:00'))
            assert dt.year == 2022
        except Exception:
            assert False, f"created_at not valid ISO 8601: {item['created_at']}"
