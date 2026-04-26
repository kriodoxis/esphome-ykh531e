# ESPHome YKH531E Climate Component

ESPHome custom component for YKH531E IR remote control protocol. Controls compatible AC units via infrared signals.

Tested with: Frigidaire FHPW122AC1

## Installation

Add to your ESPHome configuration:

```yaml
external_components:
  - source: github://kriodoxis/esphome-ykh531e
    components: [ykh531e]
```

See [ESPHome External Components](https://esphome.io/components/external_components.html) for more installation options.

## Configuration

```yaml
remote_transmitter:
  pin: GPIO14
  carrier_duty_percent: 50%

climate:
  - platform: ykh531e
    name: "AC Unit"
    supports_heat: false
    supports_cool: true
    use_fahrenheit: false # Optional: use Fahrenheit instead of Celsius
    timer_select:
      name: "AC Unit Timer"
      icon: mdi:timer-outline
```

## Features

- **Temperature**: 16-32°C (60-90°F)
- **Modes**: Auto, Cool, Dry, Fan, Heat (untested)
- **Fan Speed**: Low, Medium, High, Auto
- **Swing**: Vertical only
- **Presets**: Sleep mode
- **Units**: Celsius or Fahrenheit
- **Timers**: Up to 24h timers ON and OFF

## Hardware Setup

Connect IR transmitter to GPIO14 (or your preferred pin).

Optional: Connect IR receiver to GPIO27 to update climate state when using the physical remote control.

```yaml
remote_receiver:
  pin: GPIO27
```

## Development

To modify and test:

```bash
# Install dependencies
uv sync

# Test compilation
uv run esphome compile test_device.yaml
```
