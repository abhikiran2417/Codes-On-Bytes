import random
import string
import webbrowser
shortened_urls = {}

def generate_random_string():

    characters = string.ascii_letters + string.digits

    random_string = "".join(random.choice(characters) for i in range(6))

    return random_string

def shorten_url(long_url):

    if long_url in shortened_urls.values():
        for key, value in shortened_urls.items():
            if value == long_url:
                short_url = key
                break
    else:
        short_url = generate_random_string()
        while short_url in shortened_urls.keys():
            short_url = generate_random_string()
        shortened_urls[short_url] = long_url
    return short_url

def redirect_url(short_url):
    if short_url in shortened_urls.keys():
        long_url = shortened_urls[short_url]
        webbrowser.open(long_url)
    else:
        print("Invalid shortened URL")

long_url = input("Enter a long URL: ")

short_url = shorten_url(long_url)
print("The shortened URL is: " + short_url)
redirect_url(short_url)
