
import feedparser
import hashlib
import json
from bs4 import BeautifulSoup

def grab(url) :
    d = feedparser.parse(url)
    for e in d["entries"] :
        title = e["title"].encode("utf-8")
        summary = e["summary"]
        h = hashlib.sha224(title).hexdigest()
        summary = summary.replace("<br />","__LINEBREAK__")    
        soup = BeautifulSoup(summary)
        
        answer = soup.get_text()[11:]
        answer = answer[:-21]
        answer = answer.replace("__LINEBREAK__","\n")
        answer = answer.strip()
        print title
        print answer
        j = {"question":title,"answer":answer,"link":e["link"]}
        f=open(h+".quora.txt",'w')
        f.write(json.dumps(j))
        f.close()
