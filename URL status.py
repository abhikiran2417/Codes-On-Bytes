import requests

def check_url_status(url):
    try:
        response = requests.get(url)
    
        if response.status_code // 100 == 2:
            return True, response.status_code
        else:
            return False, response.status_code
    except requests.RequestException:
        return False, None

def main():

    urls = [
        "https://www.google.com",
        "https://www.abhikiran.com",
        "https://www.linkedin.com",
        "https://www.youtube.com",
        "https://www.codesonbytes.com"
    ]

    for url in urls:
        is_available, status_code = check_url_status(url)
        if is_available:
            print(f"{url} is available (Status Code: {status_code})")
        else:
            print(f"{url} is not available")

if __name__ == "__main__":
    main()