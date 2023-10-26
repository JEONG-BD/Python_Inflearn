# Ex03 

class MyFileWriter():

    def __init__(self, file_name, method):
        print('My File Writer started : __init__')
        self.file_obj = open(file_name, method)
    
    def __enter__(self):
        print('My File Writer started : __enter__')
        return self.file_obj 
    
    def __exit__(self, exc_type, value, trace_back):
        print('My File Writer started : __exit__')
        if exc_type : 
            print('Logging Exception {}'.format((exc_type, value, trace_back)))
        self.file_obj.close()

if __name__ == '__main__':
    # context manager 
    # Ex01 
    file = open('./Chapter03/Chapter03_resource/testfile.txt', 'w')
    try : 
        file.write('Context Manager Test1\n Context Library Test1')
    except Exception as ex :
        print('Error')
    finally : 
        file.close()
    
    
    # Ex02 
    try : 
        with open('./Chapter03/Chapter03_resource/testfile01.txt', 'w') as f :
            f.write('Context Manager Test2\n Context Library Test2')
    except FileNotFoundError as ex :
        print('File Not Found')

    # Ex03 

    with MyFileWriter('./Chapter03/Chapter03_resource/testfile02.txt', 'w') as f : 
        f.write('Context Manager Test3\n Context Library Test3')

