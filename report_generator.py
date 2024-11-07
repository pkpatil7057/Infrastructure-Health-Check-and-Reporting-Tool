from jinja2 import Template
from datetime import datetime
import json
import pdfkit

def load_report_template():
    template_str = """
    <html>
    <head><title>Health Check Report</title></head>
    <body>
        <h1>Health Check Report - {{ date }}</h1>
        <h2>Servers</h2>
        <ul>
        {% for server in servers %}
            <li>{{ server.name }} ({{ server.ip }}) - {{ 'UP' if server.status else 'DOWN' }}</li>
        {% endfor %}
        </ul>
        
        <h2>Databases</h2>
        <ul>
        {% for db in databases %}
            <li>{{ db.name }} - {{ 'Connected' if db.status else 'Disconnected' }}</li>
        {% endfor %}
        </ul>
        
        <h2>Endpoints</h2>
        <ul>
        {% for endpoint in endpoints %}
            <li>{{ endpoint.name }} - {{ 'Available' if endpoint.status else 'Unavailable' }}</li>
        {% endfor %}
        </ul>
        
        <h2>System Health</h2>
        <p>CPU Status: {{ 'Healthy' if system_health.cpu_status else 'Unhealthy' }}</p>
        <p>Memory Status: {{ 'Healthy' if system_health.memory_status else 'Unhealthy' }}</p>
    </body>
    </html>
    """
    return Template(template_str)

def generate_report(data):
    template = load_report_template()
    rendered_html = template.render(date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), **data)
    
    with open("report.html", "w") as report_file:
        report_file.write(rendered_html)
    
    # Optional: Convert HTML to PDF
    pdfkit.from_file("report.html", "report.pdf")

if __name__ == "__main__":
    with open("health_check_results.json") as json_file:
        data = json.load(json_file)
        generate_report(data)

