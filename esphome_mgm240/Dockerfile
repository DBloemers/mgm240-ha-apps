FROM ghcr.io/esphome/docker-base:debian-ha-addon-2026.11.0@sha256:2bdf027456ba4ff8df7c7d4c7de14280cacb5cbde72425238870ee74f99ccbb4

ARG ZEPHYR_REV=5b3759483217d228f160f6173cbcef7974b623ff
ARG ZEPHYR_SDK_VERSION=1.0.1

ENV ZEPHYR_BASE=/opt/zephyr-workspace/zephyr \
    ZEPHYR_SDK_INSTALL_DIR=/opt/zephyr-sdk \
    ZEPHYR_TOOLCHAIN_VARIANT=zephyr \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    ESPHOME_IS_DOCKER_IMAGE=true

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        device-tree-compiler ninja-build wget xz-utils \
    && rm -rf /var/lib/apt/lists/* \
    && python3 -m pip install --no-cache-dir uv==0.10.1 \
    && uv venv --python "$(command -v python3)" /opt/zephyr-venv

ENV PATH="/opt/zephyr-venv/bin:${PATH}"

RUN git init "$ZEPHYR_BASE" \
    && git -C "$ZEPHYR_BASE" fetch --depth 1 https://github.com/zephyrproject-rtos/zephyr.git "$ZEPHYR_REV" \
    && git -C "$ZEPHYR_BASE" checkout --detach FETCH_HEAD \
    && uv pip install --no-cache-dir --python /opt/zephyr-venv/bin/python \
        -r "$ZEPHYR_BASE/scripts/requirements-base.txt" "cmake>=3.28,<5" \
    && cd /opt/zephyr-workspace \
    && west init -l zephyr \
    && west update --narrow -o=--depth=1 \
        cmsis cmsis_6 hal_silabs mbedtls tf-psa-crypto tf-psa-crypto-drivers \
        openthread mcuboot picolibc segger \
    && west blobs fetch hal_silabs

RUN cd /opt/zephyr-workspace \
    && west sdk install --version "$ZEPHYR_SDK_VERSION" \
        -d "$ZEPHYR_SDK_INSTALL_DIR" -t arm-zephyr-eabi -H

COPY sources.tar.gz /tmp/sources.tar.gz
RUN mkdir -p /tmp/esphome-sources \
    && tar -xzf /tmp/sources.tar.gz -C /tmp/esphome-sources \
    && uv pip install --no-cache-dir --python /opt/zephyr-venv/bin/python \
        /tmp/esphome-sources/esphome /tmp/esphome-sources/device-builder \
    && rm -rf /tmp/esphome-sources /tmp/sources.tar.gz \
    && esphome version \
    && esphome-device-builder --version

COPY nano-matter-smoke.yaml /opt/nano-matter-smoke.yaml
COPY rootfs/ /
RUN chmod 755 /etc/s6-overlay/s6-rc.d/builder/run /etc/s6-overlay/s6-rc.d/builder/finish
