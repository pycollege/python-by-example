import subprocess
import sys


result = subprocess.run(["echo", "hello"], capture_output=True, text=True)
print(result.stdout.strip())
print(result.returncode)


# check_output captures stdout; stderr=STDOUT merges stderr into it
version = subprocess.check_output(
    [sys.executable, "--version"], text=True, stderr=subprocess.STDOUT
)
print(version.strip())


# check=True raises CalledProcessError on non-zero exit
try:
    subprocess.run(["false"], check=True)
except subprocess.CalledProcessError as e:
    print(f"Command failed with exit code {e.returncode}")


output = subprocess.check_output(["echo", "captured"], text=True)
print(output.strip())
