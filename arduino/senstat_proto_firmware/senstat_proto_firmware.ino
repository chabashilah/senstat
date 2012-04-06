/*
This is for prototype firmware.
Written by chabashilah.
 */

int val=0;
//----------------------------------------------------------------------
void setup(){
    //Start Serial Communication
    Serial.begin(9600);
}
//----------------------------------------------------------------------
void loop(){
    //This part is used for reading GUI controller
    //In next phase, this value gonna be the 3axis acceleration sensor value
    if(Serial.available()>0){
	//Read data
	val=Serial.read();
	//Write something
	Serial.print(65,BYTE);
    }
    //After reading the value, send it with bluetooth.


}
//----------------------------------------------------------------------
