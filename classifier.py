import torch
import torchvision.transforms as transforms
import torchvision.models as models
import json
from PIL import Image

# Load pretrained models
resnet18 = models.resnet18(pretrained=True)
alexnet = models.alexnet(pretrained=True)
vgg16 = models.vgg16(pretrained=True)

models_dict = {'resnet': resnet18, 'alexnet': alexnet, 'vgg': vgg16}

# Load ImageNet class labels
with open('imagenet_class_index.json') as f:
    imagenet_class_idx = json.load(f)

def classify_image(image_path, model_name):
    model = models_dict[model_name]
    img = Image.open(image_path)
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    img_tensor = preprocess(img).unsqueeze(0)
    model.eval()
    with torch.no_grad():
        output = model(img_tensor)
    
    _, predicted_idx = torch.max(output, 1)
    class_idx = predicted_idx.item()
    return imagenet_class_idx[str(class_idx)][1]

