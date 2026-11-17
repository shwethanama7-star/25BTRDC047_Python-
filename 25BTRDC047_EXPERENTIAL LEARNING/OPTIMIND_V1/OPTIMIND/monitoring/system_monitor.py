import psutil
from pathlib import Path

def get_system_snapshot():
    mem = psutil.virtual_memory()
    disk_path = Path.home().anchor or "C:\\"
    try:
        disk = psutil.disk_usage(disk_path)
    except Exception:
        disk = psutil.disk_usage("C:\\")
    return {
        "cpu": psutil.cpu_percent(interval=0.5),
        "ram_percent": mem.percent,
        "ram_used": mem.used,
        "ram_total": mem.total,
        "disk_percent": disk.percent,
        "disk_used": disk.used,
        "disk_total": disk.total,
    }

def get_top_processes(limit=15):
    results = []
    for proc in psutil.process_iter(["pid", "name", "memory_info", "status"]):
        try:
            info = proc.info
            mem = info.get("memory_info")
            results.append({
                "pid": info["pid"],
                "name": info.get("name") or "Unknown",
                "memory": mem.rss if mem else 0,
                "status": info.get("status") or "unknown"
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return sorted(results, key=lambda x: x["memory"], reverse=True)[:limit]
