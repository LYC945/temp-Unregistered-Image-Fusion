import os
from pathlib import Path

import torch
import torch.utils.data as data
import torchvision
from PIL import Image
from tqdm import tqdm

import model.model as model
import utils.utils as utils
import args

device = torch.device("cuda:" + device_id if torch.cuda.is_available() else "cpu")
print(device)
