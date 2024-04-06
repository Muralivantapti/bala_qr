import qrcode
import cv2

# Function to generate QR code for table number
def generate_qr(table_number):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(table_number)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save(f"table_{table_number}_qr.png")

# Function to scan QR code
def scan_qr():
    camera = cv2.VideoCapture(0)
    qr_decoder = cv2.QRCodeDetector()

    while True:
        ret, frame = camera.read()
        decoded_data, points, _ = qr_decoder.detectAndDecode(frame)

        if points is not None:
            # Draw bounding box around the detected QR code
            for i in range(4):
                cv2.line(frame, tuple(points[i][0]), tuple(points[(i + 1) % 4][0]), color=(255, 0, 0), thickness=2)

            if decoded_data:
                print("QR Code Scanned:", decoded_data)
                return decoded_data

        cv2.imshow("QR Scanner", frame)
        if cv2.waitKey(1) == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

# Main function
def main():
    table_number = input("Enter the table number: ")
    generate_qr(table_number)
    print(f"QR code generated for Table {table_number}")

    print("Please scan the QR code with the camera to take orders.")
    scanned_table_number = scan_qr()
    if scanned_table_number == table_number:
        print("Order taking process started for Table", table_number)
        # Add your order taking logic here
    else:
        print("QR code scanned does not match the table number.")

if __name__ == "__main__":
    main()
