import csv

with open("C:/Users/32589/Desktop/books-en.csv",encoding="latin-1") as file:
    reader=csv.DictReader(file,delimiter=";")
    Author=input("Author:")
    filtered_books=[]
    for row in reader:
        try:
            price=int(row["Year-Of-Publication"])
            if price>=150 and row["Book-Author"]==Author:
                filtered_books.append(row)
        except:
            print("no books>=150")
    for i in filtered_books:
       print(i["Book-Title"],i["Book-Author"],i["Year-Of-Publication"])