#Import package to scrape data
from bs4 import BeautifulSoup
#selenium to trigger javascript events
from selenium import webdriver
import requests
import time
import csv
from merge_data import merge

def travel_blog():
    
    #initializing chrome driver
    driver=webdriver.Chrome(executable_path='C:/Users/Abhilash/Downloads/chromedriver_win32/chromedriver.exe')
    #search videos for travel blogs
    driver.get('https://www.youtube.com/results?search_query=travel+blogs')
    
    #scrolling down 100 times to load all videos
    for i in range(100):
        #scrolling down
        driver.execute_script('window.scrollTo(1, '+str(i*5000)+');')
        #wait for 5 seconds to load new videos
        time.sleep(5)

    #get the page source
    source = driver.page_source
    soup = BeautifulSoup(source, 'lxml')

    # print(soup)

    csv_file = open('data/YouTube Scraped Data travel_blog.csv','w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Video Id', 'Title', 'Description', 'Category'])
    flag = 0 
    for content in soup.find_all('div', class_= "text-wrapper style-scope ytd-video-renderer"):
        
        #scrape video id
        vid_id = content.find('a',  href=True)
        vid_id = vid_id['href'].replace("watch?v=","").encode("utf-8")
        print(vid_id)

        #scrape title
        title = content.find('a', class_= "yt-simple-endpoint style-scope ytd-video-renderer").text.encode("utf-8")
        print(title)

        #scrape description
        description = content.find('yt-formatted-string', class_="style-scope ytd-video-renderer").text.encode("utf-8")
        print(description)

        category = "Travel Blogs"

        print('\n')
        #write to csv
        csv_writer.writerow([vid_id, title, description, category])
        flag += 1
    
    driver.quit()


    csv_file.close()


    #scrape data for science and technology
def science_technology():
    
    driver=webdriver.Chrome(executable_path='C:/Users/Abhilash/Downloads/chromedriver_win32/chromedriver.exe')
    driver.get('https://www.youtube.com/results?search_query=science+and+technology')

    for i in range(100):
        driver.execute_script('window.scrollTo(1, '+str(i*5000)+');')
        time.sleep(5)

    source = driver.page_source
    soup = BeautifulSoup(source, 'lxml')

    # print(soup)

    csv_file = open('data/YouTube Scraped Data science_technology.csv','w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Video Id', 'Title', 'Description', 'Category'])
    flag = 0 
    for content in soup.find_all('div', class_= "text-wrapper style-scope ytd-video-renderer"):

        vid_id = content.find('a',  href=True)
        vid_id = vid_id['href'].replace("watch?v=","").encode("utf-8")
        print(vid_id)

        title = content.find('a', class_= "yt-simple-endpoint style-scope ytd-video-renderer").text.encode("utf-8")
        print(title)

        description = content.find('yt-formatted-string', class_="style-scope ytd-video-renderer").text.encode("utf-8")
        print(description)

        category = "Science and Technology"

        print('\n')
        csv_writer.writerow([vid_id, title, description, category])
        flag += 1
    
    driver.quit()


    csv_file.close()


#scrape data for food
def food():
    
    driver=webdriver.Chrome(executable_path='C:/Users/Abhilash/Downloads/chromedriver_win32/chromedriver.exe')
    driver.get('https://www.youtube.com/results?search_query=food')

    # for i in range(100):
    #     driver.execute_script('window.scrollTo(1, '+str(i*5000)+');')
    #     time.sleep(5)

    source = driver.page_source
    soup = BeautifulSoup(source, 'lxml')

    # print(soup)

    csv_file = open('data/YouTube Scraped Data food.csv','w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Video Id', 'Title', 'Description', 'Category'])
    flag = 0 
    for content in soup.find_all('div', class_= "text-wrapper style-scope ytd-video-renderer"):

        vid_id = content.find('a',  href=True)
        vid_id = vid_id['href'].replace("watch?v=","").encode("utf-8")
        print(vid_id)

        title = content.find('a', class_= "yt-simple-endpoint style-scope ytd-video-renderer").text.encode("utf-8")
        print(title)

        description = content.find('yt-formatted-string', class_="style-scope ytd-video-renderer").text.encode("utf-8")
        print(description)

        category = "Food"

        print('\n')
        csv_writer.writerow([vid_id, title, description, category])
        flag += 1
    
    driver.quit()


    csv_file.close()


    #scrape data for manufacturing
