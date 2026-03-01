
lights = data.get('lights', [])
colors = data.get('colors', [])
mode = data.get('mode', 'wave')
transition_speed = data.get('transition_speed', 1)
repetitions = data.get('repetitions', 1)

def sleep(seconds):
    end = datetime.datetime.now() + datetime.timedelta(seconds = seconds)
    while datetime.datetime.now() < end:
        pass

def get_current_states():
    states = {}
    for light in lights:
        state = hass.states.get(light)
        attributes = state.attributes
       
        states[light] = {
            'state':state.state,
            'brightness':attributes.get('brightness'),
            'rgb_color':attributes.get('rgb_color'),
            'color_temp_kelvin':attributes.get('color_temp_kelvin'),
            'color_mode':attributes.get('color_mode')
        }
    return states
        
start_states = get_current_states()

logger.warning(f'current states: {start_states}')

def start_color_wave():
    for color in colors:
        for light in lights:
            hass.services.call('light', 'turn_on', {
                'entity_id':light,
                'brightness':255,
                'rgb_color':color,
                'transition': 1
            }, blocking = True)
            sleep(transition_speed)

def start_color_sync():
    for color in colors:
        for light in lights:
            hass.services.call('light', 'turn_on', {
                'entity_id':light,
                'brightness':255,
                'rgb_color':color,
                'transition': 1
            }, blocking = True)
        sleep(transition_speed)

def reset_states():
    for light, state in start_states.items():
            if(state['state'] == 'on'):
                if(state['color_mode'] == 'hs'):
                    hass.services.call('light', 'turn_on', {
                        'entity_id':light,
                        'brightness':state['brightness'],
                        'rgb_color':state['rgb_color'],
                        'transition': 1
                    })
                else:
                    hass.services.call('light', 'turn_on', {
                        'entity_id':light,
                        'brightness':state['brightness'],
                        'color_temp_kelvin': state['color_temp_kelvin'],
                        'transition': 1
                    })
            else:
                 hass.services.call('light', 'turn_off', {
                    'entity_id':light,
                    'transition': 1
                })
                 
def repeat_func(func):
    count = 0
    while count < repetitions:
        count += 1
        func()

if mode == 'wave':
    repeat_func(start_color_wave)
elif mode == 'sync':
    repeat_func(start_color_sync)

reset_states()