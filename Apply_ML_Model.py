# So given an image as input and ML_Model, it will classify as mitosis [1] or not mitosis [0].
# returns 1 or 0.

import sys

def perform_classification(image, model):
    #output = model.predict(image)
    #The output would be something like 1 or 0
    output = 1
    return output

if __name__ == "__main__":
    image = "BuckId.jpg"
    val = perform_classification(image, 5)
    print("Classification output=",val)