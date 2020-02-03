import psutil
import subprocess 

if __name__ == "__main__":
    
    shell_cmd = "python3 ./run_sleep.py"
    main_proc = subprocess.Popen(shell_cmd, shell=True)
    parent = psutil.Process(main_proc.pid)
    children = parent.children(recursive=True)
    while main_proc.poll() not in (0, 1):
        print('process status: ', main_proc.poll())

    print("Done")
