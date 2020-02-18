import argparse
from pathlib import Path

import open3d
from mayavi import mlab

from vgn.dataset import VgnDataset, RandomAffine
from vgn.utils.vis import draw_sample


def main(args):
    sample_path = Path(args.sample_path)

    transforms = [RandomAffine()] if args.augment else []

    dataset = VgnDataset(sample_path.parent, transforms=transforms)
    tsdf, (qual, rot, width), mask = dataset[dataset.samples.index(sample_path.name)]

    mlab.figure()
    draw_sample(tsdf, qual, rot[1], width, mask)
    mlab.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="visualize data from a sample")
    parser.add_argument("sample_path", type=str, help="path to the sample to be showed")
    parser.add_argument("--augment", action="store_true", help="augment sample")
    args = parser.parse_args()
    main(args)