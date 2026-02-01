import subprocess
import re

class NetworkScanner:
    def scan_network(self):
        """Executes 'arp -a' to find devices on the local network."""
        try:
            # Run the scanning command
            result = subprocess.run(['arp', '-a'], capture_output=True, text=True)
            output = result.stdout
            
            devices = []
            # Parse output - this regex is tailored for Windows arp -a output
            # Format usually: Interface: 192.168.1.x ... Internet Address Physical Address Type
            lines = output.split('\n')
            for line in lines:
                parts = line.split()
                if len(parts) == 3:
                     # very basic heuristic
                     ip, mac, type_ = parts
                     if self._is_valid_ip(ip) and self._is_valid_mac(mac):
                         devices.append({'ip': ip, 'mac': mac, 'type': type_})
            
            return devices

        except Exception as e:
             return f"Error scanning network: {e}"

    def _is_valid_ip(self, ip):
        # Basic check
        return re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip) is not None

    def _is_valid_mac(self, mac):
        # Basic check for MAC address format (00-11-22-33-44-55) or (00:11...)
        return re.match(r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$", mac) is not None
