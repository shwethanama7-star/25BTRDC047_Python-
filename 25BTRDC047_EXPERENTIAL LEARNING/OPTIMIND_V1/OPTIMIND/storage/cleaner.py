from pathlib import Path

def clean_selected(items):
    deleted = 0
    reclaimed = 0
    for item in items:
        path = Path(item["path"])
        try:
            # Re-check path and symlink status immediately before deletion.
            if path.is_symlink() or not path.is_file():
                continue
            size = path.stat().st_size
            path.unlink()
            deleted += 1
            reclaimed += size
        except (OSError, PermissionError, FileNotFoundError):
            continue
    return deleted, reclaimed
