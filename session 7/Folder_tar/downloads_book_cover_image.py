# Question 1

import csv
import requests

print("\nList of downloaded images\n")
with open('100books.csv') as csv_file :
    books = csv.DictReader(csv_file)
    for book in books:
        image_url = book['image_url']
        image_name = image_url.split("/")[-1]
        with open(image_name,"wb") as file :
            response = requests.get(image_url)
            content = response.content
            file.write(content)
            print("\nDownloaded {}".format(image_name))

