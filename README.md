# Pylpaca (ASCOM Alpaca API micro-framework for Python)

This is a python implementation of the [ASCOM](https://ascom-standards.org/) driver interfaces and the [ASCOM Alpaca API](https://ascom-standards.org/api).

It is built on top of the [Tornado microframework](http://www.tornadoweb.org), and code has been borrowed from the [Tornado-Rest](https://github.com/rancavil/tornado-rest) project (Acknoledgments to their authors).
This framework allows you to wrap around your custom astronomy device driver (Telescope, Dome, Camera...) , so that they can be called by simple Http requests.

Pylpaca works with Python 3+. It has **not** been tested on older versions of python.

**/!\ Please note that this framework is under active development as of March 2019, and is not mature to be used in a production environment. Watch this repository for keeping up to date with regular changesand.**

# How to use ?

The repository contains an some template for building a device driver which follows the ASCOM protocol and presents the same interfaces defined for ASCOM in Windows.

Note that currently this framework will not register your driver with the ASCOM registry even if you are running on Windows. We prefer not to add any Python to COM interop functionality at this stage, for stability reasons.

The `MyDomeDriver` template within the `ASCOMDriver/` folder is a working example of a Dome driver which simulates the Opening and Closing of a shutter. One can extend this class to talk directly to your Serial (Arduino or other) device.

The `dome_service`, under `services/`, is the Alpaca REST endpoint which processes incoming Http REST requests directed to the dome. Note that it uses a little bit of reflection/inspection to dynamically call the driver members (class instance methods or properties).

# Configuration

The `config.json` file is where must be defined the drivers to expose functionality via the Alpaca REST API server `server.py`.

The drivers must be listed in the configuration file as shown in the example below :

```
{
  "drivers": [
    {
      "device_type": "dome",
      "device_number": 0,
      "device_driver": "MyASCOMDomeDriver",
      "driver_config": {}
    }
  ]
}
```

Driver configuration is loaded on start, so any change made will require a server restart.

# Starting the server

The Tornado microframework does not require a WSGI server to run (unlike the Flask framework), thus the server can be simply started by running :
`python server.py`

The server is listening to the port 11111 by default (similarly to the ASCOM REST Server), but this can be changed in `server.py`.

