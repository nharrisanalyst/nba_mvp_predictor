from django.shortcuts import render

# Create your views here.

## data for the main site 
main_context = {
    "title":"NBA MVP Predictor",
    "header": "Lorem Ipsum",
    "explenation":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed velit ut orci maximus lobortis eget id lectus. In at metus quis lacus fringilla sagittis. Nam volutpat non quam sit amet malesuada. Fusce varius, nibh a tincidunt porttitor, urna risus ultrices lectus, non accumsan tortor nulla quis ligula. Curabitur lacinia, mauris ac cursus hendrerit, odio elit interdum turpis, id ultrices libero dui et odio. Maecenas euismod nunc eu metus consequat dictum sed sit amet nibh. Maecenas a dui eget neque ultrices consectetur. "
    }

def main(request):
    return render(
        request,
        'main.html',
        main_context
    )