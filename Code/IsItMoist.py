
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Software SPI configuration:
CLK  = 11
MISO = 9
MOSI = 10
CS   = 8
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)


# Print nice channel column headers.
print('|             {}             |'.format(*range(1)))
print('-' * 8)
# Main program loop.
while True:
    # Read all the ADC channel values in a list.
    values = [0] * 1
    for i in range(1):
        # The read_adc function will get the value of the specified channel (0-7).
        values[i] = mcp.read_adc(i)
        percent = 100 - int(round(values[i] - 280) / 7.43)
        #values[i] = 1023 - values[i]

    # Print the ADC values.
    print('\033[H\033[J')
    print('     Is It Moist?')
    print('*********************')
    print('Moisture ADC: {0}'.format(*values))
    print('Moisture Level: {0}%'.format(percent))
    print('*********************')

    # Measure every second
    time.sleep(0.5)
    print('\033[H\033[J')
