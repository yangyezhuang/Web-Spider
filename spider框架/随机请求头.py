from fake_useragent import UserAgent

ua = UserAgent()
headers = {'User-Agent': ua.random}

for i in range(10):
    headers = {'User-Agent': ua.random}
    print(headers)
