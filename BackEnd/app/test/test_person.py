def test_create_person(client):
    response = client.post("/persons/", json={
        "name": "John",
        "surname": "Doe",
        "email": "john.doe@example.com",
        "address": "123 Main St",
        "phone": "1234567890"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "John"
    assert data["surname"] == "Doe"

def test_get_person(client):
    response = client.get("/persons/1")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "John"
    assert data["surname"] == "Doe"

def test_update_person(client):
    response = client.put("/persons/1", json={
        "name": "Jane",
        "surname": "Doe",
        "email": "jane.doe@example.com",
        "address": "456 Main St",
        "phone": "0987654321"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Jane"
    assert data["surname"] == "Doe"

def test_delete_person(client):
    response = client.delete("/persons/1")
    assert response.status_code == 200
