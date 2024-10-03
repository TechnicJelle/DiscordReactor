#!/usr/bin/env python3

import sys

emojiDict = {
	"II": [":pause_button:"],
	"ID": [":id:"],
	"OFF": [":mobile_phone_off:"],
	"VS": [":vs:"],
	"AB": [":ab:"],
	"CL": [":cl:"],
	"SOS": [":sos:"],
	"ATM": [":atm:"],
	"WC": [":wc:"],
	"ABC": [":abc:"],
	"NG": [":ng:"],
	"OK": [":ok:"],
	"UP": [":up:"],
	"COOL": [":cool:"],
	"NEW": [":new:"],
	"FREE": [":free:"],
	"END": [":end:"],
	"BACK": [":back:"],
	"ON": [":on:"],
	"TOP": [":top:"],
	"SOON": [":soon:"],
	"ZZZ": [":zzz:"],
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
	"M": [":regional_indicator_m:", ":m:", ":part_alternation_mark:", ":scorpius:", ":virgo:"],
	"N": [":regional_indicator_n:", ":capricorn:"],
	"O": [":regional_indicator_o:", ":o2:", ":o:", ":ring_buoy:", ":record_button:", ":arrows_counterclockwise:", ":repeat:", ":globe_with_meridians:", ":repeat_one:"],
	"P": [":regional_indicator_p:", ":parking:"],
	"Q": [":regional_indicator_q:"],
	"R": [":regional_indicator_r:", ":registered:"],
	"S": [":regional_indicator_s:", ":moneybag:", ":heavy_dollar_sign:", ":dollar:"],
	"T": [":regional_indicator_t:", ":cross:"],
	"U": [":regional_indicator_u:", ":ophiuchus:"],
	"V": [":regional_indicator_v:", ":aries:", ":ballot_box_with_check:", ":white_check_mark:", ":heavy_check_mark:"],
	"W": [":regional_indicator_w:", ":wavy_dash:"],
	"X": [":regional_indicator_x:", ":negative_squared_cross_mark:", ":x:", ":heavy_multiplication_x:"],
	"Y": [":regional_indicator_y:", ":yen:"],
	"Z": [":regional_indicator_z:"],
	" ": [":black_small_square:", ":black_medium_small_square:", ":black_medium_square:", ":black_large_square:"],
	"10": [":keycap_ten:"],
	"17": [":date:", ":calendar:"],
	"18": [":underage:"],
	"24": [":convenience_store:"],
	"100": [":100:"],
	"777": [":slot_machine:"],
	"1": [":one:", ":first_place:"],
	"2": [":two:", ":second_place:"],
	"3": [":three:", ":third_place:"],
	"4": [":four:"],
	"5": [":five:"],
	"6": [":six:"],
	"7": [":seven:"],
	"8": [":eight:", ":8ball:"],
	"9": [":nine:"],
	"0": [":zero:"],
	"!!": [":bangbang:"],
	"!?": [":interrobang:"],
	"!": [":exclamation:", ":grey_exclamation:"],
	"?": [":question:", ":grey_question:"],
}


def text2emojis(inpOriginal: str) -> list[str] | None:
	inp: str = inpOriginal.upper()

	# Loop over all keys with substitutes in the dict and see if they match a part of the input.
	# If they do, add the substitute to the result and move on to the next letter.
	# If they don't, the message is impossible to convert.

	i: int = 0
	result: list[str] = []

	while i < len(inp):  # Not a for-loop because `i` increments in irregular steps, manually.
		substitute: str | None = None
		lettersToAdd: int = 0

		for key, substitutes in emojiDict.items():
			if len(substitutes) == 0:
				continue  # This key has no substitutes left, but we do not break entirely yet, because there may still be other keys with substitutes left.

			lettersToAdd: int = len(key)
			lettersLeft: int = len(inp) - i

			if lettersToAdd > lettersLeft:
				continue  # We're trying a long key, but there are not enough letters left in the input, so let's try the next key. It may be sorter and be a match.

			if key == inp[i:i + len(key)]:
				substitute: str | None = substitutes.pop(0)
				break

		if substitute is None:  # No key had any substitutes left, so we have an impossible message.
			char: str = inpOriginal[i]
			if char == ' ': char = "space"
			print("Not enough emojis exist to convert all the \"" + char + "\"s in your message...")
			return None

		# We have a substitute, so let's add it to the result and move on to the next letter.
		result.append(substitute)
		i += lettersToAdd

	return result


originalMessage: str = " ".join(sys.argv[1:]) \
	if len(sys.argv) > 1 \
	else input("Message to turn into Discord react emojis: ")

emojis: list[str] | None = text2emojis(originalMessage)

if emojis is None:
	print("\033[91mImpossible to convert message to emojis.\033[0m")
	exit(1)
else:
	endString: str = " ".join(emojis)
	print(endString)
