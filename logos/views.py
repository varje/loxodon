from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from logos.forms import LogoAnalyzeForm
from logos.models import LogoAnalyze
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
    # Handle file upload
    if request.method == 'POST':
        form = LogoAnalyzeForm(request.POST, request.FILES)
        if form.is_valid():
            logoanalyze = form.save(commit=False)
            logoanalyze.precision = "Enter your precision here"
            logoanalyze.suggested_logo_name = "Enter your suggested logo name here"
            # Redirect to index page
            logoanalyze.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = LogoAnalyzeForm()  # A empty, unbound form

    # Load documents for the list page
    logoanalyzes = LogoAnalyze.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'index.html',
        {'logoanalyzes': logoanalyzes, 'form': form}
    )
