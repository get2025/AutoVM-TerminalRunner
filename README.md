# AutoVM-TerminalRunner

## Overview

This project automates the process of starting a VMware Workstation virtual machine (VM) from a Windows host using a Python script, and then automatically running a series of commands inside a Linux VM terminal after it boots.

### How it works

1. You run `open_vmware_workstation.py` on your Windows host machine using VS Code or any Python environment. This script opens VMware Workstation and starts the Linux VM.
2. Inside the Linux VM, the script `start_with_terminal.sh` is set to run automatically on boot. This script opens a terminal window.
3. The opened terminal runs the `run_msf.sh` script, which executes predefined Linux commands such as system updates, installing packages, or running `msfconsole`.
4. The automation continues with specific delays between commands to ensure proper execution.

---

## Features

- Automates VM startup from the Windows host.
- Automatically opens a terminal inside the Linux VM after boot.
- Runs a customizable shell script (`run_msf.sh`) inside the Linux VM terminal.
- Designed for easy modification to suit various automation tasks.

---

## Requirements

- VMware Workstation installed on the Windows host.
- Python 3 installed on the host machine.
- Linux VM configured with scripts `start_with_terminal.sh` and `run_msf.sh`.
- Both scripts inside the Linux VM must have execute permissions (`chmod +x filename.sh`).

---

## Setup Instructions

1. **Host machine:**

   - Place `open_vmware_workstation.py` on your Windows machine.
   - Run this Python script to launch the VMware VM.

2. **Linux VM:**

   - Ensure `start_with_terminal.sh` and `run_msf.sh` are in a known directory, e.g., `/root/`.
   - Make both scripts executable:

     ```bash
     chmod +x /root/start_with_terminal.sh
     chmod +x /root/run_msf.sh
     ```

   - **Important:** Configure `start_with_terminal.sh` to run automatically after boot in the Linux VM.

     For example, using `crontab`:

     ```bash
     sudo crontab -e
     ```

     Add this line to the root crontab:

     ```
     @reboot /root/start_with_terminal.sh
     ```

     Alternatively, you can use systemd services or your desktop environment's startup applications.

---

## Usage

- Run `open_vmware_workstation.py` on your Windows host to start the VM.
- After the Linux VM boots, `start_with_terminal.sh` will launch a terminal window and execute `run_msf.sh`.
- The commands in `run_msf.sh` will execute sequentially with delays as configured.

---

## Notes

- This project is designed for personal automation but can be customized for different environments or command sequences.
- Always verify script paths and permissions inside your Linux VM.
- You can modify `run_msf.sh` to add or remove commands based on your needs.

---

## License

This project is licensed under the MIT License.

---

## Contribution

Feel free to fork the repository, submit issues, or create pull requests to improve the project.

---

## Contact

For questions or suggestions, open an issue on this GitHub repository.

