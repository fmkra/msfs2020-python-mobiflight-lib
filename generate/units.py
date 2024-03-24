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
        # The kilometer is an SI unit of length, equal to one thousand meters. 1km is equal to 0.621371 imperial miles.
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
        FAHRENHEIT = "fahrenheit" # TODO: check if this isn't FARENHEIT
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
    

    class GlobalPosition(Enum):
        # A degree latitude is an angle used to measure the geographic position along the North-South axis of the Earth, over it's surface. Degrees latitude range from 0° at the Equator to +90° at the North pole or -90° at the South pole.
        DEGREE_LATITUDE = 'degree latitude'
        # A degree longitude is an angle used to measure the geographic position along the East-West axis of the Earth, over it's surface. Degrees longitude range from 0° at the Prime Meridian to +180° Eastward and -180° Westward.
        DEGREE_LONGITUDE = 'degree longitude'
        # A meter latitude is defined as the number of degrees traveled for a meter of circumference of the Earth. Essentially this equals meters * (360 / 40007000).
        METER_LATITUDE = 'meter latitude'


    class AngularVelocity(Enum):
        # This is a unit of measurement that defines the number of radians that something will rotate for every second of time that passes.
        RADIAN_PER_SECOND = 'radian per second'
        # This is a unit of measurement that defines the number of full revolutions that something will complete for every minute of time that passes. A revolution is considered as a rotation of 360°.
        REVOLUTION_PER_MINUTE = 'revolution per minute'
        # This is the same as the rpm unit, only scaled by 16K using the formula: VALUE / 16384.0
        RPM_1_OVER_16K = 'rpm 1 over 16k'
        # This is a unit of measurement that defines the number minutes that something will require for to complete a full round. A round is considered as a rotation of 360°.
        MINUTE_PER_ROUND = 'minute per round'
        # TODO: check what is 'nice minute per round'
        # This is a unit of measurement that defines the number of degrees that something will rotate for every second of time that passes.
        DEGREE_PER_SECOND = 'degree per second'
        # This is a unit of measurement that defines the number of degrees that something will rotate for every second of time that passes. The value is cast as a 16bit integer using the following formula: round(VALUE) / 65536.0
        DEGREE_PER_SECOND_ANG16 = 'degree per second ang16'
    

    class AngularAcceleration(Enum):
        # This is the unit of angular (rotational) acceleration magnitude in the International System of Units (SI). Essentially it is the rate of change of angular speed or velocity by one radian per second during a one second period.
        RADIAN_PER_SECOND_SQUARED = 'radian per second squared'
        # This is a unit of angular (rotational) acceleration magnitude. Essentially it is the rate of change of angular speed or velocity by one degree per second during a one second period.
        DEGREE_PER_SECOND_SQUARED = 'degree per second squared'


    class Speed(Enum):
        # The metre per second is a unit of both speed and velocity in the International System of Units (SI). It is equal to the speed of a body covering a distance of one metre in one second of time.
        METER_PER_SECOND = 'meter per second'
        # This is the same as the meter per second (above) only scaled by 1/256, ie: VALUE / 256.
        METER_PER_SECOND_SCALER_256 = 'meter per second scaler 256'
        # The metre per minute is a unit of both speed and velocity in the metric system. It is equal to the speed of a body covering a distance of one metre in one minute of time.
        METER_PER_MINUTE = 'meter per minute'
        # The kilometer per hour is a unit of both speed and velocity in the metric system. It is equal to the speed of a body covering a distance of one kilometer in one minute of time.
        KILOMETER_PER_HOUR = 'kilometer/hour'
        # The feet/second is a unit of both speed and velocity in the imperial system. It is equal to the speed of a body covering a distance of one foot in one second of time.
        FEET_PER_SECOND = 'feet/second'
        # The feet/minute is a unit of both speed and velocity in the imperial system. It is equal to the speed of a body covering a distance of one foot in one minute of time.
        FEET_PER_MINUTE = 'feet/minute'
        # The mile per hour is a unit of both speed and velocity in the imperial system. It is equal to the speed of a body covering a distance of one mile in one hour of time.
        MILE_PER_HOUR = 'mile per hour'
        # The knot is a unit of of both speed and velocity equal to one nautical mile per hour, which is 1.852kph using the metric scale and approximately 1.15078mph using the imperial scale.
        KNOT = 'knot'
        # This is the same as the knot (above) only scaled by 1/128, ie: VALUE / 128.
        KNOT_SCALER_128 = 'knot scaler 128'
        # A mach number is a unit of of both speed and velocity based on an aircraft's speed relative to the speed of sound. An aircraft travelling at mach 1 is equivalent to 1234.8kph or 767.27mph.
        MACH = 'mach'
        # This unit will scale the mach value using the following formula: VALUE * (3.2 / 65536.0).
        MACH_3D2_OVER_64k = 'mach 3d2 over 64k'


    class Acceleration(Enum):
        # The metre per second squared is the unit of acceleration in the International System of Units (SI). It is equal to the increase in speed in meters per second for every second that passes.
        METER_PER_SECOND_SQUARED = 'meter per second squared'
        # The foot per second squared is the unit of acceleration in the imperial system. It is equal to the increase in speed in feet per second for every second that passes.
        FEET_PER_SECOND_SQUARED = 'feet per second squared'
        # The g-force is a measurement of the type of force per unit mass - typically acceleration - that causes a perception of weight. A g-force of 1g is equal to the conventional value of gravitational acceleration on Earth - about 9.8 meters per second squared, or 32.174 feet per second squared.
        G_FORCE = 'Gforce'
        # This is the same as the G Force unit, only scaled by 624 using the formula: VALUE / 624
        G_FORCE_624_SCALED = 'G Force 624 scaled'


    class Time(Enum):
        # The second is the base unit of time in the International System of Units (SI), defined as 1⁄86400 of a day, or more accurately as being equal to the time duration of 9,192,631,770 periods of the radiation corresponding to the transition between the two hyperfine levels of the fundamental unperturbed ground-state of the caesium-133 atom.
        SECOND = 'second'
        # The minute is a unit of time equal to 1⁄60 of an hour, or 60 seconds. Although not an SI unit, the minute is accepted for use with SI units.
        MINUTE = 'minute'
        # The hour is a unit of time in the International System of Units (SI), defined as 1⁄24 of a day, or more accurately as 3,600 atomic seconds.
        HOUR = 'hour'
        # The day is a unit of time equal to 24 hour. Although not an SI unit, the day is accepted for use with SI units, and is equal to 86,400 seconds.
        DAY = 'day'
        # This is a unit of time equal to 1⁄10 of an hour, or 360 seconds.
        HOUR_OVER_10 = 'hour over 10'
        # The year is a unit of time in the International System of Units (SI), defined as 3645.25 days of exactly 86,400 seconds, totaling exactly 31,557,600 seconds.
        YEAR = 'year'


    class Power(Enum):
        # The watt is a unit of power in the International System of Units (SI). It is defined as a 1 joule per second.
        WATT = 'Watt'
        # Foot pounds per second are a unit of power using the imperial system. It is the energy transferred upon applying a force of 1 pound-force through a linear displacement of 1 foot over the time of 1 second.
        FT_LB_PER_SECOND = 'ft lb per second'


    class VolumeRate(Enum):
        # A cubic metre per second is a derived International System (SI) unit of volumetric flow rate equal to that of a cube of matter with sides of one metre in length exchanged or moving each second.
        METER_CUBED_PER_SECOND = 'meter cubed per second'
        # This is a non-SI unit of volumetric flow rate, defined as the rate at which one liter of matter crosses a given surface during the period of time equal to one hour. 1 liter per hour is equivalent to 0.264172 gallons per hour.
        # NOTE: IMPORTANT! SimVars that use this unit actually require a value in liters per second (0.264172 gallons per second). This is a hold-over from the legacy FSX simulation.
        LITER_PER_HOUR = 'liter per hour'
        # This is an imperial unit of volumetric flow rate, defined as the rate at which one gallon of matter crosses a given surface during the period of time equal to one hour. 1 gallon per hour is equivalent to 3.785411784 liters per hour.
        GALLON_PER_HOUR = 'gallon per hour'

    class Weight(Enum):
        # The kilogram is the base unit of mass in the International System of Units (SI). The kilogram is defined in terms of the second and the metre, based on fixed fundamental constants of nature. It is equivalent to 2.20462 pounds.
        KILOGRAM = 'kilogram'
        # The pound is a unit of mass in the imperial system. It is equivalent to 0.453592kilos.
        POUND = 'pound'
        # This is the same as the pound (above) only scaled by 1/256, ie: VALUE / 256.
        POUND_SCALER_256 = 'pound scaler 256'
        # The slug is a unit of mass in the imperial system. A slug is defined as the mass that is accelerated by 1 foot per second when a net force of one pound is exerted on it. 1 slug is a mass equal to 32.1740 pounds or 14.59390 kilograms (based on standard gravity).
        SLUG = 'slug'


    class WeightRate(Enum):
        # This is a unit of mass flow rate in the International System of Units (SI). It is defined as the mass of matter equal to one kilogram which crosses a given surface during the period of time equal to one second.
        KILOGRAM_PER_SECOND = 'kilogram per second'
        # This is a unit of mass flow rate in the imperial system. It is defined as the mass of matter equal to one pound which crosses a given surface during the period of time equal to one hour.
        POUND_PER_HOUR = 'pound per hour'


    class ElectricalCurrent(Enum):
        # The ampere is the base unit of electric current in the International System of Units (SI). A current of one ampere is one coulomb of charge going past a given point per second.
        AMPERE = 'ampere'
        # This is the same as the amp unit, only scaled using the following formula: VALUE * (50.0 / 65535.0).
        FS7_CHARGING_AMPS = 'fs7 charging amps'


    class ElectricalPotential(Enum):
        # The volt is the derived unit for electric potential, electric potential difference (voltage), and electromotive force. It is the potential difference between two points that will impart one joule of energy per coulomb of charge that passes through it, and can be expressed in terms of SI base units.
        VOLT = 'volt'


    class Frequency(Enum):
        # The hertz is the derived unit of frequency in the International System of Units (SI) and is defined as one cycle per second.
        HERTZ = 'Hertz'
        # This is a measure of frequency equivalent to 1,000 cycles per second (103 hertz).
        KILOHERTZ = 'Kilohertz'
        # This is a measure of frequency equivalent to 1,000,000 cycles per second (106 hertz).
        MEGAHERTZ = 'Megahertz'
        # This is a definition of a frequency using a 16bit binary coded decimal.
        BDC16 = 'Frequency BCD16'
        # This is a definition of a frequency using a 32bit binary coded decimal.
        BDC32 = 'Frequency BCD32'
        # This is a definition of an ADF frequency using a 32bit binary coded decimal.
        # ['Automatic Direction Finding' is an electronic aid to navigation that identifies the relative bearing of an aircraft from a radio beacon transmitting in the MF or LF bandwidth, such as an Non-Directional Beacon or commercial radio broadcast station.]
        ADF_BCD32 = 'Frequency ADF BCD32'


    class Density(Enum):
        # The kilogram per cubic metre is an SI derived unit of density. It is defined by mass in kilograms divided by volume in cubic metres. It is equivalent to 0.00194032 slug per cubic foot, or 0.0083454 pounds per gallon.
        KILOGRAM_PER_CUBIC_METER = 'kilogram per cubic meter'
        # The slug per cubic foot is an imperial unit of density. It is defined by the mass of a slug divided by volume in cubic feet. It is equivalent to 515.379 kilograms per cubic meter, or 4.30104 pounds per gallon.
        SLUG_PER_CUBIC_FEET = 'Slug per cubic feet'
        # The pound per gallon is an imperial unit of density. It is defined by the mass of a pound divided by volume in gallons. It is equivalent to 119.826 kilograms per cubic meter, or 0.232502 slug per cubic feet.
        POUND_PER_GALLON = 'pound per gallon'


    class Pressure(Enum):
        # The pascal is the SI derived unit of pressure used to quantify internal pressure. The unit, is defined as one newton per square meter.
        PASCAL = 'pascal'
        # This is a measure of pressure equivalent to 1,000 pascal (103 pascal).
        KILOPASCAL = 'kilopascal'
        # A millimeter of mercury is a unit of pressure. It is defined as the extra pressure generated by a column of mercury one millimeter high under the force of 1 gravity. It is equivalent to 133.322 pascals, or 0.019337psi.
        MILLIMETER_OF_MERCURY = 'millimeter of mercury'
        # A centimeter of mercury is a unit of pressure. It is defined as the extra pressure generated by a column of mercury one centimeter high under the force of 1 gravity. It is equivalent to 1333.223 pascals, or 0.193367psi.
        CENTIMETER_OF_MERCURY = 'centimeter of mercury'
        # An inch of mercury is a unit of pressure. It is defined as the extra pressure generated by a column of mercury one centimeter high under the force of 1 gravity. It is equivalent to 3386.39 pascals, or 0.491154psi.
        INCH_OF_MERCURY = 'inch of mercury'
        # This unit is for inches of mercury, only the value has been scaled using the following formula: (64.0 / 65536.0) * VALUE. Generally only required for describing units of manifold pressure.
        INHG_64_OVER_64k = 'inHg 64 over 64k'
        # A millimeter of water is a unit of pressure. It is defined as the extra pressure generated by a column of water 1 mm high with a density of 1 gram per cubic centimeter, under the force of 1 gravity. It is equivalent to 9.80638 pascals, or 0.0014223psi.
        MILLIMETER_OF_WATER = 'millimeter of water'
        # Newtons per square meter is a unit that shows how the pascal unit is derived from other SI units. 1 newton per square meter equals 1 pascal.
        NEWTON_PER_SQUARE_METER = 'Newton per square meter'
        # Kilogram force per square centimeter is a unit of pressure which is not a part of the International System of Units (SI). It is equivalent to 98066.5 pascals, or 14.2233psi.
        KILOGRAM_FORCE_PER_SQUARE_CENTIMETER = 'kilogram force per square centimeter'
        # Kilograms per square meter is a unit of measurement of surface density. It is equivalent to 9.80665 pascals, or 0.001423psi.
        KILOGRAM_METER_SQUARED = 'kilogram meter squared'
        # The atmosphere is a unit of pressure defined as approximately equal to Earth's atmospheric pressure at sea level. It is equivalent to 101325 pascals, or 14.6959psi.
        ATMOSPHERE = 'atmosphere'
        # The bar is a metric unit of pressure, but not part of the International System of Units (SI). It is defined as exactly equal to 100,000 pascals, equivalent to 14.50378psi.
        BAR = 'bar'
        # The millibar is a metric unit of pressure, but not part of the International System of Units (SI). It is defined as exactly equal to 1000 pascals, equivalent to 0.0145psi.
        MILLIBAR = 'millibar'
        # This unit is the same as the millibar (above), only scaled by a factor of 1/16, ie: VALUE / 16;
        MILLIBAR_SCALER_16 = 'millibar scaler 16'
        # The pound-force per square inch is an imperial unit of pressure. It is equivalent to 6894.76 pascals.
        POUND_FORCE_PER_SQUARE_INCH = 'pound-force per square inch'
        # This is the psi value scaled by 16K, using the formula: VALUE / 16384.0
        PSI_SCALER_16K = 'psi scaler 16k'
        # This is the psi value scaled using the formula: (4 / 16384.0) * VALUE
        PSI_4_OVER_16K = 'psi 4 over 16k'
        # This is the psi value scaled using the formula: (55.0 / 16384) * VALUE. Only usually used when dealing with engine oil pressure.
        PSI_FS7_OIL_PRESSURE = 'psi fs7 oil pressure'
        # The pound-force per square foot is an imperial unit of pressure. It is equivalent to 47.8803 pascals.
        POUND_FORCE_PER_SQUARE_FOOT = 'pound-force per square foot'
        # This is the psf value scaled by 16K, using the formula: VALUE / 16384.0
        PSF_SCALER_16K = 'psf scaler 16k'
        # The slug square foot is a unit of moment of inertia in imperial units. It is equivalent to 32.17405 pound foot squared, or 1.35582 Kilogram Square Meters.
        SLUG_FEET_SQUARED = 'slug feet squared'
        # A centimeter of mercury is a unit of pressure. It is defined as the extra pressure generated by a column of mercury one centimeter high under the force of 1 gravity. It is equivalent to 1333.223 pascals, or 0.193367psi. This unit is used when defining the boost provided by superchargers or turbochargers on equipped planes.
        BOOST_CMHG = 'boost cmHg'
        # An inch of mercury is a unit of pressure. It is defined as the extra pressure generated by a column of mercury one centimeter high under the force of 1 gravity. It is equivalent to 3386.39 pascals, or 0.491154psi. This unit is used when defining the boost provided by superchargers or turbochargers on equipped planes.
        BOOST_INHG = 'boost inHg'
        # The pound-force per square inch is an imperial unit of pressure. It is equivalent to 6894.76 pascals. This unit is used when defining the boost provided by superchargers or turbochargers on equipped planes.
        BOOST_PSI = 'boost psi'


    class Torque(Enum):
        # The newton meter is a unit of torque in the International System of Units (SI). One newton-metre is equal to the torque resulting from a force of one newton applied perpendicularly to the end of a moment arm that is one metre long.
        NETWON_METER = 'Newton meter'
        # The foot-pound is a unit of energy in the imperial unit of measure. It is the energy transferred upon applying a force of one pound-force through a linear displacement of one foot. The corresponding SI unit is the joule.
        FOOT_POUND = 'foot-pound'
        # A pound-foot is a unit of torque representing one pound of force acting at a perpendicular distance of one foot from a pivot point. Conversely one pound-foot is the moment about an axis that applies one pound-force at a radius of one foot.
        LBF_FEET = 'lbf-feet'
        # A kilogram-force meter is an International System of Units (SI) unit of torque representing one kilogram-force applied perpendicularly to a one-meter long moment arm.
        KILOGRAM_METER = 'kilogram meter'
        # One poundal is the force that accelerates a mass of 1 pound at a rate of one foot per second per second. So a poundal foot is a unit of torque representing one poundal of force acting at a perpendicular distance of one foot from a pivot point.
        POUNDAL_FEET = 'poundal feet'


    class Miscellaneous(Enum):
        # The number of fractional lat / lon digits.
        FRACTIONAL_LAT_LONG_DIGITS = 'FractionalLatLonDigits'
        # This is a base unit that will be used to make conversions when using other units in RPN (Reverse Polish Notation) and SimVar calculations.
        PART = 'part'
        # The input will be halved.
        HALF = 'half'
        # The input will be divided by 3.
        THIRD = 'third'
        # Normally a value between 0 and 100, though sometimes values outside this range are possible (reverse thrust, for example).
        PERCENT = 'percent'
        # Normally a value between 0.0 and 1.0, though sometimes values outside this range are possible (reverse thrust, for example).
        PERCENT_OVER_100 = 'percent over 100'
        # This is a precentage value scaled by 16K, using the formula: VALUE / 16384.0
        PERCENT_SCALER_16K = 'percent scaler 16k'
        # This is a precentage value scaled by 32K, using the formula: VALUE / 32767.0
        PERCENT_SCALER_32K = 'percent scaler 32k'
        # This is a precentage value scaled by 223, using the formula: VALUE / 8388608.0
        PERCENT_SCALER_2POW23 = 'percent scaler 2pow23'
        # The bel is a unit used in the comparison of power levels in electrical communication or of intensities of sound, corresponding to an intensity ratio of 10 to 1.
        BEL = 'bel'
        # The decibel is a relative unit of measurement equal to one tenth of a bel.
        DECIBEL = 'decibel'
        # The input will be converted to either 0 (if it is less than a half of the "part" base value) or 1 (if it is more than half of the "part" base value)
        MORE_THAN_A_HALF = 'more_than_a_half'
        # The input value is a multiplier.
        TIMES = 'times'
        # The input value is expected to be a ratio.
        RATIO = 'ratio'
        # The input value is expected to be any real number.
        NUMBER = 'number'
        # The input value is expected to be a scaler.
        SCALER = 'scaler'
        # The input value will be converted to an integer position value either using the "part" base scale, or as a value between 0 and 16843, or 0 and , or as an integer between 0 and 128.
        # TODO: I think this should be splitted to 3 types
        POSITION = 'position'
        # A positive or negative integer corresponding to the member of the enum
        ENUM = 'Enum'
        # The only reliable numeric equivalent is that 0 is returned for False. Non-zero values, especially both 1 and -1, are used to indicate True.
        BOOL = 'Bool'
        # This unit requires a four digit octal number, and is usually only used for transponder codes.
        BCO16 = 'Bco16'
        # This indicates that the value is a bitmask where one or more bits in the value will be true/false, and each bit will represent a specific item.
        MASK = 'mask'
        # This indicates a selection of one or more flag values combined into a single value.
        FLAGS = 'flags'
        # This unit expects some kind of string input.
        STRING = 'string'
        # The input is value that will be a ratio "per radian".
        PER_RADIAN = 'per radian'
        # The input is value that will be a ratio "per degree".
        PER_DEGREE = 'per degree'
        # The input is for an animation keyframe and will be divided by 200.
        KEYFRAME = 'keyframe'