# TODO: copy the code from files to here for submission
# For now it will remain like this for comfort
import BigCross1 as bc1
import BigCross2 as bc2


def main():
    # biggest cross center at [7,4] branch size is 2
    M1 = [[1, 0, 1, 0, 1, 1, 0, 0, 1],
          [1, 1, 1, 1, 0, 1, 1, 1, 1],
          [0, 1, 1, 1, 0, 1, 0, 0, 1],
          [0, 1, 1, 0, 1, 1, 1, 0, 0],
          [1, 0, 1, 1, 0, 1, 1, 0, 1],
          [1, 1, 0, 1, 0, 0, 1, 0, 1],
          [0, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 0, 1, 0, 1, 0, 0, 1],
          [0, 0, 0, 1, 1, 1, 0, 0, 1]]

    # biggest cross center at [7,4] branch size is 3
    M2 = [[1, 0, 1, 0, 1, 1, 0, 0, 1],
          [1, 1, 1, 1, 0, 1, 1, 1, 1],
          [0, 1, 1, 1, 0, 1, 0, 0, 1],
          [0, 1, 1, 0, 1, 1, 1, 0, 0],
          [1, 0, 1, 1, 0, 1, 1, 0, 1],
          [1, 1, 0, 1, 0, 0, 1, 0, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 0, 1, 0, 1, 0, 0, 1],
          [0, 0, 0, 1, 1, 1, 0, 0, 1]]
    print("I just love matrix")
    print("first matrix: ")
    bc1.BigCross1(M1, len(M1))
    print("second matrix: ")
    bc1.BigCross1(M2, len(M2))


if __name__ == "__main__":
    main()
