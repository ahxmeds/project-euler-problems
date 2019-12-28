#Died writing this code. Still not complete. Will think of an easier solution later.


import time
import numpy as np


def convert_face_to_value(card_values):
	for i in range(len(card_values)):
		if card_values[i] == 'T':
			card_values[i] = '10'
		elif card_values[i] == 'J':
			card_values[i] = '11'
		elif card_values[i] == 'Q':
			card_values[i] = '12'
		elif card_values[i] == 'K':
			card_values[i] = '13'
		elif card_values[i] == 'A':
			card_values[i] = '14'
		else:
			pass
	return card_values

def get_card_values(card1, card2, card3, card4, card5):
	card_values = [card1[0], card2[0], card3[0], card4[0], card5[0]]
	card_values = convert_face_to_value(card_values)
	card_values.sort()
	return card_values

def is_one_pair(card1, card2, card3, card4, card5):
	card_values = get_card_values(card1, card2, card3, card4, card5)
	if card_values[0] == card_values[1]:
		if card_values[1] < card_values[2] < card_values[3] < card_values[4]:
			return True
		else:
			return False
	else:
		if card_values[1] == card_values[2]:
			if card_values[2] < card_values[3] < card_values[4]:
				return True
			else:
				return False
		else:
			if card_values[2] == card_values[3]:
				if card_values[3] < card_values[4]:
					return True
				else:
					return False
			else:
				if card_values[3] < card_values[4]:
					return True
				else:
					return False


def is_two_pairs(card1, card2, card3, card4, card5):
	card_values = get_card_values(card1, card2, card3, card4, card5)
	if card_values[0] == card_values[1]:
		if card_values[2] == card_values[3]:
			if card_values[1] < card_values[3] < card_values[4]:
				return True
			else:
				return False
		else:
			if card_values[3] == card_values[4] and card_values[1] < card_values[2] < card_values[3]:
				return True
			else:
				return False
	else:
		if card_values[1] == card_values[2] and card_values[3] == card_values[4] and card_values[2] < card_values[3]:
			return True
		else:
			return False

def is_three_of_a_kind(card1, card2, card3, card4, card5):
	card_values = get_card_values(card1, card2, card3, card4, card5)
	if card_values[0] == card_values[1]:
		if card_values[1] == card_values[2] and card_values[2] < card_values[3] < card_values[4]:
			return True
		else:
			return False
	else:
		if card_values[1] == card_values[2]:
			if card_values[2] == card_values[3] and card_values[3] < card_values[4]:
				return True
			else:
				return False
		else:
			if card_values[2] == card_values[3] == card_values[4] and card_values[1] < card_values[4]:
				return True
			else:
				return False



def is_full_house(card1, card2, card3, card4, card5):
	card_values = get_card_values(card1, card2, card3, card4, card5)
	if card_values[0] == card_values[1]:
		if card_values[1] == card_values[2]:
			if card_values[3] == card_values[4] and card_values[0] != card_values[4]:
				return True
		else:
			if card_values[2] == card_values[3] == card_values[4]:
				return True
			else:
				return False
	else:
		return False


def is_four_of_a_kind(card1, card2, card3, card4, card5):
	card_values = get_card_values(card1, card2, card3, card4, card5)
	if card_values[0] != card_values[1]:
		if card_values[1] == card_values[2] == card_values[3] == card_values[4]:
			return True
		else:
			return False
	else:
		if card_values[0] == card_values[1] == card_values[2] == card_values[3]:
			return True
		else:
			return False


def is_straight(card1, card2, card3, card4, card5):
	card_values = get_card_values(card1, card2, card3, card4, card5) 
	for i in range(0, len(card_values)-1):
		if int(card_values[i+1]) - int(card_values[i]) != 1:
			return False
	return True


def is_straight_flush(card1, card2, card3, card4, card5):
	if is_flush(card1, card2, card3, card4, card5):
		if is_straight(card1, card2, card3, card4, card5):
			return True
	return False


def is_flush(card1, card2, card3, card4, card5):
	if card1[1] == card2[1] == card3[1] == card4[1] == card5[1]:
		return True
	else:
		return False

def is_royal_flush(card1, card2, card3, card4, card5):
	royal_flush_set = set(['T','J', 'Q', 'K', 'A'])
	if set([card1[0], card2[0], card3[0], card4[0], card5[0]]) == royal_flush_set:
		if is_same_suit(card1, card2, card3, card4, card5):
			return True
	return False




