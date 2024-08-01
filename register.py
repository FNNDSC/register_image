import subprocess

def register_images_rigid(fixed_image_path, moving_image_path, registered_image_path, transform_matrix_path,
                          dof='6', cost='mutualinfo'):
    # Prepare FSL's flirt command for rigid registration
    flirt_command = [
        'flirt',
        '-in', moving_image_path,
        '-ref', fixed_image_path,
        '-out', registered_image_path,
        '-omat', transform_matrix_path,
        '-dof', dof,  # Degrees of freedom should be 6 for rigid registration
        '-cost', cost  # mutual information is the best option for images obtained at different scanners
    ]
    # Execute the flirt command
    subprocess.run(flirt_command, check=True)
    print(f"Registered image saved to {registered_image_path}")



# CODE TESTING:

if __name__ == '__main__':
    fixed_image_path = '/Users/arman/projects/register_image/data/nifti/fixed.nii.gz'
    moving_image_path = '/Users/arman/projects/register_image/data/nifti/moving.nii.gz'
    output_image_path = '/Users/arman/projects/register_image/data/nifti/moving_registered.nii.gz'
    transform_matrix_path = '/Users/arman/projects/register_image/data/nifti/transform.mat'

    register_images_rigid(fixed_image_path, moving_image_path, output_image_path, transform_matrix_path)


