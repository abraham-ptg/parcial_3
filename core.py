from subprocess import run

def running_msedge():

    try:
        result = run(["powershell", "-File", "open_msedge.ps1"], 
                     capture_output=True, text=True, timeout=10)
        
        return result.returncode, result.stdout.strip(), result.stderr.strip()
    
    except Exception as e:
        return 1, "", str(e)