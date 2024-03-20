from enum import Enum

class _FlightSim_Aircraft:
    def __init__(self, flightSim):
        self._ = flightSim
        self.Control = _FlightSim_Aircraft_Control(flightSim)


class _FlightSim_Aircraft_Control:
    def __init__(self, flightSim):
        self._ = flightSim
        self.AILERON_AVERAGE_DEFLECTION = _FlightSim_Aircraft_AILERON_AVERAGE_DEFLECTION(flightSim)
        self.AILERON_LEFT_DEFLECTION = _FlightSim_Aircraft_AILERON_LEFT_DEFLECTION(flightSim)


# Angle deflection for the aileron.	
class _FlightSim_Aircraft_AILERON_AVERAGE_DEFLECTION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle'):
        self._.get('AILERON AVERAGE DEFLECTION', unit)


# Angle deflection for the aileron.
class _FlightSim_Aircraft_AILERON_LEFT_DEFLECTION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle'):
        self._.get('AILERON LEFT DEFLECTION', unit)


class FlightSim:
    def get(self, varname):
        print('getting', varname)
    

    class Unit:
        class Length(Enum):
            # The meter is the base unit of length in the International System of Units (SI). 1m is equal to 3.28084 imperial feet.
            METER = "meter"
            # This is the same as the meter (above) only scaled by 1/256, ie: VALUE / 256.
            METER_SCALER_256 = "meter scaler 256"
            # The millimeter is an SI unit of length, equal to one thousandth of a meter. 1mm is equal to 0.0393701 inches.
            MILLIMETER = "millimeter"
            # A centimeter is an SI unit of length, equal to one hundredth of a meter. 1cm is equal to 0.393701 imperial inches.
            CENTIMETER = "centimeter"
            KILOMETER = "kilometer"

            # A nautical mile is a unit of length used in air and marine navigation. The nautical mile is defined as exactly 1852 meters (6076 ft or 1.151 miles).
            NAUTICAL_MILE = "nautical mile"
            # This is one tenth of a nautical mile, equivalent to 185.2 meters (607.61 ft).
            DECINMILE = "decinmile"
            # The inch is an imperial unit of length derived as 1/12th of a foot. It is equal to 25.4 mm.
            INCH = "inch"
            # The foot is an imperial unit of length, considered as 12 inches in length. It is equal to 0.3048 meters.
            FOOT = "foot"
            # The yard is an imperial unit of length that comprises 3 feet or 36 inches, and 1,760 yards is equal to 1 mile. It is equal to 0.9144 meters.
            YARD = "yard"
            # The mile is an imperial unit of length, equivalent to 1,609.34 meters.
            MILE = "mile"
            # This is one tenth of an imperial mile, equivalent to 160.93 meters.
            DECIMILE = "decimile"
        

        class Area(Enum):
            # A square meter is an SI unit of area, equal to the area of a square with sides of one meter. It is equal to 10.7639ft².
            SQUARE_METER = "square meter"
            # A square millimeter is an SI unit of area, equal to the area of a square with sides of one millimeter. It is equal to 0.0393701in².
            SQUARE_MILLIMETER = "square millimeter"
            # A square centimeter is an SI unit of area, equal to the area of a square with sides of one centimeter. It is equal to 0.155in².
            SQUARE_CENTIMETER = "square centimeter"
            # A square kilometer is an SI unit of area, equal to the area of a square with sides of one kilometer. It is equal to 0.386102miles².
            SQUARE_KILOMETER = "square kilometer"

            # A square inch is an imperial unit of area, equal to the area of a square with sides of one inch. It is equal to 6.4516cm².
            SQUARE_INCH = "square inch"
            # A square foot is an imperial unit of area, equal to the area of a square with sides of one foot. It is equal to 929.03cm² or 144in².
            SQUARE_FOOT = "square foot"
            # A square yard is an imperial unit of area, equal to the area of a square with sides of one yard. It is equal to 0.83612736m² or 9ft².
            SQUARE_YARD = "square yard"
            # A square mile is an imperial unit of area, equal to the area of a square with sides of one mile. It is equal to 2.58999km².
            SQUARE_MILE = "square mile"
        

        class Volume(Enum):
            # A cubic meter is an SI unit of area, equal to the area of a cube with sides of one meter. It is equal to 35.3147ft³.
            CUBIC_METER = "cubic meter"
            # A cubic millimeter is an SI unit of area, equal to the area of a cube with sides of one millimeter.
            CUBIC_MILLIMETER = "cubic millimeter"
            # A cubic centimeter is an SI unit of area, equal to the area of a cube with sides of one centimeter. It is equal to 0.0610237in³.
            CUBIC_CENTIMETER = "cubic centimeter"
            # A cubic kilometer is an SI unit of area, equal to the area of a cube with sides of one kilometer. It is equal to 0.239913miles³.
            CUBIC_KILOMETER = "cubic kilometer"

            # A cubic inch is an imperial unit of area, equal to the area of a cube with sides of one inch. It is equal to 16.3871cm³.
            CUBIC_INCH = "cubic inch"
            # A cubic foot is an imperial unit of area, equal to the area of a cube with sides of one foot. It is equal to 28316.917cm³ or 1728.01in³.
            CUBIC_FOOT = "cubic foot"
            # A cubic yard is an imperial unit of area, equal to the area of a cube with sides of one yard. It is equal to 0.764555m³ or 27ft³.
            CUBIC_YARD = "cubic yard"
            # A cubic mile is an imperial unit of area, equal to the area of a cube with sides of one mile. It is equal to 4.16818km³.
            CUBIC_MILE = "cubic mile"
            # The liter is an SI unit of volume based on the mass of one kilogram of liquid water. It is equal to 0.264172gallons.

            LITER = "liter"
            # The gallon is an imperial unit of volume, defined as 231in³. It is equal to 3.785412 litres.
            GALLON = "gallon"
            # The quart is an imperial unit of volume defined as 1 quarter of a gallon, or 57.75in³. It is equal to 0.946353 litres.
            QUART = "quart"

            # This is an imperial unit derived from quarts and gallons and only used when dealing with engine oil amounts. The formula used to derive the unit is: VALUE * ((8 / 32767) * (0.25 * (3.785411784 * 0.001)))
            FS7_OIL_QUANTITY = "fs7 oil quantity"
            

        class Temperature(Enum):
            # The kelvin is the base unit of temperature in the International System of Units (SI). The kelvin is the primary unit of temperature measurement for the physical sciences, but is often used in conjunction with the degree Celsius - which has the same magnitude - where 0 kelvin (called "Absolute Zero") corresponds to a temperature of -273.15°C. "Absolute Zero" is the equivalent -459.67°F.
            KELVIN = "kelvin"
            # The Rankine is a base unit of temperature, similar to the kelvin as 0 Rankine is the same as "Absolute Zero" kelvin. However the difference of 1 Rankine is defined as equal to 1 Fahrenheit degree, rather than the Celsius degree used on the kelvin scale. A temperature of 0K is equal to 0R which is the equivalent of -273.15°C or -459.67°F.
            RANKINE = "rankine"
            # The Fahrenheit scale is a temperature scale based on two fixed points: the temperature at which pure water ice melts (32°F) and the temperature at which water boils (212°F) both at sea level and under standard atmospheric pressure. 0°F is equal to 255.372K, 459.67R or -17.7778°C.
            FAHRENHEIT = "fahrenheit" #! check if this isn't FARENHEIT
            # The Celsius scale is a temperature scale based on 0°C for the freezing point of water and 100 °C for the boiling point of water at 1 atmosphere of pressure. 0°C is equal to 273.15K, 491.67R or 32°F
            CELSIUS = "celsius"
            # This the same as the Celsius unit only scaled by the following formula: VALUE / (1.8 * (6144 / 2060)).

            CELSIUS_FS7_EGT = "celsius fs7 egt"
            # This the same as the Celsius unit only scaled by the following formula: (VALUE - 273.15) * (16384 / 140.0). It is only used when dealing with engine oil temperature.
            CELSIUS_FS7_OIL_TEMP = "celsius fs7 oil temp"
            # This unit is for degrees Celsius scaled by 1/256, eg: VALUE / 256.
            CELSIUS_SCALER_1_OVER_256 = "celsius scaler 1/256"
            # This unit is for degrees Celsius scaled by 256, eg: VALUE * 256.
            CELSIUS_SCALER_256 = "celsius scaler 256"
            # This unit is for degrees Celsius scaled by 16K, eg: VALUE * 16384.0.
            CELSIUS_SCALER_16K = "celsius scaler 16k"


        class Angle(Enum):
            # The radian is the base unit of temperature in the International System of Units (SI). One radian is defined as the angle subtended from the center of a circle which intercepts an arc equal in length to the radius of the circle. 1 radian is equivalent to 57.296°.
            RADIAN = "radian"
            # A round is defined as an angle of the full 360 degrees (ie: a circle).
            ROUND = "round"
            # The degree (°) is a base unit of angle defined such that an entire rotation is 360 degrees. 1° is equal to 0.0174533 radians.
            DEGREE = "degree"
            # The grad (or gradian) is a unit of measurement of an angle, defined as one hundredth of the right angle. 1 grad is equal to 90°, or 1.5708 radians.
            GRAD = "grad"
            # This represents a unit that is a radian cast as a 16bit integer using the following formula: round(VALUE) / 65536.0
            ANGL16 = "angl16"
            # This represents a unit that is a radian cast as a 32bit integer using the following formula: round(VALUE) / (65536.0 * 65536.0)
            ANGL32 = "angl32"
        

        class GlobalPosition():
            pass


        class AngularVelocity():
            pass
        

        class AngularAcceleration():
            pass


        class Speed():
            pass


        class Acceleration():
            pass


        class Time():
            pass


        class Power():
            pass


        class VolumeRate():
            pass


        class Weight():
            pass


        class WeightRate():
            pass


        class ElectricalCurrent():
            pass


        class ElectricalPotential():
            pass


        class Frequency():
            pass


        class Density():
            pass


        class Pressure():
            pass


        class Torque():
            pass


        class Miscellaneous():
            pass
    

    def __init__(self):
        self.Aircraft = _FlightSim_Aircraft(self)