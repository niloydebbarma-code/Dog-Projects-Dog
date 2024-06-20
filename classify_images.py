from torchvision import models, transforms
from PIL import Image
import torch

def classify_images(images_dir, results_dic, model_name):
    model = getattr(models, model_name)(pretrained=True)
    model.eval()
    
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    
    for filename in results_dic:
        img_path = images_dir + filename
        input_image = Image.open(img_path)
        input_tensor = preprocess(input_image)
        input_batch = input_tensor.unsqueeze(0)
        
        with torch.no_grad():
            output = model(input_batch)
        
        _, predicted_idx = torch.max(output, 1)
        predicted_class = models.densenet121(pretrained=True).class_to_idx.keys()[predicted_idx.item()]
        results_dic[filename].append(predicted_class)
