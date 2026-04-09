from datetime import datetime
def analyze_log(file_path):
    results=[]
    failed_attempts={}
    with open(file_path,"r") as file:
        for line in file:
            parts=line.split()
            if len(parts)<6:
                continue
            date=parts[0]
            time=parts[1]
            status=parts[3]
            user=parts[4]
            ip=parts[5]
            timestamp=datetime.strptime(date+" "+time,"%Y-%m-%d %H:%M:%S")
            if status=="FAILED":
                if ip not in failed_attempts:
                    failed_attempts[ip]=[]
                failed_attempts[ip].append(timestamp)
    for ip,times in failed_attempts.items():
        times.sort()
        for i in range(len(times)):
            count=1
            for j in range(i+1,len(times)):
                diff=(times[j]-times[i]).seconds
                if diff<=60:
                    count+=1
                else:
                    break
            if count>=3:
                results.append(f"[ALERT] Brute force attack from {ip}({count}attempts in 1 min)")
                break
        if len(times)>=2:
            results.append(f"[WARNING] Multiple failed attempts from {ip}")
    if not results:
        results.append("[INFO] No suspicious activity detected")
    return results
 