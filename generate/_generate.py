from bs4 import BeautifulSoup
import re


unit_mapping = {
    'Percent Over 100': 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100',
    'Radians': 'FlightSim.Unit.Angle.RADIAN',
    'Number': 'FlightSim.Unit.Miscellaneous.NUMBER',
    'Bool': 'FlightSim.Unit.Miscellaneous.BOOL',
    'Degrees': 'FlightSim.Unit.Angle.DEGREE',
    'Knots': 'FlightSim.Unit.Speed.KNOT',
    'Feet (ft)': 'FlightSim.Unit.Length.FOOT',
    'Percent': 'FlightSim.Unit.Miscellaneous.PERCENT',
    'Feet (ft)/minute': 'FlightSim.Unit.Speed.FEET_PER_MINUTE',
    'Position': 'FlightSim.Unit.Miscellaneous.POSITION',
    'Amperes': 'FlightSim.Unit.ElectricalCurrent.AMPERE',
    'Volts': 'FlightSim.Unit.ElectricalPotential.VOLT',
    'Amps': 'FlightSim.Unit.ElectricalCurrent.AMPERE',
    'Pounds per square inch (psi)': 'FlightSim.Unit.Pressure.POUND_FORCE_PER_SQUARE_INCH',
    'Pound force per square foot (psf)': 'FlightSim.Unit.Pressure.POUND_FORCE_PER_SQUARE_FOOT',
    'Pounds per square foot (psf)': 'FlightSim.Unit.Pressure.POUND_FORCE_PER_SQUARE_FOOT',
    'RPM': 'FlightSim.Unit.AngularVelocity.REVOLUTION_PER_MINUTE',
    'Centimeters': 'FlightSim.Unit.Length.CENTIMETER',
    'Rankine': 'FlightSim.Unit.Temperature.RANKINE',
    'Pounds per hour': 'FlightSim.Unit.WeightRate.POUND_PER_HOUR',
    'Gallons per hour': 'FlightSim.Unit.VolumeRate.GALLON_PER_HOUR',
    'Pounds per hour': 'FlightSim.Unit.POUND_PER_HOUR',
    'Inches of mercury (inHg)': 'FlightSim.Unit.Pressure.INCH_OF_MERCURY',
    'Ratio': 'FlightSim.Unit.Miscellaneous.RATIO',
    'Scalar': 'FlightSim.Unit.Miscellaneous.SCALER',
    'Foot pounds': 'FlightSim.Unit.Torque.FOOT_POUND',
    'Hours': 'FlightSim.Unit.Time.HOUR',
    'Pounds': 'FlightSim.Unit.Weight.POUND',
    'Seconds': 'FlightSim.Unit.Time.SECOND',
    'Psf': 'FlightSim.Unit.Pressure.POUND_FORCE_PER_SQUARE_FOOT',
    'Meter': 'FlightSim.Unit.Length.METER',
    'Meters': 'FlightSim.Unit.Length.METER',
    'Meters per second': 'FlightSim.Unit.Length.METER_PER_SECOND',
    'Nautical miles': 'FlightSim.Unit.Length.NAUTICAL_MILE',
    'Hz': 'FlightSim.Unit.Frequency.HERTZ',
    'Feet': 'FlightSim.Unit.Length.FOOT',
    'MHz': 'FlightSim.Unit.Frequency.MEGAHERTZ',
    'Percent': 'FlightSim.Unit.Miscellaneous.PERCENT',
    'String': 'FlightSim.Unit.Miscellaneous.STRING',
    'Integer': 'int', # TODO: check this
    'FS7 Oil Quantity': 'FlightSim.Unit.Volume.FS7_OIL_QUANTITY',
    'Foot Pound': 'FlightSim.Unit.Torque.FOOT_POUND',
    'Mask': 'FlightSim.Unit.Miscellaneous.MASK',
    'Celsius': 'FlightSim.Unit.Temperature.CELSIUS',
    'Gallons': 'FlightSim.Unit.Volume.GALLON',
    'Foot pounds (ftlbs) per second': 'FlightSim.Unit.Power.FOOT_POUND_PER_SECOND',
    'Radians per second': 'FlightSim.Unit.AngularVelocity.RADIAN_PER_SECOND', 
    'Feet (ft) per second': 'FlightSim.Unit.Speed.FEET_PER_SECOND',
    'Foot pound': 'FlightSim.Unit.Torque.FOOT_POUND',
    'kias': 'FlightSim.Unit.Speed.KNOT', # TODO: check
    'GForce': 'FlightSim.Unit.Acceleration.G_FORCE',
    'Per radian': 'FlightSim.Unit.Miscellaneous.PER_RADIAN',
    'Mach': 'FlightSim.Unit.Speed.MACH',
    # 'Per second': 'FlightSim.Unit.',
    'Feet (ft) per minute': 'FlightSim.Unit.Speed.FEET_PER_MINUTE',
    'Square feet (ft)': 'FlightSim.Unit.Area.SQUARE_FOOT',
    'Slugs per feet squared (Slug sqft)': 'FlightSim.Unit.Pressure.SLUG_FEET_SQUARED', # TODO: check (per or times)
    'Slugs per feet squared': 'FlightSim.Unit.Pressure.SLUG_FEET_SQUARED',
    'Kilo pascal': 'FlightSim.Unit.Pressure.KILOPASCAL',
    'Feet (ft) per second squared': 'FlightSim.Unit.Acceleration.FEET_PER_SECOND_SQUARED',
    'Feet per second': 'FlightSim.Unit.Speed.FEET_PER_SECOND',
    'Radians per second squared': 'FlightSim.Unit.AngularAcceleration.RADIAN_PER_SECOND_SQUARED',
    'Frequency BCD16': 'FlightSim.Unit.Frequency.BCD16',
    'BCD16': 'FlightSim.Unit.Frequency.BCD16',
    'Inches of Mercury, inHg': 'FlightSim.Unit.Pressure.INCH_OF_MERCURY',
    'Millibars': 'FlightSim.Unit.Pressure.MILLIBAR',
    'Pounds per square foot, psf': 'FlightSim.Unit.Pressure.POUND_FORCE_PER_SQUARE_FOOT',
    'Kilometers per hour': 'FlightSim.Unit.Speed.KILOMETER_PER_HOUR',
    'Pound force per square foot': 'FlightSim.Unit.Pressure.POUND_FORCE_PER_SQUARE_FOOT',
    'Frequency ADF BCD32': 'FlightSim.Unit.Frequency.ADF_BCD32',
    # -
    # Percent with extra desc
    # Percent over 100 or position

}

