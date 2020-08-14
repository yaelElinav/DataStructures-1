# TODO: copy the code from files to here for submission
# For now it will remain like this for comfort
import BigCross1 as bc1
import BigCross2 as bc2
import numpy as np


def main():
    # Assuming both have to be in the same size

    #TODO: create a 15X15 array for submission

    # TODO: arrays for checking
    # biggest cross center at [7,4] branch size is 2
    M1 = np.array([[1, 0, 1, 0, 1, 1, 0, 0, 1],
          [1, 1, 1, 1, 0, 1, 1, 1, 1],
          [0, 1, 1, 1, 0, 1, 0, 0, 1],
          [0, 1, 1, 0, 1, 1, 1, 0, 0],
          [1, 0, 1, 1, 0, 1, 1, 0, 1],
          [1, 1, 0, 1, 0, 0, 1, 0, 1],
          [0, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 0, 1, 0, 1, 0, 0, 1],
          [0, 0, 0, 1, 1, 1, 0, 0, 1]])
    # biggest cross center at [4,6] branch size is 3
    M2 = np.array([[1, 0, 1, 0, 1, 1, 0, 0, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 0, 0, 1],
          [0, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 0, 1, 1, 0, 1, 1, 0, 1],
          [1, 1, 0, 1, 1, 1, 1, 0, 1],
          [0, 1, 1, 0, 1, 1, 1, 1, 1],
          [1, 1, 0, 1, 0, 1, 0, 0, 1],
          [0, 0, 0, 1, 1, 1, 0, 0, 1]])
    # biggest cross center at [5,5] branch size is 4
    M3 = np.array([[1, 0, 1, 0, 1, 1, 0, 0, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 0, 1, 1, 1, 0, 0, 1],
          [0, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 0, 1, 1, 1, 1, 0, 1],
          [0, 1, 1, 0, 1, 1, 0, 1, 1],
          [1, 1, 0, 1, 1, 1, 0, 0, 1],
          [0, 0, 0, 1, 1, 1, 0, 0, 1]])
    # biggest cross center at [2, 3] branch size is 1
    M4 = np.array([[1, 0, 1, 0, 1, 0, 1, 0, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1],
          [0, 0, 1, 1, 1, 1, 0, 0, 1],
          [0, 0, 0, 1, 1, 1, 0, 0, 1],
          [1, 0, 1, 1, 1, 0, 1, 0, 1],
          [0, 1, 1, 1, 0, 1, 1, 0, 1],
          [1, 0, 1, 1, 0, 0, 1, 0, 1],
          [1, 1, 0, 1, 1, 1, 0, 0, 1],
          [0, 0, 0, 1, 0, 1, 0, 0, 1]])
    # no crosses
    M5 = np.array([[1, 0, 1, 0, 1, 0, 1, 0, 1],
          [0, 1, 0, 1, 0, 1, 0, 1, 0],
          [1, 0, 1, 0, 1, 0, 1, 0, 1],
          [0, 1, 0, 1, 0, 1, 0, 1, 0],
          [1, 0, 1, 1, 1, 0, 1, 0, 1],
          [1, 0, 1, 0, 1, 0, 1, 0, 1],
          [1, 0, 1, 1, 0, 0, 1, 0, 1],
          [1, 0, 1, 0, 1, 0, 1, 0, 1],
          [0, 0, 0, 1, 0, 1, 0, 0, 1]])

    random_array_size = 30

    M10 = np.random.randint(2, size=(random_array_size, random_array_size))
    siz = M10.shape[0]
    bc1.BigCross1(M10, siz)


if __name__ == "__main__":
    main()
