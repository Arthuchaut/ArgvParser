from argvparser.argvparser import ArgvParser
import tests.argvparser_tests as unit
import pprint

def main():
    pp = pprint.PrettyPrinter(indent = 4)

    tests = {
        'test_1': unit.test_argvparser(),
        'test_2': unit.test_argvparser(['app.py', 'commit', '-am', 'commit message']),
        'test_3': unit.test_argvparser(['app.py', '--name', 'myName', '-v', 'C:/Users/UserName/App', '-rf']),
        'test_4': unit.test_argvparser(['app.py', 'hello', '--name', 'myName',  '-v', 'test2', 'none', 'C:/Users/UserName/App', '-rf', '-t', '-o', 'test', 'ok']),
        'test_5': unit.test_argvparser(['app.py', 'hello', '--name', 'myName', '-v', '2.4', '-v', '50', '-v', 'C:/Users/UserName/App', '-v', 'C:/Users/UserName/App/Directory', '-rf', '-t', '-o', 'test'])
    }

    docs = {
        'parse': ArgvParser.parse.__doc__,
        'parse_multi_options': ArgvParser.parse_multi_options.__doc__,
        'is_option': ArgvParser.is_option.__doc__,
        'parse_type': ArgvParser.parse_type.__doc__
    }

    for method, doc in docs.items():
        print(method)
        print(doc)
    
if __name__ == '__main__':
    main()