import argparse
import os
import shutil
import sys
import time
import warnings
from random import sample

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn import metrics
from torch.autograd import Variable
from torch.optim.lr_scheduler import MultiStepLR

from cgcnn.data import CIFData
from cgcnn.data import collate_pool, get_train_val_test_loader
from cgcnn.model import CrystalGraphConvNet

parser = argparse.ArgumentParser(description='Crystal Graph Convolutional Neural Networks')

parser.add_argument('--resume', default='', type=str, metavar='PATH',
                    help='path to latest checkpoint (default: none)')

args = parser.parse_args(sys.argv[1:])

if args.resume:
    if os.path.isfile(args.resume):
        print("=> loading checkpoint '{}'".format(args.resume))
        checkpoint = torch.load(args.resume)
        args.start_epoch = checkpoint['epoch']
        best_mae_error = checkpoint['best_mae_error']
        print(checkpoint)
        # model.load_state_dict(checkpoint['state_dict'])
        # optimizer.load_state_dict(checkpoint['optimizer'])
        # normalizer.load_state_dict(checkpoint['normalizer'])

        # checkpoint['epoch'] = 500
        # checkpoint['best_mae_error'] = 0.3439016342163086

        print("=> loaded checkpoint '{}' (epoch {})"
              .format(args.resume, checkpoint['epoch']))
        print("=> loaded model '{}' (epoch {}, validation {})"
              .format(args.resume, checkpoint['epoch'],
                      checkpoint['best_mae_error']))

        # torch.save({
        #     'epoch': checkpoint['epoch'],
        #     'state_dict': checkpoint['state_dict'],
        #     'best_mae_error': checkpoint['best_mae_error'],
        #     'optimizer': checkpoint['optimizer'],
        #     'normalizer': checkpoint['normalizer'],
        #     'args': 'zhouyiteng test'
        # }, 'test.pth.tar')
    else:
        print("=> no checkpoint found at '{}'".format(args.resume))