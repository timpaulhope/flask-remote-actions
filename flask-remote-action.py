# This creates an api on a host linux server that you can configure to run local shell scripts. 
from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['POST'])

def do_a_thing():
    data = request.get_json()
    what = data.get('what')
    
    if what == 'pxrestart':
        # Run the 'restart plex' shell script using subprocess
        subprocess.run(['/bin/bash', '/path/to/pxrestart_script.sh'])
        
        # Assumes naively that the script has run successfully 
        return 'pxrestart script executed successfully!'
    
    elif what == 'haupdate':
        # Run the 'home assistant' shell script using subprocess
        subprocess.run(['/bin/bash', '/path/to/haupdate_script.sh'])

        # Assumes naively that script has run successfully 
        return 'haupdate script executed successfully!'
    
    else:
        # notify user of values when unexpected `what` sent
        return 'Unknown action word ' + what + ' recieved. Contact admin for the list of valid action words.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9025)
