import os
import sys

path = "/opt/code/nndet"
site_path = "/opt/dataiku/code-env/lib/python3.9/site-packages"
with open(os.path.join(site_path,"easy-install.pth"), 'w') as f:
    f.write(path)
    
with open(os.path.join(site_path,"nndet.egg-link"), 'w') as f:
    f.write(path)
