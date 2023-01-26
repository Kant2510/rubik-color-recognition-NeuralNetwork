import Models.NeuralNetwork as nn
import numpy as np
import Utils.initialization as ini

color_recog = nn.NeuralNetwork([3, 3, 64, 128, 256, 256, 64, 6])


def Recognition(request):
    res = []
    if request.method == "POST":
        # nhan hinh anh tu web
        name = request.get_data()
        # xu ly input
        input = ini.intialization(name)

        # predict
        output = color_recog.predict(input)
        colors = ["yellow", "blue", "red", "green", "orange", "white"]
        for i in range(len(output)):
            print(colors[np.where(output[i] ==
                  np.amax(output[i]))[0][0]])
            res.append(colors[np.where(output[i]
                       == np.amax(output[i]))[0][0]])
        print("____")
    result = {'colors': res}
    return result
