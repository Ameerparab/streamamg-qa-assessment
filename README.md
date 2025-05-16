My Approach and Technical Decisions
Programming Language & Framework :
- Python is Chosen for its readability, extensive libraries and strong community support for testing.
- Pytest selected as the test automation framework due to its simplicity, powerful fixtures, excellent reporting capabilities and extensibility.
- Requests
- Pytest-html for HTML reports

Folder Structure 
streamamg-qa-assessment/
├── .venv/                     # Python virtual environment (excluded in .gitignore)
├── src/                       # Main source directory
│   ├── config/                # Configuration files
│   │   └── settings.py        # Holds constants or settings like base URLs
│   ├── tests/                 # All test cases
│   │   |── api_tests/         # Test cases for API
│   │   |   └── test_api.py    # Example test verifying API connectivity
|   |   └── streaming_test/    # Test cases for Streaming as of now no test has been developed
│   └── utils/                 # Utility/helper functions
│       └── api_client.py      # Handles API interactions (GET, POST, etc.) 
├── .gitignore                 
├── ai_usage.md                # ai usage
├── assumptions.md             # Any assumptions made while building or testing
├── conftest.py                # Global fixtures or path setup (e.g. adds src to python path)
├── pytest.ini                 # Pytest configuration file (e.g. markers, paths)
├── README.md                  # Project overview, setup, and execution instructions
├── requirements.txt           # List of Python dependencies (e.g. requests, pytest)
└── test_strategy.md           # test strategy for streaming video 

Modular Structure: Tests are organized by functionality (api_tests, streaming_tests) to improve maintainability and readability.
src/utils: Contains reusable components like API clients and configuration management, promoting code reuse and reducing duplication.

Parameterization: Leveraged where applicable to test various scenarios efficiently (e.g., different devices/resolutions).

Due to the time constraint, I have focused on demonstrating one test_api aspects:
Streaming Test: As of now, no scripts have been developed for this.

No UI Automation: Given the focus on API and streaming backend/functional aspects, and the time limit, UI automation (e.g., Selenium/Playwright) was excluded from the implementation.
No Complex Error Handling: The implemented tests include basic assertions for success/failure, but robust.

### Steps for download and execution 

### 1. Clone the repo

```bash
git clone https://github.com/Ameerparab/streamamg-qa-assessment.git
cd streamamg-qa-assessment
```

### 2. Create & activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate     # On Linux/macOS
.venv\Scripts\activate        # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Tests

```bash
 pytest 
 Or with HTML report:
 pytest --html=report.html   # This will generate a file named report.html in the root directory. You can open it in a browser to view the test summary.
```


