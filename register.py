from nipype.interfaces.fsl import FLIRT

def register_images_rigid(fixed_image_path, moving_image_path, registered_image_path, transform_matrix_path,
                          dof=6, cost='mutualinfo'):

    flirt = FLIRT()
    flirt.inputs.in_file = moving_image_path
    flirt.inputs.reference = fixed_image_path
    flirt.inputs.out_file = registered_image_path
    flirt.inputs.out_matrix_file = transform_matrix_path
    flirt.inputs.dof = dof      # Degrees of freedom should be 6 for rigid registration
    flirt.inputs.cost = cost    # mutual information is the best option for cost function

    result = flirt.run()
    print(f"Registered image saved to {registered_image_path}")
    print(f"Transform matrix saved to {transform_matrix_path}")


# CODE TESTING:

if __name__ == '__main__':
    fixed_image_path = '/Users/arman/projects/register_image/data/nifti/fixed.nii.gz'
    moving_image_path = '/Users/arman/projects/register_image/data/nifti/moving.nii.gz'
    output_image_path = '/Users/arman/projects/register_image/data/nifti/moving_registered.nii.gz'
    transform_matrix_path = '/Users/arman/projects/register_image/data/nifti/transform.mat'

    register_images_rigid(fixed_image_path, moving_image_path, output_image_path, transform_matrix_path)
