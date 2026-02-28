# Circadian Rhythm 🌅

Gradually adjusts light brightness and color temperature throughout the day.

- **Morning (06:00 → 10:00):** Lights increase from dim to full brightness with cool white light
- **Evening (16:00 → 23:30):** Lights decrease from full brightness to dim with warm light

## Installation

**1. Copy the script**
Copy `python_scripts/circadian_rythm.py` to `/config/python_scripts/` on your HA instance.

**2. Configure your lights**
Open the script and update the lights list with your entity IDs:
```python
lights = ['light.your_light_1', 'light.your_light_2']
```

**3. Create the helper toggle**
In HA go to **Settings → Devices & Services → Helpers → Create Helper → Toggle** and name it `Circadian Rythm`. This creates `input_boolean.circadian_rythm` which lets you turn the automation on/off from your dashboard.

**4. Add the automation**
Copy `automations/circadian_rythm.yaml` into your automations in HA.

## Optional: Adjust time ranges

```python
morning_start = 360   # 06:00
morning_end = 600     # 10:00
morning_temp = 4000   # cool white

evening_start = 960   # 16:00
evening_end = 1410    # 23:30
evening_temp = 2300   # warm white
```

Time is in minutes from midnight. Example: 07:30 = `7 * 60 + 30 = 450`
