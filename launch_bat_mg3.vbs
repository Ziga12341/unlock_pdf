Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "C:\["your path"]\mg3.bat" & Chr(34), 0
Set WshShell = Nothing