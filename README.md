BagSaleDetector v0.1
===============
Handbag Sale Detector
It checks the sale page (handbag) of Neiman Marcus every 15min, and
send an email notification when there is a new one

constants.py: NM sale link, smtp server host url, the duration between each check (by default, 15min)
Bag.py: define basic classes;
crawler.py: main func

To use the program:

    1) change SMTP_HOST, TO_EMAILS in constants.py

    2) open a screen

    3) python crawler.py

    4) close the screen
    

TODO:

1) add links to the newly reported item



You are more than welcome to improve the code =)

Lilian

