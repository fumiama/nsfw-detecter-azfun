import skimage.transform


def transform_and_pad_image(
    image,
    target_width,
    target_height,
    order=1,
    mode="edge",
):
    """
    Transform image and pad by edge pixles.
    """
    image_width = image.shape[1]
    image_height = image.shape[0]
    image_array = image

    # centerize
    t = skimage.transform.AffineTransform(
        translation=(-image_width * 0.5, -image_height * 0.5)
    )

    t += skimage.transform.AffineTransform(
        translation=(target_width * 0.5, target_height * 0.5)
    )

    warp_shape = (target_height, target_width)

    image_array = skimage.transform.warp(
        image_array, (t).inverse, output_shape=warp_shape, order=order, mode=mode
    )

    return image_array
