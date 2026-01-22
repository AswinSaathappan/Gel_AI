import cv2
import numpy as np

def analyze_band_reason(bands_img):
    """
    bands_img: binary band image (output of image_processing)
    """

    # Count connected components (bands)
    num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(
        bands_img, connectivity=8
    )

    # Remove background label
    band_count = num_labels - 1  

    reasons = []

    # Simple logic (you can tune numbers later)
    if band_count > 4:
        reasons.append("Extra band detected")
    elif band_count < 2:
        reasons.append("Missing band pattern")

    # Intensity variation
    intensity_std = np.std(bands_img)
    if intensity_std > 60:
        reasons.append("Uneven band intensity")

    if not reasons:
        reasons.append("Normal band pattern")

    return band_count, reasons
