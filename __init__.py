import importlib
import inspect
import subprocess
import os, sys

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
req_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "requirements.txt")


with open(req_file) as file:
    for package in file:
        package_version = None
        try:
            package = package.strip()
            if "==" in package:
                package_version = package.split('==')[1]
            elif ">=" in package:
                package_version = package.split('>=')[1]
                strict = False
            if not is_installed(package,package_version,strict):
                run_pip(package)
        except Exception as e:
            print(e)
            print(f"Warning: Failed to install {package}, ReActor will not work.")
            raise e


nodes_filename = "nodes"
module = importlib.import_module(f".{nodes_filename}", package=__name__)
for name, cls in inspect.getmembers(module, inspect.isclass):
    if cls.__module__ == module.__name__:
        name = name.replace("_", " ")

        node = f"[ComfyUI-3D] {name}"
        disp = f"{name}"

        NODE_CLASS_MAPPINGS[node] = cls
        NODE_DISPLAY_NAME_MAPPINGS[node] = disp
        
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']