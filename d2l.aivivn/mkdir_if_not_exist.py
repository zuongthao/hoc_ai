import os


# Saved in the d2l package for later use
def mkdir_if_not_exist(path):
    print('======')
    if not isinstance(path, str):
        path = os.path.join(*path)
    if not os.path.exists(path):
        os.makedirs(path)
