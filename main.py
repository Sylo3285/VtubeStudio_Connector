import asyncio
import pyvts
import numpy as np

import pyttsx3

# Specify plugin information (optional, but good practice)
plugin_info = {
    "plugin_name": "Ai Controller",
    "developer": "Sylo",
    "authentication_token_path": "./token.txt"
}
params={
    1: "AiMouthOpen",
    2: "AieyeBlink"
}

class VTS():
    def __init__(self):
        self.vts = pyvts.vts(plugin_info=plugin_info)
        self.speaking = False
    
    async def init(self):
        print("Initalizing VTube Studio connection...")
        await self.connect()
        await self.register_params()
        
    
    async def connect(self):
        await self.vts.connect()
        await self.vts.request_authenticate_token()
        await self.vts.request_authenticate()
    
    async def register_params(self):
        for i in params:
            new_parameter_name = params[i]
            await self.vts.request(
                self.vts.vts_request.requestCustomParameter(new_parameter_name)
            )

    async def speak_text(self,text):
        def tts():
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)
            engine.setProperty('volume', 1)
            engine.say(text)
            engine.runAndWait()
        await asyncio.to_thread(tts)
        self.speaking = False
        print("Finished speaking.")

    async def mouthanimation(self):
        mouth_vals=np.linspace(0,0.25,10)
        animation_speed = 0.005
        #mouth_vals = [0, 0.05, 0.1, 0.15, 0.2, 0.25]

        while self.speaking:
            for i in mouth_vals:
                if not self.speaking:
                    break
                await self.vts.request(
                    self.vts.vts_request.requestSetParameterValue("AiMouthOpen", i)
                )
                await asyncio.sleep(animation_speed)
            
            for i in range(len(mouth_vals)-1,-1,-1):
                if not self.speaking:
                    break
                await self.vts.request(
                    self.vts.vts_request.requestSetParameterValue("AiMouthOpen", mouth_vals[i])
                )
                await asyncio.sleep(animation_speed)
            
            await self.vts.request(
                    self.vts.vts_request.requestSetParameterValue("AiMouthOpen", 0)
                )

    async def speak(self,message="This is a test for VTube Studio integration."):
        self.speaking = True
        mouth_task = asyncio.create_task(self.mouthanimation())
        speak_task = asyncio.create_task(self.speak_text(message))

        await mouth_task
        await speak_task


async def main():
    connector = VTS()
    await connector.init()
    await connector.speak()

if __name__ == "__main__":
    asyncio.run(main())