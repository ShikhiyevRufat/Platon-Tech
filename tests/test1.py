import cv2
import numpy as np

image = cv2.imread("wro_map.jpg")
if image is None:
    print("Şəkil tapılmadı. Fayl adını və yolunu yoxlayın.")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    binary_adaptive = cv2.adaptiveThreshold(
        gray, 
        255, 
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY_INV, 
        15,  
        5 
    )

    kernel_size = 5
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    
    dilated = cv2.dilate(binary_adaptive, kernel, iterations=2)
    
    closed = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel, iterations=3)

    lines = cv2.HoughLinesP(
        closed, 
        rho=1, 
        theta=np.pi / 180, 
        threshold=50, 
        minLineLength=80, 
        maxLineGap=5
    )

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, 245, 255, cv2.THRESH_BINARY)

    result_image = image.copy()
    result_image[mask == 255] = [0, 0, 0]

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(result_image, (x1, y1), (x2, y2), (255, 255, 255), 2) 

    cv2.imshow("Orginal Map:", image)
    cv2.imshow("Map with line:", result_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()