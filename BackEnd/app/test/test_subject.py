def test_create_subject(client):
    response = client.post("/subjects/", json={"name": "Algebra", "description": "Algebra course", "career_id": 1})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Algebra"

def test_get_subject(client):
    response = client.get("/subjects/1")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Algebra"

def test_update_subject(client):
    response = client.put("/subjects/1", json={"name": "Calculus", "description": "Calculus course", "career_id": 1})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Calculus"

def test_delete_subject(client):
    response = client.delete("/subjects/1")
    assert response.status_code == 200