processed_classes = []

def processVariableGroup(groupName, fileName):
    class_prefix = '_FlightSim_' + groupName
    processed_classes.append((class_prefix, groupName))
    with open(fileName) as f:
        data = f.read()
        parsed = BeautifulSoup(data, 'html.parser')
        classes = []
        result = ""
        for table in parsed.find_all('table'):
            for row in table.find_all('tr')[1:]:
                tr = row.find_all('td')

                var = tr[0].find('code').text

                name = var.replace(' ', '_')
                if ':' in name:
                    var = var.split(':')[0] + f':{{self._index}}'

                if len(tr) >= 4:
                    desc = tr[1]
                    desc_p = desc.find_all('p')
                    desc_out = "\n".join(["# "+" ".join(p.text.split()) for p in desc_p]) if desc_p else "# "+" ".join(desc.text.split())
                else:
                    desc = ''

                unit = tr[-2].text.strip()
                unit_comment = ''
                extra_comment = False
                extra_class_body = ''
                if len(unit.split('\n')) == 1 and unit in unit_mapping:
                    unit = unit_mapping[unit]
                elif unit.startswith('Position'):
                    if unit != 'Position':
                        unit_comment = "\n        # unit: " + unit.replace('\n', ' ')
                    unit = unit_mapping['Position']
                elif unit.startswith('Enum'):
                    extra_class_body = '\n    class Unit(Enum):\n' if len(unit.split('\n')) > 2 else ''
                    for u in unit.split('\n')[2:]:
                        try:
                            n,v = u.split(' = ')
                        except ValueError:
                            n,*v = u.split(' ')
                            n = n.split(':')[0]
                            v = ' '.join(v)
                        v = '_'.join([x for x in re.split('[^a-zA-Z0-9]', v.upper()) if x])
                        extra_class_body += f"        {v} = {n.strip()}\n"
                    unit = 'FlightSim.Unit.Miscellaneous.ENUM'
                # elif unit.startswith('String'):
                    # unit_comment = "\n        # unit: " + " ".join(unit.split('\n'))
                    # unit = 'FlightSim.Unit.Miscellaneous.STRING'
                else:
                    u = unit.split('\n')
                    
                    if len(u) >= 2 and u[1].strip() == 'or':
                        unit = f"{unit_mapping[u[0]]} | {unit_mapping[u[2]]}"
                        unit_comment = '\n        # unit: ' + ' '.join(u)
                    elif len(u) == 2 and u[0] in unit_mapping:
                        unit = unit_mapping[u[0]]
                        unit_comment = '\n        # unit: ' + ' '.join([x.strip() for x in u])
                    else:
                        extra_comment = '#! ' + ('\n# '.join(unit.split('\n')))
                        unit = ''
                
                if extra_comment:
                    desc_out += '\n' + extra_comment

                settable = str(tr[-1]).find('checkmark_stem') != -1
                # print('# ' + " ".join(desc.get_text(strip=True, separator='__NEWLINE__').split()).replace('NOTE__NEWLINE__: ', '\n# Note:').replace('__NEWLINE__.', '.').replace('__NEWLINE__', '\n# '))
                classes.append(name)
                extra_constructor_body = "\n        self._index = index" if ':' in name else ''
                result += f"""

{desc_out}
class {class_prefix}_{name.split(':')[0]}:
    def __init__(self, flightSim{', index' if ':' in name else ''}):
        self._ = flightSim{extra_constructor_body}
    {extra_class_body}
    def get(self, unit: '{unit}'):{unit_comment}
        return self._.get(f"(A:{var},{{unit.value}})")
"""
                if settable:
                    result += f"""
    def set(self, unit: '{unit}', value: str):{unit_comment}
        self._.set(f"{{value}} (>A:{var},{{unit.value}})")
"""

        result = f"""

class {class_prefix}:
    def __init__(self, flightSim):
        self._ = flightSim
""" + "\n".join([
    f"        self.{c.split(':')[0]} = {'lambda index: ' if ':' in c else ''}{class_prefix}_{c.split(':')[0]}(flightSim{', index' if ':' in c else ''})" for c in classes
    ]) + '\n' + result
    return result


