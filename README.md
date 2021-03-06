# ELM 327 OBD Simulator
--------------
ELM327 OBD Simulator is an OBD2 compliant simulator adhering to the SAE standard J/1979 and ELM 327 command protocol, accessible over a socket

### About OBD2
----------------
In order to get engine sensor specific data, two bytes are written to the OBD2 port (I call these "query bytes"), and up to eight bytes are returned. This is best demonstrated with an example. Say we wish to get the Engine RPM. We would write 01 and 0C ("01 0C"), and would receive something akin to "41 0C 20 BC" back. The first two bytes, "41 0C" are the response code indicating the following bytes will describe the engine RPM's actual value. Therefore, "20 BC" are the two bytes representing the current Engine RPM. This query only returns two bytes, but queries can return as many as six bytes (plus the first two bytes for the response code, so a maximum eight). To calculate the ACTUAL value of the Engine RPM  from the bytes, a specific formula is needed (for Engine RPM it's ``((A*256)+B)/4``.

### What ELM327 OBD Simulator Does
---------------------------
ELM 327 OBD Simulator creates a server instance at the specified address and port that accepts query bytes, processes them, and returns a random (but appropriate) response. Once you create an instance of the simulator, all you need to do is open a socket at the correct address and port using your language of choice.

### How To Use It
-----------------
```
python.exe Program.py -address=localhost -port=1090 -shell
```
* If the address and the port are not specified, the defaults "localhost" and "35000" will be used.
* If -shell is passed, a separate python instance wll be created with a shell connected to the OBD Simulator server
instance's address and port.

Note that the simulator is designed to take string representations of bytes. If you wished to send 0x01 0x0C,
conversion will be attempted to "01 0C". This is strictly to emulate ELM 327 device behavior.

### Project Status
------------------
Currently supports:
* Mode 01
* All PIDs up to 60
* ATDP
* ATRV

Planned:
* Modes 04, 07
* Logging
* User specified values
* Engine simulation
