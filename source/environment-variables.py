import os

# Safe read with default
home = os.environ.get("HOME", os.environ.get("USERPROFILE", "/unknown"))
print("HOME:", home)

# Get PATH
path = os.environ.get("PATH", "")
print("PATH has", len(path.split(os.pathsep)), "entries")

# Set for current process
os.environ["MY_VAR"] = "hello"
print("MY_VAR:", os.environ.get("MY_VAR"))
