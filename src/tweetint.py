from argparsing import get_args
from tutil import Twitter

def main():
    args = get_args()

    twitter = Twitter(args)

    if args.userid:
        twitter.search_by_id()
    elif args.username:
        twitter.search_by_username()
    elif args.name:
        twitter.search_by_name()
    
if __name__ == "__main__":
    main()