def getFlightSimClass():
    res = "\n\nclass FlightSim:\n"
    with open('units.py', 'r') as f:
        res += '    ' + '\n    '.join(f.read().split('\n'))
    res += '\n\n\n'
    for c,g in processed_classes:
        res += f"    {g}: {c}\n"
    res += '\n'
    res += '    def __init__(self):\n'
    for c,g in processed_classes:
        res += f"        self.{g} = {c}(self)\n"
    return res


with open('flightsim.py', 'w') as f:
    f.write('from enum import Enum\n')
    f.write(processVariableGroup('Autopilot', 'sources/Autopilot.html'))
    f.write(processVariableGroup('Brake', 'sources/Brake.html'))
    f.write(processVariableGroup('Control', 'sources/Control.html'))
    f.write(processVariableGroup('Electrics', 'sources/Electrics.html'))
    f.write(processVariableGroup('Engine', 'sources/Engine.html'))
    f.write(processVariableGroup('FlightModel', 'sources/FlightModel.html'))
    f.write(processVariableGroup('Fuel', 'sources/Fuel.html'))
    f.write(processVariableGroup('Misc', 'sources/Misc.html'))
    f.write(processVariableGroup('Radio', 'sources/Radio.html'))
    f.write(processVariableGroup('System', 'sources/System.html'))
    f.write(getFlightSimClass())


# TODO: check if types shouldn't be narrower e.g. Meter -> Distance
# TODO: check how the following variables work
# - Electrics.GENERAL_ENG_MASTER_ALTERNATOR - has index
# - Electrics.BLEED_AIR_ENGINE - has index
# - Electrics.BUS_LOOKUP_INDEX - second argument to Electrics variables
# - CONCORDE_VISOR_NOSE_HANDLE - weird enum
# - Some enums
# - AUTOPILOT_MAX_BANK_ID - wtf is Integer type
# - APU_BLEED_PRESSURE_RECEIVED_BY_ENGINE - not sure if unit is correct
# TODO: split autopilot & brake into separate files, maybe rename FlightModel
# TODO: String (30)