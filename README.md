# Zero: Energy Resource Optimizer

In this project, we design a system which can help individuals optimize cost effectiveness of their electricity usage. While this seems pretty selfish, we demonstrate methods to minimize the effects of selfish consumption. This would eventually help aggregate consumption over a demography.

## Libraries you'd need
1. `python 3.5`
2. `numpy`
3. `math`
4. `ouimeaux`
5. `Tkinter` (choose according to your system, there exists a myraid of choices)
6. `Blas` (you can use OpenBlas)

Ways to install `ouimeaux`:
1. `git pull` from `https://github.com/iancmcc/ouimeaux`
2. Fix issues metioned in: `https://github.com/iancmcc/ouimeaux/issues/177`


## Files of grave importance
1. `fuelmix_parser.py`: Run this to collect the breakdown of energy sources per hour.
2. `erate_parser.py`: Run this to collect the per hour variable cost of electricity consumption for one region (here `western mass`).
3. `GUI.py`: Run this as `python3 GUI.py` to collect data from the users.
4. `optimizer.py`: Run this to get the policies you'd need to run. You should run this as a `cron` job in your Raspberry Pi. 
5. `zero_jupyter.ipynb`: This notebook gives a step-by-step information of `optimizer`'s code.
6. `report.pdf`: This is the report detailing the work done in the project. Please check the results and discussion section.
