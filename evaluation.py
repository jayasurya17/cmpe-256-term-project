import pandas as pd

# Returns list of unique user IDs in the test dataset
def get_position(item_id_orig, items):
	for index, item_id in enumerate(items):
		if item_id == item_id_orig:
			return index + 1
	return -1

def evaluate_recommendation(recommendationMethod):
	test_data = pd.read_csv("./test_stratify.csv")
	rating_positions = []
	for index, row in test_data.iterrows():
		items = recommendationMethod(row)
		items = list(items)
		position = get_position(row['item_id'], items)
		rating_positions.append(position)
		print ("Test", index, ":", "Item ID", row['item_id'], "was recommended was your", position, "recommendation")

	return sum(rating_positions) / len(rating_positions)