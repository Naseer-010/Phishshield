from django.shortcuts import render
from . utils import scan_url

def home(request):
    """
    Renders the home page of the PhishShield application.
    """
    if request.method == 'POST':
        url = request.POST.get('url')
        if url:
            result = scan_url(url)
            percentage = result.get('threat_percentage', 0)
            message = result.get('message', 'No data available')
            return render(request, 'detector/home.html', {'percentage': percentage, 'message': message})

    return render(request, 'detector/index.html')

