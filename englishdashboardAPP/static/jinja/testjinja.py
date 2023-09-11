from jinja2 import Template
import os

if os.path.exists("englishdashboard\englishdashboardAPP\static\jinja\conf.j2"):
    with open("englishdashboard\englishdashboardAPP\static\jinja\conf.j2") as f:
        template_str = f.read()
else:
    print("Template jinja not found! check the file or path ")

template = Template(template_str)

variables = {
    'SERVICE_ID' : 'FON-5511-D001',
    'SERVICE_TEST': "vzb.55.11.55",
}

output = template.render(**variables)
print(output)



