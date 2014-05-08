import sys

if __package__ == '':
    import os
    print ("inside main__pack")  
    path = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, path)

import hadoopy

if __name__ == '__main__':    
    sys.exit(hadoopy.main())