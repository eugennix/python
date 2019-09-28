'''
for tests
'''
import os

ext_to_find, test_folder = 'py', 'for test'
found_folders = set()

for fold_name, child_folders, files_in_folder in os.walk(test_folder):
    fold_name = fold_name[len(test_folder) + 1:]
    if any(f.split('.')[-1] == ext_to_find for f in files_in_folder):
        found_folders.add(fold_name)

with open(test_folder + '\\' + 'result.txt', 'w') as res:
    res.writelines(l + '\n' for l in sorted(found_folders))

# v2 (не в отдельной папке
result = [cur_dir for cur_dir, dirs, files in os.walk('main') if any((fl.endswith(".py") for fl in files))]
with open("py_dirs.txt", "w") as w:
    w.write("\n".join(sorted(result)))