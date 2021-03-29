import os
import shutil
import argparse
import sys
import random


def mkdir(n_fold, path):
    for i in range(n_fold):
        os.mkdir(os.path.join(path, '_'+str(i)))


def rmdir(n_fold, path):
    for i in range(n_fold):
        os.rmdir(os.path.join(path, '_'+str(i)))


def list_divide_inside(list_, k):
    for i in range(0, len(list_), k):
        yield list_[i:i+k]


def list_divide(list_, n_fold):
    k = int(len(list_) / n_fold) + 1
    return list(list_divide_inside(list_, k))


def n_fold_divide(root_dir, n_fold, random_seed):
    for i, (path, dir, files) in enumerate(os.walk(root_dir)):
        if i == 0:
            mkdir(n_fold, path)
            for j in range(n_fold):
                for k in dir:
                    os.mkdir(os.path.join(path, '_'+str(j), k))
        if i != 0:
            random.Random(random_seed).shuffle(files)
            temp_divide = list_divide(files, n_fold)
            for ij in range(len(temp_divide)):
                for item in temp_divide[ij]:
                    shutil.move(os.path.join(path, item), os.path.join(
                        root_dir, '_'+str(ij), path.split(os.path.sep)[-1]))
            os.rmdir(path)


def main(args):
    n_fold_divide(args.root_dir, args.n_fold, args.random_seed)


def parse_arguments(argv):

    parser = argparse.ArgumentParser()

    parser.add_argument('--root_dir',
                        type=str,
                        help='root directory containing relocated folders',
                        default='result')

    parser.add_argument('--n_fold',
                        type=int,
                        help='number of folder to divide into',
                        default=5)

    parser.add_argument('--random_seed',
                        type=int,
                        help='random_seed number',
                        default=5)

    return parser.parse_args(argv)


if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))
