import argparse

parser = argparse.ArgumentParser(description="A sample script")
parser.add_argument("name", help="Your name")
parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
parser.add_argument("--count", type=int, default=1, help="Repeat count")

args = parser.parse_args()
print(f"Hello, {args.name}!")
print(f"Verbose: {args.verbose}")
print(f"Count: {args.count}")
