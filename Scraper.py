import requests
cookies = {}

def grabSource(url):
    request = requests.get(url=url, data=cookies)
    print(request.text)

if __name__ == "__main__":
    url = input("Enter the Benchmark URL: ")
    cookies["laravel_session"]= input("Enter laravel_session cookie: ")
    cookies["XSRF-TOKEN"] = input("Enter XSRF-TOKEN cookie: ")
    cookies["__cfduid"] = input("Enter __cfduid: ")


    grabSource(url)