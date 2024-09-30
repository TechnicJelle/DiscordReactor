#!/usr/bin/env python3

import sys

emojiDict = {
	"II": [":pause_button:"],
	"OK": [":ok:"],
	"WC": [":wc:"],
	"A": [":regional_indicator_a:", ":a:", ":arrow_up_small:", ":small_red_triangle:"],
	"B": [":regional_indicator_b:", ":b:"],
	"C": [":regional_indicator_c:", ":copyright:"],
	"D": [":regional_indicator_d:", ":arrow_forward:"],
	"E": [":regional_indicator_e:", ":e_mail:"],
	"F": [":regional_indicator_f:"],
	"G": [":regional_indicator_g:"],
	"H": [":regional_indicator_h:", ":hash:", ":hotel:", ":love_hotel:"],
	"I": [":information_source:", ":regional_indicator_i:"],
	"J": [":regional_indicator_j:"],
	"K": [":regional_indicator_k:"],
	"L": [":regional_indicator_l:", ":clock3:", ":alarm_clock:", ":school:"],
	"M": [":regional_indicator_m:", ":m:", ":scorpius:", ":virgo:"],
	"N": [":regional_indicator_n:", ":capricorn:"],
	"O": [":regional_indicator_o:", ":o2:", ":o:", ":record_button:", ":arrows_counterclockwise:", ":repeat:", ":globe_with_meridians:", ":repeat_one:"],
	"P": [":regional_indicator_p:", ":parking:"],
	"Q": [":regional_indicator_q:"],
	"R": [":regional_indicator_r:", ":registered:"],
	"S": [":regional_indicator_s:", ":heavy_dollar_sign:", ":moneybag:", ":dollar:"],
	"T": [":regional_indicator_t:", ":cross:"],
	"U": [":regional_indicator_u:"],
	"V": [":regional_indicator_v:", ":aries:", ":ballot_box_with_check:", ":white_check_mark:", ":heavy_check_mark:"],
	"W": [":regional_indicator_w:", ":wavy_dash:"],
	"X": [":regional_indicator_x:", ":negative_squared_cross_mark:", ":x:", ":heavy_multiplication_x:"],
	"Y": [":regional_indicator_y:", ":yen:"],
	"Z": [":regional_indicator_z:"],
	" ": [":black_small_square:", ":black_medium_small_square:", ":black_medium_square:", ":black_large_square:"],
	"1": [":one:", ":first_place:"],
	"2": [":two:", ":second_place:"],
	"3": [":three:", ":third_place:"],
	"4": [":four:"],
	"5": [":five:"],
	"6": [":six:"],
	"7": [":seven:"],
	"8": [":eight:", ":8ball:"],
	"9": [":nine:"],
	"0": [":zero:"]
}

def text2emoji(inp):
	inp = inp.upper()

	i = 0
	result = ""

	while i < len(inp):
		substitute = None
		lettersToAdd = 0

		for original, substitutes in emojiDict.items():
			if len(substitutes) == 0:
				continue

			lettersToAdd = len(original)
			lettersLeft = len(inp) - i

			if lettersToAdd > lettersLeft:
				continue

			if original == inp[i:i + len(original)]:
				substitute = substitutes.pop(0)

				break

		if substitute is None:
			char = inp[i]

			if char == ' ':
				print("Impossibility at space")
			else:
				print("Impossibility at letter " + char)

			return "Impossible message!"

		result += substitute + " "
		i += lettersToAdd

	result = result.strip()

	return result

if len(sys.argv) > 1:
	originalMessage = ""
	for i in range(1, len(sys.argv)):
		originalMessage += sys.argv[i] + " "
	originalMessage = originalMessage.strip()
else:
	originalMessage = input("Message to turn into Discord react emojis: ")
endString = text2emoji(originalMessage)
print(endString)
