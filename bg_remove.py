from google.colab import drive
drive.mount('/content/drive')

from PIL import Image
from rembg import remove

def load_image_from_drive(image_path):
    """
    Load an image from Google Drive.
    
    Parameters:
    - image_path: str, path to the image file in Google Drive.
    
    Returns:
    - image: PIL Image, the loaded image.
    """
    image = Image.open(image_path)
    return image

def remove_background(image):
    """
    Remove the background from the provided image.
    
    Parameters:
    - image: PIL Image, the input image.
    
    Returns:
    - output: PIL Image, the image with the background removed.
    """
    output = remove(image)
    return output

def save_image_to_drive(image, output_path):
    """
    Save the image to Google Drive.
    
    Parameters:
    - image: PIL Image, the image to save.
    - output_path: str, path to save the image in Google Drive.
    """
    image.save(output_path)

def main():
    # Define the paths
    input_path = "/content/drive/MyDrive/Colab Notebooks/Intel_logo.jpg"  # Replace with your image file path in Google Drive
    output_path = "/content/drive/MyDrive/Colab Notebooks/Intel_output.png"  # Desired output file path in Google Drive

    # Load the image
    image = load_image_from_drive(input_path)

    # Remove the background
    image_no_bg = remove_background(image)

    # Save the output image
    save_image_to_drive(image_no_bg, output_path)

    print(f"Background removed and saved to {output_path}")

if __name__ == "__main__":
    main()
