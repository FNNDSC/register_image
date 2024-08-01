#!/usr/bin/env python

from os.path import join
from pathlib import Path
from argparse import ArgumentParser, Namespace, ArgumentDefaultsHelpFormatter
from chris_plugin import chris_plugin, PathMapper
from register import register_images_rigid

title = r"""

                        ###########################
                        ChRIS Register Image Plugin
                        ###########################

"""

parser = ArgumentParser(description='This plugin re-orients a 3D scan (CT, MRI, PET, etc) into standard planes,'
                                    're-slices the re-oriented image, and saves the re-oriented images as a '
                                    'NIfTI file.',
                        formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument('--fixed_image', type=str, default='fixed_image.nii.gz',
                    help='relative path to the fixed image in relation to input folder')
parser.add_argument('--moving_image', type=str, default='moving_image.nii.gz',
                    help='relative path to the moving image in relation to input folder')

parser.add_argument('--dof', type=str, default='6',
                    help='degrees of freedom to use in transformation. Default=6, i.e. rigid registration.')
parser.add_argument('--cost', type=str, default='mutualinfo',
                    help='cost function used in registration. Default=mutualinfo.')

parser.add_argument('--registered_image', type=str, default='registered_moving_image.nii.gz',
                    help='relative path to the registered image in relation to output folder')
parser.add_argument('--transform_matrix', type=str, default='transform.mat',
                    help='relative path to the transformation matrix in relation to output folder')

@chris_plugin(
    parser=parser,
    title='register_image',
    category='3D Image Processing',
    min_memory_limit='1Gi',         # supported units: Mi, Gi
    min_cpu_limit='1000m',          # millicores, e.g. "1000m" = 1 CPU core
    min_gpu_limit=0)                # set min_gpu_limit=1 to enable GPU



def main(options: Namespace, inputdir: Path, outputdir: Path):

    print(title)

    fixed_image_path = join(inputdir, options.fixed_image)
    moving_image_path = join(inputdir, options.moving_image)
    registered_image_path = join(outputdir, options.registered_image)
    transform_matrix_path = join(outputdir, options.transform_matrix)
    dof = options.dof
    cost = options.cost

    register_images_rigid(fixed_image_path, moving_image_path, registered_image_path, transform_matrix_path,
                          dof, cost)



if __name__ == '__main__':
    main()
