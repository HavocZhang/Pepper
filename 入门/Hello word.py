from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech","<IP of your robot>",9559)
tts.say("Hello,world!")