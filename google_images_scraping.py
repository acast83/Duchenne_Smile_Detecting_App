from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests
import io
from PIL import Image
user_input=input("Please enter search term: ")
#path to my chrome driver
PATH='---path to my chrome driver---'
wd=webdriver.Chrome(PATH)

# first function that finds and stores image source url's
def get_images_from_google(wd,delay,max_images):

    # function that will allow us to scroll down the page while searching for images
    def scroll_down(wd):
        #3 executing js script
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(delay)
    
    #skip variable will be used in case if during our search for image source We get duplicate source values
    skip = 0 
    #get Google images page using our web driver
    wd.get("https://www.google.com/imghp")
    #find search bar element
    search_bar=wd.find_element_by_name("q")
    #place user's search term in google search bar
    search_bar.send_keys(user_input)
    #press enter and start searching
    search_bar.send_keys(Keys.RETURN)
    time.sleep(3)
    
    #empty set in which We will store our source paths
    image_urls=set()
    #While loop will work until We finds certain number of image sources defined by the argument max_images
    while len(image_urls) +skip < max_images:
        scroll_down(wd)

        #if there is a button load more at the end of the page We want to click on it and continue expanding the search page
        try:
            end_page=wd.find_element(By.CLASS_NAME,"mye4qd")
            end_page.click()
        except:
            continue
        #find all available image thumbnails and store them in a list
        thumbnails=wd.find_elements(By.CLASS_NAME, "Q4LuWd")
       
        #looping through a list in order to find image sources. BUT, each time We return to this this
        #point with a While loop we want to start from newest entry and loop through to the end of the list
        #It is really important not to start each time from the begining of the list to avoid duplicates
        for img in thumbnails[len(image_urls)+skip : max_images]:
            #try clicking on each thumbnail
            try: 
                img.click()
                time.sleep(delay)
            except:
                continue
            
            #create a list of elements that containg img source attributes
            images=wd.find_elements(By.CLASS_NAME,"n3VNCb") 
            #loop through images list so We would find source for each image and store them in the images_urls set
            for image in images:
                #checking if We get duplicate entries in our image_urls set. 
                if image.get_attribute('src') in image_urls:
                    max_images+=1
                    skip+=1
                    break
                #checking if the source of the image is correct
                if image.get_attribute('src') and 'http' in image.get_attribute('src'):
                    #storing image source
                    image_urls.add(image.get_attribute('src'))
                    
    return image_urls
                



#second function that downloads and stores images on a specific location
def download_image(download_path,url,file_name):
    try:
        image_content=requests.get(url).content
        image_file= io.BytesIO(image_content)
        image=Image.open(image_file)
        file_path=download_path+file_name

        with open(file_path, "wb") as f:
            image.save(f, "BMP")
            print("success")
    except Exception as e:
        print("failed", e)

#create set that contains all gathered image source urls
urls_set= get_images_from_google(wd,2,50)

for i, url in enumerate(urls_set):
    download_image("images/",url,str(i) + ".bmp")
wd.quit()
