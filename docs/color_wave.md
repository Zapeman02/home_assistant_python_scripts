# Color Wave 🌈

Runs an animated color effect across a list of lights in a specified order. Before starting, the script saves each light's original state and restores it when the effect is done.

## Modes

| Mode | Description |
|------|-------------|
| `wave` | Lights change color one at a time in order, creating a flowing wave effect |
| `sync` | All lights change to the same color simultaneously, then move to the next color together |

## Requirements

- Home Assistant with `python_script` integration enabled
- Add to `configuration.yaml` if not already there:
```yaml
python_script:
```

## Installation

### 1. Copy the script
Place `color_wave.py` in your HA config folder:
```
/config/python_scripts/color_wave.py
```

### 2. Create Helpers
Go to **Settings → Devices & Services → Helpers** and create:

| Helper | Type | Details |
|--------|------|---------|
| `input_select.color_wave_mode` | Dropdown | Options: `wave`, `sync` |
| `input_number.color_wave_speed` | Number | Min: `0.1`, Max: `3`, Step: `0.1` |
| `input_number.color_wave_repetitions` | Number | Min: `1`, Max: `10`, Step: `1` |
| `input_button.color_wave_trigger` | Button | The trigger button |

### 3. Create the Automation
Import the `color_wave_automation.yaml` file in HA under **Settings → Automations**, or add it to your `automations.yaml`.

### 4. Add to Dashboard
Add an **Entity** card pointing to `input_boolean.color_wave_trigger` as a tap-to-trigger button. Add **Entity** cards for the mode, speed, and repetitions helpers to control the effect from your dashboard.

## Parameters

All parameters are passed via the automation action's `data` field:

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `lights` | list | required | Ordered list of light entity IDs |
| `colors` | list | required | List of `[R, G, B]` values |
| `mode` | string | `wave` | Effect mode: `wave` or `sync` |
| `transition_speed` | float | `1` | Seconds to wait between each step |
| `repetitions` | int | `1` | Number of times to repeat the effect |

## Example Automation

```yaml
alias: color wave
description: ""
triggers:
  - trigger: state
    entity_id:
      - input_button.color_wave_trigger
conditions: []
actions:
  - action: python_script.color_wave
    data:
      lights:
        - light.ceiling_lights_bedroom
        - light.fonsterlampa
        - light.fonsterlampa_2
        - light.ceiling_lights_kitchen
        - light.entrance_light
      colors:
        - - 255
          - 0
          - 0
        - - 255
          - 165
          - 0
        - - 0
          - 255
          - 0
        - - 0
          - 0
          - 255
        - - 148
          - 0
          - 211
      mode: "{{ states('input_select.color_wave_mode') | default('wave') }}"
      transition_speed: "{{ states('input_number.color_wave_speed') | float(0.1) }}"
      repetitions: "{{ states('input_number.color_wave_repetitions') | int(1) }}"
mode: single
```

## Rainbow Colors

A nice 5-color rainbow preset to get started:

```yaml
colors:
  - [255, 0, 0]
  - [255, 165, 0]
  - [0, 255, 0]
  - [0, 0, 255]
  - [148, 0, 211]
```

## How It Works

1. Saves the current state of every light (on/off, brightness, color mode, RGB or color temperature)
2. Runs the chosen effect for the specified number of repetitions
3. Restores every light to its original state when done

## Notes

- `transition_speed` controls the delay between steps. Lower = faster wave. Recommended range: `0.1` – `1.0`
- Colors cycle automatically if you have fewer colors than lights
- Lights that were off before the effect will be turned off again after restore
- The script handles both `hs` (color) and `color_temp` (white) light modes correctly when restoring
