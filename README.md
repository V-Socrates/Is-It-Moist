# Is It Moist
###### IOT Moisture Detector

## Table Of Contents
1. [Description](#description)
2. [Required Hardware and Software](#required-hardware-and-software)
3. [Hardware Assembly](#hardware-assembly)
4. [Software Setup](#software-setup)
5. [Initial Startup](#initial-startup)
6. [Resources](#resources)

### Description
Is It Moist is a simple moisture sensor using a Raspberry Pi 3.

### Required Hardware and Software
#### Hardware
* [Raspberry Pi 3 Model B](https://raw.githubusercontent.com/V-Socrates/It-is-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/Raspberry%20Pi%203%20Model%20B.jpg)
* [Raspberry Pi Power Adapter](https://raw.githubusercontent.com/V-Socrates/It-is-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/Raspberry%20Pi%20Power%20Supply.jpg)
* [adafruit Assembled Pi T-Cobbler Plus (Optional)](https://raw.githubusercontent.com/V-Socrates/It-is-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/Adafruit%20T-Cobbler%20Plus.jpg)
* [Micro SD Card (8GB)](https://raw.githubusercontent.com/V-Socrates/It-is-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/Micro%20SD%20Card.jpg)
* [Micro SD Card Reader](https://raw.githubusercontent.com/V-Socrates/It-is-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/Micro%20SD%20Card%20Reader.jpg)
* [MCP3008 Analog to Digital Converter](https://raw.githubusercontent.com/V-Socrates/It-is-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/MCP3008.jpg)
* [FC-28 (Moisture Sensor Probe)](https://raw.githubusercontent.com/V-Socrates/It-is-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/Moisture%20Sensor%20Probe.jpg)
* [Dual Output Module (Analog to Analog / Digital)](https://raw.githubusercontent.com/V-Socrates/It-is-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/Dual%20Output%20Module.jpg)
* [Jumper Wire Cables](https://raw.githubusercontent.com/V-Socrates/It-is-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/Jumper%20Wire.jpg)
* [USB Keyboard](https://raw.githubusercontent.com/V-Socrates/It-is-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/USB%20Keyboard.png)
* [Monitor](https://raw.githubusercontent.com/V-Socrates/It-is-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/Monitor.jpg) / [TV](https://raw.githubusercontent.com/V-Socrates/It-is-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/TV.jpg)
* [USB Mouse](https://raw.githubusercontent.com/V-Socrates/It-is-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/USB%20Mouse.jpeg)
* [HDMI Cable](https://raw.githubusercontent.com/V-Socrates/It-is-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/HDMI%20Cable.jpg)
#### Software
* [Raspbian OS (Currently Using Stretch 2017-11-29)](https://drive.google.com/file/d/1Ecotum-11qHcblA57sbwOcbmJJJ9XkQF/view?usp=sharing)
* [Etcher](https://etcher.io/)
#### Miscellaneous
* Internet Access (Ethernet / WiFi)
### Hardware Assembly
Use the following design if you are building the circuit with adafruit's T-Cobbler Plus.<br>
![alt text](https://raw.githubusercontent.com/V-Socrates/It-is-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/Is%20It%20Moist%20(T-Cobbler).png)

Use the following design if you are building the circuit without adafruit's T-Cobbler Plus.<br>
![alt text](https://raw.githubusercontent.com/V-Socrates/It-is-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/Is%20It%20Moist.jpg)
### Software Setup
Now that the circuit is built, it is time to setup your Micro SD card. The first step is to download the [Raspbian OS](https://drive.google.com/file/d/1Ecotum-11qHcblA57sbwOcbmJJJ9XkQF/view?usp=sharing) and [Etcher](https://etcher.io/). Make sure to download the version that is made for your OS. Plugin your Micro SD card into your card reader and plug it into your computer and follow the steps below.

Run Etcher and click "Select image".<br>
![alt text](https://raw.githubusercontent.com/V-Socrates/It-is-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/Etcher1.PNG)

Navigate to your downloaded Raspbian OS, select it and click "Open".<br>
![alt text](https://raw.githubusercontent.com/V-Socrates/It-is-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/Etcher3.PNG)

Now click "Change".<br>
![alt text](https://raw.githubusercontent.com/V-Socrates/It-is-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/Etcher1.PNG)

From the displayed list select your Micro SD card and click "Continue".<br>
![alt text](https://raw.githubusercontent.com/V-Socrates/It-is-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/Etcher2.PNG)

After selecting your Raspbian OS and your Micro SD card, click "Flash!".<br>
![alt text](https://raw.githubusercontent.com/V-Socrates/It-is-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/Etcher5.PNG)

The flashing of the Raspbian OS may take several minutes depending on you system and Micro SD card. After it is completed you will see the following screen below.<br>
![alt text](https://raw.githubusercontent.com/V-Socrates/It-is-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/Etcher4.PNG)

You are now ready to startup your Raspberry Pi.

### Initial Startup
Now that you Micro SD card is setup it is time to boot up your Raspberry Pi. Connect your Micro SD card, power adapter, HDMI cable, keyboard, and mouse to your Raspberry Pi. Connect the other end of you HDMI cable to you a monitor / TV. The initial startup may take several minutes.

After Booting into the OS, setup the WiFi. If you are connected to the internet using Ethernet you may skip this step. Select the WiFi button outlined in the image below.<br>
![alt text](https://raw.githubusercontent.com/V-Socrates/Is-It-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/RPI1.png)

Select your WiFi from the dropdown list.<br>
![alt text](https://raw.githubusercontent.com/V-Socrates/Is-It-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/RPI2.png)

Enter your WiFi password in the text field and click "OK". Allow a few moments for your Raspberry Pi to connect.<br>
![alt text](https://raw.githubusercontent.com/V-Socrates/Is-It-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/RPI3.png)

Open terminal highlighted in image and enter the following commands. The fist two commands may take time, so be patient.<br>
![alt text](https://raw.githubusercontent.com/V-Socrates/Is-It-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/RPI4.png)

```
wget https://raw.githubusercontent.com/V-Socrates/Is-It-Moist/master/Code/setup.sh
sudo bash setup.sh $USER
python IsItMoist.py
```
Congratulations your Is It Moist sensor is now operational.<br>
![alt text](https://raw.githubusercontent.com/V-Socrates/Is-It-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/RPI5.png)

### Resources
adafruit MCP3008 ([Site](https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/mcp3008) / [Repository](https://github.com/adafruit/Adafruit_Python_MCP3008))

[Raspberry Pi] Smarter Plants Tutorial ([Site](http://schiener.me/2015/raspberry-pi-smart-plant/) / [Repository](https://github.com/domschiener/smart-plant-raspberry))

Raspberry Pi Plant Pot Moisture Sensor with Email Notification Tutorial ([Site](https://www.modmypi.com/blog/raspberry-pi-plant-pot-moisture-sensor-with-email-notification-tutorial) / [Repository](https://github.com/modmypi/Moisture-Sensor))
