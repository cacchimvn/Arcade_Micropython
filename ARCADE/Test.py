from machine import Pin,I2C
from pyb import Timer
import time
import math
import machine
import array

class Accelerometer(object):
	def __init__( self):
		self.i2c = I2C(1,freq=400000)
		self.address = 0x1C
		self.buffer1 = bytearray(1)
		self.buffer2 = bytearray(2)
		self.__WriteRegister__(0x2A,b'1')

	def __WriteRegister__(self, register, aData):
		self.i2c.writeto_mem(self.address, register, aData)

	def __ReadRegisters__(self, register) :
		self.buffer1[0] = register
		self.i2c.writeto(self.address, self.buffer1, False)		
		return bytearray(self.i2c.readfrom(self.address, 2))

	def __ReadAxis__(self, register):
		self.buffer2 = self.__ReadRegisters__(register)
		value = ((self.buffer2[0] << 2) | (self.buffer2[1] >> 6)) * 1.0
		if (value > 511.0) :
			value -= 1024.0
		res = int((value / 256.0) * 100)
		if (res > 100):
			return 100
		if (res < -100):
			return -100
		return res

	def ReadY(self):
		return -1 * self.__ReadAxis__(0x01)

	def ReadX(self):
		return self.__ReadAxis__(0x03)

	def ReadZ(self):
		return -1 * self.__ReadAxis__(0x05)

class Buzzer(object):
	def __init__( self):
		self.pin = machine.Pin(machine.Pin.board.BUZZER)

	def StartBuzzing(self, frequency):
		self.timer = Timer(1, freq=frequency)
		self.channel = self.timer.channel(1, Timer.PWM, pin=self.pin)
		self.channel.pulse_width_percent(50)

	def StopBuzzing(self):
		self.channel.pulse_width_percent(0)

	def Beep(self):
		self.StartBuzzing(2500)
		time.sleep_ms(20)
		self.StopBuzzing()

class Led(object):
	RED = machine.Pin(machine.Pin.board.LED_RED)
	GREEN = machine.Pin(machine.Pin.board.LED_GREEN)

	def __init__( self, led):
		self.led = led

	def On(self):
		self.led.value(1)

	def Off(self):
		self.led.value(0)

class Button(object):
	UP = machine.Pin.board.U
	DOWN = machine.Pin.board.D
	LEF = machine.Pin.board.L
	RIGHT = machine.Pin.board.R
	A = machine.Pin.board.A
	B = machine.Pin.board.B
	MENU = machine.Pin.board.M
	START = machine.Pin.board.S

	def __init__( self, button):
		self.button = machine.Pin(button, machine.Pin.IN,machine.Pin.PULL_UP)

	def Read(self):
		return self.button.value()