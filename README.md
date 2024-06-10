# ScreenRipper

## Project Structure

ScreenRipper/
├── src/
│ ├── capture.py # Functions related to screen capturing.
│ ├── ocr.py # Functions related to Optical Character Recognition.
│ ├── filter.py # Functions to filter out questions or important info.
│ └── main.py # Main script to tie all functionalities together.
│
├── assets/ # Store any static files, icons, etc.
│
├── logs/
│ ├── errors.log # Logging any errors or issues.
│ └── activity.log # Logging general activities or useful debug info.
│
├── notes/
│ └── notes.txt # Storing the extracted notes.
│
├── tests/
│ ├── test_capture.py # Unit tests for capture functionalities.
│ ├── test_ocr.py # Unit tests for OCR functionalities.
│ └── test_filter.py # Unit tests for filtering functions.
│
├── .gitignore # Ignoring unnecessary files/dirs from Git.
├── README.md # Project documentation, setup instructions.
└── requirements.txt # Required Python libraries.


## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ScreenRipper.git
   cd ScreenRipper
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
  source venv/bin/activate   # On Windows use `venv\Scripts\activate`

3. Install the required dependencies:
      ```bash
      pip install -r requirements.txt


## Usage
Run the main script to start the application:
      ```bash
      python src/main.py


## Directory Descriptions
src/: Contains the main source code for the application.

capture.py: Functions related to screen capturing.
ocr.py: Functions related to Optical Character Recognition.
filter.py: Functions to filter out questions or important information.
main.py: Main script to tie all functionalities together.
assets/: Directory to store any static files, icons, etc.

logs/: Contains log files.

errors.log: Logging any errors or issues.
activity.log: Logging general activities or useful debug information.
notes/: Directory to store extracted notes.

notes.txt: File storing the extracted notes.
tests/: Contains unit tests for the application.

test_capture.py: Unit tests for capture functionalities.
test_ocr.py: Unit tests for OCR functionalities.
test_filter.py: Unit tests for filtering functions.
.gitignore: File specifying which files and directories to ignore in the Git repository.

README.md: Project documentation and setup instructions.

requirements.txt: List of required Python libraries.

## Contributing
  Fork the repository.
  Create your feature branch (git checkout -b feature/AmazingFeature).
  Commit your changes (git commit -m 'Add some AmazingFeature').
  Push to the branch (git push origin feature/AmazingFeature).
  Open a Pull Request.
# License
This project is licensed under the MIT License.


