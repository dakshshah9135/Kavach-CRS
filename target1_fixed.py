import subprocess

import platform



def check_host_alive(hostname):

    """Checks if a host responds to ping."""

    if platform.system().lower() == 'windows':

        command = ['ping', '-n', '1', hostname]

    else:

        command = ['ping', '-c', '1', hostname]

    result = subprocess.run(command, capture_output=True, text=True)

    return result.returncode == 0
