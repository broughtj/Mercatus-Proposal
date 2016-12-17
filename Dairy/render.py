import subprocess 

cmd = "R CMD BATCH render.R"
print(cmd)
subprocess.call(cmd, shell=True)
