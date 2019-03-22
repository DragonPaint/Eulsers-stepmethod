def y_prim_start():
    print("This program calculates the curve of the function that is specified in the code. \n"
          'To change the function you have to change the two functions marked with "write your function below".')
    x_start = input("Input starting x = ")
    y_noll = input("Input starting y, y(0) = ")
    y_x = input("Input y(x), x = ")
    step_length_input = input("Input Step length = ")
    y_prim_calc(y_x, x_start, y_noll, step_length_input)


def y_prim_calc(y_x, x_start, y_noll, step_length_input):
    step_length = ""
    for step_length_comma_search in step_length_input:
        if 44 == ord(step_length_comma_search):
            step_length += "."
        else:
            step_length += step_length_comma_search
    x = float(x_start)
    y = float(y_noll)
    y_x_total_length = (float(y_x) - float(x_start)) / float(step_length) + 1
    round(y_x_total_length, 0)

    # write your function below, ex y' = xy^2 but write it: x ** y
    y_p = x * y
    # x ** x = x to the power of x, x = x times x

    for abc in range(int(y_x_total_length)):
        print("X = " + str(round(x, 3)) + " Y = " + str(round(y, 3)) + " Y' = " + str(round(y_p, 3)))
        x += float(step_length)
        y += (float(y_p) * float(step_length))

        # write your function below, ex y' = xy^2 but write it: x * y * y,
        y_p = x * y
        # x ** x = x to the power of x, x = x times x

    step_length_input = input("Want to change the step width and try again?, just input new step_length = ")
    y_prim_calc(y_x, x_start, y_noll, step_length_input)


y_prim_start()
