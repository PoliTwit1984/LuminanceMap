# Luminance Map Generator

A Flask web application that converts images into luminance maps with a modern, user-friendly interface. The application provides a visual representation of image luminance using a color-coded mapping system.

## Features

- Modern, minimalist interface with energetic colors
- Drag-and-drop file upload functionality
- Support for PNG, JPG, JPEG, and GIF formats
- Real-time image processing with loading indicator
- Color-coded luminance mapping
- Scale bar showing luminance values
- Download functionality for processed images
- Responsive design for various screen sizes

## Prerequisites

- Python 3.12 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone [your-repository-url]
cd LuminanceMap
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install flask pillow numpy
```

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://127.0.0.1:5000
```

3. Use the application:
   - Drag and drop an image onto the upload area, or click "Choose File" to select an image
   - Click "Generate Luminance Map" to process the image
   - View the original and processed images side by side
   - Use the "Download Result" button to save the processed image
   - Click "Process Another Image" or the close button to return to the upload page

## How It Works

The application uses the following process to generate luminance maps:

1. Converts the uploaded image to grayscale to obtain luminance values
2. Maps luminance values (0-255) to a color spectrum using 25 distinct colors
3. Creates a scale bar showing the luminance-to-color mapping
4. Combines the processed image with the scale bar for reference

The color mapping ranges from dark blue (low luminance) through cyan, green, yellow, to red (high luminance).

## Project Structure

```
LuminanceMap/
├── app.py              # Main Flask application
├── lumap2.py          # Luminance mapping logic
├── templates/         # HTML templates
│   ├── upload.html    # Upload page template
│   └── result.html    # Results page template
├── uploads/           # Directory for uploaded images
├── requirements.txt   # Project dependencies
└── README.md         # Project documentation
```

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Flask web framework
- Pillow (PIL) for image processing
- NumPy for numerical operations
