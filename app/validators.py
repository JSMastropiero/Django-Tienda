from django.core.exceptions import ValidationError

#Se puede crear un validador personalizado mediante una función o una clase
#la función es más básica, no permite parametros en cambio la clase si.
#es recomendable usar la clase.

class MaxSizeFileValidator:

    def __init__(self,max_file_size=5):
        self.max_file_size = max_file_size


    def __call__(self, value):
        size = value.size
        max_size = self.max_file_size*1048576  #valor de un byte

        if size > max_size:
            raise ValidationError(f"El tamaño máximo del archivo debe ser de {self.max_file_size}MB ")
        
        return value

    