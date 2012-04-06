/*
This is for prototype firmware.
Written by chabashilah.
 */

int val=0;
int debugLedPin = 5;
//----------------------------------------------------------------------
void setup(){
    //Start Serial Communication
    Serial.begin(115200);
    pinMode(debugLedPin, OUTPUT);
}
//----------------------------------------------------------------------
void loop(){
    //This part is used for reading GUI controller
    //In next phase, this value gonna be the 3axis acceleration sensor value
    while(Serial.available()>0){
	//Read data
	val=Serial.read();
	//Write something
	//Serial.print(65,BYTE);
	digitalWrite(debugLedPin, HIGH);
	Serial.write(val);
    }
    Serial.flush();

    //After reading the value, send it with bluetooth.


}
//----------------------------------------------------------------------
