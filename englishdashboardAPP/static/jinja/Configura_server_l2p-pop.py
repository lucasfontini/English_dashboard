import sys
import paramiko
from st2common.runners.base_action import Action
from jinja2 import Template
import os


def mikrotik_connect(host, username, password, port):
    try:        
        # Create SSH client
        print(host, username, password, port)
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # Connect to device
        client.connect(host ,username=username , password=password , port=port)
        return client
    except paramiko.ssh_exception.AuthenticationException as e:
        print("Authentication error:", e)
        return None
    except paramiko.ssh_exception.SSHException as e:
        print("Timeout error:", e)
        return None


def run_command(client, command):
    # Execute command
    stdin, stdout, stderr = client.exec_command(command)
    return stdout.read().decode()

class main(Action):
    def run(self, pop, user, password, Path_jinja2 , SOLUTION, PROFILE_L2TP_POP, SERVICE_ID, PRIVATE_IP_IGN_POP, PRIVATE_IP_IGN_CPE, PUBLIC_IP_CUSTOMER_BLOCK, port):
        vars = {
        'PROFILE_L2TP_POP':PROFILE_L2TP_POP,
        'SERVICE_ID':SERVICE_ID,
        'PRIVATE_IP_IGN_POP':PRIVATE_IP_IGN_POP,
        'PRIVATE_IP_IGN_CPE':PRIVATE_IP_IGN_CPE,
        'PUBLIC_IP_CUSTOMER_BLOCK':PUBLIC_IP_CUSTOMER_BLOCK,
        }

        if os.path.exists(Path_jinja2):
            with open(Path_jinja2) as f:
                template_str = f.read()
                template = Template(template_str)
        else:
            print("File .j2 was not found, check the path ")

        try:
            if SOLUTION == 'l2tp-v3':
                client = mikrotik_connect(pop, user, password, port)
                if client is not None:
                    output = run_command(client,template.render(**vars))
                    print(output)
                    return f'device configured'
        except:
            sys.stderr.write("An error has occurred and the config was not apllied")

