"""
Base64 is a binary to text encoding used mainly by protocols like HTTP or SMTP which transfer reliably only text.
With this encoding binary data can be exchanged as text.

The encoding itself must choose characters which are common to other encodings (ASCII, UTF-8, etc.) and these
characters must be printable.

Index	Binary	Char	Index	Binary	Char	Index	Binary	Char    Index   Binary  Char
0	    000000	A	    16	    010000	Q	    32	    100000	g	    48	    110000	w
1	    000001	B	    17	    010001	R	    33	    100001	h	    49	    110001	x
2	    000010	C	    18	    010010	S	    34	    100010	i	    50	    110010	y
3	    000011	D	    19	    010011	T	    35	    100011	j	    51	    110011	z
4	    000100	E	    20	    010100	U	    36	    100100	k	    52	    110100	0
5	    000101	F	    21	    010101	V	    37	    100101	l	    53	    110101	1
6	    000110	G	    22	    010110	W	    38	    100110	m	    54	    110110	2
7	    000111	H	    23	    010111	X	    39	    100111	n	    55	    110111	3
8	    001000	I	    24	    011000	Y	    40	    101000	o	    56	    111000	4
9	    001001	J	    25	    011001	Z	    41	    101001	p	    57	    111001	5
10	    001010	K	    26	    011010	a	    42	    101010	q	    58	    111010	6
11	    001011	L	    27	    011011	b	    43	    101011	r	    59	    111011	7
12	    001100	M	    28	    011100	c	    44	    101100	s	    60	    111100	8
13	    001101	N	    29	    011101	d	    45	    101101	t	    61	    111101	9
14	    001110	O	    30	    011110	e	    46	    101110	u	    62	    111110	+
15	    001111	P	    31	    011111	f	    47	    101111	v	    63	    111111	/

Example:

data    = [0x31, 0x32, 0x33]
chars   = '1', '2', '3'
binary  = 00110001 00110010 00110011
base64  = 001100 010011 001000 110011
encoded = MTIz

"""

import binascii

# Basic operations
data = "\x31\x32\x33"
encoded = data.encode(encoding="base64")
print(encoded)
decoded = encoded.decode(encoding="base64")
print(decoded)


# Input stream is hex
# test = b"72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
# data = test.decode(encoding="hex")
# flag = data.encode(encoding="base64")
# print(flag)