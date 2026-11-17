def build_recommendations(data):
    recommendations = []
    ram = data["ram_percent"]
    disk = data["disk_percent"]
    cpu = data["cpu"]

    if ram >= 90:
        recommendations.append(("HIGH", "Very high RAM pressure",
            "Review the top memory-consuming applications. Save work before closing anything."))
    elif ram >= 75:
        recommendations.append(("MEDIUM", "Elevated RAM usage",
            "Inspect the process list and close only applications you recognize and no longer need."))
    else:
        recommendations.append(("INFO", "RAM usage looks reasonable",
            "No memory action is suggested based on the current snapshot."))

    if disk >= 90:
        recommendations.append(("HIGH", "Disk is nearly full",
            "Review large files and the user temporary folder. Back up important files before removing anything."))
    elif disk >= 80:
        recommendations.append(("MEDIUM", "Storage space is getting low",
            "Review Downloads and temporary files for items you no longer need."))
    else:
        recommendations.append(("INFO", "Disk space looks reasonable",
            "No urgent storage action is suggested by the current usage percentage."))

    if cpu >= 85:
        recommendations.append(("MEDIUM", "High CPU activity",
            "Check Task Manager and identify which application is currently using CPU."))
    else:
        recommendations.append(("INFO", "CPU activity is not unusually high",
            "Current CPU usage does not indicate a sustained high-load issue."))

    recommendations.append(("INFO", "Safety mode enabled",
        "OPTIMIND never closes applications or deletes files without your explicit confirmation."))
    return recommendations
