This program monitors the health of a list of HTTP endpoints provided in a YAML file. It performs regular checks and calculates the availability percentage for each domain. Here's how it works:

1.Input File:
The program reads a YAML file containing endpoint details like URL, HTTP method, headers, and optional body.
Example: Endpoints for fetch.com and fetchrewards.com.

2.Health Checks:
The program sends HTTP requests to each endpoint every 15 seconds.
An endpoint is marked UP if:
The HTTP response code is in the 200–299 range.
The response time is under 500 milliseconds.
Otherwise, the endpoint is marked DOWN.

3.Availability Tracking:
The program calculates the percentage of successful (UP) requests over the total requests for each domain.

4.Logging:
After each 15-second cycle, the program logs the availability percentage of each domain to the console.

5.Continuous Monitoring:
The program runs indefinitely, monitoring and reporting until manually stopped.
