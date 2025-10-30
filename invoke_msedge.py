"""Invoca navegador a utilizar."""
from subprocess import run, CREATE_NO_WINDOW


def invoke_msedge():
    """Invoca el navegarod Microsoft Edge con la URL adecuada."""
    creationflags = CREATE_NO_WINDOW
    cmd = "Stop-Process -Name \"msedge\" -Force ; Start-Sleep -Seconds 1 ; Start-Process \"msedge\" -ArgumentList @(\"https://forms.office.com/pages/responsepage.aspx\?id=EZDKymp73kSGHwlaLKiDt4wXC_YfIWlGrUcWrbkA4-NURjFZQjdBMkJNSlkwQkVCM0c2V0cyWTVHNSQlQCNjPTEu&classId=31f16070-5361-4de8-9624-98f60a6f24ae&assignmentId=c865c317-1511-4faa-8a46-565ecf1dd392&submissionId=d6e96aee-73d5-bc05-1769-7e7db0c29f9d&route=shorturl\", \"--new-window\", \"--start-fullscreen\")"
    
    run([r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe", "-Command",
          cmd], capture_output=True, text=True,
         check=True, timeout=10, creationflags=creationflags)