import pandas as pd

# Returns list of unique user IDs in the test dataset
def get_position(item_id_test, items):
	for index, item_id in enumerate(items):
		if item_id in item_id_test:
			return index + 1
	return 0

def get_recommendations(userGroups, row, recommendationMethod, topValueCount):
	if row.name > topValueCount - 1:
		return 0
	recommendations = recommendationMethod(row)
	recommended_items = list(recommendations['item_id'])

	user_data = userGroups.get_group(row['user_id'])
	item_test = set(user_data['item_id'])
	position = get_position(item_test, recommended_items)
# 	print ("Test ID:", row.name + 1, "recommendation was found at position", position)
	return position

def evaluate_recommendation(recommendationMethod, topValueCount):
	test_data = pd.read_csv("../dataset/test.csv")
	if topValueCount == -1:
		topValueCount = len(test_data)
	user_groups = test_data.groupby(['user_id'])
	test_data['evaluation'] = test_data.apply(lambda x: get_recommendations(user_groups, x, recommendationMethod, topValueCount), axis = 1)
	counts = test_data['evaluation'].value_counts()
	number_of_predictions = len(test_data) - counts[0] 
	return {
        'average_of_recommendations': test_data['evaluation'].sum() / number_of_predictions, 
        'number_of_recommendations': number_of_predictions,
        'total_test_cases': topValueCount,
        '% of recommendations':  number_of_predictions / topValueCount * 100
    }