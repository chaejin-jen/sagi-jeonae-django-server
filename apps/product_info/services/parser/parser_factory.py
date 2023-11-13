from abc import ABC, abstractmethod

site_parsers = {}

class BaseParser(ABC):
    @abstractmethod
    def parse(self, url):
        raise NotImplementedError("Subclasses must implement this method")

    @staticmethod
    def get_headers():
        return {
            'method': 'GET',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }

def regist_site(site):
    def decorator(cls):
        site_parsers[site] = cls
        return cls
    return decorator

class ParserFactory:
    @staticmethod
    def get_parser(site):
        parser_cls = site_parsers.get(site)
        if parser_cls:
            return parser_cls()
        else:
            raise ValueError(f"No parser found for `{site}`")