# this script is to test in-line matplotlib plot display when using nvim in kitty

# steps:
# 1. config matplotlib backend in /.bashrc
# 2. open a second kitty terminal window as the target (shift+cmd+d to open on the right side vertically)
# 3. obtain $KITTY_WINDOW_ID, $KITTY_LISTEN_ON with `echo $KITTY_WINDOW_ID`, `echo $KITTY_LISTEN_ON`
# 4. activate the proper env. Check for matplotlib version: `conda list matplotlib`. If the backend is installed it'd show up as well
# 5. if the backend is not on the list, do `pip install matplotlib-backend-kitty`
# 6. if need to change the version, uninstall and then install again
# 7. launch ipython by typing 'ipython' in terminal after activate env
# 8. move back in editor, use <ctrl-c><ctrl-c> to send code to target

import matplotlib
matplotlib.use('module://matplotlib-backend-kitty')
# matplotlib.use('module://kitty')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# $ export MPLBACKEND='module://matplotlib-backend-kitty' --> can put it in .bashrc
# $ python -i
n = 10000
df = pd.DataFrame({'x': np.random.randn(n),
                       'y': np.random.randn(n)})
df.plot.hexbin(x='x', y='y', gridsize=20)
# <plot is shown>

