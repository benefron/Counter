/* Encoder Library - Basic Example
 * http://www.pjrc.com/teensy/td_libs_Encoder.html
 *
 * This example code is in the public domain.
 */
#define ENCODER_OPTIMIZE_INTERRUPTS
#include <Encoder.h>

// Change these two numbers to the pins connected to your encoder.
//   Best Performance: both pins have interrupt capability
//   Good Performance: only the first pin has interrupt capability
//   Low Performance:  neither pin has interrupt capability
Encoder XEnc(5, 6);
Encoder YEnc(2,3);
Encoder ZEnc(22,23);
Encoder DEnc(25,26);
//   avoid using pins with LEDs attached

void setup() {
  Serial.begin(9600);
  //Serial.println("Basic Encoder Test:");
}

long XoldPosition  = 0;
long YoldPosition  = 0;
long ZoldPosition  = 0;
long DoldPosition  = 0;

void loop() {
  long XnewPosition = XEnc.read();
  long YnewPosition = YEnc.read();
  long ZnewPosition = ZEnc.read();
  long DnewPosition = DEnc.read();

  if (XnewPosition != XoldPosition) {
    Serial.print('X');
    Serial.println(XoldPosition - XnewPosition);
    XoldPosition = XnewPosition;
  }
  if (YnewPosition != YoldPosition) {
    Serial.print('Y');
    Serial.println(YoldPosition - YnewPosition);
    YoldPosition = YnewPosition;
    //Serial.println(oldPosition);
  }
  if (ZnewPosition != ZoldPosition) {
    Serial.print('Z');
    Serial.println(ZoldPosition - ZnewPosition);
    ZoldPosition = ZnewPosition;
  }
  if (DnewPosition != DoldPosition) {
    Serial.print('D');
    Serial.println(DoldPosition - DnewPosition);
    DoldPosition = DnewPosition;
  }
}
