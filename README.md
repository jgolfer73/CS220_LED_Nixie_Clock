# CS220_LED_Nixie_Clock

Jacob Moebius
CS 220
12/18/20
Final Project – Raspberry Pi
LED Nixie Clock

# Introduction

	The project is an LED conversion of a Nixie clock. Nixie clocks typically use Nixie tubes widely used between the 1920’s to 1960’s. None have been produced since the 1990’s. These Nixie tubes have 10 wires, 1 for each number, enclosed in a neon filled tube. When the wires have current passed through them, they ionize the gas around them, causing the gas to light up in the shape of the wire. In the case of a clock, the wires are bent in to the shape of numbers 0-9. Simply, the Nixie tubes are replaced by LEDs and acrylic plates, and the clock is run by a program on a Raspberry Pi with the GPIO pins connecting the Raspberry Pi to the number modules.

# Hardware

Swapping the Nixie tubes out for LEDs is straight forward. Using the limited I/O pins on the Raspberry Pi is less so. The Raspberry Pi has 28 I/O pins on its GPIO pins. For a HH:mm clock format, each digit needs 10 LEDs for a total of 40 LEDs plus a colon or some other potential light separating the hours and minutes if desired. For RGB LEDs (https://www.adafruit.com/product/315), there’s an additional 2 wires per LED needed to select the color. In total 123 I/O is needed for the clock. To simplify this, one could provide a common wire for each color with a wire leading from an I/O pin to two groups of 5 common anodes on the LEDs. This alone reduces the I/O to 44 required for the LEDs. For simplicity though, the LEDs are not grouped and left as 10 individual LEDs, generating an I/O requirement of 52 pins. Next a shift register is required to multiplex the RGB pins. A Mux16 was used instead (https://www.sparkfun.com/products/9056 ), as it was quicker to pick-up and go, but a standard shift register (i.e. 74HC595) would be better suited for this project. This is due to the Mux output on each pin being momentary. A shift register can have latching outputs on each pin. Because a Mux was used and this property was found out late in the project, the clock only handles blue light emission by being wired to ground instead of the Mux. The remaining colors are left unused and the remaining anodes are wired up with no changes.

Acrylic plates (https://www.mcmaster.com/8560K239/) are laser etched and cut to be installed on the LED array. The light shines up through the LED plate without leaking to other acrylic plates in a process called light piping. Because the index of refraction of the acrylic is greater than the index of refraction of the air, the light bounces off of the boundary between the acrylic and air, after entering from the bottom of the acrylic plate, and continues in the acrylic until the top of the acrylic plate is reached. ABS is used as a top plate with slits to absorb errant light.

	The Raspberry Pi has a Broadcom BCM2837B0, Cortex-A53 (ARMv8) 64-bit processor operating at 1.4GHz. It has 1GB of RAM and 40 I/O pins. An Adafruit Pi T-Cobbler Plus – GPIO Breakout board (https://www.adafruit.com/product/2028) was used to interface the GPIO pins with a full sized breadboard. Using Ohm’s law, Power= 〖Current〗^2*Resistance, 4 LEDs running at the same time (2 for showing the hour, 2 for showing the minute) dissipates 120mW, uses 16mA (limited by the GPIO pins), and has a 39Ω resistor. Total power consumed is 130mW. Surface mount LEDs would have a brighter output without the focusing lens, allowing for a 5mA LED replacement to reduce the power requirement to 121mW. Not a significant savings, but is still an improvement. The Raspberry Pi 3B+ at 1.9W can be swapped for a Raspberry Pi Zero W at 0.7W (https://www.pidramble.com/wiki/benchmarks/power-consumption).

# Software

	Python was used to program the clock. Python is pre-packaged with Raspberry Pi’s and is extremely well documented both for the language itself as well as in use with the Raspberry Pi. Having learned it in the past, it was easy to pick up again, even after years of not using it. These reasons are why Python was used.
	Raspbian OS was used as it allowed for a Python IDE for coding and a command line for executing the code.
	Raspberry Pi has a library to use its GPIO pins. The sys, datetime, and time libraries are used for error handling, clock info fetching, and program block timing respectively. All of this is part of a standard library for either Raspberry Pi or Python. No other libraries were used.
	One could easily repurpose this into other data displays, such as temperature for the local weather. Just fetch the relevant info from the internet, parse it, and light up the corresponding LEDs.
