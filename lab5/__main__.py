import pandas as pd
from .LR1Parser import LR1Parser
import json
import re


if __name__ == '__main__':
    path = r'./lab5/table.csv'
    table = pd.read_csv(path)
    
    with open('./lab5/rules_meta.json', 'r') as json_file:
        rules_meta = json.load(json_file)
        
    with open('./lab5/terminal_symbols.txt', 'r', encoding='utf-8') as f:
        terminal_symbols = f.readline().split()
        
    lr1 = LR1Parser(table, rules_meta, terminal_symbols)
    
    example = """
        type id ;
        type id = ( number + id ( number , number ) ) / ( number - number * ( id > number ) ) ;
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
    
    print(lr1.analyze(example))
