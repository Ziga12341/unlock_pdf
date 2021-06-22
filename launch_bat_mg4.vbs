Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "C:\["your path"]\mg4.bat" & Chr(34), 0
Set WshShell = Nothing