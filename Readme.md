# Web Application Framework

This repository contains the framework code and drivers for automating the testing of Sause demo applications.

pages : contains the wrapper of selenium methods as per the need of the SauceDemo testing
utils : additional utilities like logger, params json parser, element handler etc.

This repository is a requirement and contains all libraries to execute the testscripts under the test case repo : SauceTestCases

## Prerequisites

- Python 3.8+
- Google Chrome 
- ChromeDriver 
- 
## Setup Instructions

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd WebAppFramework
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Download the appropriate WebDriver (ChromeDriver/GeckoDriver) and place it in the `drivers/` directory.

## Directory Structure

- `framework/`: Contains the framework code organized in Page Object Model.
- `drivers/`: Contains WebDriver executables.
- `requirements.txt`: Python dependencies.
- `setup.py`: Python package setup.

## Usage

To use this framework in your test scripts repository, install it as a package:
```bash
pip install -e /path/to/WebAppFramework
