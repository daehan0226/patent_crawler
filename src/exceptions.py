class ElementByTypeError(Exception):
    
    def __init__(self, by, message="Find element error, by type"):
        self.by = by
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message} : {self.by}"

class ElementInfoError(Exception):
    
    def __init__(self, element_info, message="Could not find the element"):
        self.element_info = element_info
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}, {self.element_info}"

class WrongPageError(Exception):
    
    def __init__(self, message="Wrong page, check the url"):
        self.message = message
        super().__init__(self.message)

class SwitchTabError(Exception):
    
    def __init__(self, index, message="Could not find the tab"):
        self.index = index
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}, index : {self.index}"

class AlertTimeoutError(Exception):
    def __init__(self, wait_time, message="Alert time out error"):
        self.wait_time = wait_time
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"{self.message}, waited for : {self.wait_time}"

class NoElementError(Exception):
    def __init__(self, target, message="Could not find the element"):
        self.target = target
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"{self.message}, {self.target}"