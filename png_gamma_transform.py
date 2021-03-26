import numpy as np
import cv2
import matplotlib.pyplot as plt
import argparse
import os
import sys


def gamma_gen( g_val):
    def gamma (im):
        temp = im.copy().astype(np.float)
        g = float(g_val)
        temp = ((temp/255)**(1/g))*255
        return temp.astype(np.uint8)
    return gamma

def parse_arguments(argv):
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--gamma',
                       type = int,
                       help = "The gamma value to make new png file",
                       default = '3')
    parser.add_argument('--root_dir',
                        type=str,
                        help='root directory containing the dataset',
                        default='./')
    
    return parser.parse_args(argv)

def main(args):
    
    gam = gamma_gen(args.gamma)
    for i in os.listdir(args.root_dir):
        path = os.path.join(args.root_dir,i)
        k = cv2.imread(path)
        plt.imsave(path, gam(k))
        
if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))

