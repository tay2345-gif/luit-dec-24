import requests
import yaml
import time
import sys
from collections import defaultdict

# Function to load the YAML file containing the endpoints
def load_endpoints(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Function to perform the health check for a given endpoint
def check_health(endpoint):
    try:
        # Determine HTTP method (GET or POST) and other parameters
        method = endpoint.get("method", "GET").upper()
        url = endpoint["url"]
        headers = endpoint.get("headers", {})
        body = endpoint.get("body", None)

        # Perform the HTTP request based on the method
        if method == "POST":
            response = requests.post(url, headers=headers, data=body, timeout=5)
        else:  # Default to GET method
            response = requests.get(url, headers=headers, timeout=5)

        # Return True if status code is 200 (success), otherwise False
        return response.status_code == 200

    except requests.RequestException:
        # If any error occurs (e.g., connection error), return False
        return False

# Function to log the cumulative availability percentage for each domain
def log_availability(endpoint_success_counts, endpoint_test_counts):
    for domain, successes in endpoint_success_counts.items():
        tests = endpoint_test_counts.get(domain, 0)
        if tests > 0:
            availability = (successes / tests) * 100
        else:
            availability = 0.0
        print(f"Domain: {domain}, Availability: {availability:.2f}%")

# Function to monitor the health of endpoints every 15 seconds
def monitor_endpoints(file_path):
    endpoints = load_endpoints(file_path)
    
    # Initialize dictionaries to track success and test counts for each endpoint
    endpoint_success_counts = defaultdict(int)
    endpoint_test_counts = defaultdict(int)

    try:
        while True:
            for endpoint in endpoints:
                domain = endpoint["url"].split("//")[-1].split("/")[0]  # Extract domain from URL
                # Check health of the endpoint
                is_healthy = check_health(endpoint)
                
                # Update test count and success count for the domain
                endpoint_test_counts[domain] += 1
                if is_healthy:
                    endpoint_success_counts[domain] += 1

            # Log availability statistics after each 15-second cycle
            log_availability(endpoint_success_counts, endpoint_test_counts)

            # Wait for 15 seconds before the next cycle
            time.sleep(15)
    
    except KeyboardInterrupt:
        print("Monitoring stopped.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python monitor.py <path_to_yaml_file>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    monitor_endpoints(file_path)
