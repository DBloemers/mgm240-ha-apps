# ESPHome Device Builder for Arduino Nano Matter

Open the app and build the included `nano-matter-smoke.yaml` using
**Install → Manual download → Intel HEX (USB debugger)**. Flash the HEX
over USB using the board's onboard CMSIS-DAP probe and OpenOCD.

This experimental app keeps its own ESPHome configurations. The smoke
firmware tests GPIO and serial logging. Thread integration with Home
Assistant requires a Thread border router and a matching network dataset.
