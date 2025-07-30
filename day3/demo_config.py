import configparser

cp = configparser.ConfigParser()
cp.read("C:\\Users\\d.duraivelan\\PycharmProjects\\ness-jul-25\day3\config.ini")

print(cp.get("login",'username'))

print(cp.get("login",'password'))