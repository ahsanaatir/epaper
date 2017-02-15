from django.shortcuts import render, get_object_or_404
from .models import question_detail,CourseLevel, Subject, Unit
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.views import generic
# from easy_pdf.views import PDFTemplateView
# Create your views here.



def index(request):
    # detail = question_detail.objects.all()
    course_detail = CourseLevel.objects.all()
    # subject_detail = Subject.objects.all()
    # unit_detail = Unit.objects.all()
    return render(request,'question/index.html', { 'course_details': course_detail})

def select_subjects(request):
    if request.method == "POST":
        course1 = request.POST['course']
        detail = Subject.objects.filter(course_level__id = course1)
        return render(request, 'question/index1.html', {'details': detail})
    else:
        # error msg for wrong selection
        detail = Subject.objects.all()
        return render(request, 'question/index.html', {'details': detail})



def select_unit(request):
    if request.method == "POST":
        subject_id = request.POST['subject_id']
        detail = Unit.objects.filter(subject__id=subject_id)
        return render(request, 'question/index2.html', {'details': detail})
    else:
        # error msg for wrong selection
        detail = Unit.objects.all()
        return render(request, 'question/index2.html', {'details': detail})



def select_question(request):
    if request.method == "POST":
        unit_id = request.POST['unit_id']
        detail = question_detail.objects.filter(unit__id=unit_id)
        unit_detail = Unit.objects.filter(pk=unit_id)
        return render(request, 'question/paper.html', {'details': detail}, {'unit_detail': unit_detail})
    else:
        # error msg for wrong selection
        detail = question_detail.objects.all()
        return render(request, 'question/paper.html', {'details': detail})



def paper(request):
    detail = question_detail.objects.all()
    # course_detail = CourseLevel.objects.all()
    return render(request,'question/paper.html', {'details': detail})




def pdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "question/index.html")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response


# class HelloPDFView(PDFTemplateView):
#     template_name = "question/index.html"
#
#     def get_context_data(self, **kwargs):
#         return super(HelloPDFView, self).get_context_data(
#             pagesize="A4",
#             title="paper!",
#             **kwargs
#         )