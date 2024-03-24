from bs4 import BeautifulSoup

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
                    extra_class_body = '\n    class Unit(Enum):\n'
                    for u in unit.split('\n')[2:]:
                        try:
                            n,v = u.split(' = ')
                        except ValueError:
                            n,*v = u.split(' ')
                            n = n.split(':')[0]
                            v = ' '.join(v)
                        v = v.upper().replace(' ', '_').replace(',', '').replace('.', '_')
                        extra_class_body += f"        {v} = {n}\n"
                    unit = 'FlightSim.Unit.Miscellaneous.ENUM'
                elif unit.startswith('String'):
                    unit_comment = "\n        # unit: " + " ".join(unit.split('\n'))
                    unit = 'FlightSim.Unit.Miscellaneous.STRING'
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
    f.write(processVariableGroup('Autopilot', 'Autopilot.html'))
    f.write(processVariableGroup('Control', 'Control.html'))
    f.write(processVariableGroup('Electrics', 'Electrics.html'))
    f.write(getFlightSimClass())



# TODO: check how the following variables work
# - Electrics.GENERAL_ENG_MASTER_ALTERNATOR - has index
# - Electrics.BLEED_AIR_ENGINE - has index
# - Electrics.BUS_LOOKUP_INDEX - second argument to Electrics variables
# - CONCORDE_VISOR_NOSE_HANDLE - weird enum
# - Some enums
# - AUTOPILOT_MAX_BANK_ID - wtf is Integer type
# - APU_BLEED_PRESSURE_RECEIVED_BY_ENGINE - not sure if unit is correct