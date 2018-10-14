import glob
import math
import time

import numpy as np

import wemo_access

location, priority, appliances, _priority_list, appliance_objects = None, None, None, None, None
#max_val = None

def isin(element, test_elements, assume_unique=False, invert=False):
    #"..."
    element = np.asarray(element)
    return np.in1d(element, test_elements, assume_unique=assume_unique,
                invert=invert).reshape(element.shape)

def get_daily_rates(location, date):
	_electricity_rate = np.load('erate_simplified.npy')
	_clean_e_percentage = np.load('fuel_mix_simplified.npy')
	
	_electricity_rate = _electricity_rate/np.max(_electricity_rate)
	#print _electricity_rate

	return _electricity_rate, _clean_e_percentage

'''
_cost_function is a global function
'''
def _cost_function(_electricity_rate, _clean_e_percentage, _priority_list):
	'''
	INPUTs:
	_electricity_rate: 1D array of 24 values.
	_clean_e_percentage: 1D array of 24 values.
	_priority_list: 1D array of 2 values
	OUTPUTs:
	_cost: 1D array of 24 values
	'''
	_global_cost = _priority_list[0]*_electricity_rate + _priority_list[1]*(1-_clean_e_percentage)
	_sorted_ids = np.argsort(_global_cost)

	#print _global_cost
	#print _sorted_ids
	return _global_cost, _sorted_ids

'''
_find_best_slot is defined within ??
'''
def _find_best_slot(_sorted_ids, _ids_for_usage_based_on_window):
	_check_position = isin(_sorted_ids, _ids_for_usage_based_on_window)

	_check_position = np.array(_check_position.astype(int))

	#print len(_sorted_ids), len(_check_position)
	_usage_hours = _sorted_ids*_check_position
	_ids_of_usage_hours = np.nonzero(_usage_hours)
	_usage_hours_final_list = _usage_hours[_ids_of_usage_hours]

	return _usage_hours_final_list
'''
_recompute is defined in ??
'''
def _recompute(_global_cost, _operating_duration):
	_convolution_window = np.ones((math.ceil(_operating_duration)))
	_frac, _whole = math.modf(_operating_duration)
	if _frac == 0:
		_frac = 1
	_convolution_window[0] = _convolution_window[0]*_frac

	_altered_global_cost = list(_global_cost)
	_altered_global_cost.append(_global_cost[-1])
	_altered_global_cost = [_global_cost[0]] + _altered_global_cost
	_altered_global_cost = np.asarray(_altered_global_cost)
	_altered_global_cost = _altered_global_cost[0]

	#print 'convolution_window is: '+str(_convolution_window)
	#print '_altered_global_cost: '+str(_altered_global_cost)
	_new_global_cost = np.convolve(_convolution_window, _altered_global_cost, 'same')

	_new_global_cost = _new_global_cost[1:-1]
	_new_sorted_ids = np.argsort(_new_global_cost)
	
	return _new_global_cost, _new_sorted_ids

def first_run_init(_passed_location, _passed_appliances, _passed_priority):
	"""
	First run initailization. Instantiate all appliances and save priority preferences. 
	Inputs:
	location: tuple of latitiude and longitude
	appliances: a dictionary of appliances with the following name as key and value as a tuple of following format: (switch_id, differablility, interruptable, usage_window, operating_duration, electricity_consumption)
	priority: what the user prioritizes for optimization. Can be cost, clean_energy or both
	"""
	global location, priority, appliances, _priority_list, appliance_objects
	appliance_objects = {}
	location, priority, appliances = _passed_location, _passed_priority, _passed_appliances
	if priority == 'both':
		_priority_list = 0.5*np.ones((2))
	elif priority == '_electricity_rate':
		_priority_list = np.array([1,0])
	else:
		_priority_list = np.array([0,1])

	#print _priority_list

	for name in appliances.keys():
		appliance_objects[name] = appliance(appliances[name])

	pass


def daily_policy_update():
	date = None
	_electricity_rate, _clean_e_percentage = get_daily_rates(location, date)
	_global_cost, _sorted_ids = _cost_function(_electricity_rate, _clean_e_percentage, _priority_list)
	
	policies = {}

	for name in appliance_objects.keys():
		policies[name] = appliance_objects[name]._optimizer_function(_global_cost, _sorted_ids)
	
	return policies


'''
FROM SOURABH
'''


