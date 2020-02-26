import pdfkit

from pdf2image import convert_from_path, convert_from_bytes

from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

#DECLARE CONSTANTS

urls = []

pdf_paths = ["Exhibit.pdf","ex99-2.pdf"]

images_arr = []

def getURLS():
    urls.insert(0,'https://www.sec.gov/Archives/edgar/data/882835/000088283518000017/a180420q1earningsrelease.htm')
    urls.insert(1, 'https://www.sec.gov/Archives/edgar/data/1507277/000143774916023052/ex99-2.htm')

def getPDFS():
    pdfkit.from_url(urls[0], pdf_paths[0])
    pdfkit.from_url(urls[1], pdf_paths[1])

def getImages(path):
    images = convert_from_path(path, poppler_path="C:/Program Files/poppler-0.68.0/bin")
    images_arr.append(images)

    for ele in images_arr:
        i = 1
        for image in ele:
            image.save(str(path)+"page_"+str(i)+".jpg")
            i+=1

#pdfkit.from_url('https://www.sec.gov/Archives/edgar/data/882835/000088283518000017/a180420q1earningsrelease.htm','Exhibit.pdf')
#pdfkit.from_url('https://www.sec.gov/Archives/edgar/data/1507277/000143774916023052/ex99-2.htm','ex99-2.pdf')

def main():
    getURLS()
    getPDFS()
    for path in pdf_paths:
        getImages(path)

if __name__ == "__main__":
    main()
