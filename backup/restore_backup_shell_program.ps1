# Define paths
$timestamp = "2025-09-07_13-49"  # Change this to match your actual backup timestamp
$backupDir = "C:\jegan\automation\github_J\PythonLearn\backup\"
$zipFile = "$backupDir\backup_$timestamp.zip"
$restoreDir = "$backupDir\Restored"
$sqlFile = "$restoreDir\backup_$timestamp.sql"
$database = "mydatabase"

# Step 1: Unzip the backup
if (!(Test-Path $restoreDir)) {
    New-Item -ItemType Directory -Path $restoreDir
}
Expand-Archive -Path $zipFile -DestinationPath $restoreDir -Force

# Step 2: Restore using Docker + psql
if (Test-Path $sqlFile) {
    Write-Host "Restoring backup from $sqlFile..."
    Get-Content $sqlFile | docker exec -i postgres_c psql -U admin -d $database
    Write-Host "✅ Restore complete."
} else {
    Write-Host "❌ SQL file not found at $sqlFile"
}