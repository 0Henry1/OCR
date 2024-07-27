import pytesseract
import PIL.Image
import cv2

# Specify the path to Tesseract executable if not in PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Configuration for Tesseract OCR
myconfig = r"--psm 6 --oem 3"

# Path to the image (adjust this path to your image file)
image_path = r"C:\Users\shekh\Documents\Projects\OCR\dsp.jpg"

try:
    # Extract text from image using Tesseract OCR
    text = pytesseract.image_to_string(PIL.Image.open(image_path), config=myconfig)
    print("Extracted Text:\n", text)

    # Read image using OpenCV
    img = cv2.imread(image_path)
    height, width, _ = img.shape

    # Perform OCR on the image and get bounding boxes
    boxes = pytesseract.image_to_boxes(img, config=myconfig)

    # Draw bounding boxes on the image
    for box in boxes.splitlines():
        box = box.split(" ")
        img = cv2.rectangle(img, (int(box[1]), height - int(box[2])), (int(box[3]), height - int(box[4])), (0, 255, 0), 2)

    # Display the image with bounding boxes
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Extract text from the image again (optional, as it has already been done)
    text = pytesseract.image_to_string(PIL.Image.open(image_path), config=myconfig)
    print("Extracted Text Again:\n", text)

except PermissionError:
    print("Permission denied: Check the file path and ensure you have read permissions.")
except FileNotFoundError:
    print("File not found: Ensure the file exists at the specified path.")
except Exception as e:
    print(f"An error occurred: {e}")
