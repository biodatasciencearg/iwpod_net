### Install
#### 01. Create wheel.

````
python setup.py bdist_wheel

````

#### 02. Install from wheel.

````
pip install .\dist\iwpodnet-0.1-py3-none-any.whl
````

#### 03. Test

````
import cv2
from iwpodnet.detector import *

# Instantiate net
detector = IwpodNet()

# Load test image.
 frame = cv2.imread("002.jpg")

#  Get List of Regions Of Interest (ROI).
roi = a.get_roi(frame)

# Save The first ROI
cv2.imwrite('roi_best.jpg',roi[0])

````