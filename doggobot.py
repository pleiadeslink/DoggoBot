import requests, json, os
from mastodon import Mastodon

# Mastodon token and domain
mastodon = Mastodon(
    access_token = 'abcdef',
    api_base_url = 'https://domain.com/'
)

# Get the image URL
URL = json.loads(requests.get('https://dog.ceo/api/breeds/image/random').content)["message"]

# Save image from URL
img = requests.get(URL).content
with open("dog.png", "wb") as png:
    png.write(img)

# Upload PNG file to Mastodon
media = mastodon.media_post("dog.png")
mastodon.status_post("#dogs #dogsofmastodon #mastodogs", media_ids=media)

# Delete the image, since it is no longer needed
os.remove("dog.png")