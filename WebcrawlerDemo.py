import os

# new folder for crawled website

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating Project ' + directory)
        os.makedirs(directory)

# queued and crawled files 

def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawl = project_name + '/crawl.txt'
    if not os.path.isfile(queue):
        print('Creating file ' + queue)
        write_file(queue, base_url)
    if not os.path.isfile(crawl):
        print('Creating file ' + crawl)
        write_file(crawl, '')


# create file

def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

 #create_project_dir('LegInfo')
#create_data_files('LegInfo', 'http://leginfo.legislature.ca.gov/') 

# adding data onto existing file

def append_to_file(path, data):
    with open(path, 'a') as file: 
        file.write(data + '\n')

# delete the contents of a file 

def delete_file_contents(path):
    with open(path, 'w'):
        pass

# read file and convert each line to set items

def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f: 
        for line in f: 
            results.add(line.replace('\n', ''))
    return results

# Iterate through set, each item is new line in file

def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)
