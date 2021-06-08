# Image scrapers with selenium

Disclaimer: Please read the official terms of services of the respective websites and run the scripts at your own risk. This is made for educational purposes only.

4 files are added to this repo, their names & functionality being self explainatory:
1. Google Images scraper
2. Pexelsbot
3. Unsplashbot
4. Pixabaybot

The four files *DO NOT* download the images directly from the websites; *RATHER* get the "src" or the "srcset" attributes of the rendered images and write them to an ".xls" file.

This file can be then used to perform duplicate filtering or other requisite function by using xlrd library

combine.py is used to combine all xls sheets in a directory into a single one for simplicity incase one decides to run the scripts multiple times with different queries and stores the results in different spreadsheets.