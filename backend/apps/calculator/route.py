from fastapi import APIRouter
import base64
from io import BytesIO
from apps.calculator.utils import analyze_image
from schema import ImageData
from PIL import Image

router = APIRouter()

@router.post('')
async def run(data: ImageData):
    # Decode the base64 image data (assuming it's PNG)
    image_data = base64.b64decode(data.image.split(",")[1])  # Assumes data:image/png;base64,<data>
    image_bytes = BytesIO(image_data)
    image = Image.open(image_bytes)

    # Process the image using the analyze_image function
    responses = analyze_image(image, dict_of_vars=data.dict_of_vars)

    # Collect responses into a list
    data = [response for response in responses]

    print('response in route: ', responses)
    return {"message": "Image processed", "data": data, "status": "success"}
