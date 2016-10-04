
bool on = false;
bool debounce = false;
int count = 0;

unsigned long inputStart = 0;
unsigned long debounceDelay = 300;

void setup() {
  pinMode(7, OUTPUT);
  pinMode(2, INPUT);
}

void loop() {
  int input;

  input = digitalRead(2);
  if (!debounce && input == HIGH) {
    debounce = true;
    inputStart = millis();
  } 

  if (debounce && (millis() - inputStart) > debounceDelay) {
    debounce = false;
    on = !on;
 
    digitalWrite(7, on ? HIGH : LOW);
    pinMode(2, OUTPUT);
    digitalWrite(2, LOW);
    pinMode(2, INPUT);
  }
    
}
