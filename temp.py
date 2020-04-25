import comtypes.client
import glob
import os

input_direc = r"C:\Users\HP\Downloads\Table-Reading-Understanding-in-Documents-Images-master\Table-Reading-Understanding-in-Documents-Images-master\INPUT FILES"

wdFormatPDF = 17

word = comtypes.client.CreateObject('Word.Application')

docx_direc = r"C:\Users\HP\Downloads\Table-Reading-Understanding-in-Documents-Images-master\Table-Reading-Understanding-in-Documents-Images-master\INPUT FILES"
#total_docx_files = len(os.listdir(docx_direc))
#docx_lists=[]

#docx_files_name=os.listdir(input_direc)
   
results = [each for each in os.listdir(docx_direc) if each.endswith('.docx')]
print(results)

def save_to_pdf(in_file,name):
    word = comtypes.client.CreateObject('Word.Application')
    doc = word.Documents.Open(in_file)
    out_file = r"C:\Users\HP\Downloads\Table-Reading-Understanding-in-Documents-Images-master\Table-Reading-Understanding-in-Documents-Images-master\INPUT FILES\{}.pdf".format(name)
    doc.SaveAs(out_file, FileFormat=wdFormatPDF)
    docx_orig.Close()
    print("DONE: "+str(i))
    word.Quit()

i=10
for in_file in glob.glob(r"C:\Users\HP\Downloads\Table-Reading-Understanding-in-Documents-Images-master\Table-Reading-Understanding-in-Documents-Images-master\INPUT FILES\*.docx"):
    save_to_pdf(in_file,i)
    i+=1

def save_to_pdf2(in_file, name):
    word = comtypes.client.CreateObject('Word.Application')
    doc = word.Documents.Open(in_file)
    out_file = r"C:\Users\HP\Downloads\Table-Reading-Understanding-in-Documents-Images-master\Table-Reading-Understanding-in-Documents-Images-master\INPUT FILES\PDF of DOC_%d.pdf"%doc_no
    doc.SaveAs(out_file, FileFormat = wdFormatPDF)
    doc.Close()
    word.Quit()

i=10
for in_file in glob.glob(r"C:\Users\HP\Downloads\Table-Reading-Understanding-in-Documents-Images-master\Table-Reading-Understanding-in-Documents-Images-master\INPUT FILES\*.doc"):
    save_to_pdf2(in_file,i)
    i+=1

docx_no = len(glob.glob(r"C:\Users\HP\Downloads\Table-Reading-Understanding-in-Documents-Images-master\Table-Reading-Understanding-in-Documents-Images-master\INPUT FILES\*.docx"))
doc_no = len(glob.glob(r"C:\Users\HP\Downloads\Table-Reading-Understanding-in-Documents-Images-master\Table-Reading-Understanding-in-Documents-Images-master\INPUT FILES\*.doc"))

total_word_file = docx_no + doc_no
