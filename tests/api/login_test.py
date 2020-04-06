import requests


def test_login():
    result = requests.get('http://jira.hillel.it:8080', auth=('webinar5', 'webinar5'))
    assert result.status_code == 200
