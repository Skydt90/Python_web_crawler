# Python Web Crawler

This repository contains the source code solution to the first exam assignment in the python elective at KEA's computer science course. See project description and install instructions below.  

***Programmers:*** *Christian Skydt & Jakob Wulff*


### Project Description
The requirements for this assignment, was to build a program capable of "crawling & scraping" the contents of a website and saving the content from each individual site into locally stored .md files without the use of any third party modules. The advice was to choose a small website and also get some sort of limit on how many links should be followed.

#### Project Outline
This program is built to specifically target at dummy website setup by the teacher in order to keep the scope and magnitude of the assignment to a managable level. 
The main actor in the program is the "scraper.py" module, which uses a combination of Python's built in modules to solve the task at hand. The html content from the dummy site is retrieved using urllib.request which is then passed to a custom subclassed HTMLParser that extracts the content and links from each site. The scraper then passes this to a custom filehandler module, which formats and writes it to individual files. To ensure the same link is never scraped twice, each time a link has been scraped, the scraper will add it to a "scraped.txt" file and likewise add new links to a "queue.txt" file. To restrict the amount of pages scraped, the program will only go to links if it contain a specified domain name, if it doesn't the program will not add it to the queue and simply ignore it.
