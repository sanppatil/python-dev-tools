import base64

def base64_decode(input_string):
    input_string_bytes = input_string.encode("UTF-8")
    output_string_bytes = base64.b64decode(input_string_bytes)
    output_string = output_string_bytes.decode("UTF-8")
    return output_string

def base64_encode(input_string):
    input_string_bytes = input_string.encode("UTF-8")
    output_b64_bytes = base64.b64encode(input_string_bytes)
    output_b64_string = output_b64_bytes.decode("UTF-8")
    return output_b64_string