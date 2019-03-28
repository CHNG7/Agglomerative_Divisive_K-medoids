import argparse
# from argparse import ArgumentParser
def parser2():
	parser = argparse.ArgumentParser()
	parser.add_argument("echo",help="echo is the string you use here")
	args = parser.parse_args()
	heuristic = args.echo
# print(heuristic)
	return heuristic


if __name__ == "__main__":
	# print(heuristic)
	