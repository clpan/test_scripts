# test if plot can be shown
# with global python, plot is shown in kitty terminal. Yet to test other env or other terminal emulators
import matplotlib.pyplot as plt
import numpy as np

plt.plot([10, 20, 30])
plt.show()
print("hw")
