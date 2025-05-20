import subprocess
import os
import time
import sys

def countdown(seconds, message):
    for remaining in range(seconds, 0, -1):
        sys.stdout.write(f"\r{message}: {remaining} second(s) remaining")
        sys.stdout.flush()
        time.sleep(1)
    print("\r" + " " * (len(message) + 30) + "\r", end="")  # Clear line after countdown

def send_signal_to_vm(vmrun_path, vmx_path, guest_username, guest_password):
    """
    Creates (if needed) and copies the empty signal file 'start_signal' from host
    into the guest VM at /tmp/start_signal to trigger the inside script.
    """
    local_signal_file = "start_signal"  # Filename in the same folder as this script
    
    # Create an empty signal file on the host if it doesn't exist
    if not os.path.exists(local_signal_file):
        with open(local_signal_file, 'w') as f:
            pass  # Just create an empty file
    
    guest_signal_path = "/tmp/start_signal"  # Path inside VM
    
    cmd = [
        vmrun_path,
        "-gu", guest_username,
        "-gp", guest_password,
        "copyFileFromHostToGuest",
        vmx_path,
        os.path.abspath(local_signal_file),  # Full host path
        guest_signal_path  # Target path inside guest
    ]
    
    try:
        subprocess.check_call(cmd)
        print("Signal file copied to the guest VM successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to copy signal file to guest VM: {e}")

def open_vmware_workstation():
    # Paths - adjust if your VMware or VM locations differ
    vmware_path = r"C:\Program Files (x86)\VMware\VMware Workstation\vmware.exe"
    vmrun_path = r"C:\Program Files (x86)\VMware\VMware Workstation\vmrun.exe"
    
    vm_name = "kali-linux-2025.1c-vmware-amd64.vmwarevm"
    vmx_filename = "kali-linux-2025.1c-vmware-amd64.vmx"
    vmx_path = os.path.expandvars(rf"C:\Users\alok8\OneDrive\Documents\Virtual Machines\{vm_name}\{vmx_filename}")
    
    # Guest VM user credentials - change as needed
    guest_username = "kali"
    guest_password = "kali"
    
    # Check VMware executable
    if not os.path.exists(vmware_path):
        print("VMware Workstation not found.")
        return
    
    # Check vmrun utility
    if not os.path.exists(vmrun_path):
        print("vmrun executable not found.")
        return
    
    # Check VMX file
    if not os.path.exists(vmx_path):
        print(f"VM configuration file not found at: {vmx_path}")
        return
    
    try:
        subprocess.Popen(vmware_path)
        print("VMware Workstation opened.")
    except Exception as e:
        print(f"Failed to open VMware Workstation: {e}")
        return
    
    countdown(30, "Waiting before powering on VM")
    
    # Power on the VM
    cmd_power_on = [vmrun_path, "start", vmx_path]
    try:
        subprocess.check_call(cmd_power_on)
        print(f"Powered on VM '{vm_name}'.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to power on VM: {e}")
        return
    
    countdown(30, "Waiting for VM to be ready")
    
    # Send the signal file to the VM to trigger inside script
    #send_signal_to_vm(vmrun_path, vmx_path, guest_username, guest_password)

if __name__ == "__main__":
    open_vmware_workstation()
