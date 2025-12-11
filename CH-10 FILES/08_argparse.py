import argparse

parser = argparse.ArgumentParser(description="Simple calculater")

parser.add_argument("num1",type=float, help="FirstNumber")
parser.add_argument("num2",type=float, help="SecondNumber")
parser.add_argument("operation",choices=["add","sub","mul","div"],help="Operation to perform")

args=parser.parse_args()