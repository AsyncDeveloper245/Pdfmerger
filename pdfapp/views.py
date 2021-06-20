from django.shortcuts import render
from PyPDF2 import PdfFileReader,PdfFileWriter
from django.http import HttpResponse
import PyPDF2
from .forms import PdfMergeForm

# Create your views here.
def pdf_merge(request):
    if request.method == 'POST':
        # If you submit via POST
        form = PdfMergeForm(request.POST, request.FILES)
        if form.is_valid():
            # 1 Get upload files
            f1 = request.FILES['file1']
            # 2 Get upload files
            f2 = request.FILES['file2']

            # Into a PDF file objects
            pdfFileObj1 = PyPDF2.PdfFileReader(f1)
            pdfFileObj2 = PyPDF2.PdfFileReader(f2)

            # Create a PDF file merge objects, add merge files
            pdfMerger = PyPDF2.PdfFileMerger()
            pdfMerger.append(pdfFileObj1)
            pdfMerger.append(pdfFileObj2)

            # Merge file object is written to merged_file.pdf
            with open('merged_file.pdf', 'wb') as pdfOutputFile:
                pdfMerger.write(pdfOutputFile)

            # Open merger merged_file.pdf, by HttpResponse output
            with open('merged_file.pdf', 'rb') as merged_file:
                response = HttpResponse(merged_file.read(), content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="merged_file.pdf"'
                return response

        else:
            # If submitting by POST, but the form does not pass validation
            form = PdfMergeForm()

    else:
        # If the user does not pass the POST, submitting to generate an empty form
        form = PdfMergeForm()

    return render(request, 'index.html', {'form': form})