# Nano Matter ESPHome experiments

Experimental Home Assistant OS Device Builder for Arduino Nano Matter.
The app runs alongside the stock ESPHome Builder and uses separate storage.

The image build pins the ESPHome and Device Builder forks in `sources.lock`.
CI builds on native x86-64 and ARM64 Linux runners, compiles a sample in each
image, then publishes an image manifest for the two architectures.

CI tags the first successful build for the version in `esphome_mgm240/config.yaml`.
Add `https://github.com/DBloemers/mgm240-ha-apps` under **Settings → Apps →
Install app → Repositories**. The app store pulls the tested image from GHCR.
The `store` branch remains available for existing installations using that URL.
Publish a new image tag before updating the app's advertised version.

The included sample exercises GPIO and USB logging. Use the HEX download
and the board's onboard USB debugger for the initial flash.
