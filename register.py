import subprocess

def register_images_rigid(fixed_image_path, moving_image_path, registered_image_path, transform_matrix_path,
                          dof='6', cost='mutualinfo'):

    # Run FSL's flirt for rigid registration
    flirt_command = [
        'flirt',
        '-in', moving_image_path,
        '-ref', fixed_image_path,
        '-out', registered_image_path,
        '-omat', transform_matrix_path,
        '-dof', dof,  # Degrees of freedom should be 6 for rigid transformation
        '-cost', cost  # mutual information is the best option for images obtained at different scanners
    ]

    # Execute the flirt command
    subprocess.run(flirt_command, check=True)
    print(f"Registered image saved to {registered_image_path}")

if __name__ == '__main__':
    # Example usage
    fixed_image_path = '/Users/arman/projects/image-reslice/data/nifti/fixed.nii.gz'
    moving_image_path = '/Users/arman/projects/image-reslice/data/nifti/moving.nii.gz'
    output_image_path = '/Users/arman/projects/image-reslice/data/nifti/moving_registered.nii.gz'
    transform_matrix_path = '/Users/arman/projects/image-reslice/data/nifti/transform.mat'

    register_images_rigid(fixed_image_path, moving_image_path, output_image_path, transform_matrix_path)


