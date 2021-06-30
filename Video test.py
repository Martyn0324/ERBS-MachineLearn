import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor
import imageio
import matplotlib.pyplot as plt
import matplotlib.image as img
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans

#The following video has 33 seconds. Though it's short, this process is quite computationally expensive

data = imageio.get_reader(r"Teste.mp4", 'ffmpeg')
model = TSNE()
k = KMeans()

#Plotting each frame "i" using each pixel "g"

for i, g in enumerate(data):
    print(g)
    plt.imshow(g)
    plt.show(block=False)

#Attention: DO NOT TRY the following:
#Data = pd.DataFrame({'Frames': enumerate(data)})
#It'll crash your computer
