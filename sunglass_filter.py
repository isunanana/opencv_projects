img = cv2.imread("girl2.jpg")

sunglasses = cv2.imread("sunglasses.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

eye = l_eye_classifier.detectMultiScale(gray, 1.3, 9)
for (x, y, w, h) in eye:
    if h > 0 and w > 0:
        h, w = int(3 * h), int(4.5 * w)
        y -= 30
        x -= 130

        # Once again pay attention that here(x,y,h,w)is not alaways the face, but in this case this is the postiton of the left eye
        img_roi = img[y:y + h, x:x + w]

        sunglasses_small = cv2.resize(sunglasses, (w, h), interpolation=cv2.INTER_AREA)
        gray_sunglasses = cv2.cvtColor(sunglasses_small, cv2.COLOR_BGR2GRAY)

        ret, mask = cv2.threshold(gray_sunglasses, 230, 255, cv2.THRESH_BINARY_INV)
        mask_inv = cv2.bitwise_not(mask)
        masked_face = cv2.bitwise_and(sunglasses_small, sunglasses_small, mask=mask)

        masked_frame = cv2.bitwise_and(img_roi, img_roi, mask=mask_inv)
        img[y:y + h, x:x + w] = cv2.add(masked_face, masked_frame)

cv2_imshow(img)