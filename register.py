
import subprocess
from datetime import datetime


def register_images_rigid(fixed_image_path, moving_image_path, registered_moving_image_path, transform_matrix_path,
                          dof='6', cost='mutualinfo'):
    """
    This function needs FSL's FLIRT to be able to run: https://fsl.fmrib.ox.ac.uk/fsl/docs/#/registration/flirt/index
    """
    flirt_command = [
        'flirt',
        '-ref', fixed_image_path,
        '-in', moving_image_path,
        '-out', registered_moving_image_path,
        '-omat', transform_matrix_path,
        '-dof', '6',  # Degrees of freedom should be '6' for rigid body transformation
        '-cost', 'mutualinfo'  # multual information or normalized mutual information are best options
    ]
    subprocess.run(flirt_command, check=True)
    print(f"Registered image saved to {registered_moving_image_path}")
    print(f"Transform matrix saved to {transform_matrix_path}")




# CODE TESTING:

if __name__ == '__main__':
    fixed_image_path = '/Users/arman/projects/register_image/data/nifti/fixed.nii.gz'
    moving_image_path = '/Users/arman/projects/register_image/data/nifti/moving.nii.gz'
    registered_moving_image_path = '/Users/arman/projects/register_image/data/nifti/moving_registered.nii.gz'
    transform_matrix_path = '/Users/arman/projects/register_image/data/nifti/transform.mat'

    t1 = datetime.now()
    register_images_rigid(fixed_image_path, moving_image_path, registered_moving_image_path, transform_matrix_path)
    print(f'Registration computation time: {datetime.now() - t1}')

    # ToDo: test results show that:
    #  1. FLIRT takes ~2 minutes to complete. Will explore faster rigid registration strategies. It would be
    #  great if we can figure out what registration strategy Visage uses, because that takes ~10 seconds.
    #  2. the registered image is a bit blurrier than the original image. Will explore better resampling strategies
    #  such as B-spline interpolation.