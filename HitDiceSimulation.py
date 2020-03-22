
import sys
from random import randint as rdi


def dice_drop_low(dice: int) -> int:
	first_roll = rdi(1, dice)
	return first_roll if first_roll > 2 else rdi(1, dice)


def dice_drop_low_truncated(dice: int, half: int) -> int:
	first_roll = rdi(1, dice)
	return first_roll if first_roll > 2 else min(rdi(1, dice), half)


def calculate_hit_points_original(dice: int, level: int) -> int:
	increase = int(dice/2) + 1
	return dice + increase*(level-1)


def calculate_hit_points_hard(dice: int, level: int, iterations: int) -> int:
	result_pool = 0
	for _ in range(iterations):
		result_pool += dice + sum([rdi(1, dice) for _ in range(level-1)])
	return int(result_pool/iterations)


def calculate_hit_points_drop_low(dice: int, level: int, iterations: int) -> int:
	result_pool = 0
	for _ in range(iterations):
		result_pool += dice + sum([dice_drop_low(dice) for _ in range(level-1)])
	return int(result_pool/iterations)


def calculate_hit_points_drop_truncated(dice: int, level: int, iterations: int) -> int:
	result_pool = 0
	half = int(dice/2) + 1
	for _ in range(iterations):
		result_pool += dice + sum([dice_drop_low_truncated(dice, half) for _ in range(level-1)])
	return int(result_pool/iterations)


def calculate_hit_points_drop_truncated_low(dice: int, level: int, iterations: int) -> int:
	result_pool = 0
	half = int(dice/2)
	for _ in range(iterations):
		result_pool += dice + sum([dice_drop_low_truncated(dice, half) for _ in range(level-1)])
	return int(result_pool/iterations)


if __name__ == '__main__':
	dice_sides = int(sys.argv[1])
	character_level = int(sys.argv[2])
	iterations = int(sys.argv[3])

	fair_hit_points = calculate_hit_points_original(dice_sides, character_level)
	print("fair hit points:", fair_hit_points)
	hard_hit_points = calculate_hit_points_hard(dice_sides, character_level, iterations)
	print("hard hit points:", hard_hit_points)
	drop_low_hit_points = calculate_hit_points_drop_low(dice_sides, character_level, iterations)
	print("drop low hit points:", drop_low_hit_points)
	drop_truncated_hit_points = calculate_hit_points_drop_truncated(dice_sides, character_level, iterations)
	print("drop truncated hit points:", drop_truncated_hit_points)
	drop_truncated_low_hit_points = calculate_hit_points_drop_truncated_low(dice_sides, character_level, iterations)
	print("drop truncated low hit points:", drop_truncated_low_hit_points)