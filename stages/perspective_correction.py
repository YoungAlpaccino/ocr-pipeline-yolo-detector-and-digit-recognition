"""
Perspective correction (sketch).

Computes the homography from the detected corners to a canonical
rectangle and warps the image into it.
"""


CANONICAL_W = 1024
CANONICAL_H = 640


def correct_perspective(img, corners):
    """Stub: real impl is `cv2.getPerspectiveTransform` + `cv2.warpPerspective`."""
    return img
