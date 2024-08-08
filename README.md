# NOLA-AI-project

This repo contains a proof of concept to extract the name and the expiration date from an image of a driver's license. 

## Requirements

Refer to `requirements.txt` for all the packages used

## Technologies

Pytesseract - OCR

openCV - Image Processing

regEx - String Processing

## Library

Two scripts in the library contain functions for image_processing and extracting strings from images

### `image_processing`

##### Functions

`read_img`: Reads an image from a file.

`normalize_img`: Normalizes the image into a numpy array for opencv processing

`remove_noise`: Applies noise reduction to the image to clean it up.

`get_grayscale`: Converts the image to grayscale.

`thresholding`: Applies Otsu's thresholding to the image. This function needs more testing as it didn't result in a better output for the OCR

`binarization`: Applies binary thresholding to the image. This function needs more testing as it didn't result in a better output for the OCR

`preprocess_image`: Preprocesses the image by reading, normalizing, removing noise, and converting to grayscale.

`img_to_text`: Converts the image to text using Tesseract OCR.

### `extractor`

##### Functions

`combined_parser`: Parses the text to extract names using a digit-based identifier or an address-based pattern and cleans the resulting string.

`parse_name_address`: Uses a regex pattern to detect and extract lines starting with numbers (assumed to be addresses) and retrieves the two preceding strings.

`parse_name_identifier`: Uses a regex pattern to find lines that start with digits (most driver licenses have the fields 1 and 2 to identify names) followed by a name and returns the extracted names.

`clean_string`: Removes commas and extra spaces from the input string.

`check_if_valid`: Extracts dates from the text and checks if they are valid or expired.

`get_dates`: Finds dates in the text using a regex pattern.

`parse_date`: Parses a date string using a list of possible date formats.

`isValid`: Checks if the extracted dates are valid by comparing them to the current date.

### Contact

If you have any questions feel free to contact me at ali.rashid24a@gmail.com :)
 
