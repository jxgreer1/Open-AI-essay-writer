import docx2txt
import PyPDF2
from odf import text, teletype
from odf.opendocument import load
from colorama import init, Fore, Style
init(autoreset=True, convert=True)

def split(word):
    return list(word)

def input_type_docx(type):
    return type.endswith(".docx")  
def input_type_txt(type):
    return type.endswith(".txt")  
def input_type_pdf(type):
    return type.endswith(".pdf")
def input_type_odt(type):
    return type.endswith(".odt")

def doc(Doc):
    global word 
    try:
        raw_word = docx2txt.process(Doc)
        print(f"{Fore.GREEN}Sucessful!{Style.RESET_ALL}")
        word = split(raw_word)  
        return word
    except:
        print(f"{Fore.RED}Specified Word Document Cannot Be Found: Please Follow Instructions On Github\n{Style.RESET_ALL}")
        return None
def odt(Doc):
    global word 
    output = ""
    try:
        raw_word = load(Doc)
        allparas = raw_word.getElementsByType(text.P)
        print(f"{Fore.GREEN}Sucessful!{Style.RESET_ALL}")
        for i in range(len(allparas)):
            output += teletype.extractText(allparas[i])
        word = split(output)
        return word   
    except:
        print(f"{Fore.RED}Specified ODT Cannot Be Found: Please Follow Instructions On Github\n{Style.RESET_ALL}")
        return None
def txt(Doc):
    global word 
    try:
        raw_word = open(Doc,'r')
        print(f"{Fore.GREEN}Sucessful!{Style.RESET_ALL}")
        word = split(raw_word.read())
        raw_word.close()
        return word   
    except:
        print(f"{Fore.RED}Specified Txt Cannot Be Found: Please Follow Instructions On Github\n{Style.RESET_ALL}")
        return None

def pdf(Doc):
    global word 
    output = ""
    try:
        raw_word = open(Doc,'rb')
        pdfreader=PyPDF2.PdfFileReader(raw_word)
        x=pdfreader.numPages
        for i in range(x):
            pageobj = pdfreader.getPage(i)
            output += pageobj.extractText()
        print(f"{Fore.GREEN}Sucessful!{Style.RESET_ALL}")
        word = split(output)
        raw_word.close()
        return word   
    except:
        print(f"{Fore.RED}Specified PDF Cannot Be Found: Please Follow Instructions On Github\n{Style.RESET_ALL}")
        return None

def check():
    Doc = input(f"Please Enter Document Name Below (eg: ---.txt) :{Fore.YELLOW} \n")
    if input_type_docx(Doc):
        return doc(Doc)
    elif input_type_txt(Doc):
        return txt(Doc)
    elif input_type_pdf(Doc):
        return pdf(Doc)
    elif input_type_odt(Doc):
        return odt(Doc)
    elif Doc == "quit":
        print(f"{Fore.GREEN}Successful!{Style.RESET_ALL}")
        quit()
    else:
        print(f"{Fore.RED}Unspecified File Extention - Please Try Again\n{Style.RESET_ALL}")
        return None



def checkOPENAI():
    Doc = "dist/myfile.txt"
    return txt(Doc)
    

