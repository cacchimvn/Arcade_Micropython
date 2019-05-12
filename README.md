This is a basic MicroPython board definition the ARCADE, using UF2 bootloader.


To build the project, you need:
- Original micropython repository: https://github.com/micropython/micropython
- Download this repository into folder : ~\micropython\ports\stm32\boards
- cd ARCADE
- Run make. (This step will overwrite some files need to be reconfig for ARCADE)
- Back to: ~\micropython\ports\
- Follow instructions from micropython repository to build ARCADE.

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
	