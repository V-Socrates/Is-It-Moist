# It-is-Moist
###### Moisture Detector

## Table Of Contents
1. [Description](#Description)
2. [Required Hardware / Software](#required-hardware-/-software)
3. [Hardware Assembly](#hardware-assembly)
4. [Software Setup](#software-setup)
5. [Initial Startup](#initial-startup)
6. [Comments](#comments)


### Description
Is It Moist is a simple moisture sensor using a Raspberry Pi 3.

### Required Hardware / Software
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
* [USB Mouse](https://raw.githubusercontent.com/V-Socrates/It-is-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/USB%20Mouse.jpeg)
* [HDMI Cable](https://raw.githubusercontent.com/V-Socrates/It-is-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/HDMI%20Cable.jpg)
#### Software
* [Rasbian OS (Currently Using Stretch 2017-11-29)](https://drive.google.com/file/d/1Ecotum-11qHcblA57sbwOcbmJJJ9XkQF/view?usp=sharing)
* [Etcher](https://etcher.io/)
### Hardware Assembly
Use the following design if you are building the curcuit with adafruit's T-Cobbler Plus
![alt text](https://raw.githubusercontent.com/V-Socrates/It-is-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/Is%20It%20Moist%20(T-Cobbler).png)

Use the following design if you are building the curcuit without adafruit's T-Cobbler Plus
![alt text](https://raw.githubusercontent.com/V-Socrates/It-is-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/Is%20It%20Moist.jpg)
### Software Setup
Now that the circuit is built, it is time to setup your Micro SD card. The first step is to download the [Raspbian OS](https://drive.google.com/file/d/1Ecotum-11qHcblA57sbwOcbmJJJ9XkQF/view?usp=sharing) and [Etcher](https://etcher.io/). Plugin your Micro SD card into your card reader and plug it into your computer and follow the steps below.

Run Etcher and click "Select image".
![alt text](https://raw.githubusercontent.com/V-Socrates/It-is-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/Etcher1.PNG)

Navigate to your downloaded Rasbian OS, select it and click "Open"
![alt text](https://raw.githubusercontent.com/V-Socrates/It-is-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/Etcher3.PNG)

Now click "Change".
![alt text](https://raw.githubusercontent.com/V-Socrates/It-is-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/Etcher1.PNG)

From the displayed list select your Micro SD card and click "Continue".
![alt text](https://raw.githubusercontent.com/V-Socrates/It-is-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/Etcher2.PNG)

After selecting your Rasbian OS and your Micro SD card, click "Flash!".
![alt text](https://raw.githubusercontent.com/V-Socrates/It-is-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/Etcher1.PNG)

The flashing of the Rasbian OS may take several minutes depending on you system and Micro SD card. After it is completed you will see the following screen below.
![alt text](https://raw.githubusercontent.com/V-Socrates/It-is-Moist/master/Documentation/IMAGES-VIDEOS/Build%20Related/Etcher4.PNG)

You are now ready to startup your Raspberry Pi.

### Initial Startup

### Comments