class appliance:
	"""
	An appliance in the smart home framework.
	"""
	def __init__(self, args):
		"""
		Initialize an appliance.

		Inputs:
		- name: name of the appliance.
		- switch_id: identifier of smart switch to which the appliance is connected to. 
		- differablility: Specifies weather the appliance can be scheduled or not. Can take three values: differable, semi_differable, non_differable
		- usage_window: time window specified by user during which appliance should operate. 1D array with 24 values
		- operating_duration: time required for a single operation of the appliance. Integer specifing number of hours.
		- electricity_consumption: electricity consumed in a single operation of the appliance

		"""
		#self.name = name
		self.switch_id = args[0] #switch_id
		self.differablility = args[1] #differablility
		self.interruptable = args[2] #interruptable
		self.usage_window = args[3] #usage_window
		self.operating_duration = args[4] #operating_duration
		self.electricity_consumption = args[5] #electricity_consumption

		self.policy = np.zeros(24)

	def _optimizer_function(self, _global_cost, _sorted_ids):
		'''
		INPUTs:
		_global_cost: 1D array of 24 values (optimal cost suckers)
		_sorted_ids: sorted indices of _global_cost (from min to max dummy!)
		OUTPUTs:
		_usage_flaggers: 1D array of 24 values
		'''
		_usage_window = self.usage_window
		_operating_duration = self.operating_duration
		_interrupt = self.interruptable
		
		_ids_for_usage_based_on_window = np.nonzero(_usage_window)
		
		# choose according to the case that if the service can be converted
		_usage_flaggers = np.zeros((len(_usage_window)))
		if _interrupt:
			_usage_hours_final_list = _find_best_slot(_sorted_ids, _ids_for_usage_based_on_window)
			
			if _operating_duration <= 1:
				_usage_flaggers[_usage_hours_final_list[0]] = 1
			else:
				count = 0
				while _operating_duration > 0:
					_usage_flaggers[_usage_hours_final_list[count]] = 1
					_operating_duration -= 1
					count += 1
					pass
			pass
		else:
			# recompute the _global_cost based on usage window.
			if _operating_duration <= 1:
				_reval_global_cost = _global_cost
				_reval_sorted_ids = _sorted_ids
				
				_usage_hours_final_list = _find_best_slot(_reval_sorted_ids, _ids_for_usage_based_on_window)
				_usage_flaggers[_usage_hours_final_list[0]] = 1
				pass
			else:
				_reval_global_cost, _reval_sorted_ids = _recompute(_global_cost, _operating_duration)

				_usage_hours_final_list = _find_best_slot(_reval_sorted_ids, _ids_for_usage_based_on_window)
				_usage_flaggers[_usage_hours_final_list[0]] = 1
				pass
			pass
		
		return _usage_flaggers


def parse_user_input(input_data, key):
  # Load input
	time_slots = input_data[key]['Time slots']
	time_slots = time_slots.split(",")
	usage_window = np.zeros(24)
	for slot in time_slots:
		time_range = slot.split("-")
		if len(time_range) == 1:
			usage_window[int(time_range[0])] = 1
		else:
			low, high = int(time_range[0]), int(time_range[1])
		for i in range(low, high+1):
			usage_window[i] = 1

  # Weekdays
	days_window = np.zeros(7)
	day_slots = input_data[key]['Day']
	day_slots = day_slots.split(",")
	for slot in day_slots:
		day_range = slot.split("-")
		if len(day_range) == 1:
			wk_day = time.strptime(day_range[0][0:3], '%a').tm_wday
			days_window[wk_day] = 1
		else:
			low, high = time.strptime(day_range[0][0:3], '%a').tm_wday, time.strptime(day_range[1][0:3], '%a').tm_wday
		for i in range(low, high+1):
			days_window[i] = 1

  	# Duration
	duration = int(input_data[key]['Duration'])

	# Interruptible
	interupt = (input_data[key]['Interruptable'] == 'Yes')

	# Priority
	priority = input_data[key]['Priority']
	tup = ('0', interupt, True, usage_window, duration, 'high') 
	return key, tup, days_window, priority

# Create some appliances (switch_id, differablility, interruptable, usage_window, operating_duration, electricity_consumption)
appliances = {}

input_data = glob.glob("./input_data/*.npy")
input_data = np.load(input_data[0]).item()
device_keys = list(input_data.keys())
mode = "both"

for key in device_keys:
	device, tup, days_window, mode = parse_user_input(input_data, key)
	appliances[key] = tup

print (appliances)
# appliances['Heater'] =  ('1', 1, True, usage_window, 5, 'high') 
# appliances['AC'] = ('2', 1, True, usage_window1, 8, 'high')
#appliances['EV'] = ('3', 1, True, usage_window, 8, 'high')

first_run_init('new_england', appliances, '_electricity_rate')
policies = daily_policy_update()

for name in policies.keys():
	# print ('Appliance:', name, 'On time(s): ', policies[name])
	print (np.nonzero(policies[name]))

scheduler = wemo_access.wemo_accessor()
scheduler.schedule_policies(policies)
