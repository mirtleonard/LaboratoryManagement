def help_menu():
    """
        Prints help menu for application
    """
    print("add        - 'student' add a student in students list")
    print("           - 'problem' add a problem in problems list")
    print("           - 'mark' add a mark in marks list\n")
    print("find       - 'student' finds a student in students list")
    print("           - 'problem' finds a problem in problems list\n")
    print("update     - 'student' update a student from students list")
    print("           - 'problem' update a problem from problems list\n")
    print("delete     - 'student' delete a student from students list")
    print("           - 'problem' delete a problem from problems list\n")
    print("show       - 'students' print all students from students list")
    print("           - 'problems' print all problems from problems list")
    print("           - 'marks' print all marks from marks list\n")
    print("random     - 'students' adds random students")
    print("           - 'problems' adds random problems")
    print("           - 'marks' adds random marks\n")
    print("statistics - show you the menu of statistics")

def statistics_menu():
    print("1 sort students by mark and name at a given problem")
    print("2 gives students with average marks smaller than 5")
    print("3 top 50% problems with biggest number of students assign")
