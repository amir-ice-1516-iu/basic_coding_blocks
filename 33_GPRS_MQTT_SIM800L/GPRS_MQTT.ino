#include"Arduino.h"
#include"GSM_MQTT.h"

GSM_MQTT MQTT(60);
    
void setup()
{
    
    //MQTT.begin();
    MQTT.setHostPort("ctgbroker.drinkwellatm.com",1883); //MQTT.begin(); is called inside this method implicitly
    #ifdef UART_DEBUG
      UART_DEBUG.println("Setup finished");
    #endif
    
}

void loop()
{
  #ifdef UART_DEBUG
    if(UART_DEBUG.available()>0){
      String Input = UART_DEBUG.readString();
      unsigned int len = Input.length();
      char data[len+1];
      int i=0;
      for(i=0;i<len;++i){
        data[i] = Input[i];
      }
      data[i]='\0';
      if (MQTT.available())
      {
          MQTT.publish(0, 0, 0, 1, "outTopic", data);
          UART_DEBUG.println("Published");
          //delay(3000);
      }
      else
      {
          UART_DEBUG.println("MQTT busy or not available");
      }
    }
  #endif
  MQTT.processing();
}
