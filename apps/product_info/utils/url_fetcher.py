import urllib.request
import socket
import gzip
from io import BytesIO

def fetch_response_url(url, headers = None):
    try:
        socket.setdefaulttimeout(5) 
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            return response.url
    except (urllib.error.URLError, ValueError) as e:
            print(f"Error fetching URL: {e}")

def fetch_page_contents(url, headers = None):
    try:
        socket.setdefaulttimeout(5)
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            if response.info().get('Content-Encoding') == 'gzip':
                buf = BytesIO(response.read())
                f = gzip.GzipFile(fileobj=buf)
                html_content = f.read().decode('utf-8')
            else:
                html_content = response.read().decode('utf-8')
            return html_content
    except (urllib.error.URLError, ValueError) as e:
        print(f"Error fetching URL: {e}")

if __name__ == "__main__":
    # url = 'https://docs.python.org/ko/3/library/index.html'
    url = 'https://www.coupang.com/vp/products/6802219221?itemId=16060268422&vendorItemId=83263569641&isAddedCart='
    headers = {
        'method': 'GET',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }
    fetch_page_contents(url, headers)