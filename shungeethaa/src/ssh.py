import paramiko

# Setup SSH Client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Automatically add unknown hosts

# Replace with your server details
hostname = 'your.remote.server.com'
username = 'your_username'
password = 'your_password'  # Or use key_filename for key authentication

try:
    # Connect to the remote server
    client.connect(hostname, port=22, username=username, password=password)

    # Run a command on the remote server
    stdin, stdout, stderr = client.exec_command('ls -l')
    output = stdout.read().decode()
    print("Command Output:\n", output)

except paramiko.AuthenticationException:
    print("Authentication failed!")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    client.close()
