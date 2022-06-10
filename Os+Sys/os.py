import os
from pathlib import Path, PurePath

# print(os.environ)


# cur = os.getcwd()
# print("relative",cur)
# print("absolute",os.path.abspath(cur))

cur = Path.cwd()
print("relative",cur)
print("absolute",cur.resolve())

print(cur.stem)
print(cur.suffix)
print(cur.stat().st_size)
print(cur.stat().st_atime)

print(os.listdir())
# print( list( Path().iterdir() ))

sam = os.path.join(os.getcwd(), 'Hello')
# sam = PurePath.joinpath( Path.cwd(), "Hello" )
print(sam)

# os.mkdir('data')
# Path('Data/new').mkdir(exist_ok= True)

# os.rename('data', 'sys.py')
# Path.rename( Path('data'), Path('sys.py') )

# with open('sys.py', 'x') as new:
#     new.write('import sys')

print(os.path.exists('sys.py'))
# print(Path('sys.py').exists())


