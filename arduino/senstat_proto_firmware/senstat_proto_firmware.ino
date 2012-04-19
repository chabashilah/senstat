/*
This is for prototype firmware.
Written by chabashilah.
 */
#define COUNTER_MAX 10000
int _val=0;
int _debugLedPin = 5;
int _send_counter = 0;
char _module_name[] = "test_module";
int _hoge = 0;

//----------------------------------------------------------------------
void setup(){
    //Start Serial Communication
    Serial.begin(115200);
    pinMode(_debugLedPin, OUTPUT);
}
//----------------------------------------------------------------------
void loop(){
    //This part is used for reading GUI controller
    //In next phase, this value gonna be the 3axis acceleration sensor value

    char send_packet[100] = {'\0'};
    
    snprintf(send_packet, sizeof(send_packet), "%s,%d,%d,%d#",
        _module_name,
        analogRead(2),
	analogRead(1),
	analogRead(0)
    );
    

    digitalWrite(_debugLedPin, HIGH);
    Serial.write(send_packet);
    delay(2000);        

}
//----------------------------------------------------------------------
