import argvparser

def test_argvparser(argv = ['app.py', 'ls', '-la']):
    try:
        return argvparser.argvparser.parse(argv)
    except Exception as e:
        return e