def Manufacturing():
    
    driver=webdriver.Chrome(executable_path='C:/Users/Abhilash/Downloads/chromedriver_win32/chromedriver.exe')
    driver.get('https://www.youtube.com/results?search_query=manufacturing')

    for i in range(100):
        driver.execute_script('window.scrollTo(1, '+str(i*5000)+');')
        time.sleep(5)

    source = driver.page_source
    soup = BeautifulSoup(source, 'lxml')

    # print(soup)

    csv_file = open('data/YouTube Scraped Data Manufacturing.csv','w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Video Id', 'Title', 'Description', 'Category'])
    flag = 0 
    for content in soup.find_all('div', class_= "text-wrapper style-scope ytd-video-renderer"):

        vid_id = content.find('a',  href=True)
        vid_id = vid_id['href'].replace("watch?v=","").encode("utf-8")
        print(vid_id)

        title = content.find('a', class_= "yt-simple-endpoint style-scope ytd-video-renderer").text.encode("utf-8")
        print(title)

        description = content.find('yt-formatted-string', class_="style-scope ytd-video-renderer").text.encode("utf-8")
        print(description)

        category = "Manufacturing"

        print('\n')
        csv_writer.writerow([vid_id, title, description, category])
        flag += 1
    
    driver.quit()


    csv_file.close()


    #scrape data for history
def History():
    
    driver=webdriver.Chrome(executable_path='C:/Users/Abhilash/Downloads/chromedriver_win32/chromedriver.exe')
    driver.get('https://www.youtube.com/results?search_query=history')

    for i in range(100):
        driver.execute_script('window.scrollTo(1, '+str(i*5000)+');')
        time.sleep(5)

    source = driver.page_source
    soup = BeautifulSoup(source, 'lxml')

    # print(soup)

    csv_file = open('data/YouTube Scraped Data History.csv','w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Video Id', 'Title', 'Description', 'Category'])
    flag = 0 
    for content in soup.find_all('div', class_= "text-wrapper style-scope ytd-video-renderer"):

        vid_id = content.find('a',  href=True)
        vid_id = vid_id['href'].replace("watch?v=","").encode("utf-8")
        print(vid_id)

        title = content.find('a', class_= "yt-simple-endpoint style-scope ytd-video-renderer").text.encode("utf-8")
        print(title)

        description = content.find('yt-formatted-string', class_="style-scope ytd-video-renderer").text.encode("utf-8")
        print(description)

        category = "History"

        print('\n')
        csv_writer.writerow([vid_id, title, description, category])
        flag += 1
    
    driver.quit()


    csv_file.close()


    #scrape data for art and music
def Art_Music():
    
    driver=webdriver.Chrome(executable_path='C:/Users/Abhilash/Downloads/chromedriver_win32/chromedriver.exe')
    driver.get('https://www.youtube.com/results?search_query=art+and+music')

    for i in range(100):
        driver.execute_script('window.scrollTo(1, '+str(i*5000)+');')
        time.sleep(5)

    source = driver.page_source
    soup = BeautifulSoup(source, 'lxml')

    # print(soup)

    csv_file = open('data/YouTube Scraped Data Art and Music.csv','w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Video Id', 'Title', 'Description', 'Category'])
    flag = 0 
    for content in soup.find_all('div', class_= "text-wrapper style-scope ytd-video-renderer"):

        vid_id = content.find('a',  href=True)
        vid_id = vid_id['href'].replace("watch?v=","").encode("utf-8")
        print(vid_id)

        title = content.find('a', class_= "yt-simple-endpoint style-scope ytd-video-renderer").text.encode("utf-8")
        print(title)

        description = content.find('yt-formatted-string', class_="style-scope ytd-video-renderer").text.encode("utf-8")
        print(description)

        category = "Art and Music"

        print('\n')
        csv_writer.writerow([vid_id, title, description, category])
        flag += 1
    
    driver.quit()

    csv_file.close()


if __name__ == "__main__":

	print("Sit Back And Relax!! The Data is being Scraped....")

	travel_blog()
	science_technology()
	food()
	Manufacturing()
	History()
	Art_Music()

	merge.prepare_data(merge)

	print("Get Back to work!! Data Scraped Successfully")
