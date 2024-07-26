from ultralytics import YOLO
from ultralytics import YOLO
import torch
import yaml

# Load and train the model
model = YOLO("yolov8n.yaml")  # Ensure you're using the correct config file
model.train(data="config.yaml", epochs=2)

# Save the model weights
torch.save(model.model.state_dict(), r"C:\Users\harsh\OneDrive\Desktop\craters\model_weights.pth")

# Save the model configuration manually
with open(r"C:\Users\harsh\OneDrive\Desktop\craters\model_config.yaml", 'w') as f:
    yaml.dump(model.model.yaml, f)




