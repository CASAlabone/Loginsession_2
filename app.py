# app.py
from flask import Flask, request, jsonify
from diffusers import StableDiffusionPipeline
import torch
from translate import Translator
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route('/generate_image', methods=['POST'])
def generate_image():
    user_input = request.form['user_input']
    style_option = request.form['style_option']

    model_id = "dreamlike-art/dreamlike-photoreal-2.0"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe = pipe.to("cuda")

    translator = Translator(from_lang="ko", to_lang="en")
    translation = translator.translate(user_input)
    result = translation + " in " + translator.translate(style_option)
    img = pipe(result).images[0]

    # Convert image to bytes
    img_bytes = BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes = img_bytes.getvalue()

    return jsonify({'image': img_bytes})

if __name__ == '__main__':
    app.run(debug=True)
