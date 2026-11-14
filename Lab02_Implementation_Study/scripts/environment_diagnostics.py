import sys, platform, subprocess
print("Python:", sys.version)
print("Platform:", platform.platform())
for cmd in ["lscpu | head -20", "free -h", "nvidia-smi"]:
    print("\\n$", cmd)
    subprocess.run(cmd, shell=True)
