class GenerarID:
    def __init__(self, nombreUsuario, dniUsuario):
        self.nombreUsuario = nombreUsuario
        self.dniUsuario = dniUsuario
    
    def generarID():
        raise function
    

class GenerarIDAdministrador(GenerarID):
    def __init__(self, nombreUsuario, dniUsuario):
        super().__init__(nombreUsuario, dniUsuario)
    
    def generarID():
        id_administrador = f"{self.nombreUsuario}2023"
        return id_administrador
    
    
class GenerarIDUsuario(GenerarID):
    def __init__(self, nombreUsuario, dniUsuario):
        super().__init__(nombreUsuario, dniUsuario)
    
    def generarID():
        ultimos_digitos = self.dniUsuario[-3:]
        id_usuario = f"{self.nombreUsuario}{ultimos_digitos}"
        return id_usuario