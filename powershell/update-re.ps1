#Config variablesq

$createDesktopShortcut = $TRUE

# ------

# Nightly GTA 3 RC zip file for Windows 64bit D3D9 MSS build
$gta3url = "https://nightly.link/GTAmodding/re3/workflows/re3_msvc_x86/master/re3_Release_win-x86-librw_d3d9-mss.zip"
# Nightly GTA VC RC zip file for Windows 64bit D3D9 MSS build
$gtavcurl = "https://nightly.link/GTAmodding/re3/workflows/reVC_msvc_x86/miami/reVC_Release_win-x86-librw_d3d9-mss.zip"

# Get the Steam folder installed on user's machine
# Check 64bit directory
$steamFolder = (Get-ItemProperty -path 'HKLM:\SOFTWARE\Wow6432Node\Valve\Steam').InstallPath
# Fallback to the 32bit directory
if ($steamFolder -eq $null) {
	$steamFolder = (Get-ItemProperty -path 'HKLM:\SOFTWARE\Valve\Steam').InstallPath
}
# If we get nothing, it's likely it isn't installed on the user's machine (or installed properly)
if ($steamFolder -eq $null) {
	Write-Host "Steam folder not found"
	exit 1
}

$steamGamesPath = "$steamFolder\steamapps\common"
$gta3Steam = "$steamGamesPath\Grand Theft Auto 3"
$vcSteam = "$steamGamesPath\Grand Theft Auto Vice City"

# And away we go. I download it to the current directory because I couldn't find an inbuilt way to get the temp directory.
# The only ways I found were to create a temporary file, then delete that file and use it's directory. That just feels silly.

Write-Host "Downloading GTA 3 RC"

Invoke-WebRequest $gta3url -OutFile gta3.zip

Write-Host "Downloading GTA VC RC"

Invoke-WebRequest $gtavcurl -OutFile gtavc.zip

Write-Host "Extracting GTA 3 RC into Steam directory: $gta3Steam"

Expand-Archive -LiteralPath gta3.zip -DestinationPath $gta3Steam -Force

Write-Host "Downloading GTA VC RC into Steam directory: $vcSteam"

Expand-Archive -LiteralPath gtavc.zip -DestinationPath $vcSteam -Force

Write-Host "Deleting zip files"

Remove-Item gta3.zip
Remove-Item gtavc.zip

if ($createDesktopShortcut) {
	# Method to create shortcut, stole from somewhere online
	Write-Host "Creating shortcuts"
	function set-shortcut {
	param ( [string]$SourceLnk, [string]$DestinationPath )
		$WshShell = New-Object -comObject WScript.Shell
		$Shortcut = $WshShell.CreateShortcut($SourceLnk)
		$Shortcut.TargetPath = $DestinationPath
		$Shortcut.Save()
	}

	$DesktopPath = [Environment]::GetFolderPath("Desktop")
	
	set-shortcut "$DesktopPath\GTA3 Remastered.lnk" "$gta3Steam\re3.exe"
	set-shortcut "$DesktopPath\GTA VC Remastered.lnk" "$vcSteam\reVC.exe"
}