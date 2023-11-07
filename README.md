# ScreenRipper
│
├── src/
│   ├── capture.py       # Functions related to screen capturing.
│   ├── ocr.py           # Functions related to Optical Character Recognition.
│   ├── filter.py        # Functions to filter out questions or important info.
│   └── main.py          # Main script to tie all functionalities together.
│
├── assets/              # Store any static files, icons, etc.
│
├── logs/
│   ├── errors.log       # Logging any errors or issues.
│   └── activity.log     # Logging general activities or useful debug info.
│
├── notes/
│   └── notes.txt        # Storing the extracted notes.
│
├── tests/
│   ├── test_capture.py  # Unit tests for capture functionalities.
│   ├── test_ocr.py      # Unit tests for OCR functionalities.
│   └── test_filter.py   # Unit tests for filtering functions.
│
├── .gitignore           # Ignoring unnecessary files/dirs from Git.
├── README.md            # Project documentation, setup instructions.
└── requirements.txt     # Required Python libraries.
