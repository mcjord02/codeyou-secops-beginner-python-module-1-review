with open("logins.txt") as f:
    lines = f.readlines()

print(f"Loaded {len(lines)} login records.")

successful_logins = 0
failed_logins = 0

for line in lines:
    parts = line.strip().split()
   
    if len(parts) < 3: continue
    username, ip, result = parts[0], parts[1], parts[2]
    print(f"User: {username}, IP: {ip}, Result: {result}")

    if parts[2] == "FAILURE":
        failed_logins += 1
    else:
        successful_logins += 1
print(f"Total processed logins: {successful_logins + failed_logins}")
print(f"Total successful logins: {successful_logins}")
print(f"Total failed logins: {failed_logins}")