# command to run 
# python booktracker.py

# python booktracker.py add 

# python booktracker.py add -h

import argparse
def main():
    parser = argparse.ArgumentParser(description="CLITodo app")
    subParser= parser.add_subparsers(dest="command")
    add_parser = subParser.add_parser("add", help="To add a new todo")
    add_parser.add_argument("description", help="Task description" )
    list_parser= subParser.add_parser("list", help="List Tasks")
    list_parser.add_argument("completed", help="show completedTasks only")
    list_parser.add_argument("pending", help="show pendingTasks only")

    completed_parser = subParser.add_parser("complete", help="Mark as complete")
    completed_parser.add_argument("id", type=int,help="Task id to complete")
    args = parser.parse_args()
    if args.command =="add":
        print(args)
    else:
        parser.print_help()
main()