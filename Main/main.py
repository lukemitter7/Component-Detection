import Main_Files.Run as operate
def main():
    #Ask for filename
    operate.ai(user_input())
    
def user_input():
    print('Select one: [v1, v2, v3, v4, v5]')
    version = input("Please input your version: ")
    f = open('Component_Detection/versions.txt')
    lines = f.read().split('\n')
    print(lines)
    actual_selection = version.replace('.', '').lower()
    if actual_selection not in lines:
        print("Version not Found!")
        main()
    else:
        print(actual_selection + ' Selected!')
        return actual_selection
main()