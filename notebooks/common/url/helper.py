from urllib.parse import urlparse,urljoin

def normalize_urls(relative_urls, base_url):
    """ Take a list of relative urls, return a list of absolute urls. This function
    is permissive - you can mix and match absolute and relative urls, and it will 
    return a list of absolute URLs. 
    """
    
    absolute_urls = []
    for url in relative_urls:
        parsed_url = urlparse(url)
        if parsed_url.scheme:
            absolute_urls.append(url)
        else:
            absolute_urls.append(urljoin(base_url,url))
    return absolute_urls

def filter_anchor_links(urls):
    return [url for url in urls if "#" not in url]
