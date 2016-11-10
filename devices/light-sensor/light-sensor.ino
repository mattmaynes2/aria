// Sensor range constants
const int sensorMin = 0;
const int sensorMax = 800;
int photocellPin = A0;
int interval = 250; // 4 Hz

void setup() {
    // set up serial at 9600 baud   
    Serial.begin(9600);
}

void loop() {
    int cellValue;
    cellValue = analogRead(photocellPin);
    
    Serial.println(cellValue);
    delay(interval);
}
