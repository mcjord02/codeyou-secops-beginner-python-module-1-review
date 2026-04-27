with open("logins.txt") as f:
    lines = f.readlines()

print(f"Loaded {len(lines)} login records.")

successful_logins = 0
failed_logins = 0
internal_ips = 0
external_ips = 0
failure_tracker = {}

for line in lines:
    parts = line.strip().split()
   
    if len(parts) < 3: continue
    username, ip, result = parts[0], parts[1], parts[2]
    if ip.startswith("10.") or ip.startswith("192.168."):
        ip_type = "Internal"
        internal_ips += 1
    else:
        ip_type = "External"
        external_ips += 1
    print(f"User: {username}, IP: {ip}, Result: {result}")

    if parts[2] == "FAILURE":
        failed_logins += 1
    else:
        successful_logins += 1
    

print("========================================")
print(f"Total processed logins: {successful_logins + failed_logins}")
print(f"Total successful logins: {successful_logins}")
print(f"Total failed logins: {failed_logins}")
print(f"Internal IP logins: {internal_ips}")
print(f"External IP logins: {external_ips}")
