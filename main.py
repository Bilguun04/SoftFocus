from PIL import Image, ImageFilter

def blur_image(image_path, output_path, radius=2):
    # Open the image
    image = Image.open(image_path)
    
    # Apply Gaussian blur
    blurred_image = image.filter(ImageFilter.GaussianBlur(radius))
    
    # Save the blurred image
    blurred_image.save(output_path)
    print("Image blurred and saved successfully!")

if __name__ == "__main__":
    input_image_path = "input_image.jpg"
    output_image_path = "blurred_image.jpg"
    blur_image(input_image_path, output_image_path)
