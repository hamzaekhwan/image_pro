import base64
from io import BytesIO
from PIL import Image
import pickle
# from django.templatetags.static import static

def load_image_from_array(image_array):
    # Create an image from the array
    image = Image.fromarray(image_array)
    return image


def image_process(pkl_dict, image_name):
    with open(pkl_dict, 'rb') as f:
        images_dict = pickle.load(f)
    loaded_image = load_image_from_array(images_dict[image_name])

    # Convert the image to a Base64 string
    buffered = BytesIO()
    loaded_image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    return f"data:image/jpeg;base64,{img_str}"