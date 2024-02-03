import matplotlib.pyplot as plt

n = 100
x = [[1 if (j > 2 and j<5) or (j > n-5 and j<n-2) or (i > 2 and i<5) or (i > n-5 and i<n-2) else 0 for j in range(n)] for i in range(n) ]

img = plt.imshow(x, cmap='Greys')
plt.show()