def install_package(*libs):
    # print(libs)
    import os,sys
    _cwd = str(os.getcwd())
    if not os.path.isdir("libraries"):
        os.mkdir("libraries")
    allmodules = os.listdir("libraries")
    if type(libs[0]) == type([1,1]): libs = libs[0]
    for name in libs:
        fileexists=False
        for s in allmodules:
            if s.replace("-","_").find(name.replace("-","_")) == -1: fileexists = False
            else:
                fileexists = True
                # print(name,s)
                break
        if not fileexists:
            command = "pip install "+name+f" --target \"{os.path.join(_cwd,'libraries')}\" --no-user --upgrade"
            print(command)
            os.system(command)
