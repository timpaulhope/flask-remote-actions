# A Flask API for Running Shell Scripts

This Flask API provides an endpoint to execute different shell scripts on a linux machine based on the value received in a JSON payload. It listens on a specified port and triggers the corresponding shell script when the specific action word is sent.

## Use Case
**Example of action buttons created in a [Home Assistant](https://www.home-assistant.io/) dashboard that post to the api**

![alt text](/img/haButtons.PNG)
## Requirements

- Python 3.x
- pip (Python package installer)

## Installation

Clone the repository or download the script files to the host machine.

Open a command-line interface on the host machine and navigate to the project directory.

Install the required dependencies:

```shell
pip3 install flask
```
In the command-line interface, open the python script in a text editor and customise the action words and script addresses as required before proceding.

## Usage - Local Supervised Run

From the project directory, start the Flask API:
```shell
python3 flask-remote-action.py
```
The Flask API will start running on http://localhost:9025/ by default.

On a machine other than the host, Send a POST request to port 9025 of the hosts IP adress with a JSON payload containing a single word key-value pair. 

```json
{
  "what":"haupdate"
}
```

The shell script related to the action word will be triggered, and the API will (naively) return a success message indicating that the script has been executed.

If the action word is not known, the API will return a message stating that the word is not recognized.

To stop the Flask API, press `Ctrl+C` in the command-line interface session running the app on the host machine.

## Usage - Run in background on startup

Once you are happy it is behaving as expected, to run the script in the background on startup, add the following to your crontab.

```shell
# Run monitor.py a minute after startup
@reboot sleep 60 && /usr/bin/python3 /path/to/flask-remote-action.py & 
```
## Customization

You can modify the code in flask-remote-action.py to include additional scripts and action words as per your requirements.

Update the subdirectories, host, and port in the code to match your desired paths and network configuration.

## [ToDo]
Come up with some fancy way of having the api return the outcome of running the shellscript rather than naively assuming is completed.