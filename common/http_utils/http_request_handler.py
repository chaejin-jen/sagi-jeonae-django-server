import urllib.request
import socket
import gzip
from io import BytesIO

class HttpRequestHandler:
    def __init__(self, timeout=10):
        self.timeout = timeout

    def send_request(self, url, method='GET', headers=None, data=None):
        try:
            req = urllib.request.Request(url, method=method, data=data, headers=headers or {})
            response = urllib.request.urlopen(req, timeout=self.timeout)
            return self._handle_response(response)
        except urllib.error.HTTPError as e:
            return self._handle_error_response(e)
        except urllib.error.URLError as e:
            return self._handle_error_response(e)
        except socket.timeout as e:
            return self._handle_error_response(e)
        except ValueError as e:
            return self._handle_error_response(e)

    def _handle_response(self, response):
        content = ''
        if response.info().get('Content-Encoding') == 'gzip':
            content = self._decode_gzip(content)
        else:
            content = response.read().decode('utf-8')
        return content

    def _decode_gzip(self, content):
        buf = BytesIO(content)
        with gzip.GzipFile(fileobj=buf, mode='rb') as f:
            return f.read()

    def _handle_error_response(self, error):
        print(f"Error: {error}")
        return None
