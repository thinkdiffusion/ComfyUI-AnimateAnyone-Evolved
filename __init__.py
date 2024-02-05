import importlib
import inspect
import subprocess
import os, sys

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

subprocess.run(['pip', 'install', '-r', 'requirements.txt'])

nodes_filename = "nodes"
module = importlib.import_module(f".{nodes_filename}", package=__name__)
for name, cls in inspect.getmembers(module, inspect.isclass):
    if cls.__module__ == module.__name__:
        name = name.replace("_", " ")

        node = f"[AnimateAnyone] {name}"
        disp = f"{name}"

        NODE_CLASS_MAPPINGS[node] = cls
        NODE_DISPLAY_NAME_MAPPINGS[node] = disp
        
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
