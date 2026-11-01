import numpy as np
import matplotlib.pyplot as plt
# Sample indices
n = np.array([-3, -2, -1, 0, 1, 2, 3, 4, 5, 6])
# Signal values
x = np.array([2, 3, 2, 3, 2, 3, 2, 3, 2, 3])
plt.figure(figsize=(10,4))

# Stem plot
markerline, stemlines, baseline = plt.stem(n, x)
plt.xlim(-5, 7)
plt.ylim(0, 4)
plt.xticks(np.arange(-3, 7, 1))
plt.yticks([0, 1, 2, 3])
plt.title("Discrete-Time Signal")
plt.show()


# ----------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# Time samples
n = np.array([0, 1, 2, 4, 5, 6])
# Signal values
x = np.array([1, 2, 3, 2, 1, 0])
plt.figure(figsize=(8,4))
# Staircase plot
plt.step(n, x, where='post', linewidth=2)
# Limits and ticks
plt.xlim(0, 7)
plt.ylim(0, 4)
plt.xticks(np.arange(0, 7, 1))
plt.yticks([0, 1, 2, 3])
plt.grid(False)
plt.title("Staircase Signal")
plt.show()


# ----------------------------------------------------------------

import matplotlib.pyplot as plt
# Signal
plt.plot([-2,-2], [0,-2], 'b', lw=2)
plt.plot([-2,-1], [-2,-2], 'b', lw=2)
plt.plot([-1,1], [-2,2], 'b', lw=2)
plt.plot([1,2], [2,2], 'b', lw=2)
plt.plot([2,2], [2,0], 'b', lw=2)
# Axes
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlim(-2.5,3)
plt.ylim(-2.5,3)
plt.xticks([-2,-1,0,1,2])
plt.yticks([-2,0,2])
plt.text(0.1,2.3,'x[n]')
plt.text(3,-0.2,'n')
plt.grid(True)
plt.show()


# ----------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
# Sample range
n = np.arange(-2, 11)
# Unit step function
u = lambda x: np.where(x >= 0, 1, 0)
# Signal
x = u(n) - u(n-3) - 5*u(n-7)
# Plot
plt.stem(n, x)
plt.xticks(np.arange(-2,11))
plt.yticks([-5,-4,-3,-2,-1,0,1])
plt.title("x[n] = u(n) - u(n-3) - 5u(n-7)")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid(True)
plt.show()

# ----------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
# Sample range
n = np.arange(-4, 5)
# Signal
x = np.zeros(len(n))
x[n == -1] = 5
x[n == 0] = 1
x[n == 1] = 3
# Plot
plt.stem(n, x)
plt.xticks(np.arange(-4, 5))
plt.yticks([0, 1, 2, 3, 4, 5])
plt.title("x[n] = δ(n) + 3δ(n-1) + 5δ(n+1)")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid(True)
plt.show()
