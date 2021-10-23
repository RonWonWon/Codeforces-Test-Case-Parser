@echo off
set /p p=
set /p samples=
call kotlinc %p%.kt -include-runtime -d %p%.jar
for /l %%i in (1,1,%samples%) do (
  call java -jar %p%.jar <input%%i.txt> myoutput%%i.txt
  echo My Output : 
  call type myoutput%%i.txt 
  echo Correct Output : 
  call type output%%i.txt
)
pause
