import tensorflow
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from matplotlib import pyplot as plt

import numpy as np
import PIL
from tensorflow.keras.models import load_model
from PIL import Image

# 여기부터 panoramic image
# image1, image2, image3, image4: 네 방면의 이미지 디렉토리로 설정해야 함
# 아래 코드를 수정하든, 

def preprocess(path_list):
    image1 = path_list[0]
    image2 = path_list[1]
    image3 = path_list[2]
    image4 = path_list[3]


    img1 = Image.open(image1)
    img2 = Image.open(image2)
    img3 = Image.open(image3)
    img4 = Image.open(image4)

    new_img = Image.new("RGB", (2880, 2880))
    new_img.paste(img1, (0, 0))
    new_img.paste(img2, (1440, 0))
    new_img.paste(img3, (0, 1440))
    new_img.paste(img4, (1440, 1440))
    return new_img.resize((640, 640)) # 데이터 전처리 - 리사이징 작업


# 여기부터 model prediction
def main(fp):
    vgg16_model_path = '/Users/ihaemin/Desktop/codeep-flask2/vscode/new_trained_from_vgg16 (ReLU, binary, Adam).h5'
    model = load_model(vgg16_model_path)

    img_height = 224
    img_width = 224

    label_names = {0 : 'crime', 1 : 'safe'}

    filename = fp
    original = load_img(filename, target_size = (img_height,img_width))

    numpy_image = img_to_array(original)
    image_batch = np.expand_dims(numpy_image , axis = 0)

    prob = model.predict(image_batch)
    predict = np.argmax(model.predict(image_batch))
    final_prob = round(prob[0][0], 2)

    return f"결과 : {label_names[predict]} / 범죄 위험 : {final_prob:0.2f} "