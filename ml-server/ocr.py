import cv2
import pytesseract
import numpy as np

def preprocess_image(image):
    """
    Preprocesses an image for OCR.

    Args:
        image (numpy.ndarray): The image as a NumPy array.

    Returns:
        numpy.ndarray: The preprocessed image.
    """
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Perform morphological operations (optional)
    # kernel = np.ones((3, 3), np.uint8)
    # thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    return thresh

def extract_text_and_highlight(image_path):
    """
    Extracts text from an image and identifies highlighted text.

    Args:
        image_path (str): Path to the image file.

    Returns:
        tuple: A tuple containing the extracted text and a list of highlighted text regions.
    """
    # Load the image
    image = cv2.imread(image_path)

    if image is None:
        print(f"Error: Could not open or find the image at {image_path}")
        return None, []

    # Preprocess the image
    preprocessed_image = preprocess_image(image)

    # Extract text using Pytesseract
    text = pytesseract.image_to_string(preprocessed_image)

    # Identify highlighted text (assuming a specific color or pattern)
    highlighted_text_regions = []
    # Implement your logic here to detect highlighted text
    # For example, you could use color thresholding or edge detection

    return text, highlighted_text_regions

def categorize_text(text, image):
    """
    Categorizes extracted text based on its source (e.g., textbox or label).

    Args:
        text (str): The extracted text.
        image (numpy.ndarray): The original image.

    Returns:
        list: A list of tuples, where each tuple contains the text and its inferred category.
    """

    categorized_text = []
    # Implement your logic here to categorize text based on its source
    # For example, you could use image analysis techniques or machine learning models

    return categorized_text

# Example usage
image_path = "whatsapp ss"  # Provide the path to the image here
text, highlighted_text_regions = extract_text_and_highlight(image_path)

if text is not None:
    categorized_text = categorize_text(text, cv2.imread(image_path))
    print("Extracted text:", text)
    print("Highlighted text regions:", highlighted_text_regions)
    print("Categorized text:", categorized_text)
