# creating a CLI to search for tweets
import argparse
from search_by_username import return_user

# create a parser object
parser = argparse.ArgumentParser(description="Search by username")

# add arguments to the parser
parser.add_argument("username", help="Enter the username you want to search")

# parse the arguments into standard input
args = parser.parse_args()

# check if the username is valid
if len(args.username) != 0:
    return_user(args.username)
