import torch
import torchvision.models as models

mobilenet = models.mobilenet_v2(pretrained=True)

mobilenet.eval()

print(mobilenet)
