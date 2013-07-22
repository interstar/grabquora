Quora Grabber
=============

Grabs a feed of answers from a Quora user and backs them up on local machine.

Currently stores each answer in a separate text file whose name is a hash of the question and which contains a 
json structure of {"question":QUESTION,"answer":ANSWER,"link":LINK TO ORIGINAL ANSWER}

It strips out most of the HTML (which will break links and embedded YouTube videos. On the plus side, this means 
that the text is more suitable for converting to other formats.

How to Use
----------

eg. to grab the feed of Quora user Phil-Jones

    python grabquora.py Phil-Jones 

To format the answers in your current directory into an HTML page for MY NAME :

    python list.py "MY NAME" > list.html
    
Then look at list.html in your browser.

    
    


