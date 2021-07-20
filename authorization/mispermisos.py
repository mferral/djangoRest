class Permiso():

    def is_valid(user, permiso):        
        permisos = list(user.get_all_permissions())
        print (permisos)
        if permiso in permisos:
            return True
        else:
            return False
