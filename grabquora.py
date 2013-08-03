
from sys import argv
from grab_rss import grab

grab("http://www.quora.com/%s/answers/rss" % argv[1])
