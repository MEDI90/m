*This project has been created as part of the 42 curriculum by mboubaza.*

## Description

Born2BeRoot is a System Administration and Virtualization project aimed at introducing the strict rigors of server configuration. The goal is to create a secure, highly configured Virtual Machine (VM) to serve as a robust web server.

This project involves setting up a virtual machine using the Debian operating system with a focus on security, partition management, and automation. It requires the implementation of a strict password policy, firewall configuration, SSH management, and scripted system monitoring, alongside the deployment of a functional WordPress environment served via Lighttpd and MariaDB.

## Project Description

### Choice of Operating System
I chose **Debian 12 (Bookworm)** for this project.
* **Pros:** Debian is renowned for its stability, extensive package repository (APT), and large community support. It is often the upstream source for many other distributions (like Ubuntu), making it an excellent learning ground for understanding the core of Linux systems.
* **Cons:** It can have slower release cycles compared to "bleeding edge" distributions, meaning software versions in the stable repository might be older.

### Design Choices
* **Partitioning:** I utilized LVM (Logical Volume Manager) to create a flexible storage structure. To meet bonus requirements, I separated the filesystem into distinct logical volumes (`/`, `/home`, `/var`, `/srv`, `/tmp`, `/var/log`) to prevent a single directory from consuming all disk space and crashing the system.
* **Security Policies:** A strict password policy was enforced using `pam_pwquality`, requiring strong, non-repetitive passwords that expire every 30 days. Root login is disabled via SSH to ensure accountability.
* **User Management:** Administrative tasks are restricted to users in the `sudo` group, with all actions logged for auditing purposes.
* **Services:** The server hosts a WordPress site using the Lighttpd web server, MariaDB database, and PHP. Additionally, an FTP server (`vsftpd`) was configured to facilitate file transfers.

### Technical Comparisons

**Debian vs Rocky Linux**
* **Debian:** Uses the `.deb` package format and `apt`/`apt-get` package managers. It is community-driven and focuses strictly on free software principles.
* **Rocky Linux:** Uses the `.rpm` package format and `dnf`/`yum` package managers. It is a downstream rebuild of RHEL (Red Hat Enterprise Linux), designed to be a bug-for-bug compatible enterprise-grade OS.

**AppArmor vs SELinux**
* **AppArmor (Debian default):** Uses path-based Mandatory Access Control (MAC). It restricts programs based on file paths and is generally considered easier to configure and learn for beginners.
* **SELinux (Rocky default):** Uses label-based MAC (inodes). It attaches security labels to files and processes. It is more granular and powerful but significantly more complex to configure and troubleshoot.

**UFW vs firewalld**
* **UFW (Uncomplicated Firewall):** A user-friendly interface for managing `iptables`/`nftables`. It is designed to make firewall configuration simple and is standard on Debian/Ubuntu systems.
* **firewalld:** A dynamic firewall manager with support for network/firewall zones. It allows changing settings without restarting the firewall daemon and is standard on RHEL/Rocky systems.

**VirtualBox vs UTM**
* **VirtualBox:** A mature, cross-platform Type-2 hypervisor by Oracle. It supports x86 virtualization efficiently and is the standard requirement for this project on standard clusters.
* **UTM:** A virtualization tool for macOS (specifically optimized for Apple Silicon). It uses QEMU under the hood to emulate different architectures (like x86 on ARM), which is useful for running standard Linux distros on M1/M2/M3 Macs.

## Instructions

### Installation
This project does not require compilation. To deploy the environment:
1.  Ensure VirtualBox is installed on the host machine.
2.  Import the `.vdi` file provided in the submission.
3.  Create a new Virtual Machine in VirtualBox using the imported `.vdi` as the hard disk.

### Execution & Verification
To verify the integrity of the submitted machine before booting:
1.  Locate the `Born2BeRoot.vdi` file.
2.  Run the following command to check the signature:
    ```bash
    shasum Born2BeRoot.vdi
    ```
3.  Compare the output hash with the content of the `signature.txt` file at the root of the repository.
4.  If the signatures match, start the VM via VirtualBox.

### Usage
* **Login:** Use the username `mboubaza` (or the evaluator user created during defense).
* **Web Server:** Access `http://localhost:8080` (or the forwarded port) from the host machine to view WordPress.
* **SSH:** Connect via `ssh mboubaza@localhost -p 4242`.
* **FTP:** Connect via `ftp localhost` on port 21 inside the VM.

## Resources

### Classic References
* [Debian Administrator's Handbook](https://debian-handbook.info/)
* [Debian Wiki - LVM](https://wiki.debian.org/LVM)
* [UFW Documentation](https://wiki.ubuntu.com/UncomplicatedFirewall)
* [Lighttpd Configuration](https://redmine.lighttpd.net/projects/lighttpd/wiki)

### Usage of AI
Artificial Intelligence (specifically LLMs) was used during the development of this project for the following tasks:
* **Concept Explanation:** To clarify the differences between AppArmor and SELinux, and to understand the boot process (PID 1).
* **Debugging:** To troubleshoot specific errors, such as the `vsftpd` IPv6 conflict and firewall configuration issues.
* **Script Logic:** To assist in structuring the logic for the `monitoring.sh` script, specifically regarding parsing `cron` schedules and text formatting for the broadcast message.
* **Verification:** To generate an audit checklist script ensuring all mandatory and bonus requirements were met prior to defense.
