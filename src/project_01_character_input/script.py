"""
Milestone Year Calculator
------------------------
A CLI utility that calculates the specific year a user will turn 100 
based on their current age and the current system date.
"""

from datetime import date

def birthday_message(name: str, year: int) -> str:
	message = f'Hello, {name}. You will turn 100 in the year {year}'
	return message

def cal_century_year(age: int) -> int:
	""" Calculates the year the user reaches 100. """
	current_year = date.today().year
	return (100 - age) + current_year

def get_valid_age(prompt: str) -> int:
	""" Validates the age prompt is non negative number. """
	
	while True:
		raw_input = input(prompt)
		try:
			age = int(raw_input)
			# Non negative validation
			if age < 0:
				print("Error: Age cannot be negative. Try again.")
				continue
			return age

		except ValueError:
			print(f"Error: '{raw_input}' is not a valid number. Please use digits.")

def run_milestone_app():
	""" Logs to the console the name of the user and the year they turn 100. """
	name_prompt = str(input('Enter your name: '))
	age_prompt = get_valid_age('Enter your age: ')
	century_year = cal_century_year(age_prompt)
	result_str = birthday_message(name_prompt, century_year)
	print(result_str)

if __name__ == "__main__":
	run_milestone_app()