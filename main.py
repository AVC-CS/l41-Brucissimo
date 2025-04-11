def main():
    N = int(input('Enter the number N: '))
    result = []

    """
    ########################################
    Code Your Program here
    ########################################
    """
    for i in range(1, N + 1):  # Make sure this is indented inside the function
        if i % 2 == 0:
            result.append(i)
        else:
            result.append(-i)

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    print(main())  # Add print to see output
