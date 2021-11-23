#!/usr/bin/env python

from PIL import Image
from faker import Faker
from pathlib import Path
import random
import csv

fake = Faker()

images = Path("./orig").glob("*.jpg")
images = [str(p) for p in images]
print(images)

size=360, 360

with open("graduates.csv", "w") as csvfile:
    mywriter = csv.writer(csvfile)
    for i in range(350):
        if random.randint(1,2) == 1:
            fn = fake.first_name_female()
            mn = fake.first_name_female()
        else:
            fn = fake.first_name_male()
            mn = fake.first_name_male()
        ln = fake.last_name()
        if random.randint(1, 50) == 37:  #Randomly make the filename first name the middle name
            myname = "%s %s" % (mn, ln)
        else:
            myname = "%s %s" % (fn, ln)
        myfn = myname.upper().replace(" ", "") + ".jpg"
        myfile = random.choice(images)
        im = Image.open(myfile)
        im.thumbnail(size, Image.ANTIALIAS)
        im.save(myfn, "JPEG")
        print(myfn, myfile)
        mywriter.writerow([fn, mn, ln])
