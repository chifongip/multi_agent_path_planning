import yaml
import argparse

a = [{'start': [95, 76], 'goal': [57, 40], 'name': 'agent0'}, {'start': [4, 59], 'goal': [63, 75], 'name': 'agent1'}, {'start': [30, 3], 'goal': [75, 17], 'name': 'agent2'}, {'start': [93, 33], 'goal': [49, 3], 'name': 'agent3'}]

parser = argparse.ArgumentParser()
parser.add_argument("output", help="output file with the schedule")
args = parser.parse_args()

output = dict()
output["agents"] = a
with open(args.output, 'w') as input_yaml:
    yaml.safe_dump(output, input_yaml)