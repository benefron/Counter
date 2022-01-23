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
Encoder XLEnc(5, 6);
Encoder DLEnc(7,8);
Encoder YLEnc(9,10);
Encoder ZLEnc(11,12);

Encoder YREnc(13, 14);
Encoder XREnc(15,16);
Encoder ZREnc(17,18);
Encoder DREnc(19,20);
//   avoid using pins with LEDs attached

void setup() {
  Serial.begin(9600);
  //Serial.println("Basic Encoder Test:");
}

long XLoldPosition  = 0;
long YLoldPosition  = 0;
long ZLoldPosition  = 0;
long DLoldPosition  = 0;

long XRoldPosition  = 0;
long YRoldPosition  = 0;
long ZRoldPosition  = 0;
long DRoldPosition  = 0;

void loop() {
  long XLnewPosition = XLEnc.read();
  long YLnewPosition = YLEnc.read();
  long ZLnewPosition = ZLEnc.read();
  long DLnewPosition = DLEnc.read();
  long XRnewPosition = XREnc.read();
  long YRnewPosition = YREnc.read();
  long ZRnewPosition = ZREnc.read();
  long DRnewPosition = DREnc.read();

  if (XLnewPosition != XLoldPosition) {
    Serial.print("XL");
    Serial.println(XLoldPosition - XLnewPosition);
    XLoldPosition = XLnewPosition;
  }
  if (YLnewPosition != YLoldPosition) {
    Serial.print("YL");
    Serial.println(YLoldPosition - YLnewPosition);
    YLoldPosition = YLnewPosition;
    //Serial.println(oldPosition);
  }
  if (ZLnewPosition != ZLoldPosition) {
    Serial.print("ZL");
    Serial.println(ZLoldPosition - ZLnewPosition);
    ZLoldPosition = ZLnewPosition;
  }
  if (DLnewPosition != DLoldPosition) {
    Serial.print("DL");
    Serial.println(DLoldPosition - DLnewPosition);
    DLoldPosition = DLnewPosition;
  }
  if (XRnewPosition != XRoldPosition) {
    Serial.print("XR");
    Serial.println(XRoldPosition - XRnewPosition);
    XRoldPosition = XRnewPosition;
  }
  if (YRnewPosition != YRoldPosition) {
    Serial.print("YR");
    Serial.println(YRoldPosition - YRnewPosition);
    YRoldPosition = YRnewPosition;
    //Serial.println(oldPosition);
  }
  if (ZRnewPosition != ZRoldPosition) {
    Serial.print("ZR");
    Serial.println(ZRoldPosition - ZRnewPosition);
    ZRoldPosition = ZRnewPosition;
  }
  if (DRnewPosition != DRoldPosition) {
    Serial.print("DR");
    Serial.println(DRoldPosition - DRnewPosition);
    DRoldPosition = DRnewPosition;
  }
  delay(300);
}
