import pydicom
import png
import numpy as np
import os
 
def convert_to_png(file):
    ds = pydicom.dcmread(file)

    shape = ds.pixel_array.shape

    # Convert to float to avoid overflow or underflow losses.
    image_2d = ds.pixel_array.astype(float)

    # Rescaling grey scale between 0-255
    image_2d_scaled = (np.maximum(image_2d,0) / image_2d.max()) * 255.0

    # Convert to uint
    image_2d_scaled = np.uint8(image_2d_scaled)

    # Write the PNG file
    with open(f'{file.strip(".dcm")}.png', 'wb') as png_file:
        w = png.Writer(shape[1], shape[0], greyscale=True)
        w.write(png_file, image_2d_scaled)

if __name__ == '__main__':
    for root, dirs, files in os.walk(r'C:\Users\83549\OneDrive\Documents\Research Data\manifest-vKOJztmv4854774228398238645\IvyGAP'):
        for file in files:
            if '.dcm' in file:
                convert_to_png(os.path.join(root, file))
                print(f"Successful:{file}")
