@echo off
set /p p=
set /p samples=
call javac %p%.java
for /l %%i in (1,1,%samples%) do (
  call java %p% < input%%i.txt > myoutput%%i.txt
  echo My Output : 
  call type myoutput%%i.txt 
  echo Correct Output : 
  call type output%%i.txt
)
pause