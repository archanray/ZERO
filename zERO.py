import numpy as np 
location, priority, appliances = None, None, None

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

def first_run_init(location, appliances, priority):
    """
    First run initailization. Instantiate all appliances and save priority preferences. 
    Inputs:
    location: tuple of latitiude and longitude
    appliances: a dictionary of appliances with the following name as key and value as a tuple of following format: (switch_id, differablility, interruptable, usage_window, operating_duration, electricity_consumption)
    priority: what the user prioritizes for optimization. Can be cost, clean_energy or both
    """
    location, priority, appliances = location, priority, appliances

    for name in appliances.keys():
        name = appliance(appliances[name])


def daily_policy_update():
    _electricity_rate, _clean_e_percentage = get_daily_rates(location, date)
    _global_cost, _sorted_ids = _cost_function(_electricity_rate, _clean_e_percentage, priority)
    
    policies = {}

    for name in appliances.keys():
        policies[name] = name._optimizer_function(_global_cost, _sorted_ids)
    
    return policies

# Create some appliances (switch_id, differablility, interruptable, usage_window, operating_duration, electricity_consumption)
appliances = {}

usage_window = np.ones[(24)]

appliances['Heater'] = ('1', 1, True, usage_window, 4, 'high')
appliances['AC'] = ('2', 1, True, usage_window, 4, 'high')
appliances['EV'] = ('3', 'differable', usage_window, 5, 'high')

first_run_init('new_england', appliances, 'both')
policies = daily_policy_update()

for name in policies.keys():
    print ('Appliance:', name, 'On time(s): ', policies[name], '\n')
