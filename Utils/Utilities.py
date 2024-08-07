import base64


def convert_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        image_base64 = base64.b64encode(image_file.read()).decode("utf-8")
    return image_base64


def find_nth_true(boolean_list, n):
    count = 0
    for i, value in enumerate(boolean_list):
        if value:
            count += 1
            if count == n:
                return i
    return 0
