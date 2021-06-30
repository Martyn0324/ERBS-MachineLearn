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

data = imageio.get_reader(r"Teste.mp4", 'ffmpeg')
model = TSNE()
k = KMeans()

for i, g in enumerate(data):
    #print(g)
    #plt.imshow(g)
    #plt.show(block=False)
    #tree = DecisionTreeRegressor()
    #X1, X2, y1, y2 = train_test_split(i, g, test_size=0.3)
    #tree.fit(X1, y1)
    k.fit(g.reshape(-1,1))

#Attention: DO NOT TRY the following:
#Data = pd.DataFrame({'Frames': enumerate(data)})
#It'll crash your computer
