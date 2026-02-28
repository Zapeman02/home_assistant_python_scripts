# Home Assistant Python Scripts 🏠

A collection of Python scripts for Home Assistant, using the built-in `python_script` integration. Each script comes with a ready-to-use automation yaml file.

## Requirements

- Home Assistant with `python_script` integration enabled
- Add this to your `configuration.yaml` if not already there:

```yaml
python_script:
```

## Scripts

| Script | Description |
|--------|-------------|
| [Circadian Rhythm](docs/circadian_rythm.md) | Gradually adjusts light brightness and color temperature throughout the day |

## Installation

### 1. Copy the script
Place the `.py` file in your HA config folder:
```
/config/python_scripts/script_name.py
```

### 2. Copy the automation
Import the `.yaml` file in HA under **Settings → Automations** or add it to your `automations.yaml`.

### 3. Follow the script's own doc
Each script has its own doc in the `/docs` folder with specific setup instructions.

## Contributing

Feel free to open issues or pull requests if you have ideas, improvements or find bugs!
