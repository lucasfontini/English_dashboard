import sys
# import paramiko
import os
# # from st2common.runners.base_action import Action
# from jinja2 import Template


# SERVICE_ID = 'fon55'
# PRIVATE_IP_IGN_CPE= '10.10.10.10'
# PUBLIC_IP_CUSTOMER_BLOCK= '200.200.200.200'
# PROFILE_L2TP_POP= 'profile-TEST'
# PRIVATE_IP_IGN_POP ='10.10.10.1' 

# if os.path.exists("englishdashboard\englishdashboardAPP\static\jinja\conf.j2"):
#     with open("englishdashboard\englishdashboardAPP\static\jinja\conf.j2") as f:
#         template_str = f.read()
# else:
#     print("Arquivo test.j2 não encontrado.")

# template = Template(template_str)

# vars = {
#     'SERVICE_ID':SERVICE_ID,
#     'PRIVATE_IP_IGN_POP':PRIVATE_IP_IGN_POP,
#     'PRIVATE_IP_IGN_CPE':PRIVATE_IP_IGN_CPE,
#     'PUBLIC_IP_CUSTOMER_BLOCK':PUBLIC_IP_CUSTOMER_BLOCK,
#     'PROFILE_L2TP_POP':PROFILE_L2TP_POP
# }


# output = template.render(**vars)
# print(type(output))

# with open("output.rsc", "w") as file:
#     file.write(output)
# print(output)
BASEDIR = os.path.abspath(os.path.dirname(__file__))
print(BASEDIR+'/conf.j2')