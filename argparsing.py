import argparse

class ValidationException(Exception):
    pass

def validate_username(username):
    if len(username) > 15:
        raise ValidationException("Length of username cannot exceed 15 characters!")

def main():
    parser = argparse.ArgumentParser(description="OSINT Tool for Harvesting Data From Twitter.")

    # parser.add_argument("-u", "--username", type=str, nargs="+", help="Username(s) to Search")
    parser.add_argument("-u", "--username", type=str, help="Get details of the user using username")
    parser.add_argument("-id", "--userid", type=int, help="Get details of the user using numeric user id")
    parser.add_argument("-n", "--name", type=str, help="Get a list of usernames using the name")
    # parser.add_argument("-k", "--keyword", type=str, help="Search tweets based on keyword")

    args = parser.parse_args()
    if args.username is not None:
        validate_username(args.username)

if __name__ == "__main__":
    main()
