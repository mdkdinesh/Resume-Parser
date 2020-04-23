from django.shortcuts import render
from docx import *

lin=[]
def index(request):
    if request.method == 'POST':
        file1 = request.FILES['document']
        document = Document(file1)

        lines = []
        for para in document.paragraphs:
            temp = ""
            line = (para.text).split()
            c = 0
            for x in line:
                if (x == ":"):
                    c = 1
                if (c > 1):
                    temp += x + " "
                c += 1
            lines.append(temp)
        for i in lines:
            lin.append(i)

        context = {'fname': lin[0],
                   'lname': lin[1],
                   'mail': lin[2],
                   'phno': lin[3],
                   'st': lin[4],
                   'city': lin[5],
                   'state': lin[6],
                   'country': lin[7],
                   'pincode': lin[8],
                   'work': lin[9],
                   'edu': lin[10],
                   'skill': lin[11],
                   'workexp': lin[12]
                   }
        return render( request,'resume.html', context )

    return render(request,'index.html')

