# Phishing URL Detector

A Python project that uses the Google Safe Browsing API to detect potentially dangerous URLs, including phishing, malware, and unwanted software links.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/phishing-url-detector.git
   cd phishing-url-detector
   
2.  Install the required packages
    pip install -r requirements.txt
3.  Replace .env.example to .env 
4.  In the .env file ensure you use a valid GOOGLE API Key
    Go to google cloud console
    sign in and create new project
    go to nav menu (3 lines)
    select APIs & Services and then click library
    Search for "Safe Browsing API" and select it
    Enable the api
    go back to the nav menu and go to API&Services > Credentials 
    Click on create credentials and select API Key
    Copy your key into the .env file 
5. Run the script to check URL for phishing
   example run 
   Enter the URL to check: http://example.com
   output: The URL is not flagged by Google Safe Browsing.
6. Test with google examples or phishing links you know 
example : http://malware.testing.google.test/testing/malware/


