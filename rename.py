import os

dirs = os.listdir('.')
for dir_name in dirs:
    if dir_name.startswith('chapter'):
        file_list = os.listdir(dir_name)
        if 'index.md' in file_list:
            print('\nrename files in directory:', dir_name)
            with open(os.path.join(dir_name, 'index.md'), 'r') as fr:
                skipped = False
                content_list = []
                for line in fr.readlines():
                    line = line.strip()
                    if skipped:
                        if len(line) > 0 and '```' not in line:
                            content_list.append(line)
                    elif line.startswith(':maxdepth:'):
                        skipped = True
                for i in range(len(content_list)):
                    source_name = '%s.ipynb' % content_list[i]
                    target_name = '%02d_%s.ipynb' % (i + 1, content_list[i])
                    if source_name in file_list:
                        print('mv: %s --> %s' % (source_name, target_name))
                        os.rename(os.path.join(dir_name, source_name), os.path.join(dir_name, target_name))



