import argparse 
import subprocess
import os

def main():

    parser = argparse.ArgumentParser(description="recursively search for a string from given path", 
                                     usage="python3 <script Name> -p <Dirctory Path> -s <String>")
    parser.add_argument('-p','--dir', help='Path location',required=True,)
    parser.add_argument('-s','--string', help='Search string', required=True,)
    args = parser.parse_args()

    if args.dir and args.string:
        grepOutput = subprocess.check_output(['grep','-rl', args.string, args.dir])
        decodeOutput = grepOutput.decode("utf-8").strip()
        fname=[]
        for i in decodeOutput.split("\n"):
            fname.append(os.path.basename(i))
        for i in range(0, len(fname), 10):
            print(*fname[i:i+10], sep=',') 

if __name__ == '__main__':
    main()
