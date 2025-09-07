# Below is the shell programming so run this inside the power shell terminal.
# Set paths
$timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm"
$backupFile = "C:\jegan\automation\github_J\PythonLearn\backup\backup_$timestamp.sql"
$zipFile = "C:\jegan\automation\github_J\PythonLearn\backup\backup_$timestamp.zip"

# Run pg_dumpall inside Docker and save to .sql
docker exec -t postgres_c pg_dumpall -c -U admin > $backupFile

# Compress the .sql file into a .zip
Compress-Archive -Path $backupFile -DestinationPath $zipFile

# Optional: Delete the original .sql file after zipping
# Remove-Item $backupFile