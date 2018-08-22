# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 19:17:42 2018

@author: anshul
"""

from bs4 import BeautifulSoup
import requests
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque
import re


from urllib.request import urlopen
import urllib.request

f=open('scrapped.txt','w')
import numpy as np
count=0
query=input("query>>")
query=query.strip().split()
query="+".join(query)

html = "https://www.google.co.in/search?site=&source=hp&q="+query+"&gws_rd=ssl"
req = urllib.request.Request(html, headers={'User-Agent': 'Crome'})

soup = BeautifulSoup(urlopen(req).read(),"html.parser")

#Regex
reg=re.compile(".*&sa=")

links = []
#Parsing web urls
for item in soup.find_all('h3', attrs={'class' : 'r'}):
    try:
        line = (reg.match(item.a['href'][7:]).group())
        links.append(line[:-4])
    except(TypeError):
	    continue

    

list2=[]
for k in links:
   
    if(k[0:4]=='http'):
	    list2.append(k)
list3=list2[0:5]
for l in list3:
    print(l)		
list4=[]
# a queue of urls to be crawled
for m in list3:
    list4.append(m)       
        
    new_urls = deque(list4)

# a set of urls that we have already crawled
    processed_urls = set()
# a set of crawled emails
    emails = set()
    k=5
# process urls one by one until we exhaust the queue
    while (k!=0):

    # move next url from the queue to the set of processed urls
        try:
            url = new_urls.popleft()
        except(IndexError):
            k=k-1		
            continue
        processed_urls.add(url)

    # extract base url to resolve relative links
        parts = urlsplit(url)
        base_url = "{0.scheme}://{0.netloc}".format(parts)
        path = url[:url.rfind('/')+1] if '/' in parts.path else url

    # get url's content
        print("Processing %s" % url)
        try:
            response = requests.get(url.strip())
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError,):
        # ignore pages with errors
            continue

    # extract all email addresses and add them into the resulting set
        new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[gmail]+\.[a-z]+", response.text, re.I))
        emails.update(new_emails)

    # create a beutiful soup for the html document
        soup = BeautifulSoup(response.text,"html.parser")
	
	

    # find and process all the anchors in the document
        for anchor in soup.find_all("a"):
        # extract link url from the anchor
            link = anchor.attrs["href"] if "href" in anchor.attrs else ''
        # resolve relative links
            if link.startswith('/'):
                link = base_url + link
            elif not link.startswith('http'):
                link = path + link
        # add the new url to the queue if it was not enqueued nor processed yet
            if not link in new_urls and not link in processed_urls:
                new_urls.append(link)
        k=k-1
        if (not new_urls):
            break
    list4=[]	
    if  not emails:
	    print("no emails")
        
    else:
        for j in emails :
	        
            f.write(j)
            f.write('\n')
            print (j)

f.close()