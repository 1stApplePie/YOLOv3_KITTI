import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

# parse the yolov3 configuration
def parse_hyperparm_config(path):
    file = open(path, 'r')
    lines = file.read().split('\n')
    lines = [x for x in lines if x and not x.startswith('#')]
    lines = [x.rstrip().lstrip() for x in lines]

    module_defs = []
    for line in lines:
        if line.startswith('['):
            type_name = line[1:-1].rstrip()
            if type_name != "net":
                continue
            module_defs.append({})
            module_defs[-1]['type'] = type_name
            if module_defs[-1]['type'] == 'convolutional':
                module_defs[-1]['batch_normalize'] = 0
        else:
            if type_name != "net":
                continue
            key, value = line.split('=')
            value = value.strip()
            module_defs[-1][key.rstrip()] = value.strip()
    return module_defs

def get_hyperparam(data):
    for d in data:
        if d['type'] == 'net':
            batch = int(d['batch'])
            subdivision = int(d['subdivisions'])
            momentum = float(d['momentum'])
            decay = float(d['decay'])
            saturation = float(d['saturation'])
            lr = float(d['learning_rate'])
            burn_in = int(d['burn_in'])
            max_batch = int(d['max_batches'])
            lr_policy = d['policy']
            in_width = int(d['width'])
            in_height = int(d['height'])
            in_channels = int(d['channels'])
            classes = int(d['class'])
            ignore_class = int(d['ignore_cls'])

            return {'batch': batch,
                    'subdivision': subdivision,
                    'momentum': momentum,
                    'decay': decay, 
                    'saturation': saturation,
                    'lr': lr,
                    'burn_in' : burn_in,
                    'max_batch' : max_batch,
                    'lr_policy' : lr_policy,
                    'in_width' : in_width,
                    'in_height' : in_height,
                    'in_channels' : in_channels,
                    'classes' : classes,
                    'ignore_class' : ignore_class
                    }
        
def xywh2xyxy_np(x : np.array):
    y = np.zeros_like(x)
    y[...,0] = x[...,0] - x[...,2] / 2  # minx = center_x - width/2
    y[...,1] = x[...,1] - x[...,3] / 2  # miny = center_y - height/2
    y[...,2] = x[...,0] + x[...,2] / 2  # maxx = center_x + width/2
    y[...,3] = x[...,1] + x[...,3] / 2  # maxy = center_y + height/2
    return y

def drawBox(img):
    img = img * 255

    img_data = np.array(np.transpose(img, (1, 2, 0)), dtype = np.uint8)
    img_data = Image.fromarray(img_data)
    
    # draw = ImageDraw.Draw(img_data)

    plt.imshow(img_data)
    plt.show()