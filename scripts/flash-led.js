#!/usr/bin/env node

var Gpio = require('onoff').Gpio;
led = new Gpio(3, 'out');
led.writeSync(1);
c = 0
setInterval(function() { led.writeSync(Number(c = !c)); }, 1000);
// led.unexport();
