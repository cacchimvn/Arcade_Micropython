This is a basic MicroPython board definition the ARCADE, using UF2 bootloader.


To build the project, you need:
- Download micropython: https://github.com/micropython/micropython
- Download this repository into folder : ~\micropython\ports\stm32\boards
- cd ARCADE.
- Run make. (This step will overwrite some files need to be reconfig for ARCADE)
- Back to: ~\micropython\ports\
- Follow instructions from micropython repository to build ARCADE.
- Output file is in binary format, located on: ~\micropython\ports\stm32\build-ARCADE
- To run on ARCADE, you need to convert the binary file to UF2 file. (https://github.com/Microsoft/uf2)
- The address to start application is 0x08010000.

Test.py is a driver that included for:
- Accelerometer
- Buzzer
- Led
- Button
- ServoMoto
- For Display: The backlight is connected to pin N18_BL (or PC7).
	+ Turn on:
		machine.Pin(machine.Pin.board.N18_BL,machine.Pin.IN,machine.Pin.PULL_UP)
	+ Turn off:
		machine.Pin(machine.Pin.board.N18_BL,machine.Pin.IN,machine.Pin.PULL_DOWN)
	+ For other functions, there is a good link for reference: https://github.com/GuyCarver/MicroPython/blob/master/lib/ST7735.py
	