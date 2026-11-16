param(
    [string]$ArtifactPath = "dist",
    [string]$DeployRoot = "C:\Deploy\marsrover-cd"
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path $ArtifactPath)) {
    throw "Artifact directory '$ArtifactPath' was not found."
}

New-Item -ItemType Directory -Path $DeployRoot -Force | Out-Null

Get-ChildItem -Path $ArtifactPath -Force | ForEach-Object {
    Copy-Item -Path $_.FullName -Destination $DeployRoot -Force
}

Write-Host "Deployment complete. Files copied to $DeployRoot"
Get-ChildItem -Path $DeployRoot -Force | Select-Object Name, Length
