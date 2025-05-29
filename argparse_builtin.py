import argparse
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


parser = argparse.ArgumentParser()
parser.add_argument("number", type=int, help="Input number to calculate factorial")

args = parser.parse_args()


def fac(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if number <= 1:  # Base case
        return 1
    return number * fac(number - 1)

result = fac(args.number)

logger.info(f"Factorial of {args.number} is {result}")
