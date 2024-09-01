def test_create_career(client):
    response = client.post("/careers/", json={"name": "Engineering", "description": "Engineering degree"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Engineering"
    assert data["description"] == "Engineering degree"

def test_get_career(client):
    response = client.get("/careers/1")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Engineering"

def test_update_career(client):
    response = client.put("/careers/1", json={"name": "Math", "description": "Mathematics degree"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Math"

def test_delete_career(client):
    response = client.delete("/careers/1")
    assert response.status_code == 200
