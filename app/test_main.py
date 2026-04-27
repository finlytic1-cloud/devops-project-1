from main import app

def test_home_endpoint():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert 'message' in response.get_json()

def test_health_endpoint():
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json()['status'] == 'healthy'
