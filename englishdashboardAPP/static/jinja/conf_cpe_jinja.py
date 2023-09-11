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
    def run(self, cpe, user, password, port, configuration, server_backup , path , user_destination , pass_destination , port_host_destination, service_id ):

        if configuration:
            client = mikrotik_connect(cpe, user, password, port)
            if client is not None:
                output = run_command(client, configuration)
                print(output)
                with open(f"/{service_id}.cfg", "w") as arquivo:
                    arquivo.write(configuration)
                    client = mikrotik_connect(server_backup, user_destination, pass_destination, port_host_destination)
                    scp = client.open_sftp()
                    print(f"{service_id}.cfg")
                    scp.put(f"/{service_id}.cfg", path)
                    print(scp)
                return f'device configured'

                