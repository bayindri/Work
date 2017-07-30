@echo Off
REM cscript.exe "C:\Documents and Settings\abaner02\My Documents\Ayindri_Documents\Projects\2013\Automation\Automation8_NonUnique.vbs" %*
REM cscript.exe "C:\Documents and Settings\abaner02\My Documents\Ayindri_Documents\Projects\2013\Automation\Append.vbs" %*
REM cscript.exe "C:\Documents and Settings\abaner02\My Documents\Ayindri_Documents\Projects\2013\Automation\GenerateVisualizationData4.vbs" %*
set pathname="C:\Documents and Settings\abaner02\My Documents\Ayindri_Documents\Projects\2015\WhitePagesIntegration"
pushd %Pathname%

REM start chrome.exe "http://localhost:8888/Calendar.html"
REM start firefox.exe "http://localhost:8888/DigitalHealthPlanSampler.html"
REM start firefox.exe "http://localhost:8888/DigitalHealthPlan2.html"
start firefox.exe "http://localhost:8888/index.html"
c:\python27\python.exe -m SimpleHTTPServer 8888 &
pause