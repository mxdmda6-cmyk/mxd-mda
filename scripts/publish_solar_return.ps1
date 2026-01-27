# Publish the Shannon Solar Return card to GitHub Pages.
# Edit the values below before running.

# ---- EDIT THESE 3 VALUES ----
$User    = "YOUR_GITHUB_USERNAME"
$Repo    = "shannon-solar-return"
$ZipPath = "$env:USERPROFILE\Downloads\shannon_solar_return_site_v2.zip"
# -----------------------------

$WorkDir = "$env:USERPROFILE\$Repo"

New-Item -ItemType Directory -Force -Path $WorkDir | Out-Null
Expand-Archive -Force -Path $ZipPath -DestinationPath $WorkDir
Set-Location $WorkDir

git init
git add index.html .nojekyll README.md
git commit -m "Publish Solar Return card"
git branch -M main
git remote add origin "https://github.com/$User/$Repo.git"
git push -u origin main

Write-Host "`nWhen Pages is enabled, your link will be:`nhttps://$User.github.io/$Repo/`n"
