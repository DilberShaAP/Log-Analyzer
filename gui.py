import tkinter as tk
from tkinter import filedialog, scrolledtext
from analyzer import analyze_log
def load_file():
    global file_path
    file_path=filedialog.askopenfilename()
    output_box.insert(tk.END,f"\nLoaded file:{file_path}\n")
def run_analysis():
    output_box.delete(1.0,tk.END)
    results=analyze_log(file_path)
    for line in results:
        if "[ALERT]" in line:
            output_box.insert(tk.END,line+"\n","alert")
        elif "[WARNING]" in line:
            output_box.insert(tk.END,line+"\n","warning")
        else:
            output_box.insert(tk.END,line+"\n","info")
def export_report():
    with open("reports/report.txt","w") as f:
        f.write(output_box.get(1.0,tk.END))
    output_box.insert(tk.END,"\nReport exported to reports/report.txt\n")
root=tk.Tk()
root.title("SIEM Dashboard")
root.geometry("700x500")
root.configure(bg="#0f172a")
file_path="sample_logs.txt"
title=tk.Label(root,text="SOC Log Analyzer",fg="white",bg="#0f172a",font=("Arial", 18))
title.pack(pady=10)
btn_frame=tk.Frame(root,bg="#0f172a")
btn_frame.pack()
load_btn=tk.Button(btn_frame,text="Load Log File",command=load_file)
load_btn.grid(row=0,column=0,padx=5)
analyze_btn=tk.Button(btn_frame,text="Analyze",command=run_analysis)
analyze_btn.grid(row=0,column=1,padx=5)
export_btn=tk.Button(btn_frame,text="Export Report",command=export_report)
export_btn.grid(row=0,column=2,padx=5)
output_box=scrolledtext.ScrolledText(root,width=80,height=20,bg="black",fg="white")
output_box.pack(pady=10)
output_box.tag_config("alert",foreground="red")
output_box.tag_config("warning",foreground="orange")
output_box.tag_config("info",foreground="lightgreen")
root.mainloop()
 