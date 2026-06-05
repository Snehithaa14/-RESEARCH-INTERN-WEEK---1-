devices = ["Device1", "Device2", "Device3", "Device4", "Device5"]
print("Available Devices:")
for device in devices:
    print(device)
def send_packet(source, destination):
    print(f"Packet sent from {source} to {destination}")
send_packet("Device1", "Device5")
