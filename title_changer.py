import os

paths = (os.path.join(root, filename)
        for root, _, filenames in os.walk('D:\Music')
        for filename in filenames)

for path in paths:
    newname = path.replace(' -', ' ')
    if newname != path:
        os.rename(path, newname)