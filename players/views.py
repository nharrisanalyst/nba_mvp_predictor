from django.shortcuts import render

# Create your views here.

## data for the main site 
main_context = {
    "title":"NBA MVP Predictor",
    "header": "Lorem Ipsum"
    
    }

def main(request):
    return render(
        request,
        'main.html',
        main_context
    )