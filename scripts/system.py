import platform
import psutil
import cpuinfo
from colorama import init, Fore, Back, Style


# Información del sistema operativo
print(Fore.BLUE + "! " + Fore.LIGHTWHITE_EX + "Operating system: " + Fore.LIGHTBLUE_EX + f"{platform.system()} {platform.release()}")

# Información de la CPU
info = cpuinfo.get_cpu_info()
print(Fore.BLUE + "! " + Fore.LIGHTWHITE_EX + f"CPU Model: " + Fore.LIGHTBLUE_EX + f"{info['brand_raw']} {info['family']} ({info['arch']})")
print(Fore.BLUE + "! " + Fore.LIGHTWHITE_EX + f"CPU Clock Frequency: " + Fore.LIGHTBLUE_EX + f"{info['hz_actual_friendly']}")
print(Fore.BLUE + "! " + Fore.LIGHTWHITE_EX + f"Number of CPU Cores: " + Fore.LIGHTBLUE_EX + f"{info['count']}")

# Información de la memoria RAM
mem = psutil.virtual_memory()
print(Fore.YELLOW + "! " + Fore.LIGHTWHITE_EX + f"Total RAM Memory: " + Fore.LIGHTYELLOW_EX + f"{mem.total/1024/1024:.2f} MB")
print(Fore.YELLOW + "! " + Fore.LIGHTWHITE_EX + f"Available RAM Memory: " + Fore.LIGHTYELLOW_EX + f"{mem.available/1024/1024:.2f} MB")
print(Fore.YELLOW + "! " + Fore.LIGHTWHITE_EX + f"Used RAM Memory: " + Fore.LIGHTYELLOW_EX + f"{mem.used/1024/1024:.2f} MB")

# Información del disco duro
partitions = psutil.disk_partitions()
for partition in partitions:
    print(Fore.MAGENTA + "! " + Fore.LIGHTWHITE_EX + f"Disk: " + Fore.MAGENTA + f"{partition.device}")
    print(Fore.MAGENTA + "! " + Fore.LIGHTWHITE_EX + f"File System: " + Fore.GREEN + f"{partition.fstype}")
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        continue
    print(Fore.MAGENTA + "! " + Fore.LIGHTWHITE_EX + f"Total disk space: " + Fore.BLACK + f"{partition_usage.total/1024/1024:.2f} MB")
    print(Fore.MAGENTA + "! " + Fore.LIGHTWHITE_EX + f"Free disk space: " + Fore.BLACK + f"{partition_usage.free/1024/1024:.2f} MB")
    print(Fore.MAGENTA + "! " + Fore.LIGHTWHITE_EX + f"Used disk space: " + Fore.BLACK + f"{partition_usage.used/1024/1024:.2f} MB")

# Información de la red
net_io_counters = psutil.net_io_counters()
print(Fore.CYAN + "! " + Fore.LIGHTWHITE_EX + "Red Information")
print(Fore.CYAN + "! " + Fore.LIGHTWHITE_EX + f"Bytes Sent: " + Fore.CYAN + f"{net_io_counters.bytes_sent/1024/1024:.2f} MB")
print(Fore.CYAN + "! " + Fore.LIGHTWHITE_EX + f"Bytes received: " + Fore.CYAN + f"{net_io_counters.bytes_recv/1024/1024:.2f} MB" + Fore.RESET)

