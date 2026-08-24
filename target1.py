import subprocess

def check_host_alive(hostname):
    """Checks if a host responds to ping."""
    command = f"ping -n 1 {hostname}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.returncode == 0