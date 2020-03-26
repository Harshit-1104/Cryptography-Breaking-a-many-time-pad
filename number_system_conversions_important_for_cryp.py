######## to Hex and HEX to all other

import codecs
# it can do somethings but can also not do somethings

msg = 'attack at dawn' # the message

ascii_msg = codecs.encode(msg,'ascii')
# codecs work by using objects, msg is already in ascii but this converts it into an ascii object
ascii_msg

hex_msg = codecs.encode(ascii_msg,'hex')
# the ascii object converted to a hex one
len(hex_msg)

bin_msg = bin(int(hex_msg,16))
#direct xor is defined only over binary and hence ultimately everything must be converted to binary
bin_msg

ascii_msg2 = int(bin_msg,2)
#converts the binary into ascii integers
ascii_msg2 = str(ascii_msg2)
# while encoding. only strings are used
ascii_msg2 = codecs.encode(ascii_msg2,'ascii')
#creating an ascii object

len(str(ascii_msg2))

hex_msg2 = hex(ascii_msg2)
#this is then converted normally to hex
len(hex_msg2)
#this way of hex conversion adds 0x at the beginning and hence it must be omitted

msg2 = codecs.decode(hex_msg2[2:],'hex')
#simply decode the hex to get the real message
msg2
