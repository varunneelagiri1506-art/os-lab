
import os

print("Parent Process")
print("Parent PID:", os.getpid())

pid = os.fork()

if pid == 0:
    # Child Process
    print("\nChild Process")
    print("Child PID:", os.getpid())

    # Execute Linux ls -l command
    os.execlp("ls", "ls", "-l")

else:
    # Parent waits for child
    os.wait()

    print("\nChild process completed.")

    filename = "sample.txt"

    # Create or open the file
    fd = os.open(
        filename,
        os.O_CREAT | os.O_WRONLY | os.O_TRUNC,
        0o644
    )

    message = "System Calls Simulation using Python\n"
    os.write(fd, message.encode())
    os.close(fd)

    # Open file for reading
    fd = os.open(filename, os.O_RDONLY)
    data = os.read(fd, 1024)
    os.close(fd)

    print("\nFile Contents:")
    print(data.decode())

    print("Parent Process Terminated.")
