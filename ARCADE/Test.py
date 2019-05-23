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

class ServoMoto(object):
	# There is a bug, Servo1 and Servo2 are swapped.
	SERVO2 = machine.Pin(machine.Pin.board.SERVO1)
	SERVO1 = machine.Pin(machine.Pin.board.SERVO2)
	Positional = 0
	Continuous = 1

	def __init__( self, pin):
		self.pin = pin
		self.timer = Timer(2, freq=(1 / 0.020))
		
		# SERVO1 PA1 channel 2
		# SERVO2 PA0 channel 1
		ch = 2;
		if (pin == ServoMoto.SERVO2): 
			ch = 1

		self.channel = self.timer.channel(ch, Timer.PWM, pin=self.pin)
		self.channel.pulse_width_percent(0)
		self.ConfigurePulseParameters(1.0, 2.0)
		self.ConfigureAsPositional(False)

	def ConfigureAsPositional(self, inverted):
		self.type = ServoMoto.Positional
		self.invertServo = inverted

	def ConfigureAsContinuous(self, inverted):
		self.type = ServoMoto.Continuous
		self.invertServo = inverted

	def ConfigurePulseParameters(self, minimumPulseWidth, maximumPulseWidth):
		self.minPulseLength = minimumPulseWidth * 1.0
		self.maxPulseLength = maximumPulseWidth * 1.0
		
	def Set(self, value):
		if (self.type == ServoMoto.Positional):
			self.__FixedSetPosition__(value)
		else:
			self.__ContiniousSetSpeed__(value)

	def __ContiniousSetSpeed__(self, speed):
		if speed < -100 or speed > 100:
			print("speed", "degrees must be between -100 and 100.")

		speed += 100
		d = speed / 200.0 * 180
		self.__FixedSetPosition__(d)

	def __FixedSetPosition__(self, position):
		position = position * 1.0
		if position < 0 or position > 180 :
			print("degrees", "degrees must be between 0 and 180.")

		if (self.invertServo == True):
			position = 180 - position

		# Typically, with 50 hz, 0 degree is 0.05 and 180 degrees is 0.10
		# double duty = ((position / 180.0) * (0.10 - 0.05)) + 0.05
		duty = ((position / 180.0) * (self.maxPulseLength / 20 - self.minPulseLength / 20)) + self.minPulseLength / 20

		# TinyCLR 0 < duty < 1. Convert to 0->100
		self.channel.pulse_width_percent(duty * 100)

	def Stop(self):
		self.channel.pulse_width_percent(0)