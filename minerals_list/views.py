from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def show_page(request):
    widok = """
            <html>
                <body>
                    <p>To jest strona startowa!</p>
                </body>
            </html>
            """
    return HttpResponse(widok)