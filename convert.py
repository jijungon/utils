import json

example_data = {
    'status': 200,
    'message': 'OK',
    'body': {
        'cid': '0x671abe',
        'nid': '0x7654',
        'channel': 'icon_dex',
        'state': 'started',
        'height': 6410,
        'lastError': ''
    }
}

def to_json(data):
    """
    Convert dictionary to JSON format.
    
    Args:
    - data (dict): Dictionary to convert.
    
    Returns:
    - str: JSON formatted string.
    """
    return json.dumps(data)

def to_raw(data):
    """
    Convert dictionary to raw format (string representation).
    
    Args:
    - data (dict): Dictionary to convert.
    
    Returns:
    - str: Raw string representation of the dictionary.
    """
    return str(data)

# JSON으로 변환
print(type(example_data)) # dict
print(example_data["status"])
print(example_data["body"]["nid"])

json_data = to_json(example_data)
print("JSON format:")
print(json_data)
print(json_data[0])
print(type(json_data))

# raw 데이터로 변환
raw_data = to_raw(example_data)
print("\nRaw format:")
print(raw_data)
print(type(raw_data))
print(raw_data[1])