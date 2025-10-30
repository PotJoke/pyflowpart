#Basic python libs
from os import system, name
import math
import random
import urllib.request

#Pillow
from PIL import Image, ImageFont, ImageDraw, ImageEnhance

#OpenCV
import cv2
import numpy

def logo():
	print("██████╗  █████╗ ██████╗ ████████╗██╗ ██████╗██╗     ███████╗                 ")
	print("██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║██╔════╝██║     ██╔════╝                 ")
	print("██████╔╝███████║██████╔╝   ██║   ██║██║     ██║     █████╗                   ")
	print("██╔═══╝ ██╔══██║██╔══██╗   ██║   ██║██║     ██║     ██╔══╝                   ")
	print("██║     ██║  ██║██║  ██║   ██║   ██║╚██████╗███████╗███████╗                 ")
	print("╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝╚══════╝╚══════╝                 ")
	print("                                                                             ")
	print(" ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ ")
	print("██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗")
	print("██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝")
	print("██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗")
	print("╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║")
	print(" ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝")
	print("                                                                   By PotJoke")

#--------------------------------------------------------

#Class for particle
class Particle:
	def __init__(self, posX, posY, size, spread):
		self.posX = posX
		self.posY = posY
		self.size = size
		self.direction = random.uniform(-spread, spread)
		self.start_frame = random.randint(0, length)

#Project variables
output_name = "output"
scr_size_x = 1920
scr_size_y = 1080
framerate = 30
length_seconds = 4
ptc_status = "default"
bg_color = "green"

try:
	ptc = Image.open("example.png")
	ptc = ptc.resize((100,100))
except FileNotFoundError:
	reserv = Image.new('RGBA', (100, 100), color = "white")
	ptc = reserv

flow_type = "(source) up-down"
particle_size = 100
particle_spread = 2
particle_count = 60
particle_speed = 20

#Messages
Error_Number = "[!] Error: Invalid number"

#--------------------------------------------------------

#Main menu
def menu():
	clear()
	print(f"[1] Output name: {output_name}")
	print(f"[2] Size: {scr_size_x}x{scr_size_y}")
	print(f"[3] Length: {length_seconds}")
	print(f"[4] Framerate: {framerate}")
	print(f"[5] Background color: {bg_color}")
	print(f"[6] Flow type: {flow_type}")
	print(f"[7] Particle texture: {ptc_status}")
	print(f"[8] Particle spread: {particle_spread}")
	print(f"[9] Particle size: {particle_size}")
	print(f"[10] Total particle count: {particle_count}")
	print(f"[11] Particle speed: {particle_speed}")
	print(f"")
	print(f"[0] Render")
	print(f"\n ------------------------- \n")

	try:
		selection = int(input("[*] Enter selection: "))
		if selection in range(0, 12):
			if selection == 1:
				set_output()
			elif selection == 2:
				set_scr_size()
			elif selection == 3:
				set_length()
			elif selection == 4:
				set_framerate()
			elif selection == 5:
				set_color()
			elif selection == 6:
				set_flow_type()
			elif selection == 7:
				set_image()
			elif selection == 8:
				set_spread()
			elif selection == 9:
				set_prt_size()
			elif selection == 10:
				set_amount()
			elif selection == 11:
				set_speed()
			elif selection == 0:
				generation()

		else:
			clear()
			print("[!] Error: not a valid number")
			menu()

	except ValueError:
		clear()
		print("[!] Error: Not a valid number")
		menu()

#Output name
def set_output():
	global output_name
	clear()
	output_name = str(input("[#] Enter new output name (ex. file): "))
	menu()

#Screen size
def set_scr_size():
	global scr_size_x
	global scr_size_y
	clear()
	try:

		scr_size_x = int(input("[#] Enter width in pixels: "))

		if scr_size_x > 0:
			try:
				scr_size_y = int(input("[#] Enter height in pixels: "))
				if scr_size_y > 0:
					menu()
				elif scr_size_y < 0:
					clear()
					set_scr_size()				

			except ValueError:
				clear()
				set_scr_size()				

		elif scr_size_x < 0:
			clear()
			set_scr_size()

	except ValueError:
		clear()
		set_scr_size()	

#Length of video in seconds
def set_length():
	global length_seconds
	clear()
	try:

		length_seconds = int(input("[#] Enter length of video in seconds: "))

		if length_seconds > 0:
			menu()

		elif length_seconds < 0:
			clear()
			set_length()

	except ValueError:
		clear()
		set_length()

#Framerate
def set_framerate():
	global framerate
	clear()
	try:
		framerate = int(input("[#] Enter new framerate: "))
		if framerate > 0:
			menu()
		elif framerate < 0:
			clear()
			set_framerate()
			
	except ValueError:
		clear()
		set_framerate() 

#Background color
def set_color():
	global bg_color
	clear()
	bg_color = str(input("Input background color (green, red, yellow, blue): "))

	if bg_color in ["green", "red", "yellow", "blue"]:
		menu()
	elif bg_color not in ["green", "red", "yellow", "blue"]:
		clear()
		print("Error: not a valid color")
		set_color()

