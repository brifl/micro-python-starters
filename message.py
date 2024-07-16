from machine import Pin
import time

# Define the LED pin
led = Pin(17, Pin.OUT)

# Define Morse code dictionary
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': ' '
}

# Define Morse code timing (seconds)
DOT_DURATION = 0.2
DASH_DURATION = 0.6
LETTER_SPACE = 0.6
WORD_SPACE = 1.4

# Define the message to blink
message = "HELLO WORLD"

def blink_dot():
    led.on()
    time.sleep(DOT_DURATION)
    led.off()
    time.sleep(DOT_DURATION)

def blink_dash():
    led.on()
    time.sleep(DASH_DURATION)
    led.off()
    time.sleep(DOT_DURATION)

def blink_morse_code(message):
    for letter in message:
        code = morse_code.get(letter.upper(), '')
        for symbol in code:
            if symbol == '.':
                blink_dot()
            elif symbol == '-':
                blink_dash()
        time.sleep(LETTER_SPACE)
        if letter == ' ':
            time.sleep(WORD_SPACE - LETTER_SPACE)

# Run the Morse code blink
blink_morse_code(message)
