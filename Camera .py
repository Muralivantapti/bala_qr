import cv2
def scan_qr():
    camera = cv2.VideoCapture(0)
    qr_decoder = cv2.QRCodeDetector()

    while True:
        ret, frame = camera.read()
        decoded_data, points, _ = qr_decoder.detectAndDecode(frame)

        if points is not None:
            if decoded_data:
                print("QR Code Scanned:", decoded_data)
                return decoded_data

        if cv2.waitKey(1) == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()
