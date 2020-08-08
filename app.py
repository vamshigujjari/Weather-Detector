from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import torch
import torchvision
from CNN_Model import model 
from torchvision import transforms
from PIL import Image

app = Flask(__name__)
app.config["DEBUG"] = True

cnn_model = model()
cnn_model.load_state_dict(torch.load('weather_model_4.pth', map_location=torch.device('cpu')))
cnn_model.eval()

classes = ['Cloudy', 'Rain', 'Shine', 'Sunrise']

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', data = None)


@app.route('/predict', methods =['GET','POST'])
def predict():
    if request.method == 'POST':
        f = request.files['file']
        if f is not None:
            input_tensor = transform_image(f)
            prediction_idx = get_prediction(input_tensor)
            class_name = classes[prediction_idx]
            print("vamshi!!!", class_name)
            return render_template("index.html", data=class_name)



def get_prediction(input_tensor):
    outputs = cnn_model.forward(input_tensor)                 # Get likelihoods for all ImageNet classes
    _, y_hat = outputs.max(1)                             # Extract the most likely class
    prediction = y_hat.item()                             # Extract the int value from the PyTorch tensor
    return prediction


def transform_image(infile):
    input_transforms = [transforms.Resize((224,224)), transforms.ToTensor()]
    my_transforms = transforms.Compose(input_transforms)
    image = Image.open(infile)                            # Open the image file
    timg = my_transforms(image)                           # Transform PIL image to appropriately-shaped PyTorch tensor
    timg.unsqueeze_(0)                                    # PyTorch models expect batched input; create a batch of 1
    return timg

if __name__ == '__main__':
   app.run(debug = True)






