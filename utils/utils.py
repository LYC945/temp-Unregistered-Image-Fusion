import os

import cv2
import numpy as np
import torch

def check_dir(base):
    if os.path.isdir(base):
        pass
    else:
        os.makedirs(base)

def save_state_dir(network, save_model_dir):
    state_dict = network.state_dict()
    for key in state_dict.keys():
        state_dict[key] = state_dict[key].to(torch.device('cpu'))
    torch.save(state_dict, save_model_dir)

def load_state_dir(network, pretrain_dir, device):
    network.load_state_dict({k.replace('module.', ''): v for k, v in torch.load(pretrain_dir).items()})
    network.to(device)
    network.eval()

def save_img(x, save_dir):
    if x.dim() == 4:
        x = x[0]
    x = x.permute(1, 2, 0)
    x = x.cpu().detach().numpy()
    x = (x * 255.).astype(np.uint8)  # ✅ Key update: Using uint8 is common for images
    cv2.imwrite(save_dir, x)

# --- Add this function to load a checkpoint ---
def load_checkpoint(checkpoint_path, model, optimizer=None):
    """
    Loads the checkpoint and updates model (and optimizer if provided).
    Returns the starting epoch.
    """
    if os.path.isfile(checkpoint_path):
        print(f"Loading checkpoint '{checkpoint_path}'")
        checkpoint = torch.load(checkpoint_path, map_location=device)
        model.load_state_dict(checkpoint['model_state_dict'])
        if optimizer is not None and 'optimizer_state_dict' in checkpoint:
            optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
        start_epoch = checkpoint.get('epoch', 0)
        print(f"Loaded checkpoint '{checkpoint_path}' (epoch {start_epoch})")
        return start_epoch
    else:
        print(f"No checkpoint found at '{checkpoint_path}'")
        return 0