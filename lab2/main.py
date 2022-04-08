import numpy as np
import matplotlib.pyplot as plt

# Ex a
# imagini = np.array([np.load(r"imagini/car_{idx}.npy".format(idx=i)) for i in range(9)])
# print(imagini)

# Ex b
# imagini = np.array([np.load(r"imagini/car_{idx}.npy".format(idx=i)) for i in range(9)])
# suma = np.sum(imagini)
# print(suma)

# Ex c
# imagini = np.array([np.load(r"imagini/car_{idx}.npy".format(idx=i)) for i in range(9)])
# suma_imaginii = np.sum(imagini, axis=(1,2))
# print(suma_imaginii)

# Ex d
# imagini = np.array([np.load(r"imagini/car_{idx}.npy".format(idx=i)) for i in range(9)])
# print(np.argmax(np.sum(imagini, axis=(1,2))))

# Ex e
# imagini = np.array([np.load(r"imagini/car_{idx}.npy".format(idx=i)) for i in range(9)])
from skimage import io
# mean_image = np.mean(imagini, axis=0)
# io.imshow(mean_image.astype(np.uint8))
# io.show()

# Ex f
# imagini = np.array([np.load(r"imagini/car_{idx}.npy".format(idx=i)) for i in range(9)])
# deviație = np.std(imagini)
# print(deviație)

# Ex g
# imagini = np.array([np.load(r"imagini/car_{idx}.npy".format(idx=i)) for i in range(9)])
# mean_image = np.mean(imagini, axis=0)
# normalizațe = (imagini - mean_image) / np.std(imagini)
# print(normalizațe)

# Ex h
# imagini = np.array([np.load(r"imagini/car_{idx}.npy".format(idx=i)) for i in range(9)])
# decupație = imagini[:, 200:301, 290:401]
# plt.imshow(imagini[7].astype(np.uint), cmap='gray')
# plt.imshow(decupație[7].astype(np.uint), cmap='gray')