#Flow type
def set_flow_type():
	clear()
	print(f"\n ------------------------- \n")
	print(f"[1] Source presets")
	print(f"[2] Wave presets")
	print(f"[3] Double wave presets")
	print(f"\n ------------------------- \n")

	try:
		selection = int(input("[#] Select flow type: "))
		if selection in range(1, 4):
			if selection == 1:
				set_flow_source()

			elif selection == 2:
				set_flow_wave()

			elif selection == 3:
				set_flow_double_wave()

		else:
			clear()
			set_flow_type()
			
	except ValueError:
		clear()
		set_flow_type()

def set_flow_source():
	global flow_type
	clear()
	print(f"\n ------------------------- \n")
	print(f"[1] (source) up-down")
	print(f"[2] (source) down-up")
	print(f"[3] (source) left-right")
	print(f"[4] (source) right-left")
	print(f"\n ------------------------- \n")

	try:
		selection = int(input("[#] Select flow type: "))
		if selection in range(1, 5):
			if selection == 1:
				flow_type = "(source) up-down"
				menu()
			elif selection == 2:
				flow_type = "(source) down-up"
				menu()
			elif selection == 3:
				flow_type = "(source) left-right"
				menu()
			elif selection == 4:
				flow_type = "(source) right-left"
				menu()

		else:
			clear()
			set_flow_source()
			
	except ValueError:
		clear()
		set_flow_source()

def set_flow_wave():
	global flow_type
	clear()
	print(f"\n ------------------------- \n")
	print(f"[1] (wave) up-down")
	print(f"[2] (wave) down-up")
	print(f"[3] (wave) left-right")
	print(f"[4] (wave) right-left")
	print(f"\n ------------------------- \n")

	try:
		selection = int(input("[#] Select flow type: "))
		if selection in range(1, 5):
			if selection == 1:
				flow_type = "(wave) up-down"
				menu()
			elif selection == 2:
				flow_type = "(wave) down-up"
				menu()
			elif selection == 3:
				flow_type = "(wave) left-right"
				menu()
			elif selection == 4:
				flow_type = "(wave) right-left"
				menu()

		else:
			clear()
			set_flow_wave()
			
	except ValueError:
		clear()
		set_flow_wave()

def set_flow_double_wave():
	global flow_type
	clear()
	print(f"\n ------------------------- \n")
	print(f"[1] (double wave) up-down")
	print(f"[2] (double wave) down-up")
	print(f"[3] (double wave) left-right")
	print(f"[4] (double wave) right-left")
	print(f"\n ------------------------- \n")

	try:
		selection = int(input("[#] Select flow type: "))
		if selection in range(1, 5):
			if selection == 1:
				flow_type = "(double wave) up-down"
				menu()
			elif selection == 2:
				flow_type = "(double wave) down-up"
				menu()
			elif selection == 3:
				flow_type = "(double wave) left-right"
				menu()
			elif selection == 4:
				flow_type = "(double wave) right-left"
				menu()

		else:
			clear()
			set_flow_double_wave()
			
	except ValueError:
		clear()
		set_flow_double_wave()

#Particle texture
def set_image():
	clear()
	print(f"\n ------------------------- \n")
	print(f"[1] Use local image")
	print(f"[2] Use web url")
	print(f"\n ------------------------- \n")

	try:
		selection = int(input("[*] Enter selection: "))
		if selection in [1, 2]:
			if selection == 1:
				img_local()
			elif selection == 2:
				img_web()
		else:
			clear()
			set_image()

	except ValueError:
		clear()
		menu()

def img_local():
	global ptc
	global ptc_status
	clear()
	try:
		ptc = Image.open(input("[!] Enter particle file: "))
		ptc_status = "local image(changed)"
		menu()
	except ValueError:
		pass
		img_local()

def img_web():
	global ptc
	global ptc_status
	clear()
	try:
		ptc = Image.open(urllib.request.urlopen(input("[#] Enter url: ")))
		ptc_status = "web image(changed)"
		menu()
	except ValueError:
		pass
		img_web()

#Particle spread
def set_spread():
	global particle_spread
	clear()
	try:
		particle_spread = int(input("[#] Enter new spread amount: "))
		if particle_spread > 0:
			menu()
		elif particle_spread < 0:
			clear()
			set_spread()
	except ValueError:
		clear()
		set_spread()

#Particle size
def set_prt_size():
	global particle_size
	clear()
	try:

		particle_size = int(input("[#] Enter size of particles in pixels: "))

		if particle_size > 0:
			menu()

		elif particle_size < 0:
			clear()
			set_prt_size()

	except ValueError:
		clear()
		set_prt_size()

#Total amount of particles
def set_amount():
	global particle_count
	clear()
	try:
		particle_count = int(input("[#] Enter new total amount: "))
		if particle_count > 0:
			menu()
		elif particle_count < 0:
			clear()
			set_amount()

	except ValueError:
		clear()
		set_amount()

