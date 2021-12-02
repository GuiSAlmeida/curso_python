import subprocess

# Linx - ping 127.0.0.1 -c 4

proc = subprocess.run(
    ['ping', '127.0.0.1', '-c', '4'],
    capture_output=True,
    text=True
)

print(proc.stderr)
print(proc.returncode)
print(proc.args)
print(proc.stdout)
