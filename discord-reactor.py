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

	# Loop over all keys with substitutes in the dict and see if they match a part of the input.
	# If they do, add the substitute to the result and move on to the next letter.
	# If they don't, the message is impossible to convert.

	i = 0
	result = ""

	while i < len(inp):  # Not a for-loop because `i` increments in irregular steps, manually.
		substitute = None
		lettersToAdd = 0

		for key, substitutes in emojiDict.items():
			if len(substitutes) == 0:
				continue  # This key has no substitutes left, but we do not break entirely yet, because there may still be other keys with substitutes left.

			lettersToAdd = len(key)
			lettersLeft = len(inp) - i

			if lettersToAdd > lettersLeft:
				continue  # We're trying a long key, but there are not enough letters left in the input, so let's try the next key. It may be sorter and be a match.

			if key == inp[i:i + len(key)]:
				substitute = substitutes.pop(0)

				break

		if substitute is None:  # No key had any substitutes left, so we have an impossible message.
			char = inp[i]

			if char == ' ':
				print("Impossibility at space")
			else:
				print("Impossibility at letter " + char)

			return "Impossible message!"

		# We have a substitute, so let's add it to the result and move on to the next letter.
		result += substitute + " "
		i += lettersToAdd

	result = result.strip()

	return result

if len(sys.argv) > 1:
	originalMessage = " ".join(sys.argv[1:])
else:
	originalMessage = input("Message to turn into Discord react emojis: ")
endString = text2emoji(originalMessage)
print(endString)
