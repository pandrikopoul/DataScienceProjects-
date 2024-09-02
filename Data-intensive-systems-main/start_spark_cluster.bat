@echo off
set SPARK_HOME=C:\spark\spark-3.5.1-bin-hadoop3
set MASTER_HOST=192.168.1.81
set MASTER_PORT=7077
set NUM_WORKERS=3
set WORKER_MEMORY=8G
set WORKER_CORE=2

echo Starting Spark Master...
start cmd /k "%SPARK_HOME%\bin\spark-class2.cmd org.apache.spark.deploy.master.Master"

timeout /t 5

echo Starting 12 Spark Workers...
for /L %%i in (1,1,%NUM_WORKERS%) do (
    start cmd /k "%SPARK_HOME%\bin\spark-class2.cmd org.apache.spark.deploy.worker.Worker -c %WORKER_CORE% -m %WORKER_MEMORY% spark://%MASTER_HOST%:%MASTER_PORT%"
    timeout /t 1
)

echo Spark Cluster Started.
pause