from app import app

def test_home():
    assert app.test_client().get("/").status_code == 200

def test_pass():
    response = app.test_client().post(
        "/result", json={"marks": 75}
    )
    assert response.json["result"] == "PASS"

def test_fail():
    response = app.test_client().post(
        "/result", json={"marks": 25}
    )
    assert response.json["result"] == "FAIL"
