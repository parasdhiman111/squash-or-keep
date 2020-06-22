from urlshort import create_app

def test_shorten(client_app):
    response= client_app.get('/')
    assert b'Shorten' in response.data
