import PyPDF2

n=int(input("enter the number of pdfs u wnat to merge: "))
pdffiles=[]
for i in range(n):
    pname=input(f"enter name of {i+1}st pdf: ")
    pname=pname+".pdf"
    pdffiles.append(pname)
# print(pdffiles)

def pdfmerger():
    merger=PyPDF2.PdfMerger()
    for filename in pdffiles:
        pdffile=open(filename,'rb')
        pdfReader=PyPDF2.PdfReader(pdffile)
        merger.append(pdfReader)
    pdffile.close()
    merger.write('merger.pdf')
pdfmerger()
print("the merged pdf is in the file name 'merger.pdf'")
