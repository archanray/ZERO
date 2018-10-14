import json
from collections import defaultdict
from datetime import datetime, timedelta

import iso8601
import numpy as np
import csv


def hour_rounder(t):
    # Rounds to nearest hour by adding a timedelta hour if minute >= 30
    return (t.replace(second=0, microsecond=0, minute=0, hour=t.hour)
               +timedelta(hours=t.minute//59))

def read_json(file):
	"""
	file: File name
	rtype: List[dict]
	"""
	json_file = open(file)
	json_str = json_file.read()
	json_data = json.loads(json_str)["GenFuelMixes"]["GenFuelMix"]
	return json_data

def map_json_data(json_data):
	"""
	json_data: List[dict]
	rtype: List[dict]
	"""
	# Transform json data to dictionary.
	fuel_mix_dict = {}
	for gen_fuel in json_data:
		key = gen_fuel["BeginDate"]
		category = gen_fuel["FuelCategoryRollup"]
		if not key in fuel_mix_dict:
			fuel_mix_dict[key] = defaultdict(int)
		fuel_mix_dict[key][category] += gen_fuel["GenMw"]
	# Transform values to percentages.
	fuel_mix_perc_list = [[] for _ in range(24)]
	for key, value in fuel_mix_dict.items():
		key_time = hour_rounder(iso8601.parse_date(key))
		key_time_hour = key_time.hour
		total = sum(value.values(), 0.0)
		percs = {k: v / total for k, v in value.items()}
		fuel_mix_perc_list[key_time_hour].append(percs['Natural Gas'])
	fuel_mix_perc_list = np.array(fuel_mix_perc_list)
	fuel_mix_perc_list = np.array([np.mean(np.array(arr)) for arr in fuel_mix_perc_list])
	np.save('./data/fmix_20181005.npy', fuel_mix_perc_list)


if __name__ == '__main__':
	json_data = read_json("./data/fuel-mix/20181005.json")
	map_json_data(json_data)
