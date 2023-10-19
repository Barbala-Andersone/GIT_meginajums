#pip install Pillow
# python -m pip install pip==23.0.1
"""
from PIL import Image 

fails=Image.open("bilde.png")
fails.show()
fails.close()
"""

import os
#os.remove("aste.txt")
if os.path.exists("kaste.txt"):
    os.remove("kaste.txt")
else:
    print("Fails neeksistē!")
