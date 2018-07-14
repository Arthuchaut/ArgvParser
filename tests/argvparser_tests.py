from argvparser.argvparser import ArgvParser

def test_argvparser(argv = ['app.py', 'ls', '-la']):
    try:
        return ArgvParser(argv).args
    except Exception as e:
        return e