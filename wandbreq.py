import os
import wandb

import os
import wandb



class wandb_class():
    def __init__(self,project, key):
        self.project = project
        self.key = key
        
    def env(self):
        os.environ["WANDB_API_KEY"] = self.key

    def conf(self):
        wandb.init(
            project=self.project
        )

    def log(self,key,value):
        #wandb.log({"Directory": directory_path, "Memory Utilization": result})
        wandb.log({key:value})
        

    
    def end(self):
        wandb.finish()


        