#Speed of particles
def set_speed():
	global particle_speed
	clear()
	try:
		particle_speed = int(input("[#] Enter new speed: "))
		menu()
	except ValueError:
		clear()
		set_speed()

#Video Render
def generation():
	clear()
	global length
	global ptc
	resize_ptc()
	length = length_seconds * framerate
	video = cv2.VideoWriter(f'{output_name}.avi', cv2.VideoWriter_fourcc(*'DIVX'), framerate, (scr_size_x, scr_size_y))

	if flow_type == "(source) up-down" or flow_type == "(wave) up-down" or flow_type == "(double wave) up-down":
		particles = [Particle(scr_size_x/2-particle_size/2, 0, particle_size, particle_spread) for i in range(particle_count)]

	elif flow_type == "(source) down-up" or flow_type == "(wave) down-up" or flow_type == "(double wave) down-up":
		particles = [Particle(scr_size_x/2-particle_size/2, scr_size_y - particle_size, particle_size, particle_spread) for i in range(particle_count)]

	elif flow_type == "(source) left-right" or flow_type == "(wave) left-right" or flow_type == "(double wave) left-right":
		particles = [Particle(0, scr_size_y/2-particle_size/2, particle_size, particle_spread) for i in range(particle_count)]

	elif flow_type == "(source) right-left" or flow_type == "(wave) right-left" or flow_type == "(double wave) right-left":
		particles = [Particle(scr_size_x-particle_size, scr_size_y/2-particle_size/2, particle_size, particle_spread) for i in range(particle_count)]

	else:
		particles = [Particle(scr_size_x/2-particle_size/2, 0, particle_size, particle_spread) for i in range(particle_count)]

	current_frame = 0
	while current_frame < length:
		img = Image.new('RGB', (scr_size_x, scr_size_y), color = bg_color)
		draw = ImageDraw.Draw(img)

		for i in particles:
			if current_frame >= i.start_frame:

				frame = current_frame - i.start_frame

				if flow_type == "(source) up-down":
					positionX = int(i.posX + i.direction * math.sqrt(frame) * 20)
					positionY = int(i.posY + frame * particle_speed)

				elif flow_type == "(source) down-up":
					positionX = int(i.posX + i.direction * math.sqrt(frame) * 20)
					positionY = int(i.posY - frame * particle_speed)

				elif flow_type == "(source) left-right":
					positionX = int(i.posX + frame * particle_speed)
					positionY = int(i.posY + i.direction * math.sqrt(frame) * 20)

				elif flow_type == "(source) right-left":
					positionX = int(i.posX - frame * particle_speed)
					positionY = int(i.posY + i.direction * math.sqrt(frame) * 20)

				elif flow_type == "(wave) up-down":
					positionX = int(i.posX + math.cos(frame * 0.1) * 200)
					positionY = int(i.posY + frame * particle_speed)

				elif flow_type == "(wave) down-up":
					positionX = int(i.posX + math.cos(frame * 0.1) * 200)
					positionY = int(i.posY - frame * particle_speed)

				elif flow_type == "(wave) left-right":
					positionX = int(i.posX + frame * particle_speed)
					positionY = int(i.posY + math.cos(frame * 0.1) * 200)

				elif flow_type == "(wave) right-left":
					positionX = int(i.posX - frame * particle_speed)
					positionY = int(i.posY + math.cos(frame * 0.1) * 200)

				elif flow_type == "(double wave) up-down":
					positionX = int(i.posX + i.direction * math.cos(frame * 0.1) * 200)
					positionY = int(i.posY + frame * particle_speed)

				elif flow_type == "(double wave) down-up":
					positionX = int(i.posX + i.direction * math.cos(frame * 0.1) * 200)
					positionY = int(i.posY - frame * particle_speed)

				elif flow_type == "(double wave) left-right":
					positionX = int(i.posX + frame * particle_speed)
					positionY = int(i.posY + i.direction * math.cos(frame * 0.1) * 200)

				elif flow_type == "(double wave) right-left":
					positionX = int(i.posX - frame * particle_speed)
					positionY = int(i.posY + i.direction * math.cos(frame * 0.1) * 200)

				else:
					positionX = int(i.posX + i.direction * math.sqrt(frame) * 20)
					positionY = int(i.posY + frame * particle_speed)

				if ptc.has_transparency_data:
					img.paste(ptc, (positionX, positionY), ptc)
				else:
					img.paste(ptc, (positionX, positionY))

			else:
				pass

		video.write(numpy.array(img)[:, :, ::-1].copy())

		print(f"Render progress: {current_frame} of {length}")

		current_frame+=1

	placeholder = input("Done! Please press ENTER to return main menu")

	menu()

def resize_ptc():
	global ptc
	width, height = ptc.size
	ptc = ptc.resize((particle_size, int(height / (width / particle_size))))

#Clear console
def clear():
	#Windows
	if name == 'nt':
		_ = system('cls')
	#Linux
	else:
		_ = system('clear')
	logo()
	print(f"\n ------------------------- \n")

#Start here
clear()
print(logo)
menu()