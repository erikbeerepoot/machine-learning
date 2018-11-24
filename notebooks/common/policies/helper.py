from common.url.helper import normalize_urls

from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests
import html2text
import re 
def save_policies(policy_list, path):
    """ Save a list of policies to disk
    Keyword arguments:
    policy_list -- A list of (title, content) tuples representing the policies
    path -- The path to save the policies to
    """
    for policy in policy_list:
        if policy is not None:
            # Remove special characters from filename (if necessary)
            title = re.sub('[?\n!@#$%^&*]', '', policy[0])
            # Prevent spurious whitepace in filename
            title = title.replace(" ", "_")
            # Prevent open() from seeing filename as path
            title = title.replace("/","_")
            contents = policy[1]
            f = open(f"{path}/{title}.md","w+")
            f.write(contents)
            f.close()

def fetch_policy_links(policies_url, target_tag, tag_class=None, tag_id=None):
    """ Fetch policy links from a webpage by looking for anchor links that are descendants of 'target-tag'.
    You should pass in the closest viable tag to avoid including URLs that aren't policy URLs.
    """
    page = requests.get(policies_url)
    soup = BeautifulSoup(page.text,"lxml")

    # Lookup target tag that should contain policy links as descendants   
    if tag_class is not None:
        policy_toc = soup.find(target_tag,class_=tag_class)
    elif tag_id is not None:
        policy_toc = soup.find(target_tag, id=tag_id)
    else :
        policy_toc = soup.find(target_tag)
    
    if policy_toc is None:
        return None
    
    # Find all anchor links that are descendants of the target tag
    policy_link_tags = policy_toc.findChildren("a",href=True)
    
    # Extract base url from policies url 
    parsed_uri = urlparse(policies_url)
    base_url = f"{parsed_uri.scheme}://{parsed_uri.netloc}"
    return normalize_urls([el["href"] for el in policy_link_tags], base_url)

def fetch_policy_document(policy_url, title_tag, content_tag, content_class):
    """ Fetches a policy document. Call this on a leaf node that actually contains
    the policy contents
    Keyword arguments:
    policy_url -- The URL of the policy to fetch
    title_tag -- The tag to look for and scrape the title from
    content_tag -- The tag to look for that contains the content
    content_clss -- The class of the tag that contains the content
    """
    try:
        policy_page = requests.get(policy_url)
        policy_text = str(policy_page.text)
        s = BeautifulSoup(policy_text,"lxml")
        content = s.find(content_tag, class_=content_class)
        if content is None:
            return
        heading = content.find(title_tag)        
        title = html2text.html2text(heading.text.strip())
        text = html2text.html2text(content.text)
        return (title, text)
    except: return None

