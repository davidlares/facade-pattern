class FacadeFactory(object): # this instanciate a Facade object
    @staticmethod
    # dynamic run-time importing
    def create_facade(module_name):
        module = import_module ('.' + module_name, __package__) # imports a module from the current package
        # looks from the content to find a class not abstract but is a subclass of AbsFacade
        classes = getmembers(module, lambda m: (isclass(m) and not isabstract(m) and issubclass(m, AbsFacade)))
        return classes[0][1]()
