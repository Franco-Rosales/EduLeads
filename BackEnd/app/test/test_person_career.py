def test_create_person_career(client):
    response = client.post("/person-careers/", json={"person_id": 1, "career_id": 1, "time_taken": 1})
    assert response.status_code == 201
    data = response.json()
    assert data["person_id"] == 1
    assert data["career_id"] == 1

def test_get_person_careers(client):
    response = client.get("/person-careers/1")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
