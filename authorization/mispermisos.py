class Permiso():

    def is_valid(user, permiso):        
        permisos = list(user.get_all_permissions())
        if permiso in permisos:
            return True
        else:
            return False
