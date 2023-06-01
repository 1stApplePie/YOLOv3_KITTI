import torch
import torch.nn as nn
from utils.tools import *
import os, sys

class Yololoss(nn.Module):
    def __init__(self, device, num_class):
        super(Yololoss, self).__init__()
        self.device = device
        self.num_class = num_class

    # def compute_loss(self, pred, target, yololayer):
