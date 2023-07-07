"""
Script Name: terminateSuspiciousProcess.py
Author: Joshua Khokhar
Creation Date: 7/7/2023
Purpose: This script finds the process it is provided with and terminates it.
"""

import wmi
c = wmi.WMI()

# Replace "Notepad.exe" with the suspicious process to terminate it
for process in c.Win32_Process(Name="Notepad.exe"):
    print(process.Name, process.ProcessId, process.VirtualSize)
    process.terminate
