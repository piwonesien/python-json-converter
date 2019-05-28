from BackendTask import *
from example_input import example_input


def main():
    propertyset1 = Converter.deserialize(example_input[0])
    print(Converter.serialize(propertyset1))
    print("Pass 1")

    propertyset2 = Converter.deserialize(example_input[1])
    print(Converter.serialize(propertyset2))
    print("Pass 2")

    propertyset3 = Converter.deserialize(example_input[2])
    print(Converter.serialize(propertyset3))
    print("Pass 3")


    propertyset4 = Converter.deserialize(example_input[3])
    print(Converter.serialize(propertyset4))
    print("Pass 4")


    propertyset5 = Converter.deserialize(example_input[4])
    print(Converter.serialize(propertyset5))
    print("Pass 5")


    propertyset6 = Converter.deserialize(example_input[5])
    print(Converter.serialize(propertyset6))
    print("Pass 6")




main()
