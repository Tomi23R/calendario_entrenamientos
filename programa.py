import pickle
import numpy as np
from datetime import datetime, timedelta

# Listado de constantes
dias_semana = {
    0: 'lunes',
    1: 'martes',
    2: 'miercoles',
    3: 'jueves',
    4: 'viernes',
    5: 'sabado',
    6: 'domingo'
}

tipos_deporte = {
    0: 'carrera',
    1: 'ciclismo',
    2: 'natacion',
    3: 'otros'
}

tipos_entrenamiento = {
    0: 'volumen',
    1: 'series con tiempo',
    2: 'series con distancia',
    3: 'otro'
}

# Programa de entrenamientos de un deportista
class Programa:
    def __init__(self):
        # Contiene informacion de los entrenos realizados
        # Estructura del fichero data
        # - Contiene fecha del primer dia de la semana(Lunes)
        #   - Contiene el numero del dia como clave(0,1,2,3,4,5,6)
        #       - Contiene el tipo de entrenamiento como clave
        #           - name: Contiene el nombre del entrenamiento
        #           - date: La fecha del entrenamiento
        #           - times: Dependiendo del entreno contiene un array con los tiempos 
        #           - paces: Dependiendo del entreno contiene un array con los ritmos 
        #           - pace: Ritmo medio del entrenamiento       
        #           - distance: Contiene la distancia total
        #           - total_time: Contiene el tiempo total
        #   - total_time:
        #       - Contiene el deporte como clave y el numero de horas dedicadas
        #   - total_distance:
        #       - Contiene el deporte como clave y la distancia total recorrida
        self.data = {}
        # Contiene los mejores records en los entrenamientos
        # Estructura del fichero best
        # - Contiene los tipos de deporte como clave
        #   - Contiene el tipo de entrenamiento como clave
        #       - name: Contiene el nombre del entrenamiento
        #       - date: La fecha del entrenamiento
        #       - times: Dependiendo del entreno contiene un array con los tiempos 
        #       - paces: Dependiendo del entreno contiene un array con los ritmos
        self.best = {}

    # Guardar programa de entrenamientos en un pickle
    def save(self):
        return

    # Programar semana de entrenamientos
    def programar(self, current):
        today = datetime.today()
        # Si los entrenamientos que se quieren programar son de esta semana
        if current:
            # Obtenemos la fecha del lunes
            monday = today - timedelta(days=today.weekday())
        # Si los entrenamientos se quieren programar para la semana siguiente
        else:
            # Obtenemos la fecha del lunes siguiente
            monday = today + timedelta(days=(7 - today.weekday()))
        # Una vez obtenida la fecha pasamos a programar los entrenamientos
        date = '%d-%d-%d' % (monday.day, monday.month, monday.year)
        # Si esa semana ya ha sido programada pasamos a preguntar si se desea modificar
        if date in self.data:
            salida = input('\nLa semana del %s ya ha sido programada, deseas modificarla? (S/N): ' % date)
            if salida == 'N':
                print('Saliendo del programa...')
                quit()
        
        # Si se quiere programar la semana
        self.data[date] = {}
        # Recorremos los dias de la semana y programamos
        for i in range(7):
            progamar_date = monday + timedelta(days=i)
            progamar_date_str = '%d-%d-%d' % (progamar_date.day, progamar_date.month, progamar_date.year)
            salida = input('\nQuieres programar entrenamiento para el %s(%s)? (S/N): ' 
                % (dias_semana[progamar_date.weekday()], progamar_date_str))
            # Preguntamos si se quiere programar entrenamientos para ese dia
            if salida == 'N':
                self.data[date][i] = None
                break
            self.data[date][i] = {}
            continuar = 'S'
            while continuar == 'S':
                # Preguntamos por el tipo de deporte
                print('\nQue tipo de deporte deseas programar para el %s(%s)?' 
                    % (dias_semana[progamar_date.weekday()], progamar_date_str))
                print('Carrera(0), Ciclismo(1), Natacion(2), Gimasio(3), Otro(4)')
                tipo_deporte = int(input('Introduce el tipo de deporte: '))
                # Comprobamos si ya se han programado entrenamientos de este deporte
                if tipo_deporte not in self.data[date][i]:
                    self.data[date][i][tipo_deporte] = {}
                # Si el deporte esta contemplado
                if tipo_deporte != 4:
                    # Preguntamos por el tipo de entrenamiento
                    print('\nQue tipo de entrenamiento de %s deseas programar para el %s(%s)?'
                        % (tipos_deporte[tipo_deporte], dias_semana[progamar_date.weekday()], progamar_date_str))
                    print('Volumen(0), series con tiempo(1), series con distancia(2), otro(3)')
                    tipo_entrenamiento = int(input('Introduce el tipo de entrenamiento: '))
                    self.data[date][i][tipo_deporte][tipo_entrenamiento] = {}
                    self.data[date][i][tipo_deporte][tipo_entrenamiento]['date'] = progamar_date_str
                    # Si el tipo de entrenamiento es de series preguntamos por las caracterisitcas
                    if tipo_entrenamiento == 1 or tipo_entrenamiento == 2:
                        print('\nQue tipo de entrenamiento de series quiere hacer?')
                        print('Formato series de tiempo: 2x2x2 (Siempre en minutos)')
                        print('Formato series de distancia: 4x1000 (Siempre en metros)')
                        series = input('Introduce el entrenamiento de series: ')
                        self.data[date][i][tipo_deporte][tipo_entrenamiento]['name'] = series
                        self.data[date][i][tipo_deporte][tipo_entrenamiento]['times'] = []
                        self.data[date][i][tipo_deporte][tipo_entrenamiento]['paces'] = []
                        series_sum = series.split('+')
                        for serie in series_sum:
                            series_mult = serie.split('x')
                            multiplicador = 1
                            # Obtenemos el numero de series
                            for serie in series_mult[:-1]:
                                multiplicador * serie
                            self.data[date][i][tipo_deporte][tipo_entrenamiento]['times'].append(np.array(multiplicador))
                            self.data[date][i][tipo_deporte][tipo_entrenamiento]['paces'].append(np.array(multiplicador))
                    else:
                        self.data[date][i][tipo_deporte][tipo_entrenamiento]['times'] = None
                        self.data[date][i][tipo_deporte][tipo_entrenamiento]['paces'] = None
                        print('\nFormato de entrenamiento volumen por distancia: 10km')
                        print('Formato de entrenamiento volumen por tiempo(en minutos): 30')
                        nombre = input('Introduce el entrenamiento de volumen: ')
                        self.data[date][i][tipo_deporte][tipo_entrenamiento]['name'] = nombre
                # Si es otro tipo de deporte que no esta contemplado
                else:
                    nombre = input('\nIntroduce el nombre del entrenamiento: ')
                    self.data[date][i][tipo_deporte]['name'] = nombre

                # Una vez guardado el entrenamiento pasamos a preguntar si se quiere anadir mas entrenamientos ese dia
                continuar = input('\nQuieres seguir anadiendo entrenamientos para el %s(%s)? (S/N): ' 
                    % (dias_semana[progamar_date.weekday()], progamar_date_str))        

    # Cargar de actividades semana de entrenamientos          
    def load_activities(self):
        return

    # Mostrar los records
    def records(self):
        return

    # Imprimir semana de entrenamientos
    def imprimir(self, current):
        return

# Cargar programa de entrenamientos de un pickle
def load(filename):
        return