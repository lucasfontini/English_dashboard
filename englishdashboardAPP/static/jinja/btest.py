import sys
import paramiko
from st2common.runners.base_action import Action




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
    def run(self, cpe, user, password, port , ip_pop , service_id):
        client = mikrotik_connect(cpe, user,  password, port)
        output = run_command(client,f"/ping {ip_pop} count=50 interval=0.3 ; /tool bandwidth-test  {ip_pop} duration=30s direction=both protocol=tcp")
        return {f'{service_id}':output}