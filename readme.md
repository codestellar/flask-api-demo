# Learn Building API in python

## This tutorial's code is generated using ChatGPT and is tested.

1. Install and activate venv
````
python3 -m venv venv
source venv/bin/activate
````
2. For windows, use git bash. Skip this step if venv is already active.
````
source venv/Scripts/activate
````
3. Or powershell. Skip this step if venv is already active. 
````
.\venv\Scripts\activate
````
Common issues in windows, if you are unable to run the script in Powershell, then run the following command after open Powershell in administrator mode
````
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
````
4. Generate requirements.txt
````
pip freeze > requirements.txt
````
5. Install flask and perform step 4 again.
````
pip install flask
````
6. Run the application
````
python app.py
````
