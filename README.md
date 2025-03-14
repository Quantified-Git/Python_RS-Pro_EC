# Python_RS-Pro_EC
Library for digital readout of the RS PRO 123.8777 Conductivity Meter.

##  Function description
### Constructor
The constructor of this library opens the COM port, hence it needs the COM port as argument.

### RS_EC.read()
This function wil read the most recent measurment from the screen of the EC meter.  

The function doesn't need any arguments and will return a dictionary in the following format:  
- 'upValue': Upper value displayed on the screen.  
- 'upUnit': Unit of the upper value. (C, F, uS, mS)  
- 'lowValue': Lower value displayed on the screen.  
- 'lowUnit': Unit of the lower value. (noUnit, C, F)

For an example see example.py

## Hardware
A special cable is needed to connect the meter to a computer these are commercially avalble but are rather easy to make:

### Needed parts:
- DB9 serial connector
- 3.5mm mono jack connector
- A length of two core cable

Make the following connections:   
- DB9 pin 2 -> jack sleeve  
- DB9 pin 5 -> jack tip

An RS232 usb adapter is also necessary to use this cable with a modern computer.  
Please note that a TTL UART usb adapter is not a proper substitute for a regular RS232 adapter.

## Generate package
Make sure you have the latest version of PyPA’s build installed:
```console
py -m pip install --upgrade build
```

Run this command from the same directory where pyproject.toml is located:
```console
py -m build
```