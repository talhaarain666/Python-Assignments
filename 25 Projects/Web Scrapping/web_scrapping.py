import requests
from bs4 import BeautifulSoup as bs

github_user = input("Enter the GitHub username: ")
url = f'https://github.com/{github_user}'
r = requests.get(url)
soup = bs(r.content, 'html.parser') # all html page content
profile_img = soup.find('img', {'class': 'avatar avatar-user width-full border color-bg-default'})

if profile_img:
    print(profile_img['src'])  # Print the profile image URL
else:
    print("Profile image not found. Make sure the username is correct.")