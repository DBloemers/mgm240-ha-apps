# Nano Matter ESPHome experiments

Experimental Home Assistant OS Device Builder for Arduino Nano Matter.
The app runs alongside the stock ESPHome Builder and uses separate storage.

The image build pins the ESPHome and Device Builder forks in `sources.lock`.
CI builds on native x86-64 and ARM64 Linux runners, compiles a sample in each
image, then publishes an image manifest for the two architectures.

CI tags the first successful build for the version in `esphome_mgm240/config.yaml`.
For distribution, make the container package public and publish the app metadata
with its registry image on the `store` branch. Bump the version before publishing
changes to an existing release.

The included sample exercises GPIO and USB logging. Use the HEX download
and the board's onboard USB debugger for the initial flash.
