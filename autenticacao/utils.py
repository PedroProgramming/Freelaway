def validar_campos(*args):
    return all(arg.strip() != '' for arg in args)