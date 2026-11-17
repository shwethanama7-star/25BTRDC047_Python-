import os
import tempfile
from pathlib import Path

# Deliberately limited to the current user's temporary directory.
# No Windows, Program Files, browser profile, or application data folders are scanned for deletion.
MAX_FILE_SIZE_SCAN = 2 * 1024 * 1024 * 1024

def scan_temp_files():
    root = Path(tempfile.gettempdir())
    found = []
    total = 0
    try:
        for current, dirs, names in os.walk(root):
            # Avoid traversing reparse points/symlinked directories.
            dirs[:] = [d for d in dirs if not (Path(current) / d).is_symlink()]
            for name in names:
                path = Path(current) / name
                try:
                    if path.is_symlink() or not path.is_file():
                        continue
                    size = path.stat().st_size
                    found.append({"path": path, "size": size})
                    total += size
                except (OSError, PermissionError):
                    continue
    except (OSError, PermissionError):
        pass
    found.sort(key=lambda x: x["size"], reverse=True)
    return found, total

def find_large_files(limit=10, min_size=250 * 1024 * 1024):
    roots = [Path.home() / "Downloads", Path.home() / "Desktop", Path.home() / "Documents"]
    found = []
    for root in roots:
        if not root.exists():
            continue
        try:
            for current, dirs, names in os.walk(root):
                dirs[:] = [d for d in dirs if not (Path(current) / d).is_symlink()]
                for name in names:
                    path = Path(current) / name
                    try:
                        if path.is_symlink() or not path.is_file():
                            continue
                        size = path.stat().st_size
                        if size >= min_size:
                            found.append({"path": path, "size": size})
                    except (OSError, PermissionError):
                        continue
        except (OSError, PermissionError):
            continue
    return sorted(found, key=lambda x: x["size"], reverse=True)[:limit]
