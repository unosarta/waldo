#!/bin/bash
chmod +x python_to_bash.py
chmod +x modules.py
python python_to_bash.py

read -p "Please input the path to your version of VisIt: " visit_location
PATH=$PATH:/$visit_location
visit -cli -s visit_commands.py
