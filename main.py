
import kivy
kivy.require('1.7.1')

from kivy.app import App

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

from kivy.properties import ListProperty

from datetime import datetime, timedelta





class Mindful(FloatLayout):
    
    def s_cycles(self, *args):
        l_result1 = self.ids['result1']
        r_cycles = self.ids.cycle.text

        
        try:
            r_cycles = int(r_cycles)
            sleep_time = timedelta(minutes = (90*r_cycles))
            current_time = datetime.now()
            
            ringRing = sleep_time + current_time
            ringRing = timedelta(hours=ringRing.hour, minutes = ringRing.minute)
         
            l_result1.text = "Wake up at " + str(ringRing)
            
        except: 
            l_result1.text = "Input number of cycles"

        
    def waking_times(self, *args):
        l_result2 = self.ids['result2']
        l_result3 = self.ids['result3']
        waking_t = self.ids.waking_time.text
        right_now = datetime.now()
        
        try:
            waking_t = datetime.strptime(waking_t, "%H:%M")        

            counter = timedelta(hours = 4, minutes = 30)
            
            sleep_table = []
            
            for i in xrange(4):
                # waking up time minus sleep cycles, minus meditation time.

                zZleep = waking_t - counter

                if zZleep < right_now:
                    zZleep = timedelta (hours = zZleep.hour, minutes = zZleep.minute)
                                     
                    zZleep = str(zZleep)              
                    sleep_table.append(zZleep)
                    
                else:
                    sleep_table.append("       ")

                counter += timedelta(minutes = 90)                   
            
            l_result2.text = "- "+sleep_table[3] +"   - "+ sleep_table[2]
            l_result3.text = "- "+sleep_table[1] +"   - "+ sleep_table[0] 
            
    
        except: 
            l_result2.text = "Input Time HH:MM"
            l_result3.text = " "

    pass
    
    
class MindfulApp(App):

    current_time = datetime.now()
    current_time = str(timedelta(hours = current_time.hour, minutes = current_time.minute))
    
    def build(Self):
        return Mindful()
        
if __name__=='__main__':
    MindfulApp().run()
    
       
