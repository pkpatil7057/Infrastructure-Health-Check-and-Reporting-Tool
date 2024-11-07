# Infrastructure Health Check and Reporting Tool

This project performs regular health checks on infrastructure components (e.g., servers, databases, API endpoints) and generates a report on the status.

## Project Structure

- **health_check.py**: Performs health checks on infrastructure components.
- **config.json**: Stores configuration data like server IPs, ports, and threshold values.
- **report_generator.py**: Generates a report (HTML or PDF) using health check results.
- **tests/test_health_check.py**: Contains test cases for the health check functionality.

## Requirements

- Python 3.x
- requests
- psutil
- jinja2
- reportlab

## Installation

```bash
pip install -r requirements.txt

