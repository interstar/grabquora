from os import listdir
from os.path import isfile, join
onlyfiles = [ f for f in listdir(".") if isfile(join("",f)) ]

import json
from sys import argv

print """
<html>
<style>
body {
    font-family:sans;
    color:#333333;
    padding:3px;
}

dt {
    top-margin:4px;
    font-weight:bold;
}


</style>
<body>
<h2>Quora Answers by %s</h2>
<dl>
""" % argv[1]
count = 0
for fn in onlyfiles :
    if fn[-3:] == "txt":
        f = open(fn) 
        entry = json.loads(f.read())
        
        print "<dt>%s <a href='%s'>Link</a></dt>" % (entry["question"].encode("utf-8"), entry["link"].encode("utf-8"))
        answer = entry["answer"].encode("utf-8")
        answer = answer.replace("\n\n","<br/>")
        print "<dd>%s</dd>" % answer
        count = count+1
        
print """
</dl>
<p>%s items</p>
</body>
</html>""" % count
