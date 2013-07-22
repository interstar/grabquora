Quora Grabber
=============

Grabs a feed of answers from a Quora user and backs them up on local machine.

Currently stores each answer in a separate text file whose name is a hash of the question and which contains a 
json structure of {"question":QUESTION,"answer":ANSWER,"link":LINK TO ORIGINAL ANSWER}

It strips out most of the HTML (which will break links and embedded YouTube videos.) On the plus side, this means 
that the text is more suitable for converting to other formats.

How to Use
----------

eg. to grab the feed of Quora user Phil-Jones

    python grabquora.py Phil-Jones 

To format the answers in your current directory into an HTML page for MY NAME :

    python list.py "MY NAME" > list.html
    
Then look at list.html in your browser.

FAQ
---
Q : Why do the files have such weird names?

A : The file names are based on the questions. I wanted to make the file names shorter than the full question,
but also unique.

If you just tried to truncate a question like "Which do people who program in Python like best : Zope or Django?" to 
make the filename you'd get something like "whichdopeoplewhoprogaminpytho.txt" And next year, when you answer 
"Which do people who program in Python like best : Strawberry or Vanilla?" you'd overwrite the earlier question.

A "hashing" function takes a piece of text and is *almost* certain to come up with a unique code-number based on it, so 
I'm using a hashing function to generate a name from the question which is short(ish), but almost certainly unique.

Q : I looked inside the file and its weird.
A : I'm storing answers in JSON format. A very simple data-structure that most pramming languages can handle very 
easily. (More easily than XML in most cases.) 

This gives other people the chance to write scripts to render those answers in different human readable formats. The 
list.py program included here puts them into a single HTML page. But there'll be other options. Talk to me if you'd 
like to request one.

    
    


