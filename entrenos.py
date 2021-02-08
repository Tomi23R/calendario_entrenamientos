import argparse
from programa import Programa

if __name__ == '__main__':
    # Parser de los argumentos del programa
    parser = argparse.ArgumentParser(prog='Calendario de entrenamientos', 
            description='Calendario de entrenamientos junto con historico de mejores tiempos',
            formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=80))

    parser.add_argument('-p', '--program', dest='program', 
                        action='store_true', help='Programar entrenamientos')

    parser.add_argument('-c', '--current', dest='current',
                        action='store_true', help='Programar entrenamientos de la semana actual')

    parser.add_argument('-l', '--load', dest='load', 
                        action='store_true', help='Cargar entrenamientos')

    parser.add_argument('-r', '--records', dest='records', 
                        action='store_true', help='Ver records')

    # Parseamos argumentos
    args = parser.parse_args()
    program = args.program
    current = args.current
    load = args.load
    records = args.records
    
    # Si se quiere programar entrenamiento
    programa = Programa()
    if program: programa.programar(current)
