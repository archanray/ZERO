import datetime
import threading as td
import time

import numpy as np
from ouimeaux.environment import Environment


class wemo_accessor:
  def __init__(self):
    # Init the enviroment.
    self.env = Environment()
    self.env.start()
    self.env.discover(seconds=2)
    self.sleep_time = 2

  def schedule_switch(self, switch_name, schedule):
    """
    switch_name: String
    schedule: numpy array
    """
    switch = self.env.get_switch(switch_name)
    # Schedule
    does_reset = False
    current_hour = 0
    while (not does_reset):
      # current_hour = datetime.datetime.now().second
      if schedule[current_hour % 24] == 1:
        switch.on()
      else:
        switch.off()
      does_reset = ((current_hour % 24) == 23)
      print (current_hour, schedule[current_hour % 24])
      time.sleep(self.sleep_time)
      current_hour += 1
    switch.off()


  def schedule_policies(self, policies):
    """
    policies: Dictionary
    """
    print (policies)
    daemon_threads = []
    for switch, schedule in policies.items():
      thread = td.Thread(target=self.schedule_switch, args=(switch, schedule, ))
      daemon_threads.append(thread)

    for thread in daemon_threads:
      thread.start()


if __name__ == '__main__':
  schedule = np.zeros(24)
  schedule[18] = 1
  wa = wemo_accessor()
  schedule2 = np.zeros(24)
  schedule2[16] = 1
  wa.schedule_policies({'Ambati-Switch': schedule2, "Testing": schedule})
