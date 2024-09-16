setlocal
set ddf=%TEMP%\cabprof.ddf
(echo %1) > "%ddf%"
REM 100MB単位でファイルを分割する
makecab ^
  /d MaxDiskSize=102400000 ^
  /d RptFileName=NUL ^
  /d InfFileName=NUL ^
  /d DiskDirectoryTemplate="%~n1" ^
  /f "%ddf%"
del "%ddf%"