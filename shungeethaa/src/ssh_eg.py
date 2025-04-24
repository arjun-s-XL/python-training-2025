import paramiko

# Define server details
hostname = 'your.remote.server.com'  # Replace with the IP or hostname of the remote server
port = 22                           # Default SSH port
username = 'your_username'          # Replace with your SSH username
password = 'your_password'          # Replace with your SSH password (or use SSH key)

# Create an SSH client
client = paramiko.SSHClient()

# Automatically add the server's SSH key if it's not already in known_hosts
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the remote server
    client.connect(hostname, port=port, username=username, password=password)

    # Run a command on the remote server
    stdin, stdout, stderr = client.exec_command('ls -l')  # Example: list files in the home directory

    # Print the output of the command
    print("Output of the command:")
    print(stdout.read().decode())  # Decode bytes to string

    # Print any error messages
    err = stderr.read().decode()
    if err:
        print("Error:")
        print(err)

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the SSH connection
    client.close()
