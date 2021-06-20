from django import forms

class PdfMergeForm(forms.Form):
    file1 = forms.FileField(label="Upload PDF file 1")
    file2 = forms.FileField(label="Upload PDF files 2")