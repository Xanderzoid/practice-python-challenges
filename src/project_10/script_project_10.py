"""
List Overlap Comprehensions
---------------------------
A CLI app that randomly rolls 4 1D3, 2 1D6, and 1 1d12 100 times. Displays there numbers in commmon with the dice sets and state the proabilities of the most rolled numbers. Note for the sake of learning I increaed the program requriments.
"""

import random

# Globle Constants
INTRO_MSG = "Displays there numbers in commmon with the dice sets and state the proabilities of the most rolled numbers.\n"
MAX_DATASET = 100
MAX_SAMPLE = 10


# Input: None
# Process: Generate 300 dice rolls, compare dice list , compute probailties
def roll_any_die(die: int, num: int, x: int) -> dict:
    """Rolls 'num' number of 'die' (die number) 'x' amount of times. Returns number distrubution."""
    # Initialize dict
    max_num = num * die
    result_dict = {}
    for i in range(1, max_num + 1):
        result_dict[f"{i}"] = 0
    # Roll dice x times
    for _ in range(x):
        num_on_die = 0
        # Roll set of dice
        for _ in range(num):
            die_roll = random.randint(1, die)
            num_on_die += die_roll
        result_dict[f"{num_on_die}"] += 1
    return result_dict


def roll_dataset(dataset_size: int) -> dict:
    """Returns a dict of dict of 3 dice rolled 'dataset_size' times."""
    result_dict = {}
    dataset_4D3 = roll_any_die(3, 4, dataset_size)
    dataset_2D6 = roll_any_die(6, 2, dataset_size)
    dataset_1D12 = roll_any_die(12, 1, dataset_size)
    result_dict["4D3"] = dataset_4D3
    result_dict["2D6"] = dataset_2D6
    result_dict["1D12"] = dataset_1D12
    return result_dict


def avg_dataset(dataset: dict) -> float:
    num_of_rolls = 0
    total = 0
    for key, value in dataset.items():
        total += int(key) * value
        num_of_rolls += value
    return round(total / num_of_rolls, 1)


def min_max_dataset(dataset: dict) -> dict:
    """
    Returns lists of {key: value} for all items matching the absolute min and max.
    Time: O(n) | Space: O(n)
    """
    if not dataset:
        return {"min": [], "max": []}

    # Step 1: Find the actual min and max values O(n)
    vals = dataset.values()
    min_val = min(vals)
    max_val = max(vals)

    # Step 2: Collect all items matching those values O(n)
    min_items = [{k: v} for k, v in dataset.items() if v == min_val]
    max_items = [{k: v} for k, v in dataset.items() if v == max_val]

    return {"min": min_items, "max": max_items}


def merge_dataset(all_datasets: dict) -> dict:
    """Returns the combined total rolls of datasets with the same keys."""
    data_values = []
    merged_dataset = {}
    for value in all_datasets.values():
        data_values.append(value)
    for data in data_values:
        for key, value in data.items():
            if key in merged_dataset:
                merged_dataset[key] += value
            else:
                merged_dataset[key] = value
    return merged_dataset


def dice_stats(all_datasets: dict) -> dict:
    """Return a dict of stats of the sample dataset dice rolls."""
    # Each die stat
    merged_dataset = merge_dataset(all_datasets)
    full_dataset = all_datasets
    full_dataset["merged"] = merged_dataset
    result_dict = {}
    for key, value in full_dataset.items():
        avg = avg_dataset(value)
        min_max = min_max_dataset(value)
        min_max["avg"] = avg
        result_dict[f"{key}"] = min_max
    return result_dict


def generate_roll_list(dice: int, num_dice: int, size: int) -> list:
    result_list = []
    for _ in range(size):
        roll_total = 0
        for _ in range(num_dice):
            dice_roll = random.randint(1, dice)
            roll_total += dice_roll
        result_list.append(roll_total)
    return result_list


def merged_proabilities(dataset: dict) -> dict:
    total_num_rolls = MAX_DATASET
    prob_dict = {}
    for key, value in dataset["merged"].items():
        prob_dict[key] = round((value / total_num_rolls) * 100, 1)
    return prob_dict


# Output: Display intro, truncated dice rolls, and dice stats


def msg_stats(dataset: dict, data_stats: dict) -> str:
    """Retuen the stats for diced rolled."""
    # Visulize rolls for each die
    size = 10
    list_4D3 = generate_roll_list(3, 4, size)
    list_2D6 = generate_roll_list(6, 2, size)
    list_1D12 = generate_roll_list(12, 1, size)
    prob_dict = merged_proabilities(dataset)

    visualize_msg = f"Truncated example lists:\n4D3:  {list_4D3}\n2D6:  {list_2D6}\n1D12: {list_1D12}"
    # Roll data
    stat_msg = "\nStats of 100 dice rolls per dice set:"
    stat_str_4D3 = f"4D3  AVG: {data_stats['4D3']['avg']} MIN: {data_stats['4D3']['min']} MAX: {data_stats['4D3']['max']}"
    stat_str_2D6 = f"2D6  AVG: {data_stats['2D6']['avg']} MIN: {data_stats['2D6']['min']} MAX: {data_stats['2D6']['max']}"
    stat_str_1D12 = f"1D12 AVG: {data_stats['1D12']['avg']} MIN: {data_stats['1D12']['min']} MAX: {data_stats['1D12']['max']}"
    stat_str_merged = f"All  AVG: {data_stats['merged']['avg']} MIN: {data_stats['merged']['min']} MAX: {data_stats['merged']['max']}"
    prob_str_merged = f"\nThe proabilities of number rolled for All:\n{prob_dict}"

    stat_list = [
        visualize_msg,
        stat_msg,
        stat_str_4D3,
        stat_str_2D6,
        stat_str_1D12,
        stat_str_merged,
        prob_str_merged,
    ]
    result_str = "\n".join(stat_list)
    return result_str


def msg_logo() -> str:
    """Displays BLX Data.Mine logo."""
    ascii_art = """                 
                 ###                                       
                ##  #                                      
               ## ####                                     
              ##  #   #             =========================
             ## #### ###            B L X   D A T A . M I N E
            ##  #    #  #           =========================
           ## ####  ######                 [Est. 2026]       
          ##  #   ###     #                                
         ## #### ##  ##  ###                                """
    msg = "A CLI app that randomly rolls 4 1D3, 2 1D6, and 1 1d12 100 times."
    spacer = "-" * len(msg)
    return f"{ascii_art}\n{spacer}\n{msg}\n{spacer}"


def main() -> None:
    print(msg_logo())
    print(INTRO_MSG)
    dataset = roll_dataset(100)
    data_stats = dice_stats(dataset)
    print(msg_stats(dataset, data_stats))


if __name__ == "__main__":
    main()
