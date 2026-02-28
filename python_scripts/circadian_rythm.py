# get current time
# calculate minutes from midnight
# if inside watching hours update the brightness
# calculate brightness based on current time

now = datetime.datetime.now()
hour = now.hour
minute = now.minute

current_minutes = hour * 60 + minute

# 06:00 to 10:00
morning_start = 360
morning_end = 600
morning_temp = 4000

# 16:00 to 23:30
evening_start = 960
evening_end = 1410
evening_temp = 2300

def set_light(entity_id, brightness, temp):
    hass.services.call('light', 'turn_on', {
        'entity_id':entity_id,
        'brightness':brightness,
        'color_temp_kelvin':temp
    })

def set_lights(lights, brightness, temp):
    for entity_id in lights:
        set_light(entity_id, brightness, temp)

def calcMorningBrightness():
    progress = (current_minutes-morning_start)/(morning_end-morning_start) #0-1
    brightness = int(10 + (progress*245)) #0-255
    return brightness

def calcEveningBrightness():
    progress = (current_minutes-evening_start)/(evening_end-evening_start) #0-1
    brightness = int(255 - (progress*255)) #255-0
    return brightness

def isMorning():
    return morning_start <= current_minutes <= morning_end

def isEvening():
    return evening_start <= current_minutes <= evening_end


def update_lights():
    logger.warning('circadian_rythm.py running')
    lights = ['light.ceiling_lamps_all', 'light.fonsterlampa', 'light.fonsterlampa_2']

    if isMorning():
        brightness = calcMorningBrightness()
        set_lights(lights, brightness, morning_temp)
        logger.warning(f'Morning Brightness: {brightness}')
    elif isEvening():
        brightness = calcEveningBrightness()
        set_lights(lights, brightness, evening_temp)
        logger.warning(f'Evening Brightness: {brightness}')
    else:
        logger.warning(f'Not inside morning or evening hours')


update_lights()