import time
from pathlib import Path


def client(file_com = "com1.txt"):
    pp = Path(file_com)
    while True:
        cmd = input("Input text")
        if cmd == '_exit_client_':
            exit(0)
        elif cmd == '_exit_server_':
            pp.write_text("_exit_")
        else:
            pp.write_text(cmd)
            

def server(file_com = "com1.txt"):
    
    pp = Path(file_com)
    
    if not pp.exists():
        pp.write_text("")
    
    prev_mtime = pp.stat().st_mtime
        
    while True:
        time.sleep(0.3)
        cur_mtime = pp.stat().st_mtime
        if cur_mtime != prev_mtime:
            print("new command")
            prev_mtime = cur_mtime
            text = pp.read_text().strip()
            if text == '_exit_':
                print("exit command")
                exit(0)
            else:
                print(text)
        else:
            pass


if __name__ =='__main__':
    import fire
    fire.Fire()