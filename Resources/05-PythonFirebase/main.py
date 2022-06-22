#https://otcollect.com/collection/firebase/page/dAx8bQ6J/how-to-upload-a-json-file-to-firebase-firestore-using-python
import sys
import json

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import timeit

# Use a service account
cred = credentials.Certificate('api-key.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


def mykwargs(argv):
    '''
    Processes argv list into plain args and kwargs.
    Just easier than using a library like argparse for small things.
    Example:
        python file.py arg1 arg2 arg3=val1 arg4=val2 -arg5 -arg6 --arg7
        Would create:
            args[arg1, arg2, -arg5, -arg6, --arg7]
            kargs{arg3 : val1, arg4 : val2}
        
        Params with dashes (flags) can now be processed seperately

    Shortfalls: 
        spaces between k=v would result in bad params
    Returns:
        tuple  (args,kargs)
    '''
    args = []
    kargs = {}

    for arg in argv:
        if '=' in arg:
            key, val = arg.split('=')
            kargs[key] = val
        else:
            args.append(arg)
    return args, kargs


class UploadJsonFileToFirestore:

    def __init__(self, jsonData, method, collectionName):
        # Get class running time
        self.start = timeit.default_timer()
        self.json_data = jsonData
        self.method = method
        self.collection_name = collectionName

    def __str__(self) -> str:
        return (f'Uploading ****{self.file}***** JSON items to firestore!')

    # Firestore upload method getter method
    @property
    def method(self):
        return self._method

    # Firestore upload method setter method
    @method.setter
    def method(self, val):
        if val == 'set' or val == 'add':
            self._method = val
        else:
            print(f'Wrong method {val}, use set or add')

    # Get Json file path property
    @property
    def json_data(self):
        return self._json_data

    # Set and process Json file path property
    @json_data.setter
    def json_data(self, val):
        if val:
            try:
                # Opening JSON file
                f = open(val, )

                # returns JSON object as a dictionary
                data = json.load(f)

                # make sure to close file
                f.close()
                self._json_data = data
            except Exception as e:
                print(f'FILE EXCEPTION: {str(e)}')
        else:
            print(f'Wrong file path {val}')

    # Main class method to populate firestore
    # With the said data
    def upload(self):
        if self.json_data and self.method:

            # Iterating through the json list
            for idx, item in enumerate(self.json_data):
                '''
                 START FOR JUST FOR DEMO REASONS
                '''
                from pygments import highlight
                from pygments.lexers import JsonLexer
                from pygments.formatters import TerminalFormatter

                json_str = json.dumps(item, indent=4, sort_keys=True)
                print(highlight(json_str, JsonLexer(), TerminalFormatter()))
                '''
                 END FOR JUST FOR DEMO REASONS
                '''

                if self.method == 'set':
                    self.set(item)
                else:
                    self.add(item)
                # Successfully got to end of data;
                # print success message
                if idx == len(self.json_data) - 1:
                    # All the program statements
                    stop = timeit.default_timer()
                    print(
                        '**************************\n****SUCCESS UPLOAD*****\n**************************'
                    )
                    print("Time taken " + str(stop - self.start))

    # Collection Add method
    # Adds all data under a collection
    # With firebase firestore auto generated IDS
    def add(self, item):
        return db.collection(self.collection_name).add(item)

    # Collection document set method
    # Adds all data under a collection
    # With custom document IDS
    def set(self, item):
        return db.collection(self.collection_name).document(str(
            item['id'])).set(item)


if __name__ == '__main__':
    # Check to make sure the command line arguements
    # are atleast 3 arguements
    if len(sys.argv[1:]) != 3:
        print(f'ERROR: Check your command line arguments!')
        print(
            'file=filepath, method=[set or add], collectionName=firestore_collection_name'
        )

        sys.exit()

    argv = sys.argv[1:]

    args, k = mykwargs(argv)

    # Initialize instance variables
    file = sys.argv[1:][0]
    method = sys.argv[1:][1]
    collectionName = sys.argv[1:][2]

    uploadjson = UploadJsonFileToFirestore(k['file'], k['method'],
                                           k['collectionName'])
    uploadjson.upload()
