# Scrape IMDB Reviews
 A simple application to help you fetch IMDB reviews and ratings to a spreadsheet

 This application takes 3 input parameters - the IMDB review location URL, the number of pages you want to scrape and the path where you want to save the extract  
 
 Ensure you have the compatible Chrome Driver (same as the Chrome Version installed, Chrome Browser > Help > About Google Chrome) in the same folder as the python script, you can find the Chrome Driver here: https://chromedriver.chromium.org/downloads
 
 ![image](https://user-images.githubusercontent.com/29762153/118753533-d8f31280-b882-11eb-8bc7-6290b354b591.png)
 Steps:
 
* This application is a simple command line program
* Migrate to the location where you have cloned the application (here for example: D:\AnuragHalder\Work\scraping>)
* Here is the example command line - >python imdb.py https://www.imdb.com/title/tt0111161/reviews?ref_=tt_ov_rt D:\AnuragHalder\Work\Radhe\scraping 30
* Once completed you would find in your provided location a spreadsheet of the extracted reviews

![image](https://user-images.githubusercontent.com/29762153/118754370-8d416880-b884-11eb-92e2-2831c77bb3f4.png)
