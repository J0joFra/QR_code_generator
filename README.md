# QR Code Generator

This project generates a QR code using the `pyqrcode` library. The QR code links to the YouTube channel: [Click HERE](https://www.youtube.com/@jofrancalanci).

## Files

- `QR_code.svg`: This is the generated QR code in SVG format.

## Requirements

- Python 3.x
- `pyqrcode` library

## How to Use

1. **Install the required library**:
    ```bash
    pip install pyqrcode
    ```

2. **Generate the QR Code**:
    The QR code is already generated and saved as `QR_code.svg`. If you want to generate it again or modify the link, run the following Python script:

    ```python
    import pyqrcode

    qr = pyqrcode.create(r"https://www.youtube.com/@jofrancalanci")
    qr.svg('QR_code.svg', scale=10, background="white", module_color="black")
    ```

3. **View the QR Code**:
   You can view the generated QR code by opening the `QR_code.svg` file with any web browser or image viewer that supports SVG format.

## License

This project is licensed under the MIT License.
