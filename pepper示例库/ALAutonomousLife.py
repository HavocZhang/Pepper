import qi
class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)

    def onLoad(self):
        #put initialization code here
        self.session=qi.Session()
        pass

    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self):
    
        
        ip="127.0.0.1"
        port=9559
        self.logger.info("connect start")
        try:
            self.session.connect("tcp://" + ip + ":" + str(port))
            service=self.session.service("ALAutonomousLife")
            service.setAutonomousAbilityEnabled("All",False)
        except RuntimeError:
            self.logger.info("connect failed!")
            pass
        
        self.onStopped() #activate the output of the box
        pass

    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box
