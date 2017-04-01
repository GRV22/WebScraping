Lots of time I was facing problem to get all Accepted solutions with 100 score of Long challenge problems on Codechef.
So thats why I write python script to get all Accepted solutions Links with 100 score.
I am using BeautifulSoup 4 and requests module.

How to use it :

1) Go to Long Challenge problem page of Codechef.
2) Click on All Submissions button
3) Copy this URL for input.
4) Now run webscrap.py file using command on terminal
		>> python webscrap.py
5) A file will get create named "codechefSolutions.txt" which will have all Accepted solution URLs.