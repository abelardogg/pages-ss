import os


def createDir(path):
    ss_dir_path_exists = os.path.exists(path)
    if(ss_dir_path_exists):
        print('screenshots path exists!')
    else:
        print("screenshots path DOESN'T exists! but will be created")
        try:
            os.makedirs(path)
        except:
            print(f'Something failed while trying to create {path}, try again or create it manually.')
            exit()
