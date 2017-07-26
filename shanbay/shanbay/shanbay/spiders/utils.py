import urlparse


def parse_params(url):
    """
    parse the params(ndde, page) from the url
    """
    res = urlparse.urlparse(url).query
    return urlparse.parse_qs(res).items()
