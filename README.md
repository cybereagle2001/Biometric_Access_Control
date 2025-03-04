# Biometric Access Control

## Overview
**Biometric Access Control** is a fingerprint recognition system built using OpenCV and machine learning techniques. It compares input fingerprints against a stored database and determines a match based on keypoint descriptors.

This project is based on the old research done by:
- [Kristijan Jankoski](https://github.com/kjanko)
- [Gabriel Oliveira](https://github.com/ogabriel)
- [Sashwat K](https://github.com/sashuu69)
- [Utkarsh Deshmukh](https://github.com/Utkarsh-Deshmukh)

Additionally, deprecated commands and syntax errors from the original model ([python-fingerprint-recognition](https://github.com/kjanko/python-fingerprint-recognition)) have been fixed to ensure compatibility with modern Python and OpenCV versions.

## Features
- Fingerprint preprocessing and enhancement
- Feature extraction using Harris corner detection and ORB descriptors
- Matching system using the BFMatcher algorithm
- Visualization of matching fingerprints
- Automated comparison with a stored fingerprint database

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- OpenCV
- NumPy
- Matplotlib
- scikit-image

### Setup
Clone the repository:
```bash
git clone https://github.com/cybereagle2001/Biometric_Access_Control.git
cd Biometric_Access_Control/recognition_model
```

Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage
To run the fingerprint recognition program, execute the `search.py` script:
```bash
python3 search.py <fingerprint_image>
```
- `<fingerprint_image>`: Path to the fingerprint image you want to check.
- The script will compare the input fingerprint with the database and display the match result.

## Project Structure
```
Biometric_Access_Control/
│── recognition_model/
│   ├── app.py              # Main fingerprint recognition script
│   ├── enhance/            # Image enhancement functions
│   │── database/           # Fingerprint dataset
|   │── search.py           # Main entry point for fingerprint search
│── requirements.txt        # List of dependencies
│── README.md               # Project documentation
```

## Acknowledgments
Special thanks to the original contributors whose research and projects helped shape this implementation.

## License
This project is open-source and available under the MIT License.

