from __future__ import division
import csv
import itertools



filepath = "resources/Transakcje.csv"

items = set() #list of items
item_count_dict = {} # how many items
item_list_dict = {} # dictionary (transaction_number, item) : item_quantity
transaction_quantity = 0
threshold = 0.5

with open(filepath) as f:
        for row in [content for content in csv.reader(f, delimiter='\n')]:
            for transaction in row:
                transaction_quantity += 1
                for item in transaction.split(','):
                    items.add(item)
items.remove('')

transaction_number = 0
with open(filepath) as f:
        for row in [content for content in csv.reader(f, delimiter='\n')]:
            for transaction in row:
                transaction_number += 1
                for item in items:
                    if item in transaction.split(','):
                        item_list_dict[(transaction_number, item)] = 1
                    else:
                        item_list_dict[(transaction_number, item)] = 0


# pojedyncze count percent

for item in items:
    item_count_dict[item] = 0
    for transaction, exists in item_list_dict.iteritems():
        if transaction[1] == item and exists:
            item_count_dict[item] += 1 / transaction_quantity

frequent_items = {}
for item in items:
    if item_count_dict[item] > threshold:
        frequent_items[item] = item_count_dict[item]

print("ZADANIE 1")
print(item_count_dict)
print(frequent_items)


# podwojne
item_pair_count = {}

item_set = set()
for x in itertools.permutations(items,2):
    item_set.add(x)

for item in item_set:
    item_pair_count[item] = (0, 0)
    first_item_counter = 0
    for l in range(1, transaction_quantity):
        if item_list_dict[(l, item[0])] or item_list_dict[(l, item[1])]:
            item_pair_count[item] = (item_pair_count[item][0] + 1/transaction_quantity, item_pair_count[item][1])
        if item_list_dict[(l, item[0])]:
            first_item_counter += 1

    for l in range(1, transaction_quantity):
        if item_list_dict[(l, item[0])]:
            if item_list_dict[(l, item[1])]:
                item_pair_count[item] = (item_pair_count[item][0], item_pair_count[item][1] + 1/first_item_counter)

print("ZADANIE 2")
print(item_pair_count)

frequent_pair_items = {}
for item in item_set:
    if item_pair_count[item][0] > threshold and item_pair_count[item][1] > threshold:
        frequent_pair_items[item] = item_pair_count[item]

print(frequent_pair_items)

# Ekwiwalentna transformacja klas
eclat = {}

for item in items:
    eclat[item] = list()
    for transaction, exists in item_list_dict.iteritems():
        if transaction[1] == item and exists:
            eclat[item].append(transaction[0])

print("ZADANIE 3")
print(eclat)

item_comb = set()
for x in itertools.combinations(items,2):
    item_comb.add(x)

item_intersection = {}
for item in item_comb:
    item_intersection[item] = set(eclat[item[0]]).intersection(eclat[item[1]])

print(item_intersection)