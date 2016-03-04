import requests

INSTAGRAM_MEDIA_LINK = "https://www.instagram.com/{username}/media/"

def fetch_user_photos(username):
    print "fetching..."
    url = INSTAGRAM_MEDIA_LINK.format(username=username)
    response = requests.get(url);
    return response
