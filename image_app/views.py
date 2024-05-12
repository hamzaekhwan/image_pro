from django.shortcuts import render
from django.templatetags.static import static
from .load_image import image_process
# import image_functions
# Create your views here.
def process_image(request, tab_id):
    # Example processing functions are process1, process2, process3
    input_image = f'image_{tab_id}'
    output_image = image_process("image_app/saved_dictionary.pkl" , input_image)
    # Assume function modifies the image and saves it to output path
    input_image_path=static(f'images/original/image_{tab_id}.jpg')
    context = {
        'original': input_image_path,
        'processed': output_image
    }
    print(context['original'])
    return render(request, 'index.html', context)
