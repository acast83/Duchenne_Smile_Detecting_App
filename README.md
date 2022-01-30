# Duchenne smile detecting app
Duchenne smile detection app is a Python app that detects honest smile (and ignores fake smile) in real time using your web cam. 
This project is ongoing, not finished because I am still not satisfied with the Haar cascade model I created.

The idea for me was to create a tool that will detect genuine smile, and ignore fake smile
![No smile VS Fake Smile VS Genuine Smile](/fake_smile_vs_genuine_smile.png)

First step was to create a script that will allow me to download a large number of images and store them in a specific folder.
I achieved this using Python and Selenium, an open-source web-based automation tool. [google_images_scraping.py](https://github.com/acast83/duchenne_smile_detecting_app/blob/master/google_images_scraping.py) script automates search and downloading images, allowing user to choose specific search term
that will be used during automated search. To create a cascade model We need to use images stored in bmp format. For this purpose I downloaded around 250 images positive images and 50 negative images.

After that I created a Haar cascade model using [this tutorial](https://www.cs.auckland.ac.nz/~m.rezaei/Tutorials/Creating_a_Cascade_of_Haar-Like_Classifiers_Step_by_Step.pdf)

Final Python script [duchenne_smile_detection_on_web_cam_video.py](https://github.com/acast83/duchenne_smile_detecting_app/blob/master/duchenne_smile_detection_on_web_cam_video.py)
runs our webcam using OpenCv library and displays rectangle around detected object.

Both Python scripts are fully functioning but I am still not satisfied with the Haar cascade model I created. I will experiment more, if anyone is interested in collaboration  and improvement of my Haar cascade model please email me.

Screenshot of my app using current Haar cascade model
![picture](https://github.com/acast83/duchenne_smile_detecting_app/blob/master/Screenshot%20from%202021-11-03%2014-04-55.png)





