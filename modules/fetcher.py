import requests
import cv2
import numpy as np
import time

def check_camera(ip):
    test_url = f"http://{ip}/shot.jpg"
    try:
        r = requests.get(test_url, timeout=3)
        if r.status_code == 200 and 'image' in r.headers['Content-Type']:
            return True
    except:
        pass
    return False

def save_snapshot(ip):
    url = f"http://{ip}/shot.jpg"
    r = requests.get(url, stream=True)
    img_array = np.asarray(bytearray(r.content), dtype=np.uint8)
    img = cv2.imdecode(img_array, -1)
    filename = f"results/snapshots/{ip.replace('.', '_')}.jpg"
    cv2.imwrite(filename, img)
    print(f"[+] Saved snapshot from {ip}")
  
