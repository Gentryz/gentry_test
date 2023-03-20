

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

if __name__ == '__main__':
    print(hex_to_rgb("FFFFFF"))
    print(rgb_to_hex((178, 178, 183)))