def test_create_person_subject(client):
    response = client.post("/person-subjects/", json={"person_id": 1, "subject_id": 1, "career_id": 1, "time_taken": 1})
    assert response.status_code == 201
    data = response.json()
    assert data["person_id"] == 1
    assert data["subject_id"] == 1

def test_get_person_subjects(client):
    response = client.get("/person-subjects/1")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
