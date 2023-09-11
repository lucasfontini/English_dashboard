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
    def run(self, cpe, user, password, port ):
        client = mikrotik_connect(cpe, user,  password, port)

        commands = ['/system script remove [find name=ztp_fetch]',
            '/system script remove [find name=static_ip]',
            '/ip route remove [find dst-address=0.0.0.0/0 distance=10 gateway=ether1]',
            '/interface ethernet set 0 arp=enable',
            '/system script remove [find name=dhcp_ip]',
            '/system scheduler remove [find name=find_wan_ip]',
            '/system script remove [find name=remove_defaultcfg]',
            '/interface l2tp-client remove [find name=l2tp-ztp-cpe]']
        
        for command in commands:
            output = run_command(client, command)
            
        return output
