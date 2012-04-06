/**
 * Button. 
 * 
 * Click on one of the colored squares in the 
 * center of the image to change the color of 
 * the background. 
 */
//Rect parameter
int buttonRectX, buttonRectY;      // Position of square button
int buttonRectHeight, buttonRectWidth;     // Diameter of rect
int backgroundRectX, backgroundRectY;
int backgroundRectHeight, backgroundRectWidth;

//Label parameter
int statTitleLabelX, statTitleLabelY;
int statNameLabelX, statNameLabelY;
int sensorTitleLabelX, sensorTitleLabelY;
int sensorValueLabelX, sensorValueLabelY;

//collor parameter
color rectColor, graphBackgroundColor, baseColor;
color rectHighlight;
color currentColor;
boolean rectOver = false;
int statFlag = 0;

//Font setting
PFont fontA;

int xspacing = 8;   // How far apart should each horizontal location be spaced
int w;              // Width of entire wave
float theta = 0.0;  // Start angle at 0
float amplitude = 75.0;  // Height of wave
float period = 500.0;  // How many pixels before the wave repeats
float dx;  // Value for incrementing X, a function of period and xspacing
float[] yvalues;  // Using an array to store height values for the wave
String [] stat;


void setup()
{
    size(600, 400);
    smooth();
    //Color setting
    rectColor = color(200);
    rectHighlight = color(255);
    baseColor = color(102);
    graphBackgroundColor = color(0);
    currentColor = baseColor;
    
    buttonRectX = 400;
    buttonRectY = 20;  
    buttonRectWidth = 150;
    buttonRectHeight = 30;

    backgroundRectX = 0;
    backgroundRectY = height/2;  
    backgroundRectWidth = width;
    backgroundRectHeight = height/2;

    statTitleLabelX = 10;
    statTitleLabelY = 40;

    statNameLabelX = buttonRectX - 100;
    statNameLabelY = statTitleLabelY;

    sensorTitleLabelX = statTitleLabelX ;
    sensorTitleLabelY = statTitleLabelY + 40;

    fontA = loadFont("CourierNewPSMT-48.vlw");
    textFont(fontA, 24);

    w = width+16;
    dx = (TWO_PI / period) * xspacing;
    yvalues = new float[w/xspacing];
    stat = new String[]{"OFF", "ON"};
}

void draw()
{
    update(mouseX, mouseY);
    background(currentColor);
  
    if(rectOver) {
	fill(rectHighlight);
    } else {
	fill(rectColor);
    }
    rect(buttonRectX, buttonRectY, buttonRectWidth, buttonRectHeight);
    fill(graphBackgroundColor);
    noStroke();
    rect(backgroundRectX, backgroundRectY, backgroundRectWidth, backgroundRectHeight);

    stroke(255);
    fill(255 ,0);
    rect(width/2-10, height/2, 20, height/2);

    
    fill(255);
    text("Trasmission Status : ", statTitleLabelX, statTitleLabelY);
    text("Value : ", sensorTitleLabelX, sensorTitleLabelY);
    text(stat[statFlag], statNameLabelX, statNameLabelY);
    fill(0);
    text("Switch", buttonRectX+30, buttonRectY+22);
    calcWave();
    renderWave();
}

void update(int x, int y)
{
    if(overRect(buttonRectX, buttonRectY, buttonRectWidth, buttonRectHeight) ) {
	rectOver = true;
    }else{
	rectOver = false;
    }
}

void mousePressed()
{
    if(rectOver) {
	statFlag = (statFlag ^ 0x01);
    }
}

boolean overRect(int x, int y, int width, int height) 
{
    if (mouseX >= x && mouseX <= x+width && 
	mouseY >= y && mouseY <= y+height) {
	return true;
    } else {
	return false;
    }
}


void calcWave() {
    // Increment theta (try different values for 'angular velocity' here
    theta += 0.02;

    // For every x value, calculate a y value with sine function
    float x = theta;
    for (int i = 0; i < yvalues.length; i++) {
	yvalues[i] = sin(x)*amplitude;
	x+=dx;
    }
}

void renderWave() {
    // A simple way to draw the wave with an ellipse at each location
    for (int x = 0; x < yvalues.length; x++) {
	noStroke();
	fill(255,80);
	ellipseMode(CENTER);
	ellipse(x*xspacing,width/2+yvalues[x],5,5);
    }

    //Display value
    fill(255);
    int send_value = (int)(150-(yvalues[yvalues.length/2]+amplitude-1));
    text(send_value, sensorTitleLabelX+150, sensorTitleLabelY);

    //send_value
    if(statFlag){

    }
    
}
