from rubik_solver import utils as rs


def Solver(request):
    result_of_solve = ""
    if request.method == "POST":
        string_color_to_solve = str(request.get_data())[2:-1]
        print(string_color_to_solve)
        try:
            result_of_solve = str(rs.solve(string_color_to_solve, 'Kociemba'))
            print(result_of_solve)
        except:
            result_of_solve = "Error! Try again!"
    result = {'step': result_of_solve}
    return result
