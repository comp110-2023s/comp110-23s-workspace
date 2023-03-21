"""Practice with Dictionaries!"""

def zip(dict_one: list[str], dict_two: list[int]) -> dict: 
	"returns a dictionary"
	final_dict = {}
	if len(dict_one) == len(dict_two):
		for key in dict_one:
			for value in dict_two:
				final_dict[key] = value
		return final_dict 
	else:
		return dict()
