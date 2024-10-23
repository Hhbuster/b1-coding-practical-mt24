class PDController:
    def __init__(self, kp=0.15, kd=0.6):
        self.kp = kp  # Proportional gain
        self.kd = kd  # Derivative gain
        self.previous_error = 0.0  # To store the previous error
        print(kp)
        print(kd)
        
    def compute_control(self, reference, output):
        
        #Compute the error
        error = reference - output
        
        control_next = (self.kp * error) + (self.kd * (error - self.previous_error))
        
        self.previous_error = error
        
        return control_next