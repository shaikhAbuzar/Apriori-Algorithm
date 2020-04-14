from itertools import combinations

no_transac = int(input('No. of transactions: '))  # 4
transactions = {}  # {'t1': ['I1', 'I2', 'I5'], 't2': ['I2', 'I4'], 't3': ['I2', 'I3'], 't4': ['I1', 'I2', 'I4'], 't5': ['I1', 'I3'], 't6': ['I2', 'I3'], 't7': ['I1', 'I3'], 't8': ['I1', 'I2', 'I3', 'I5'], 't9': ['I1', 'I2', 'I3']}
items_list = []  # ['I1', 'I2', 'I3', 'I4', 'I5']
for i in range(no_transac):
	items = list(input(f't{i + 1} items: ').split())
	for item in items:
		if item in items_list:
			continue
		else:
			items_list.append(item)
	transactions[f't{i + 1}'] = items
support_count = int(input('Support Count: '))  # 2

candidate = {}
large_itemset_old = {}
iterator = 1
while True and len(items_list) >= iterator:
	large_itemset = {}
	item_combos = list(combinations(items_list, iterator))
	item_combos_list = []
	for item_combo in item_combos:
		candidate[f'{list(item_combo)}'] = 0
		item_combos_list.append(list(item_combo))

	for item_combo in item_combos_list:
		count = 0
		for transaction in list(transactions.values()):
			flag = 1
			for item in item_combo:
				if item in transaction:
					continue
				else:
					flag = 0
					break
			if flag == 1:
				candidate[f'{item_combo}'] += 1

	for candidate_key, candidate_value in candidate.items():
		if candidate_value >= support_count:
			large_itemset[candidate_key] = candidate_value

	if large_itemset == {}:
		break

	large_itemset_old = large_itemset
	temp_list = list(large_itemset.keys())
	for i in range(len(temp_list)):
		element = list(temp_list[i][1:-1].split(', '))
		# print(element)
		for j in range(len(element)):
			element[j] = element[j][1:-1]
		temp_list[i] = element
	candidate = {}
	iterator += 1
	items_list = []
	for item_combo in temp_list:
		for item in item_combo:
			if item not in items_list:
				items_list.append(item)
	# print(large_itemset_old)

print('\nFINAL RESULT')
for keys, values in large_itemset_old.items():
	print(f'| {{{keys[1:-1]}}} | {values} |')
