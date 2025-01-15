This program monitors the health of HTTP endpoints defined in a YAML file, checks their availability every 15 seconds, and logs the availability percentage for each domain.

Features

- Supports HTTP methods (GET, POST) and custom headers.
- Tracks and logs the availability of each domain over time.
- Lightweight and easy to use.

Prerequisites
1.Python Installation
- Ensure Python 3.7+ is installed.
- Download from python.org if not already installed.
  
2.Required Libraries
- Install dependencies using pip.

Setup Instructions
1. Clone or Download the Repository
Clone using Git:
```bash
git clone <repository_url>
cd <repository_folder>
```
- Or download the ZIP and extract it.
  
2. Install Dependencies
- Run the following command to install required libraries:
```bash
pip install -r requirements.txt
```
- Note: A requirements.txt file containing necessary dependencies (e.g., PyYAML, requests) is included.

Usage
1.Prepare the YAML File

- Create a YAML file with your endpoint details. Example:

```yaml

- name: Example GET request
  url: https://example.com
  headers:
    user-agent: health-checker
- name: Example POST request
  url: https://example.com/api
  method: POST
  headers:
    content-type: application/json
  body: '{"key": "value"}'
```

2.Run the Program

- Use the following command, replacing config.yaml with the path to your YAML file:
```bash
python health_checker.py config.yaml
```

3.View Logs
- The program will output the availability percentage for each domain every 15 seconds.

Stopping the Program
- To stop monitoring, press Ctrl + C (Windows/Linux) or Cmd + C (Mac).
Example Output:

```yaml
Domain: example.com, Availability: 100.00%
Domain: example.org, Availability: 97.50%
```

- This output updates every 15 seconds, showing the cumulative availability percentage for each domain.

Troubleshooting
1.Missing Libraries:
- If you encounter a ModuleNotFoundError, ensure dependencies are installed:

```bash
pip install -r requirements.txt
```

YAML File Issues:

- Ensure your YAML file is correctly formatted.
- Verify all required fields (name, url) are present.
Connectivity Problems:

Check your network connection and the accessibility of the provided endpoints.
