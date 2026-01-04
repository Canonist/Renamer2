import os

def program():
    location = input("Please enter the folder containing files to be sequentially renamed.")
    os.chdir(location)
    print("---PWD---")
    print(os.getcwd())

    #get number of files
    filecount = sum(len(files) for _, _, files in os.walk(location))
    print(f'total number of files found is {filecount}')

    loops = 0
    #loop for entering subfolders
    for (dirs) in os.walk(location, topdown=True):
        #print(dirs[0]) #THIS ITERATES TO FOLDERS CORRECTLY!
        rnloops = 0
        print(f'loop index# {loops}')
        print(f'changing folders to {dirs[0]}')
        os.chdir(dirs[0])
        #print("---PWD---") #this was test
        #print(os.getcwd()) #this was test
        filesin = sum(len(files) for _, _, files in os.walk(os.getcwd()))
        print(f'total number of files found in {os.getcwd()} is {filesin}')

        #renaming protocols
        for _, _, files in os.walk(os.getcwd()):
            print(files)

            print(f'looped for {rnloops} times')
            rnloops += 1
        #renaming end


        if sum(len(dirs) for _, dirs, _ in os.walk(location)) > loops:
            loops += 1


        '''while sum(len(dirs) for _, dirs, _ in os.walk(location)) > loops:
            print(f'loop {loops}')
            loops += 1
            print(dirs[0])
            #os.chdir(somewaytoconnectpaths)
            #print("---PWD---")
            print(os.getcwd())'''

"""  USE THIS POWER FOR GOOD
    #this needs to start in the subfolder itself!
    os.chdir(location)
    print(os.getcwd())
    for filecount, f in enumerate(os.listdir()):
        f_name, f_ext = os.path.splitext(f)
        f_name = str(count)

        new_name = f'{f_name}{f_ext}'
        os.rename(f, new_name)
"""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    program()
