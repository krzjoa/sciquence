import numpy as np
from sciquence.dtw import segmental_dtw

Z = np.zeros((200, 222))

print segmental_dtw(Z, Z)


#