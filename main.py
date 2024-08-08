from Library.image_processing import preprocess_image, img_to_text
from Library.extractor import combined_parser, check_if_valid
from glob import glob

def main(img):
    img_name = img.split('/')[-1]
    print(f'Run with {img_name}')
    pro_img = preprocess_image(img)
    ocr_text = img_to_text(pro_img)
    
    extracted_names = combined_parser(ocr_text)
    print(f'{extracted_names}')
    is_valid = check_if_valid(ocr_text)

    return

# Main Method

if __name__ == "__main__":
    images = glob('Data\*')
    for i in images:
        main(i)