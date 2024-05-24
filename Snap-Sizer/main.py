import cv2

# Get the image file path from the user
# image_path = input("Please enter the path to the image file: ")

# Read the image from the provided path
src = cv2.imread('coding_image.jpg', cv2.IMREAD_UNCHANGED)

# Check if the image was successfully loaded
if src is None:
    print("Error: Unable to load image. Please check the file path.")
else:
    # Display the original image
    cv2.imshow("Original Image", src)

    # Percent by which the image is resized
    scale_percent = 50

    # Calculate the 50 percent of original dimensions
    width = int(src.shape[1] * scale_percent / 100)
    height = int(src.shape[0] * scale_percent / 100)

    # dsize --> tuple
    dsize = (width, height)

    # Resize the image
    output = cv2.resize(src, dsize)

    # Save the resized image
    output_path = 'new_image.png'
    cv2.imwrite(output_path, output)

    # Display the resized image
    cv2.imshow("Resized Image", output)

    print(f"The resized image has been saved as {output_path}")

    # Wait for a key press and close the image windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