def get_rank(hand):
	card1 = hand[0]
	card2 = hand[1]
	card3 = hand[2]
	card4 = hand[3]
	card5 = hand[4]

	if is_royal_flush(card1, card2, card3, card4, card5):
		return 10
	elif is_straight_flush(card1, card2, card3, card4, card5):
		return 9
	elif is_four_of_a_kind(card1, card2, card3, card4, card5):
		return 8
	elif is_full_house(card1, card2, card3, card4, card5):
		return 7
	elif is_flush(card1, card2, card3, card4, card5):
		return 6
	elif is_straight(card1, card2, card3, card4, card5):
		return 5
	elif is_three_of_a_kind(card1, card2, card3, card4, card5):
		return 4
	elif is_two_pairs(card1, card2, card3, card4, card5):
		return 3
	elif is_one_pair(card1, card2, card3, card4, card5):
		return 2
	else:
		return 1


def find_winner(hand1, hand2):
	p1card1 = hand1[0]
	p1card2 = hand1[1]
	p1card3 = hand1[2]
	p1card4 = hand1[3]
	p1card5 = hand1[4]
	p2card1 = hand2[0]
	p2card2 = hand2[1]
	p2card3 = hand2[2]
	p2card4 = hand2[3]
	p2card5 = hand2[4]

	if is_royal_flush(p1card1, p1card2, p1card3, p1card4, p1card5) == True and is_royal_flush(p2card1, p2card2, p2card3, p2card4, p2card5) == True:
		if is_straight_flush(p1card1, p1card2, p1card3, p1card4, p1card5) == True and is_straight_flush(p2card1, p2card2, p2card3, p2card4, p2card5) == True:
			if is_four_of_a_kind(p1card1, p1card2, p1card3, p1card4, p1card5) == True and is_four_of_a_kind(p2card1, p2card2, p2card3, p2card4, p2card5) == True:
				if is_full_house(p1card1, p1card2, p1card3, p1card4, p1card5) == True and is_full_house(p2card1, p2card2, p2card3, p2card4, p2card5) == True:
					if is_flush(p1card1, p1card2, p1card3, p1card4, p1card5) == True and is_flush(p2card1, p2card2, p2card3, p2card4, p2card5) == True:
						if is_straight(p1card1, p1card2, p1card3, p1card4, p1card5) == True and is_straight(p2card1, p2card2, p2card3, p2card4, p2card5) == True:
							if is_three_of_a_kind(p1card1, p1card2, p1card3, p1card4, p1card5) == True and is_three_of_a_kind(p2card1, p2card2, p2card3, p2card4, p2card5) == True:
							elif is_three_of_a_kind(p1card1, p1card2, p1card3, p1card4, p1card5) == True or is_three_of_a_kind(p2card1, p2card2, p2card3, p2card4, p2card5) == True:
						elif is_straight(p1card1, p1card2, p1card3, p1card4, p1card5) == True or is_straight(p2card1, p2card2, p2card3, p2card4, p2card5) == True:
					elif is_flush(p1card1, p1card2, p1card3, p1card4, p1card5) == True or is_flush(p2card1, p2card2, p2card3, p2card4, p2card5) == True:
				elif is_full_house(p1card1, p1card2, p1card3, p1card4, p1card5) == True or is_full_house(p2card1, p2card2, p2card3, p2card4, p2card5) == True:
			elif is_four_of_a_kind(p1card1, p1card2, p1card3, p1card4, p1card5) == True or is_four_of_a_kind(p2card1, p2card2, p2card3, p2card4, p2card5) == True:
		elif is_straight_flush(p1card1, p1card2, p1card3, p1card4, p1card5) == True or is_straight_flush(p2card1, p2card2, p2card3, p2card4, p2card5) == True:
	elif is_royal_flush(p1card1, p1card2, p1card3, p1card4, p1card5) == True or is_royal_flush(p2card1, p2card2, p2card3, p2card4, p2card5) == True:


rfile = open("PE054.txt", "r")

file_data = rfile.readlines()

#print(file_data)

player1 = []
player2 = []

#print(file_data[0])

for i in range(len(file_data)):
	array1 = file_data[i][0:14].split(" ")
	player1.append(array1)
	array2 = file_data[i][15:29].split(" ")
	player2.append(array2)

hand = ['TS', 'KS', 'JS', 'AS', 'QS']
print(is_three_of_a_kind('AS', 'QS', '9S', 'AS', 'AS'))

#print(player2[0][0])
#for i in player1:
#	print(i)