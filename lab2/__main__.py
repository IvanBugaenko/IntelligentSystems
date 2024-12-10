from .LL1Parser import LL1Parser
import pandas as pd
import re


if __name__ == '__main__':
    path = r'lab2\table.csv'
    table = pd.read_csv(path)

    ll1 = LL1Parser(table)

    example = """
        type id ;
        type id = ( number + number ) / ( number - number * ( id > number ) ) ;
        type id = true && false ;
        type id = id || true ;
        type id = ! id ;
        type id = ! true ;
        id = id >= id ;
        const type id = number ;
        type id ( type id , type id ) {
            type id = id + number ;
            return id + id ;
        } ;
    """

    example = re.sub('\n', ' ', re.sub('\t', '', example))
    
    print(ll1.analyze(example))
