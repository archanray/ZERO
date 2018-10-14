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
1. `GUI.py`: Run this to collect data from the users.
2. `optimizer.py`: Run this to get the policies you'd need to run. You should run this as a `cron` job in your Raspberry Pi. 
3. `zero_jupyter.ipynb`: This notebook gives a step-by-step information of `optimizer`'s code.
