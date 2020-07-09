#!/usr/bin/env python
# coding: utf-8

# # TITLE
# 
# Some notes on the topic of the exercise <br><br>
# 
# 
# Link to the videos related to the exercise <br>
# 
# 

# ### Task 1
# <br>
# Story of the exercise ... What is the goal? ...
# 
# ### Task 2
# <br>
# Story of the exercise ... What is the goal? ...
# 
# <br>
# ...
# 
# ### Task N

# In[1]:


#
#   import libraries
#
import cv2
import numpy as np
from matplotlib import pyplot as plt


# In[2]:


def ourCanny(input_image, lowThreshold, highThreshold):
    #example
    return cv2.Canny(input_image, lowThreshold, highThreshold)


# # Local Evaluations:
#  Here you can test the function/class you created
# <br>
# <br>
# 
#  <span style="color:red">WARNING</span>: do not change the code below.

# ### Local evaluation Task 1

# In[3]:


#
#   Some Code to evaluate the task 1
#

file_path = './../chessboard.png'
image_original = cv2.imread(file_path,cv2.IMREAD_UNCHANGED)

lowThreshold = 75
highThreshold = 150

output = ourCanny(image_original, lowThreshold, highThreshold)

plt.subplot(121),plt.imshow(cv2.cvtColor(image_original, cv2.COLOR_BGR2RGB),cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(output,cmap = 'gray')
plt.title('Cv2 Canny'), plt.xticks([]), plt.yticks([])

plt.show()


# In[ ]:




