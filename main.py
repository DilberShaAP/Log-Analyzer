log_file="sample_logs.txt"
failed_logins={}
successful_logins={}
with open(log_file,"r") as file:
   for line in file:
       parts=line.split()
       if len(parts)<6:
           print("Skipping invalid line:",line)
           continue
       status=parts[3]
       user=parts[4]
       ip=parts[5]
       if status=="FAILED":
           failed_logins[ip]=failed_logins.get(ip,0)+1
       if status=="SUCCESS":
           successful_logins[user]=successful_logins.get(user,0)+1

print("\n=== Failed Login Report ===")
for ip,count in failed_logins.items():
   print(f"{ip}→{count} failed attempts")
   if count>=3:
       print(f"[ALERT] Possible brute force attack from {ip}")
print("\n=== Successful Login Report ===")
for user,count in successful_logins.items():
   print(f"{user}→{count} successful logins")