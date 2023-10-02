import os
import argparse
import subprocess
from wandbreq import wandb_class

parser = argparse.ArgumentParser(description="Please provide inputs ")

parser.add_argument("target_directory", help="directory path for with storage is logged")
parser.add_argument("key", help="Wandb dashboard key to log file/folder wise memory in bits")
parser.add_argument("project", help="wandb project name")
args = parser.parse_args()

wandb = wandb_class(args.project,args.key)
wandb.env()
wandb.conf()


def get_memory_utilization(path):
    try:
        cmd = ["du", "-s", path]
        result = subprocess.check_output(cmd, universal_newlines=True)
        return result.strip()  # Remove leading/trailing whitespace and return the result
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

def main():
    target_directory =  args.target_directory # Replace with your directory path
    print(f"Memory Utilization for {target_directory}:\n")
    for dirpath, dirnames, filenames in os.walk(target_directory):
        for dirname in dirnames:
            directory_path = os.path.join(dirpath, dirname)
            result = get_memory_utilization(directory_path)
            print(f"Directory: {directory_path}\n{result}\n")
            wandb.log(str(directory_path),float(result.split('\t')[0]))
            
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            result = get_memory_utilization(file_path)
            print(f"File: {file_path}\n{result}\n")
            wandb.log(str(file_path),float(result.split('\t')[0]))
        wandb.end()
        break;

if __name__ == "__main__":
    main()
