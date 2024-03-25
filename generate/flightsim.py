from enum import Enum


class _FlightSim_Autopilot:
    def __init__(self, flightSim):
        self._ = flightSim
        self.AUTOPILOT_AIRSPEED_ACQUISITION = _FlightSim_Autopilot_AUTOPILOT_AIRSPEED_ACQUISITION(flightSim)
        self.AUTOPILOT_AIRSPEED_HOLD = _FlightSim_Autopilot_AUTOPILOT_AIRSPEED_HOLD(flightSim)
        self.AUTOPILOT_AIRSPEED_HOLD_CURRENT = _FlightSim_Autopilot_AUTOPILOT_AIRSPEED_HOLD_CURRENT(flightSim)
        self.AUTOPILOT_AIRSPEED_HOLD_VAR = _FlightSim_Autopilot_AUTOPILOT_AIRSPEED_HOLD_VAR(flightSim)
        self.AUTOPILOT_AIRSPEED_MAX_CALCULATED = _FlightSim_Autopilot_AUTOPILOT_AIRSPEED_MAX_CALCULATED(flightSim)
        self.AUTOPILOT_AIRSPEED_MIN_CALCULATED = _FlightSim_Autopilot_AUTOPILOT_AIRSPEED_MIN_CALCULATED(flightSim)
        self.AUTOPILOT_ALT_RADIO_MODE = _FlightSim_Autopilot_AUTOPILOT_ALT_RADIO_MODE(flightSim)
        self.AUTOPILOT_ALTITUDE_ARM = _FlightSim_Autopilot_AUTOPILOT_ALTITUDE_ARM(flightSim)
        self.AUTOPILOT_ALTITUDE_LOCK = _FlightSim_Autopilot_AUTOPILOT_ALTITUDE_LOCK(flightSim)
        self.AUTOPILOT_ALTITUDE_LOCK_VAR = _FlightSim_Autopilot_AUTOPILOT_ALTITUDE_LOCK_VAR(flightSim)
        self.AUTOPILOT_ALTITUDE_MANUALLY_TUNABLE = _FlightSim_Autopilot_AUTOPILOT_ALTITUDE_MANUALLY_TUNABLE(flightSim)
        self.AUTOPILOT_ALTITUDE_SLOT_INDEX = _FlightSim_Autopilot_AUTOPILOT_ALTITUDE_SLOT_INDEX(flightSim)
        self.AUTOPILOT_APPROACH_ACTIVE = _FlightSim_Autopilot_AUTOPILOT_APPROACH_ACTIVE(flightSim)
        self.AUTOPILOT_APPROACH_ARM = _FlightSim_Autopilot_AUTOPILOT_APPROACH_ARM(flightSim)
        self.AUTOPILOT_APPROACH_CAPTURED = _FlightSim_Autopilot_AUTOPILOT_APPROACH_CAPTURED(flightSim)
        self.AUTOPILOT_APPROACH_HOLD = _FlightSim_Autopilot_AUTOPILOT_APPROACH_HOLD(flightSim)
        self.AUTOPILOT_APPROACH_IS_LOCALIZER = _FlightSim_Autopilot_AUTOPILOT_APPROACH_IS_LOCALIZER(flightSim)
        self.AUTOPILOT_ATTITUDE_HOLD = _FlightSim_Autopilot_AUTOPILOT_ATTITUDE_HOLD(flightSim)
        self.AUTOPILOT_AVAILABLE = _FlightSim_Autopilot_AUTOPILOT_AVAILABLE(flightSim)
        self.AUTOPILOT_AVIONICS_MANAGED = _FlightSim_Autopilot_AUTOPILOT_AVIONICS_MANAGED(flightSim)
        self.AUTOPILOT_BACKCOURSE_HOLD = _FlightSim_Autopilot_AUTOPILOT_BACKCOURSE_HOLD(flightSim)
        self.AUTOPILOT_BANK_HOLD = _FlightSim_Autopilot_AUTOPILOT_BANK_HOLD(flightSim)
        self.AUTOPILOT_BANK_HOLD_REF = _FlightSim_Autopilot_AUTOPILOT_BANK_HOLD_REF(flightSim)
        self.AUTOPILOT_CRUISE_SPEED_HOLD = _FlightSim_Autopilot_AUTOPILOT_CRUISE_SPEED_HOLD(flightSim)
        self.AUTOPILOT_DEFAULT_PITCH_MODE = _FlightSim_Autopilot_AUTOPILOT_DEFAULT_PITCH_MODE(flightSim)
        self.AUTOPILOT_DEFAULT_ROLL_MODE = _FlightSim_Autopilot_AUTOPILOT_DEFAULT_ROLL_MODE(flightSim)
        self.AUTOPILOT_DISENGAGED = _FlightSim_Autopilot_AUTOPILOT_DISENGAGED(flightSim)
        self.AUTOPILOT_FLIGHT_DIRECTOR_ACTIVE = _FlightSim_Autopilot_AUTOPILOT_FLIGHT_DIRECTOR_ACTIVE(flightSim)
        self.AUTOPILOT_FLIGHT_DIRECTOR_BANK = _FlightSim_Autopilot_AUTOPILOT_FLIGHT_DIRECTOR_BANK(flightSim)
        self.AUTOPILOT_FLIGHT_DIRECTOR_BANK_EX1 = _FlightSim_Autopilot_AUTOPILOT_FLIGHT_DIRECTOR_BANK_EX1(flightSim)
        self.AUTOPILOT_FLIGHT_DIRECTOR_PITCH = _FlightSim_Autopilot_AUTOPILOT_FLIGHT_DIRECTOR_PITCH(flightSim)
        self.AUTOPILOT_FLIGHT_DIRECTOR_PITCH_EX1 = _FlightSim_Autopilot_AUTOPILOT_FLIGHT_DIRECTOR_PITCH_EX1(flightSim)
        self.AUTOPILOT_FLIGHT_LEVEL_CHANGE = _FlightSim_Autopilot_AUTOPILOT_FLIGHT_LEVEL_CHANGE(flightSim)
        self.AUTOPILOT_GLIDESLOPE_ACTIVE = _FlightSim_Autopilot_AUTOPILOT_GLIDESLOPE_ACTIVE(flightSim)
        self.AUTOPILOT_GLIDESLOPE_ARM = _FlightSim_Autopilot_AUTOPILOT_GLIDESLOPE_ARM(flightSim)
        self.AUTOPILOT_GLIDESLOPE_HOLD = _FlightSim_Autopilot_AUTOPILOT_GLIDESLOPE_HOLD(flightSim)
        self.AUTOPILOT_HEADING_LOCK = _FlightSim_Autopilot_AUTOPILOT_HEADING_LOCK(flightSim)
        self.AUTOPILOT_HEADING_LOCK_DIR = _FlightSim_Autopilot_AUTOPILOT_HEADING_LOCK_DIR(flightSim)
        self.AUTOPILOT_HEADING_MANUALLY_TUNABLE = _FlightSim_Autopilot_AUTOPILOT_HEADING_MANUALLY_TUNABLE(flightSim)
        self.AUTOPILOT_HEADING_SLOT_INDEX = _FlightSim_Autopilot_AUTOPILOT_HEADING_SLOT_INDEX(flightSim)
        self.AUTOPILOT_MACH_HOLD = _FlightSim_Autopilot_AUTOPILOT_MACH_HOLD(flightSim)
        self.AUTOPILOT_MACH_HOLD_VAR = _FlightSim_Autopilot_AUTOPILOT_MACH_HOLD_VAR(flightSim)
        self.AUTOPILOT_MANAGED_INDEX = _FlightSim_Autopilot_AUTOPILOT_MANAGED_INDEX(flightSim)
        self.AUTOPILOT_MANAGED_SPEED_IN_MACH = _FlightSim_Autopilot_AUTOPILOT_MANAGED_SPEED_IN_MACH(flightSim)
        self.AUTOPILOT_MANAGED_THROTTLE_ACTIVE = _FlightSim_Autopilot_AUTOPILOT_MANAGED_THROTTLE_ACTIVE(flightSim)
        self.AUTOPILOT_MASTER = _FlightSim_Autopilot_AUTOPILOT_MASTER(flightSim)
        self.AUTOPILOT_MAX_BANK = _FlightSim_Autopilot_AUTOPILOT_MAX_BANK(flightSim)
        self.AUTOPILOT_MAX_BANK_ID = _FlightSim_Autopilot_AUTOPILOT_MAX_BANK_ID(flightSim)
        self.AUTOPILOT_MAX_SPEED_HOLD = _FlightSim_Autopilot_AUTOPILOT_MAX_SPEED_HOLD(flightSim)
        self.AUTOPILOT_NAV1_LOCK = _FlightSim_Autopilot_AUTOPILOT_NAV1_LOCK(flightSim)
        self.AUTOPILOT_NAV_SELECTED = _FlightSim_Autopilot_AUTOPILOT_NAV_SELECTED(flightSim)
        self.AUTOPILOT_PITCH_HOLD = _FlightSim_Autopilot_AUTOPILOT_PITCH_HOLD(flightSim)
        self.AUTOPILOT_PITCH_HOLD_REF = _FlightSim_Autopilot_AUTOPILOT_PITCH_HOLD_REF(flightSim)
        self.AUTOPILOT_RPM_HOLD = _FlightSim_Autopilot_AUTOPILOT_RPM_HOLD(flightSim)
        self.AUTOPILOT_RPM_HOLD_VAR = _FlightSim_Autopilot_AUTOPILOT_RPM_HOLD_VAR(flightSim)
        self.AUTOPILOT_RPM_SLOT_INDEX = _FlightSim_Autopilot_AUTOPILOT_RPM_SLOT_INDEX(flightSim)
        self.AUTOPILOT_SPEED_SETTING = _FlightSim_Autopilot_AUTOPILOT_SPEED_SETTING(flightSim)
        self.AUTOPILOT_SPEED_SLOT_INDEX = _FlightSim_Autopilot_AUTOPILOT_SPEED_SLOT_INDEX(flightSim)
        self.AUTOPILOT_TAKEOFF_POWER_ACTIVE = _FlightSim_Autopilot_AUTOPILOT_TAKEOFF_POWER_ACTIVE(flightSim)
        self.AUTOPILOT_THROTTLE_ARM = _FlightSim_Autopilot_AUTOPILOT_THROTTLE_ARM(flightSim)
        self.AUTOPILOT_THROTTLE_MAX_THRUST = _FlightSim_Autopilot_AUTOPILOT_THROTTLE_MAX_THRUST(flightSim)
        self.AUTOPILOT_VERTICAL_HOLD = _FlightSim_Autopilot_AUTOPILOT_VERTICAL_HOLD(flightSim)
        self.AUTOPILOT_VERTICAL_HOLD_VAR = _FlightSim_Autopilot_AUTOPILOT_VERTICAL_HOLD_VAR(flightSim)
        self.AUTOPILOT_VS_SLOT_INDEX = _FlightSim_Autopilot_AUTOPILOT_VS_SLOT_INDEX(flightSim)
        self.AUTOPILOT_WING_LEVELER = _FlightSim_Autopilot_AUTOPILOT_WING_LEVELER(flightSim)
        self.AUTOPILOT_YAW_DAMPER = _FlightSim_Autopilot_AUTOPILOT_YAW_DAMPER(flightSim)
        self.ASSISTANCE_LANDING_ENABLED = _FlightSim_Autopilot_ASSISTANCE_LANDING_ENABLED(flightSim)
        self.ASSISTANCE_TAKEOFF_ENABLED = _FlightSim_Autopilot_ASSISTANCE_TAKEOFF_ENABLED(flightSim)
        self.AI_ANTISTALL_STATE = _FlightSim_Autopilot_AI_ANTISTALL_STATE(flightSim)
        self.AI_AUTOTRIM_ACTIVE = _FlightSim_Autopilot_AI_AUTOTRIM_ACTIVE(flightSim)
        self.AI_AUTOTRIM_ACTIVE_AGAINST_PLAYER = _FlightSim_Autopilot_AI_AUTOTRIM_ACTIVE_AGAINST_PLAYER(flightSim)
        self.AI_CONTROLS = _FlightSim_Autopilot_AI_CONTROLS(flightSim)
        self.AI_CURSOR_MODE_ACTIVE = _FlightSim_Autopilot_AI_CURSOR_MODE_ACTIVE(flightSim)
        self.ATTITUDE_BARS_POSITION = _FlightSim_Autopilot_ATTITUDE_BARS_POSITION(flightSim)
        self.ATTITUDE_CAGE = _FlightSim_Autopilot_ATTITUDE_CAGE(flightSim)
        self.ATTITUDE_INDICATOR_BANK_DEGREES = _FlightSim_Autopilot_ATTITUDE_INDICATOR_BANK_DEGREES(flightSim)
        self.ATTITUDE_INDICATOR_PITCH_DEGREES = _FlightSim_Autopilot_ATTITUDE_INDICATOR_PITCH_DEGREES(flightSim)
        self.DELEGATE_CONTROLS_TO_AI = _FlightSim_Autopilot_DELEGATE_CONTROLS_TO_AI(flightSim)
        self.FLY_ASSISTANT_CANCEL_DESTINATION = _FlightSim_Autopilot_FLY_ASSISTANT_CANCEL_DESTINATION(flightSim)
        self.FLY_ASSISTANT_CANCEL_DESTINATION_DISPLAY = _FlightSim_Autopilot_FLY_ASSISTANT_CANCEL_DESTINATION_DISPLAY(flightSim)
        self.FLY_ASSISTANT_COM_AI_LOCKED = _FlightSim_Autopilot_FLY_ASSISTANT_COM_AI_LOCKED(flightSim)
        self.FLY_ASSISTANT_HAVE_DESTINATION = _FlightSim_Autopilot_FLY_ASSISTANT_HAVE_DESTINATION(flightSim)
        self.FLY_ASSISTANT_LANDING_SPEED = _FlightSim_Autopilot_FLY_ASSISTANT_LANDING_SPEED(flightSim)
        self.FLY_ASSISTANT_LANDING_SPEED_DISPLAY_MODE = _FlightSim_Autopilot_FLY_ASSISTANT_LANDING_SPEED_DISPLAY_MODE(flightSim)
        self.FLY_ASSISTANT_NEAREST_CATEGORY = _FlightSim_Autopilot_FLY_ASSISTANT_NEAREST_CATEGORY(flightSim)
        self.FLY_ASSISTANT_NEAREST_COUNT = _FlightSim_Autopilot_FLY_ASSISTANT_NEAREST_COUNT(flightSim)
        self.FLY_ASSISTANT_NEAREST_METADATA = _FlightSim_Autopilot_FLY_ASSISTANT_NEAREST_METADATA(flightSim)
        self.FLY_ASSISTANT_NEAREST_NAME = _FlightSim_Autopilot_FLY_ASSISTANT_NEAREST_NAME(flightSim)
        self.FLY_ASSISTANT_NEAREST_SELECTED = _FlightSim_Autopilot_FLY_ASSISTANT_NEAREST_SELECTED(flightSim)
        self.FLY_ASSISTANT_RIBBONS_ACTIVE = _FlightSim_Autopilot_FLY_ASSISTANT_RIBBONS_ACTIVE(flightSim)
        self.FLY_ASSISTANT_SET_AS_DESTINATION = _FlightSim_Autopilot_FLY_ASSISTANT_SET_AS_DESTINATION(flightSim)
        self.FLY_ASSISTANT_STALL_SPEED = _FlightSim_Autopilot_FLY_ASSISTANT_STALL_SPEED(flightSim)
        self.FLY_ASSISTANT_STALL_SPEED_DISPLAY_MODE = _FlightSim_Autopilot_FLY_ASSISTANT_STALL_SPEED_DISPLAY_MODE(flightSim)
        self.FLY_ASSISTANT_TAKEOFF_SPEED = _FlightSim_Autopilot_FLY_ASSISTANT_TAKEOFF_SPEED(flightSim)
        self.FLY_ASSISTANT_TAKEOFF_SPEED_DISPLAY_MODE = _FlightSim_Autopilot_FLY_ASSISTANT_TAKEOFF_SPEED_DISPLAY_MODE(flightSim)
        self.FLY_ASSISTANT_TAKEOFF_SPEED_ESTIMATED = _FlightSim_Autopilot_FLY_ASSISTANT_TAKEOFF_SPEED_ESTIMATED(flightSim)


# Currently not used within the simulation.
class _FlightSim_Autopilot_AUTOPILOT_AIRSPEED_ACQUISITION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT AIRSPEED ACQUISITION,{unit.value})")


# returns whether airspeed hold is active (1, TRUE) or not (0, FALSE).
class _FlightSim_Autopilot_AUTOPILOT_AIRSPEED_HOLD:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT AIRSPEED HOLD,{unit.value})")


# Currently not used within the simulation.
class _FlightSim_Autopilot_AUTOPILOT_AIRSPEED_HOLD_CURRENT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT AIRSPEED HOLD CURRENT,{unit.value})")


# Returns the target holding airspeed for the autopilot.
class _FlightSim_Autopilot_AUTOPILOT_AIRSPEED_HOLD_VAR:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.KNOT'):
        return self._.get(f"(A:AUTOPILOT AIRSPEED HOLD VAR,{unit.value})")


# Returns the maximum calculated airspeed (kcas) limit set for the autopilot.
class _FlightSim_Autopilot_AUTOPILOT_AIRSPEED_MAX_CALCULATED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.KNOT'):
        return self._.get(f"(A:AUTOPILOT AIRSPEED MAX CALCULATED,{unit.value})")


# Returns the minimum calculated airspeed (kcas) limit set for the autopilot.
class _FlightSim_Autopilot_AUTOPILOT_AIRSPEED_MIN_CALCULATED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.KNOT'):
        return self._.get(f"(A:AUTOPILOT AIRSPEED MIN CALCULATED,{unit.value})")


# If enabled the Autopilot will use the Radio Altitude rather than the Indicated Altitude.
class _FlightSim_Autopilot_AUTOPILOT_ALT_RADIO_MODE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT ALT RADIO MODE,{unit.value})")


# Returns whether the autopilot is in Altitude Arm mode (1, TRUE) or not (0, FALSE).
class _FlightSim_Autopilot_AUTOPILOT_ALTITUDE_ARM:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT ALTITUDE ARM,{unit.value})")


# Altitude hold active
class _FlightSim_Autopilot_AUTOPILOT_ALTITUDE_LOCK:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT ALTITUDE LOCK,{unit.value})")


# Set or get the slot index which the altitude hold mode will track when captured. See alt_mode_slot_index for more information.
class _FlightSim_Autopilot_AUTOPILOT_ALTITUDE_LOCK_VAR:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.FOOT'):
        return self._.get(f"(A:AUTOPILOT ALTITUDE LOCK VAR,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Length.FOOT', value: str):
        self._.set(f"{value} (>A:AUTOPILOT ALTITUDE LOCK VAR,{unit.value})")


# Whether or not the autopilot altitude is manually tunable or not.
class _FlightSim_Autopilot_AUTOPILOT_ALTITUDE_MANUALLY_TUNABLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT ALTITUDE MANUALLY TUNABLE,{unit.value})")


# Index of the slot that the autopilot will use for the altitude reference. Note that there are 3 slots (1, 2, 3) that you can set/get normally, however you can also target slot index 0. Writing to slot 0 will overwrite all other slots with the slot 0 value, and by default the autopilot will follow slot 0 if you have not selected any slot index.
# See alt_mode_slot_index for more information.
class _FlightSim_Autopilot_AUTOPILOT_ALTITUDE_SLOT_INDEX:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:AUTOPILOT ALTITUDE SLOT INDEX,{unit.value})")


# When true, the autopilot is currently flying the approach Flight Plan (the last legs).
class _FlightSim_Autopilot_AUTOPILOT_APPROACH_ACTIVE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT APPROACH ACTIVE,{unit.value})")


# Returns true when the autopilot is active on the approach, once it reaches the adequate condition (in most cases, once it reaches the second-last waypoint of the flightplan).
class _FlightSim_Autopilot_AUTOPILOT_APPROACH_ARM:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT APPROACH ARM,{unit.value})")


# Returns true when the lateral NAV mode is engaged and the angular deviation with the current tuned navigation frequency is less than 5°.
class _FlightSim_Autopilot_AUTOPILOT_APPROACH_CAPTURED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT APPROACH CAPTURED,{unit.value})")


# Returns whether pproach mode is active (1, TRUE) or not (0, FALSE).
class _FlightSim_Autopilot_AUTOPILOT_APPROACH_HOLD:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT APPROACH HOLD,{unit.value})")


# Returns true if the current approach is using a localizer.
class _FlightSim_Autopilot_AUTOPILOT_APPROACH_IS_LOCALIZER:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT APPROACH IS LOCALIZER,{unit.value})")


# Attitude hold active
class _FlightSim_Autopilot_AUTOPILOT_ATTITUDE_HOLD:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT ATTITUDE HOLD,{unit.value})")


# Available flag
class _FlightSim_Autopilot_AUTOPILOT_AVAILABLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT AVAILABLE,{unit.value})")


# Returns whether the autopilot has active managed avionics (1, TRUE) or not (0, FALSE).
class _FlightSim_Autopilot_AUTOPILOT_AVIONICS_MANAGED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT AVIONICS MANAGED,{unit.value})")


# Returns whether the autopilot back course mode is active (1, TRUE) or not (0, FALSE).
class _FlightSim_Autopilot_AUTOPILOT_BACKCOURSE_HOLD:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT BACKCOURSE HOLD,{unit.value})")


# Returns whether the autopilot bank hold mode is active (1, TRUE) or not (0, FALSE).
class _FlightSim_Autopilot_AUTOPILOT_BANK_HOLD:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT BANK HOLD,{unit.value})")


# The current bank-hold bank reference.
# Note that if you set this, the next frame the value will be overwritten by the engine, so you may need to write to this every game frame to ensure it maintains the required value.
class _FlightSim_Autopilot_AUTOPILOT_BANK_HOLD_REF:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:AUTOPILOT BANK HOLD REF,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Angle.DEGREE', value: str):
        self._.set(f"{value} (>A:AUTOPILOT BANK HOLD REF,{unit.value})")


# Currently not used within the simulation.
class _FlightSim_Autopilot_AUTOPILOT_CRUISE_SPEED_HOLD:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT CRUISE SPEED HOLD,{unit.value})")


# The current default pitch mode of the autopilot as configured in the plane configuration with the parameter default_pitch_mode.
class _FlightSim_Autopilot_AUTOPILOT_DEFAULT_PITCH_MODE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        NONE = 0
        PITCH = 1
        ALTITUDE_HOLD = 2
        VERTICAL_SPEED = 3

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:AUTOPILOT DEFAULT PITCH MODE,{unit.value})")


# The current default roll mode of the autopilot as configured in the plane configuration with the parameter default_bank_mode.
class _FlightSim_Autopilot_AUTOPILOT_DEFAULT_ROLL_MODE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        NONE = 0
        WING_LEVELER = 1
        HEADING = 2
        ROLL_HOLD = 3

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:AUTOPILOT DEFAULT ROLL MODE,{unit.value})")


# Returns whether the autopilot has been disengaged (1, TRUE) or not (0, FALSE).
class _FlightSim_Autopilot_AUTOPILOT_DISENGAGED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT DISENGAGED,{unit.value})")


# Flight director active
class _FlightSim_Autopilot_AUTOPILOT_FLIGHT_DIRECTOR_ACTIVE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT FLIGHT DIRECTOR ACTIVE,{unit.value})")


# Reference bank angle
class _FlightSim_Autopilot_AUTOPILOT_FLIGHT_DIRECTOR_BANK:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:AUTOPILOT FLIGHT DIRECTOR BANK,{unit.value})")


# Raw reference bank angle
class _FlightSim_Autopilot_AUTOPILOT_FLIGHT_DIRECTOR_BANK_EX1:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:AUTOPILOT FLIGHT DIRECTOR BANK EX1,{unit.value})")


# Reference pitch angle
class _FlightSim_Autopilot_AUTOPILOT_FLIGHT_DIRECTOR_PITCH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:AUTOPILOT FLIGHT DIRECTOR PITCH,{unit.value})")


# Raw reference pitch angle
class _FlightSim_Autopilot_AUTOPILOT_FLIGHT_DIRECTOR_PITCH_EX1:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:AUTOPILOT FLIGHT DIRECTOR PITCH EX1,{unit.value})")


# Boolean, toggles the autopilot Flight Level Change mode
class _FlightSim_Autopilot_AUTOPILOT_FLIGHT_LEVEL_CHANGE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT FLIGHT LEVEL CHANGE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:AUTOPILOT FLIGHT LEVEL CHANGE,{unit.value})")


# When true, the autopilot is receiving a signal from the runway beacon and is following the slope to reach the ground.
class _FlightSim_Autopilot_AUTOPILOT_GLIDESLOPE_ACTIVE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT GLIDESLOPE ACTIVE,{unit.value})")


# Returns true when the autopilot is active on the glide slope.
class _FlightSim_Autopilot_AUTOPILOT_GLIDESLOPE_ARM:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT GLIDESLOPE ARM,{unit.value})")


# Returns whether the autopilot glidslope hold is active (1, TRUE) or not (0, FALSE).
class _FlightSim_Autopilot_AUTOPILOT_GLIDESLOPE_HOLD:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT GLIDESLOPE HOLD,{unit.value})")


# Returns whether the autopilot heading lock is enabled (1, TRUE) or not (0, FALSE).
class _FlightSim_Autopilot_AUTOPILOT_HEADING_LOCK:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT HEADING LOCK,{unit.value})")


# Specifies / Returns the locked in heading for the autopilot.
class _FlightSim_Autopilot_AUTOPILOT_HEADING_LOCK_DIR:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:AUTOPILOT HEADING LOCK DIR,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Angle.DEGREE', value: str):
        self._.set(f"{value} (>A:AUTOPILOT HEADING LOCK DIR,{unit.value})")


# Whether or not the autopilot heading is manually tunable or not.
class _FlightSim_Autopilot_AUTOPILOT_HEADING_MANUALLY_TUNABLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT HEADING MANUALLY TUNABLE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:AUTOPILOT HEADING MANUALLY TUNABLE,{unit.value})")


# Index of the slot that the autopilot will use for the heading reference. Note that there are 3 slots (1, 2, 3) that you can set/get normally, however you can also target slot index 0. Writing to slot 0 will overwrite all other slots with the slot 0 value, and by default the autopilot will follow slot 0 if you have not selected any slot index.
class _FlightSim_Autopilot_AUTOPILOT_HEADING_SLOT_INDEX:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:AUTOPILOT HEADING SLOT INDEX,{unit.value})")


# Mach hold active
class _FlightSim_Autopilot_AUTOPILOT_MACH_HOLD:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT MACH HOLD,{unit.value})")


# Returns the target holding mach airspeed for the autopilot.
class _FlightSim_Autopilot_AUTOPILOT_MACH_HOLD_VAR:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:AUTOPILOT MACH HOLD VAR,{unit.value})")


# Currently not used within the simulation.
class _FlightSim_Autopilot_AUTOPILOT_MANAGED_INDEX:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:AUTOPILOT MANAGED INDEX,{unit.value})")


# Returns whether the managed speed is in mach (1, TRUE) or not (0, FALSE).
class _FlightSim_Autopilot_AUTOPILOT_MANAGED_SPEED_IN_MACH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT MANAGED SPEED IN MACH,{unit.value})")


# Returns whether the autopilot managed throttle is active (1, TRUE) or not (0, FALSE).
class _FlightSim_Autopilot_AUTOPILOT_MANAGED_THROTTLE_ACTIVE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT MANAGED THROTTLE ACTIVE,{unit.value})")


# On/off flag
class _FlightSim_Autopilot_AUTOPILOT_MASTER:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT MASTER,{unit.value})")


# Returns the maximum banking angle for the autopilot, in radians.
class _FlightSim_Autopilot_AUTOPILOT_MAX_BANK:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:AUTOPILOT MAX BANK,{unit.value})")


# Returns the index of the current maximum bank setting of the autopilot.
class _FlightSim_Autopilot_AUTOPILOT_MAX_BANK_ID:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'int'):
        return self._.get(f"(A:AUTOPILOT MAX BANK ID,{unit.value})")


# Currently not used within the simulation.
class _FlightSim_Autopilot_AUTOPILOT_MAX_SPEED_HOLD:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT MAX SPEED HOLD,{unit.value})")


# Returns TRUE (1) if the autopilot Nav1 lock is applied, or 0 (FALSE) otherwise.
class _FlightSim_Autopilot_AUTOPILOT_NAV1_LOCK:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT NAV1 LOCK,{unit.value})")


# Index of Nav radio selected
class _FlightSim_Autopilot_AUTOPILOT_NAV_SELECTED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:AUTOPILOT NAV SELECTED,{unit.value})")


# Set to True if the autopilot pitch hold has is engaged.
class _FlightSim_Autopilot_AUTOPILOT_PITCH_HOLD:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT PITCH HOLD,{unit.value})")


# Returns the current autotpilot reference pitch.
class _FlightSim_Autopilot_AUTOPILOT_PITCH_HOLD_REF:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:AUTOPILOT PITCH HOLD REF,{unit.value})")


# True if autopilot rpm hold applied
class _FlightSim_Autopilot_AUTOPILOT_RPM_HOLD:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT RPM HOLD,{unit.value})")


# Selected rpm
class _FlightSim_Autopilot_AUTOPILOT_RPM_HOLD_VAR:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:AUTOPILOT RPM HOLD VAR,{unit.value})")


# Index of the slot that the autopilot will use for the RPM reference. Note that there are 3 slots (1, 2, 3) that you can set/get normally, however you can also target slot index 0. Writing to slot 0 will overwrite all other slots with the slot 0 value, and by default the autopilot will follow slot 0 if you have not selected any slot index.
class _FlightSim_Autopilot_AUTOPILOT_RPM_SLOT_INDEX:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:AUTOPILOT RPM SLOT INDEX,{unit.value})")


# Currently not used within the simulation.
class _FlightSim_Autopilot_AUTOPILOT_SPEED_SETTING:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.KNOT'):
        return self._.get(f"(A:AUTOPILOT SPEED SETTING,{unit.value})")


# Index of the managed references
class _FlightSim_Autopilot_AUTOPILOT_SPEED_SLOT_INDEX:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:AUTOPILOT SPEED SLOT INDEX,{unit.value})")


# Takeoff / Go Around power mode active
class _FlightSim_Autopilot_AUTOPILOT_TAKEOFF_POWER_ACTIVE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT TAKEOFF POWER ACTIVE,{unit.value})")


# Returns whether the autopilot auto-throttle is armed (1, TRUE) or not (0, FALSE).
class _FlightSim_Autopilot_AUTOPILOT_THROTTLE_ARM:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT THROTTLE ARM,{unit.value})")


# This can be used to set/get the thrust lever position for autopilot maximum thrust.
class _FlightSim_Autopilot_AUTOPILOT_THROTTLE_MAX_THRUST:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:AUTOPILOT THROTTLE MAX THRUST,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT', value: str):
        self._.set(f"{value} (>A:AUTOPILOT THROTTLE MAX THRUST,{unit.value})")


# True if autopilot vertical hold applied
class _FlightSim_Autopilot_AUTOPILOT_VERTICAL_HOLD:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT VERTICAL HOLD,{unit.value})")


# Selected vertical speed
class _FlightSim_Autopilot_AUTOPILOT_VERTICAL_HOLD_VAR:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.FEET_PER_MINUTE'):
        return self._.get(f"(A:AUTOPILOT VERTICAL HOLD VAR,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Speed.FEET_PER_MINUTE', value: str):
        self._.set(f"{value} (>A:AUTOPILOT VERTICAL HOLD VAR,{unit.value})")


# Index of the slot that the autopilot will use for the VS reference. Note that there are 3 slots (1, 2, 3) that you can set/get normally, however you can also target slot index 0. Writing to slot 0 will overwrite all other slots with the slot 0 value, and by default the autopilot will follow slot 0 if you have not selected any slot index.
class _FlightSim_Autopilot_AUTOPILOT_VS_SLOT_INDEX:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:AUTOPILOT VS SLOT INDEX,{unit.value})")


# Wing leveler active
class _FlightSim_Autopilot_AUTOPILOT_WING_LEVELER:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT WING LEVELER,{unit.value})")


# Yaw damper active
class _FlightSim_Autopilot_AUTOPILOT_YAW_DAMPER:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOPILOT YAW DAMPER,{unit.value})")


# Returns whether landing assistance has been enabled or not.
class _FlightSim_Autopilot_ASSISTANCE_LANDING_ENABLED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:ASSISTANCE LANDING ENABLED,{unit.value})")


# Returns whether takeoff assistance has been enabled or not.
class _FlightSim_Autopilot_ASSISTANCE_TAKEOFF_ENABLED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:ASSISTANCE TAKEOFF ENABLED,{unit.value})")


# The current state of the AI anti-stall system.
class _FlightSim_Autopilot_AI_ANTISTALL_STATE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        ACTIVE = 0
        STABILIZING = 1
        INACTIVE = 2

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:AI ANTISTALL STATE,{unit.value})")


# Returns whether the AI auto-trim system is enabled or not.
class _FlightSim_Autopilot_AI_AUTOTRIM_ACTIVE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AI AUTOTRIM ACTIVE,{unit.value})")


# Returns whether the AI auto-trim system is enabled or not for AI controlled aircraft.
class _FlightSim_Autopilot_AI_AUTOTRIM_ACTIVE_AGAINST_PLAYER:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AI AUTOTRIM ACTIVE AGAINST PLAYER,{unit.value})")


# Returns whether the AI control system is enabled or not.
class _FlightSim_Autopilot_AI_CONTROLS:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AI CONTROLS,{unit.value})")


# Returns whether the AI cursor mode is active or not.
class _FlightSim_Autopilot_AI_CURSOR_MODE_ACTIVE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AI CURSOR MODE ACTIVE,{unit.value})")


# AI reference pitch reference bars
class _FlightSim_Autopilot_ATTITUDE_BARS_POSITION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:ATTITUDE BARS POSITION,{unit.value})")


# AI caged state
class _FlightSim_Autopilot_ATTITUDE_CAGE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:ATTITUDE CAGE,{unit.value})")


# AI bank indication
class _FlightSim_Autopilot_ATTITUDE_INDICATOR_BANK_DEGREES:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:ATTITUDE INDICATOR BANK DEGREES,{unit.value})")


# AI pitch indication
class _FlightSim_Autopilot_ATTITUDE_INDICATOR_PITCH_DEGREES:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:ATTITUDE INDICATOR PITCH DEGREES,{unit.value})")


# Returns whether the AI control system is active or not.
class _FlightSim_Autopilot_DELEGATE_CONTROLS_TO_AI:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:DELEGATE CONTROLS TO AI,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:DELEGATE CONTROLS TO AI,{unit.value})")


# When set with any value this will cancel the current flight assistant destination.
class _FlightSim_Autopilot_FLY_ASSISTANT_CANCEL_DESTINATION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:FLY ASSISTANT CANCEL DESTINATION,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER', value: str):
        self._.set(f"{value} (>A:FLY ASSISTANT CANCEL DESTINATION,{unit.value})")


# When set with any value this will cancel the display of the current flight assistant destination.
class _FlightSim_Autopilot_FLY_ASSISTANT_CANCEL_DESTINATION_DISPLAY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:FLY ASSISTANT CANCEL DESTINATION DISPLAY,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER', value: str):
        self._.set(f"{value} (>A:FLY ASSISTANT CANCEL DESTINATION DISPLAY,{unit.value})")


# Returns true when the copilot AI control is active and therefore COM AI is locked on active too.
class _FlightSim_Autopilot_FLY_ASSISTANT_COM_AI_LOCKED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:FLY ASSISTANT COM AI LOCKED,{unit.value})")


# Returns true when a destination has been set in the flight assistant.
class _FlightSim_Autopilot_FLY_ASSISTANT_HAVE_DESTINATION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:FLY ASSISTANT HAVE DESTINATION,{unit.value})")


# Returns the POH range or an estimated value for this speed.
class _FlightSim_Autopilot_FLY_ASSISTANT_LANDING_SPEED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.STRING'):
        # unit: String (max 32 chars)
        return self._.get(f"(A:FLY ASSISTANT LANDING SPEED,{unit.value})")


# Returns the display mode of the speed, CSS side (only STALL SPEED is working and will turn red when below).
class _FlightSim_Autopilot_FLY_ASSISTANT_LANDING_SPEED_DISPLAY_MODE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.STRING'):
        # unit: String (max 32 chars)
        return self._.get(f"(A:FLY ASSISTANT LANDING SPEED DISPLAY MODE,{unit.value})")


# Selected category
class _FlightSim_Autopilot_FLY_ASSISTANT_NEAREST_CATEGORY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        AIRPORT = 1
        CITIES = 2
        LANDMARK = 3
        FAUNA = 4

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:FLY ASSISTANT NEAREST CATEGORY,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM', value: str):
        self._.set(f"{value} (>A:FLY ASSISTANT NEAREST CATEGORY,{unit.value})")


# Number of elements in this category
class _FlightSim_Autopilot_FLY_ASSISTANT_NEAREST_COUNT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:FLY ASSISTANT NEAREST COUNT,{unit.value})")


# Currently not used within the simulation.
#! -
class _FlightSim_Autopilot_FLY_ASSISTANT_NEAREST_METADATA:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: ''):
        return self._.get(f"(A:FLY ASSISTANT NEAREST METADATA,{unit.value})")


# Returns the name of the element at the specified index.
class _FlightSim_Autopilot_FLY_ASSISTANT_NEAREST_NAME:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.STRING'):
        # unit: String (max 256 chars)
        return self._.get(f"(A:FLY ASSISTANT NEAREST NAME,{unit.value})")


# Returns the index of the currently selected element.
class _FlightSim_Autopilot_FLY_ASSISTANT_NEAREST_SELECTED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:FLY ASSISTANT NEAREST SELECTED,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER', value: str):
        self._.set(f"{value} (>A:FLY ASSISTANT NEAREST SELECTED,{unit.value})")


# Returns true when both ribbon assistances are active (taxi and landing), and can also be used to set them.
class _FlightSim_Autopilot_FLY_ASSISTANT_RIBBONS_ACTIVE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:FLY ASSISTANT RIBBONS ACTIVE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:FLY ASSISTANT RIBBONS ACTIVE,{unit.value})")


# When set with any value, it will set the selected element as the current destination.
class _FlightSim_Autopilot_FLY_ASSISTANT_SET_AS_DESTINATION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:FLY ASSISTANT SET AS DESTINATION,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER', value: str):
        self._.set(f"{value} (>A:FLY ASSISTANT SET AS DESTINATION,{unit.value})")


# Returns the flight assistant stall speed.
class _FlightSim_Autopilot_FLY_ASSISTANT_STALL_SPEED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.KNOT'):
        return self._.get(f"(A:FLY ASSISTANT STALL SPEED,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Speed.KNOT', value: str):
        self._.set(f"{value} (>A:FLY ASSISTANT STALL SPEED,{unit.value})")


# Returns the flight assistant stall speed display mode.
class _FlightSim_Autopilot_FLY_ASSISTANT_STALL_SPEED_DISPLAY_MODE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.STRING'):
        # unit: String (max 32 chars)
        return self._.get(f"(A:FLY ASSISTANT STALL SPEED DISPLAY MODE,{unit.value})")


# Returns the flight assistant takeoff speed.
class _FlightSim_Autopilot_FLY_ASSISTANT_TAKEOFF_SPEED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.KNOT'):
        return self._.get(f"(A:FLY ASSISTANT TAKEOFF SPEED,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Speed.KNOT', value: str):
        self._.set(f"{value} (>A:FLY ASSISTANT TAKEOFF SPEED,{unit.value})")


# Returns the flight assistant takeoff speed display mode.
class _FlightSim_Autopilot_FLY_ASSISTANT_TAKEOFF_SPEED_DISPLAY_MODE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.STRING'):
        # unit: String (max 32 chars)
        return self._.get(f"(A:FLY ASSISTANT TAKEOFF SPEED DISPLAY MODE,{unit.value})")


# Can be set to override the estimated takeoff speed
class _FlightSim_Autopilot_FLY_ASSISTANT_TAKEOFF_SPEED_ESTIMATED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.KNOT'):
        return self._.get(f"(A:FLY ASSISTANT TAKEOFF SPEED ESTIMATED,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Speed.KNOT', value: str):
        self._.set(f"{value} (>A:FLY ASSISTANT TAKEOFF SPEED ESTIMATED,{unit.value})")


class _FlightSim_Brake:
    def __init__(self, flightSim):
        self._ = flightSim
        self.ANTISKID_BRAKES_ACTIVE = _FlightSim_Brake_ANTISKID_BRAKES_ACTIVE(flightSim)
        self.AUTOBRAKES_ACTIVE = _FlightSim_Brake_AUTOBRAKES_ACTIVE(flightSim)
        self.AUTO_BRAKE_SWITCH_CB = _FlightSim_Brake_AUTO_BRAKE_SWITCH_CB(flightSim)
        self.BRAKE_DEPENDENT_HYDRAULIC_PRESSURE = _FlightSim_Brake_BRAKE_DEPENDENT_HYDRAULIC_PRESSURE(flightSim)
        self.BRAKE_INDICATOR = _FlightSim_Brake_BRAKE_INDICATOR(flightSim)
        self.BRAKE_LEFT_POSITION = _FlightSim_Brake_BRAKE_LEFT_POSITION(flightSim)
        self.BRAKE_LEFT_POSITION_EX1 = _FlightSim_Brake_BRAKE_LEFT_POSITION_EX1(flightSim)
        self.BRAKE_PARKING_INDICATOR = _FlightSim_Brake_BRAKE_PARKING_INDICATOR(flightSim)
        self.BRAKE_PARKING_POSITION = _FlightSim_Brake_BRAKE_PARKING_POSITION(flightSim)
        self.BRAKE_RIGHT_POSITION = _FlightSim_Brake_BRAKE_RIGHT_POSITION(flightSim)
        self.BRAKE_RIGHT_POSITION_EX1 = _FlightSim_Brake_BRAKE_RIGHT_POSITION_EX1(flightSim)
        self.REJECTED_TAKEOFF_BRAKES_ACTIVE = _FlightSim_Brake_REJECTED_TAKEOFF_BRAKES_ACTIVE(flightSim)
        self.TOE_BRAKES_AVAILABLE = _FlightSim_Brake_TOE_BRAKES_AVAILABLE(flightSim)
        self.CONTACT_POINT_COMPRESSION = lambda index: _FlightSim_Brake_CONTACT_POINT_COMPRESSION(flightSim, index)
        self.CONTACT_POINT_IS_ON_GROUND = lambda index: _FlightSim_Brake_CONTACT_POINT_IS_ON_GROUND(flightSim, index)
        self.CONTACT_POINT_IS_SKIDDING = lambda index: _FlightSim_Brake_CONTACT_POINT_IS_SKIDDING(flightSim, index)
        self.CONTACT_POINT_POSITION = lambda index: _FlightSim_Brake_CONTACT_POINT_POSITION(flightSim, index)
        self.CONTACT_POINT_SKIDDING_FACTOR = lambda index: _FlightSim_Brake_CONTACT_POINT_SKIDDING_FACTOR(flightSim, index)
        self.CONTACT_POINT_WATER_DEPTH = lambda index: _FlightSim_Brake_CONTACT_POINT_WATER_DEPTH(flightSim, index)
        self.AUX_WHEEL_ROTATION_ANGLE = _FlightSim_Brake_AUX_WHEEL_ROTATION_ANGLE(flightSim)
        self.AUX_WHEEL_RPM = _FlightSim_Brake_AUX_WHEEL_RPM(flightSim)
        self.CENTER_WHEEL_ROTATION_ANGLE = _FlightSim_Brake_CENTER_WHEEL_ROTATION_ANGLE(flightSim)
        self.CENTER_WHEEL_RPM = _FlightSim_Brake_CENTER_WHEEL_RPM(flightSim)
        self.GEAR_ANIMATION_POSITION = lambda index: _FlightSim_Brake_GEAR_ANIMATION_POSITION(flightSim, index)
        self.GEAR_AUX_POSITION = _FlightSim_Brake_GEAR_AUX_POSITION(flightSim)
        self.GEAR_AUX_STEER_ANGLE = _FlightSim_Brake_GEAR_AUX_STEER_ANGLE(flightSim)
        self.GEAR_AUX_STEER_ANGLE_PCT = _FlightSim_Brake_GEAR_AUX_STEER_ANGLE_PCT(flightSim)
        self.GEAR_CENTER_POSITION = _FlightSim_Brake_GEAR_CENTER_POSITION(flightSim)
        self.GEAR_CENTER_STEER_ANGLE = _FlightSim_Brake_GEAR_CENTER_STEER_ANGLE(flightSim)
        self.GEAR_CENTER_STEER_ANGLE_PCT = _FlightSim_Brake_GEAR_CENTER_STEER_ANGLE_PCT(flightSim)
        self.GEAR_DAMAGE_BY_SPEED = _FlightSim_Brake_GEAR_DAMAGE_BY_SPEED(flightSim)
        self.GEAR_EMERGENCY_HANDLE_POSITION = _FlightSim_Brake_GEAR_EMERGENCY_HANDLE_POSITION(flightSim)
        self.GEAR_HANDLE_POSITION = _FlightSim_Brake_GEAR_HANDLE_POSITION(flightSim)
        self.GEAR_HYDRAULIC_PRESSURE = _FlightSim_Brake_GEAR_HYDRAULIC_PRESSURE(flightSim)
        self.GEAR_IS_ON_GROUND = lambda index: _FlightSim_Brake_GEAR_IS_ON_GROUND(flightSim, index)
        self.GEAR_IS_SKIDDING = lambda index: _FlightSim_Brake_GEAR_IS_SKIDDING(flightSim, index)
        self.GEAR_LEFT_POSITION = _FlightSim_Brake_GEAR_LEFT_POSITION(flightSim)
        self.GEAR_LEFT_STEER_ANGLE = _FlightSim_Brake_GEAR_LEFT_STEER_ANGLE(flightSim)
        self.GEAR_LEFT_STEER_ANGLE_PCT = _FlightSim_Brake_GEAR_LEFT_STEER_ANGLE_PCT(flightSim)
        self.GEAR_POSITION = lambda index: _FlightSim_Brake_GEAR_POSITION(flightSim, index)
        self.GEAR_RIGHT_POSITION = _FlightSim_Brake_GEAR_RIGHT_POSITION(flightSim)
        self.GEAR_RIGHT_STEER_ANGLE = _FlightSim_Brake_GEAR_RIGHT_STEER_ANGLE(flightSim)
        self.GEAR_RIGHT_STEER_ANGLE_PCT = _FlightSim_Brake_GEAR_RIGHT_STEER_ANGLE_PCT(flightSim)
        self.GEAR_SKIDDING_FACTOR = _FlightSim_Brake_GEAR_SKIDDING_FACTOR(flightSim)
        self.GEAR_SPEED_EXCEEDED = _FlightSim_Brake_GEAR_SPEED_EXCEEDED(flightSim)
        self.GEAR_STEER_ANGLE = lambda index: _FlightSim_Brake_GEAR_STEER_ANGLE(flightSim, index)
        self.GEAR_STEER_ANGLE_PCT = lambda index: _FlightSim_Brake_GEAR_STEER_ANGLE_PCT(flightSim, index)
        self.GEAR_TAIL_POSITION = _FlightSim_Brake_GEAR_TAIL_POSITION(flightSim)
        self.GEAR_TOTAL_PCT_EXTENDED = _FlightSim_Brake_GEAR_TOTAL_PCT_EXTENDED(flightSim)
        self.GEAR_WARNING = lambda index: _FlightSim_Brake_GEAR_WARNING(flightSim, index)
        self.GEAR_WATER_DEPTH = _FlightSim_Brake_GEAR_WATER_DEPTH(flightSim)
        self.IS_GEAR_FLOATS = _FlightSim_Brake_IS_GEAR_FLOATS(flightSim)
        self.IS_GEAR_RETRACTABLE = _FlightSim_Brake_IS_GEAR_RETRACTABLE(flightSim)
        self.IS_GEAR_SKIDS = _FlightSim_Brake_IS_GEAR_SKIDS(flightSim)
        self.IS_GEAR_SKIS = _FlightSim_Brake_IS_GEAR_SKIS(flightSim)
        self.IS_GEAR_WHEELS = _FlightSim_Brake_IS_GEAR_WHEELS(flightSim)
        self.LEFT_WHEEL_ROTATION_ANGLE = _FlightSim_Brake_LEFT_WHEEL_ROTATION_ANGLE(flightSim)
        self.LEFT_WHEEL_RPM = _FlightSim_Brake_LEFT_WHEEL_RPM(flightSim)
        self.NOSEWHEEL_LOCK_ON = _FlightSim_Brake_NOSEWHEEL_LOCK_ON(flightSim)
        self.NOSEWHEEL_MAX_STEERING_ANGLE = _FlightSim_Brake_NOSEWHEEL_MAX_STEERING_ANGLE(flightSim)
        self.RETRACT_FLOAT_SWITCH = _FlightSim_Brake_RETRACT_FLOAT_SWITCH(flightSim)
        self.RETRACT_LEFT_FLOAT_EXTENDED = _FlightSim_Brake_RETRACT_LEFT_FLOAT_EXTENDED(flightSim)
        self.RETRACT_RIGHT_FLOAT_EXTENDED = _FlightSim_Brake_RETRACT_RIGHT_FLOAT_EXTENDED(flightSim)
        self.RIGHT_WHEEL_ROTATION_ANGLE = _FlightSim_Brake_RIGHT_WHEEL_ROTATION_ANGLE(flightSim)
        self.RIGHT_WHEEL_RPM = _FlightSim_Brake_RIGHT_WHEEL_RPM(flightSim)
        self.STEER_INPUT_CONTROL = _FlightSim_Brake_STEER_INPUT_CONTROL(flightSim)
        self.TAILWHEEL_LOCK_ON = _FlightSim_Brake_TAILWHEEL_LOCK_ON(flightSim)
        self.WATER_LEFT_RUDDER_EXTENDED = _FlightSim_Brake_WATER_LEFT_RUDDER_EXTENDED(flightSim)
        self.WATER_LEFT_RUDDER_STEER_ANGLE = _FlightSim_Brake_WATER_LEFT_RUDDER_STEER_ANGLE(flightSim)
        self.WATER_LEFT_RUDDER_STEER_ANGLE_PCT = _FlightSim_Brake_WATER_LEFT_RUDDER_STEER_ANGLE_PCT(flightSim)
        self.WATER_RIGHT_RUDDER_EXTENDED = _FlightSim_Brake_WATER_RIGHT_RUDDER_EXTENDED(flightSim)
        self.WATER_RIGHT_RUDDER_STEER_ANGLE = _FlightSim_Brake_WATER_RIGHT_RUDDER_STEER_ANGLE(flightSim)
        self.WATER_RIGHT_RUDDER_STEER_ANGLE_PCT = _FlightSim_Brake_WATER_RIGHT_RUDDER_STEER_ANGLE_PCT(flightSim)
        self.WATER_RUDDER_HANDLE_POSITION = _FlightSim_Brake_WATER_RUDDER_HANDLE_POSITION(flightSim)
        self.WHEEL_ROTATION_ANGLE = lambda index: _FlightSim_Brake_WHEEL_ROTATION_ANGLE(flightSim, index)
        self.WHEEL_RPM = lambda index: _FlightSim_Brake_WHEEL_RPM(flightSim, index)


# True if antiskid brakes active. This can be set using the AntiSkidActive parameter.
class _FlightSim_Brake_ANTISKID_BRAKES_ACTIVE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:ANTISKID BRAKES ACTIVE,{unit.value})")


# Whether or not the AutoBrakes are currently active.
class _FlightSim_Brake_AUTOBRAKES_ACTIVE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOBRAKES ACTIVE,{unit.value})")


# Auto brake switch position
class _FlightSim_Brake_AUTO_BRAKE_SWITCH_CB:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:AUTO BRAKE SWITCH CB,{unit.value})")


# Brake dependent hydraulic pressure reading
class _FlightSim_Brake_BRAKE_DEPENDENT_HYDRAULIC_PRESSURE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Pressure.POUND_FORCE_PER_SQUARE_FOOT'):
        return self._.get(f"(A:BRAKE DEPENDENT HYDRAULIC PRESSURE,{unit.value})")


# Brake on indication
class _FlightSim_Brake_BRAKE_INDICATOR:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION'):
        # unit: Position (0 to 16K) 0 = off 16K = full
        return self._.get(f"(A:BRAKE INDICATOR,{unit.value})")


# Percent left brake.
# Note that this SimVar no longer sets the right brake percent and simply triggers a brake pressure increase regardless of the value passed.
class _FlightSim_Brake_BRAKE_LEFT_POSITION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION'):
        # unit: Position (0 to 32K) 0 = off 32K = full
        return self._.get(f"(A:BRAKE LEFT POSITION,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION', value: str):
        # unit: Position (0 to 32K) 0 = off 32K = full
        self._.set(f"{value} (>A:BRAKE LEFT POSITION,{unit.value})")


# Triggers a brake pressure increase on the left brake regardless of the value passed.
class _FlightSim_Brake_BRAKE_LEFT_POSITION_EX1:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION'):
        # unit: Position (0 to 32K) 0 = off 32K = full
        return self._.get(f"(A:BRAKE LEFT POSITION EX1,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION', value: str):
        # unit: Position (0 to 32K) 0 = off 32K = full
        self._.set(f"{value} (>A:BRAKE LEFT POSITION EX1,{unit.value})")


# Parking brake indicator
class _FlightSim_Brake_BRAKE_PARKING_INDICATOR:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:BRAKE PARKING INDICATOR,{unit.value})")


# Gets the parking brake position - either on (true) or off (false).
class _FlightSim_Brake_BRAKE_PARKING_POSITION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:BRAKE PARKING POSITION,{unit.value})")


# Percent right brake.
class _FlightSim_Brake_BRAKE_RIGHT_POSITION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION'):
        # unit: Position (0 to 32K) 0 = off 32K = full
        return self._.get(f"(A:BRAKE RIGHT POSITION,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION', value: str):
        # unit: Position (0 to 32K) 0 = off 32K = full
        self._.set(f"{value} (>A:BRAKE RIGHT POSITION,{unit.value})")


# Triggers a brake pressure increase on the right brake regardless of the value passed.
class _FlightSim_Brake_BRAKE_RIGHT_POSITION_EX1:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION'):
        # unit: Position (0 to 32K) 0 = off 32K = full
        return self._.get(f"(A:BRAKE RIGHT POSITION EX1,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION', value: str):
        # unit: Position (0 to 32K) 0 = off 32K = full
        self._.set(f"{value} (>A:BRAKE RIGHT POSITION EX1,{unit.value})")


# Whether or not the rejected takeoff brakes are currently active.
class _FlightSim_Brake_REJECTED_TAKEOFF_BRAKES_ACTIVE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:REJECTED TAKEOFF BRAKES ACTIVE,{unit.value})")


# True if toe brakes are available
class _FlightSim_Brake_TOE_BRAKES_AVAILABLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:TOE BRAKES AVAILABLE,{unit.value})")


# The percentage value representing the amount the contact point is compressed. Index is from 0-19.
class _FlightSim_Brake_CONTACT_POINT_COMPRESSION:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION'):
        return self._.get(f"(A:CONTACT POINT COMPRESSION:{self._index},{unit.value})")


# Returns true if the indexed contact point is on the ground, or will return false otherwise. Index is from 0 - 19.
class _FlightSim_Brake_CONTACT_POINT_IS_ON_GROUND:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:CONTACT POINT IS ON GROUND:{self._index},{unit.value})")


# Returns true if the indexed contact point is skidding, or will return false otherwise. Index is from 0 - 19.
class _FlightSim_Brake_CONTACT_POINT_IS_SKIDDING:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:CONTACT POINT IS SKIDDING:{self._index},{unit.value})")


# The currently extended position of the (retractable) contact point, expressed as a percentage. Index is from 0 - 19.
class _FlightSim_Brake_CONTACT_POINT_POSITION:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION'):
        return self._.get(f"(A:CONTACT POINT POSITION:{self._index},{unit.value})")


# The skidding factor associated with the indexed contact point, from 0 to 1. Index is from 0 - 19.
class _FlightSim_Brake_CONTACT_POINT_SKIDDING_FACTOR:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:CONTACT POINT SKIDDING FACTOR:{self._index},{unit.value})")


# This returns the depth of the water for the indexed contact point. Index is from 0 - 19.
class _FlightSim_Brake_CONTACT_POINT_WATER_DEPTH:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Length.FOOT'):
        return self._.get(f"(A:CONTACT POINT WATER DEPTH:{self._index},{unit.value})")


# Aux wheel rotation angle (rotation around the axis for the wheel).
class _FlightSim_Brake_AUX_WHEEL_ROTATION_ANGLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:AUX WHEEL ROTATION ANGLE,{unit.value})")


# Rpm of fourth set of gear wheels.
class _FlightSim_Brake_AUX_WHEEL_RPM:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.AngularVelocity.REVOLUTION_PER_MINUTE'):
        return self._.get(f"(A:AUX WHEEL RPM,{unit.value})")


# Center wheel rotation angle (rotation around the axis for the wheel).
# NOTE: This is available in multiplayer to all near aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_Brake_CENTER_WHEEL_ROTATION_ANGLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:CENTER WHEEL ROTATION ANGLE,{unit.value})")


# Center landing gear rpm.
class _FlightSim_Brake_CENTER_WHEEL_RPM:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.AngularVelocity.REVOLUTION_PER_MINUTE'):
        return self._.get(f"(A:CENTER WHEEL RPM,{unit.value})")


# Percent indexed gear animation extended. NOTE: This is available in multiplayer to all near aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_Brake_GEAR_ANIMATION_POSITION:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:GEAR ANIMATION POSITION:{self._index},{unit.value})")


# Percent auxiliary gear extended.
class _FlightSim_Brake_GEAR_AUX_POSITION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:GEAR AUX POSITION,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100', value: str):
        self._.set(f"{value} (>A:GEAR AUX POSITION,{unit.value})")


# Aux wheel angle, negative to the left, positive to the right. The aux wheel is the fourth set of landing gear, sometimes used on helicopters.
class _FlightSim_Brake_GEAR_AUX_STEER_ANGLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:GEAR AUX STEER ANGLE,{unit.value})")


# Aux steer angle as a percentage.
class _FlightSim_Brake_GEAR_AUX_STEER_ANGLE_PCT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:GEAR AUX STEER ANGLE PCT,{unit.value})")


# Percent center gear extended.
class _FlightSim_Brake_GEAR_CENTER_POSITION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:GEAR CENTER POSITION,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100', value: str):
        self._.set(f"{value} (>A:GEAR CENTER POSITION,{unit.value})")


# Center wheel angle, negative to the left, positive to the right.
# NOTE: This is available in multiplayer to all near aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_Brake_GEAR_CENTER_STEER_ANGLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:GEAR CENTER STEER ANGLE,{unit.value})")


# Center steer angle as a percentage.
class _FlightSim_Brake_GEAR_CENTER_STEER_ANGLE_PCT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:GEAR CENTER STEER ANGLE PCT,{unit.value})")


# True if gear has been damaged by excessive speed.
class _FlightSim_Brake_GEAR_DAMAGE_BY_SPEED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GEAR DAMAGE BY SPEED,{unit.value})")


# True if gear emergency handle applied.
class _FlightSim_Brake_GEAR_EMERGENCY_HANDLE_POSITION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GEAR EMERGENCY HANDLE POSITION,{unit.value})")


# The gear handle position, where 0 means the handle is retracted and 1 is the handle fully applied.
class _FlightSim_Brake_GEAR_HANDLE_POSITION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:GEAR HANDLE POSITION,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100', value: str):
        self._.set(f"{value} (>A:GEAR HANDLE POSITION,{unit.value})")


# Gear hydraulic pressure.
class _FlightSim_Brake_GEAR_HYDRAULIC_PRESSURE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Pressure.POUND_FORCE_PER_SQUARE_FOOT'):
        return self._.get(f"(A:GEAR HYDRAULIC PRESSURE,{unit.value})")


# True if the gear is on the ground.
class _FlightSim_Brake_GEAR_IS_ON_GROUND:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GEAR IS ON GROUND:{self._index},{unit.value})")


# True if the gear is skidding.
class _FlightSim_Brake_GEAR_IS_SKIDDING:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GEAR IS SKIDDING:{self._index},{unit.value})")


# Percent left gear extended.
class _FlightSim_Brake_GEAR_LEFT_POSITION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:GEAR LEFT POSITION,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100', value: str):
        self._.set(f"{value} (>A:GEAR LEFT POSITION,{unit.value})")


# Left wheel angle, negative to the left, positive to the right.
# NOTE: This is available in multiplayer to all near aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_Brake_GEAR_LEFT_STEER_ANGLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:GEAR LEFT STEER ANGLE,{unit.value})")


# Left steer angle as a percentage.
class _FlightSim_Brake_GEAR_LEFT_STEER_ANGLE_PCT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:GEAR LEFT STEER ANGLE PCT,{unit.value})")


# Position of landing gear.
# NOTE: This is available in multiplayer to all near aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_Brake_GEAR_POSITION:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    class Unit(Enum):
        UNKNOWN = 0
        UP = 1
        DOWN = 2

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:GEAR POSITION:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM', value: str):
        self._.set(f"{value} (>A:GEAR POSITION:{self._index},{unit.value})")


# Percent right gear extended.
class _FlightSim_Brake_GEAR_RIGHT_POSITION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:GEAR RIGHT POSITION,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100', value: str):
        self._.set(f"{value} (>A:GEAR RIGHT POSITION,{unit.value})")


# Right wheel angle, negative to the left, positive to the right.
# NOTE: This is available in multiplayer to all near aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_Brake_GEAR_RIGHT_STEER_ANGLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:GEAR RIGHT STEER ANGLE,{unit.value})")


# Right steer angle as a percentage.
class _FlightSim_Brake_GEAR_RIGHT_STEER_ANGLE_PCT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:GEAR RIGHT STEER ANGLE PCT,{unit.value})")


# The gear skidding factor, expressed as a value between 0 and 1.
class _FlightSim_Brake_GEAR_SKIDDING_FACTOR:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:GEAR SKIDDING FACTOR,{unit.value})")


# True if safe speed limit for gear exceeded.
class _FlightSim_Brake_GEAR_SPEED_EXCEEDED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GEAR SPEED EXCEEDED,{unit.value})")


# Alternative method of getting the steer angle.
# NOTE: This is available in multiplayer to all near aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_Brake_GEAR_STEER_ANGLE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:GEAR STEER ANGLE:{self._index},{unit.value})")


# Alternative method of getting steer angle as a percentage.
class _FlightSim_Brake_GEAR_STEER_ANGLE_PCT:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:GEAR STEER ANGLE PCT:{self._index},{unit.value})")


# Percent tail gear extended.
# NOTE: This is a deprecated legacy SimVar and should not be used, as it will always return 0.
class _FlightSim_Brake_GEAR_TAIL_POSITION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:GEAR TAIL POSITION,{unit.value})")


# Percent total gear extended.
class _FlightSim_Brake_GEAR_TOTAL_PCT_EXTENDED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:GEAR TOTAL PCT EXTENDED,{unit.value})")


# Gear warnings.
class _FlightSim_Brake_GEAR_WARNING:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    class Unit(Enum):
        NONE = 0
        GEAR_UP = 1
        AMPHIBIOUS_GEAR_UP = 2
        AMPHIBIOUS_GEAR_DOWN = 3
        ON_GROUND_HANDLE_UP = 4

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:GEAR WARNING:{self._index},{unit.value})")


# The depth of the gear in the water.
class _FlightSim_Brake_GEAR_WATER_DEPTH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.CENTIMETER'):
        return self._.get(f"(A:GEAR WATER DEPTH,{unit.value})")


# True if landing gear are floats
class _FlightSim_Brake_IS_GEAR_FLOATS:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:IS GEAR FLOATS,{unit.value})")


# True if gear can be retracted
class _FlightSim_Brake_IS_GEAR_RETRACTABLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:IS GEAR RETRACTABLE,{unit.value})")


# True if landing gear is skids
class _FlightSim_Brake_IS_GEAR_SKIDS:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:IS GEAR SKIDS,{unit.value})")


# True if landing gear is skis
class _FlightSim_Brake_IS_GEAR_SKIS:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:IS GEAR SKIS,{unit.value})")


# True if landing gear is wheels
class _FlightSim_Brake_IS_GEAR_WHEELS:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:IS GEAR WHEELS,{unit.value})")


# Left wheel rotation angle (rotation around the axis for the wheel).
class _FlightSim_Brake_LEFT_WHEEL_ROTATION_ANGLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:LEFT WHEEL ROTATION ANGLE,{unit.value})")


# Left landing gear rpm
class _FlightSim_Brake_LEFT_WHEEL_RPM:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.AngularVelocity.REVOLUTION_PER_MINUTE'):
        return self._.get(f"(A:LEFT WHEEL RPM,{unit.value})")


# True if the nosewheel lock is engaged. This can be set using the NosewheelLock parameter.
class _FlightSim_Brake_NOSEWHEEL_LOCK_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:NOSEWHEEL LOCK ON,{unit.value})")


# Can be used to get or set the maximum permitted steering angle for the nose wheel of the aircraft.
class _FlightSim_Brake_NOSEWHEEL_MAX_STEERING_ANGLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:NOSEWHEEL MAX STEERING ANGLE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Angle.RADIAN', value: str):
        self._.set(f"{value} (>A:NOSEWHEEL MAX STEERING ANGLE,{unit.value})")


# True if retract float switch on
class _FlightSim_Brake_RETRACT_FLOAT_SWITCH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        RETRACTED = -1
        NEUTRAL = 0
        EXTENDED = 1

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:RETRACT FLOAT SWITCH,{unit.value})")


# If aircraft has retractable floats.
class _FlightSim_Brake_RETRACT_LEFT_FLOAT_EXTENDED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        # unit: Percent (0 is fully retracted, 100 is fully extended)
        return self._.get(f"(A:RETRACT LEFT FLOAT EXTENDED,{unit.value})")


# If aircraft has retractable floats.
class _FlightSim_Brake_RETRACT_RIGHT_FLOAT_EXTENDED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        # unit: Percent (0 is fully retracted, 100 is fully extended)
        return self._.get(f"(A:RETRACT RIGHT FLOAT EXTENDED,{unit.value})")


# Right wheel rotation angle (rotation around the axis for the wheel).
class _FlightSim_Brake_RIGHT_WHEEL_ROTATION_ANGLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:RIGHT WHEEL ROTATION ANGLE,{unit.value})")


# Right landing gear rpm.
class _FlightSim_Brake_RIGHT_WHEEL_RPM:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.AngularVelocity.REVOLUTION_PER_MINUTE'):
        return self._.get(f"(A:RIGHT WHEEL RPM,{unit.value})")


# Position of steering tiller.
class _FlightSim_Brake_STEER_INPUT_CONTROL:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:STEER INPUT CONTROL,{unit.value})")


# True if tailwheel lock applied. This can be set using the TailwheelLock parameter.
class _FlightSim_Brake_TAILWHEEL_LOCK_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:TAILWHEEL LOCK ON,{unit.value})")


# Percent extended.
class _FlightSim_Brake_WATER_LEFT_RUDDER_EXTENDED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:WATER LEFT RUDDER EXTENDED,{unit.value})")


# Water left rudder angle, negative to the left, positive to the right.
class _FlightSim_Brake_WATER_LEFT_RUDDER_STEER_ANGLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:WATER LEFT RUDDER STEER ANGLE,{unit.value})")


# Water left rudder angle as a percentage.
class _FlightSim_Brake_WATER_LEFT_RUDDER_STEER_ANGLE_PCT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:WATER LEFT RUDDER STEER ANGLE PCT,{unit.value})")


# Percent extended.
class _FlightSim_Brake_WATER_RIGHT_RUDDER_EXTENDED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:WATER RIGHT RUDDER EXTENDED,{unit.value})")


# Water right rudder angle, negative to the left, positive to the right.
class _FlightSim_Brake_WATER_RIGHT_RUDDER_STEER_ANGLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:WATER RIGHT RUDDER STEER ANGLE,{unit.value})")


# Water right rudder as a percentage.
class _FlightSim_Brake_WATER_RIGHT_RUDDER_STEER_ANGLE_PCT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:WATER RIGHT RUDDER STEER ANGLE PCT,{unit.value})")


# Position of the water rudder handle (0 handle retracted, 1 rudder handle applied).
class _FlightSim_Brake_WATER_RUDDER_HANDLE_POSITION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:WATER RUDDER HANDLE POSITION,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100', value: str):
        self._.set(f"{value} (>A:WATER RUDDER HANDLE POSITION,{unit.value})")


# Wheel rotation angle (rotation around the axis for the wheel).
class _FlightSim_Brake_WHEEL_ROTATION_ANGLE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:WHEEL ROTATION ANGLE:{self._index},{unit.value})")


# Wheel rpm.
class _FlightSim_Brake_WHEEL_RPM:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.AngularVelocity.REVOLUTION_PER_MINUTE'):
        return self._.get(f"(A:WHEEL RPM:{self._index},{unit.value})")


class _FlightSim_Control:
    def __init__(self, flightSim):
        self._ = flightSim
        self.AILERON_AVERAGE_DEFLECTION = _FlightSim_Control_AILERON_AVERAGE_DEFLECTION(flightSim)
        self.AILERON_LEFT_DEFLECTION = _FlightSim_Control_AILERON_LEFT_DEFLECTION(flightSim)
        self.AILERON_LEFT_DEFLECTION_PCT = _FlightSim_Control_AILERON_LEFT_DEFLECTION_PCT(flightSim)
        self.AILERON_POSITION = _FlightSim_Control_AILERON_POSITION(flightSim)
        self.AILERON_RIGHT_DEFLECTION = _FlightSim_Control_AILERON_RIGHT_DEFLECTION(flightSim)
        self.AILERON_RIGHT_DEFLECTION_PCT = _FlightSim_Control_AILERON_RIGHT_DEFLECTION_PCT(flightSim)
        self.AILERON_TRIM = _FlightSim_Control_AILERON_TRIM(flightSim)
        self.AILERON_TRIM_DISABLED = _FlightSim_Control_AILERON_TRIM_DISABLED(flightSim)
        self.AILERON_TRIM_PCT = _FlightSim_Control_AILERON_TRIM_PCT(flightSim)
        self.ELEVATOR_DEFLECTION = _FlightSim_Control_ELEVATOR_DEFLECTION(flightSim)
        self.ELEVATOR_DEFLECTION_PCT = _FlightSim_Control_ELEVATOR_DEFLECTION_PCT(flightSim)
        self.ELEVATOR_POSITION = _FlightSim_Control_ELEVATOR_POSITION(flightSim)
        self.ELEVATOR_TRIM_DISABLED = _FlightSim_Control_ELEVATOR_TRIM_DISABLED(flightSim)
        self.ELEVATOR_TRIM_DOWN_LIMIT = _FlightSim_Control_ELEVATOR_TRIM_DOWN_LIMIT(flightSim)
        self.ELEVATOR_TRIM_INDICATOR = _FlightSim_Control_ELEVATOR_TRIM_INDICATOR(flightSim)
        self.ELEVATOR_TRIM_NEUTRAL = _FlightSim_Control_ELEVATOR_TRIM_NEUTRAL(flightSim)
        self.ELEVATOR_TRIM_PCT = _FlightSim_Control_ELEVATOR_TRIM_PCT(flightSim)
        self.ELEVATOR_TRIM_POSITION = _FlightSim_Control_ELEVATOR_TRIM_POSITION(flightSim)
        self.ELEVATOR_TRIM_UP_LIMIT = _FlightSim_Control_ELEVATOR_TRIM_UP_LIMIT(flightSim)
        self.ELEVON_DEFLECTION = _FlightSim_Control_ELEVON_DEFLECTION(flightSim)
        self.FLAP_DAMAGE_BY_SPEED = _FlightSim_Control_FLAP_DAMAGE_BY_SPEED(flightSim)
        self.FLAP_POSITION_SET = _FlightSim_Control_FLAP_POSITION_SET(flightSim)
        self.FLAP_SPEED_EXCEEDED = _FlightSim_Control_FLAP_SPEED_EXCEEDED(flightSim)
        self.FLAPS_AVAILABLE = _FlightSim_Control_FLAPS_AVAILABLE(flightSim)
        self.FLAPS_EFFECTIVE_HANDLE_INDEX = lambda index: _FlightSim_Control_FLAPS_EFFECTIVE_HANDLE_INDEX(flightSim, index)
        self.FLAPS_HANDLE_INDEX = lambda index: _FlightSim_Control_FLAPS_HANDLE_INDEX(flightSim, index)
        self.FLAPS_HANDLE_PERCENT = _FlightSim_Control_FLAPS_HANDLE_PERCENT(flightSim)
        self.FLAPS_NUM_HANDLE_POSITIONS = _FlightSim_Control_FLAPS_NUM_HANDLE_POSITIONS(flightSim)
        self.LEADING_EDGE_FLAPS_LEFT_ANGLE = _FlightSim_Control_LEADING_EDGE_FLAPS_LEFT_ANGLE(flightSim)
        self.LEADING_EDGE_FLAPS_LEFT_INDEX = _FlightSim_Control_LEADING_EDGE_FLAPS_LEFT_INDEX(flightSim)
        self.LEADING_EDGE_FLAPS_LEFT_PERCENT = _FlightSim_Control_LEADING_EDGE_FLAPS_LEFT_PERCENT(flightSim)
        self.LEADING_EDGE_FLAPS_RIGHT_ANGLE = _FlightSim_Control_LEADING_EDGE_FLAPS_RIGHT_ANGLE(flightSim)
        self.LEADING_EDGE_FLAPS_RIGHT_INDEX = _FlightSim_Control_LEADING_EDGE_FLAPS_RIGHT_INDEX(flightSim)
        self.LEADING_EDGE_FLAPS_RIGHT_PERCENT = _FlightSim_Control_LEADING_EDGE_FLAPS_RIGHT_PERCENT(flightSim)
        self.TRAILING_EDGE_FLAPS_LEFT_ANGLE = _FlightSim_Control_TRAILING_EDGE_FLAPS_LEFT_ANGLE(flightSim)
        self.TRAILING_EDGE_FLAPS_LEFT_INDEX = _FlightSim_Control_TRAILING_EDGE_FLAPS_LEFT_INDEX(flightSim)
        self.TRAILING_EDGE_FLAPS_LEFT_PERCENT = _FlightSim_Control_TRAILING_EDGE_FLAPS_LEFT_PERCENT(flightSim)
        self.TRAILING_EDGE_FLAPS_RIGHT_ANGLE = _FlightSim_Control_TRAILING_EDGE_FLAPS_RIGHT_ANGLE(flightSim)
        self.TRAILING_EDGE_FLAPS_RIGHT_INDEX = _FlightSim_Control_TRAILING_EDGE_FLAPS_RIGHT_INDEX(flightSim)
        self.TRAILING_EDGE_FLAPS_RIGHT_PERCENT = _FlightSim_Control_TRAILING_EDGE_FLAPS_RIGHT_PERCENT(flightSim)
        self.FLY_BY_WIRE_ALPHA_PROTECTION = _FlightSim_Control_FLY_BY_WIRE_ALPHA_PROTECTION(flightSim)
        self.FLY_BY_WIRE_ELAC_FAILED = _FlightSim_Control_FLY_BY_WIRE_ELAC_FAILED(flightSim)
        self.FLY_BY_WIRE_ELAC_SWITCH = _FlightSim_Control_FLY_BY_WIRE_ELAC_SWITCH(flightSim)
        self.FLY_BY_WIRE_FAC_FAILED = _FlightSim_Control_FLY_BY_WIRE_FAC_FAILED(flightSim)
        self.FLY_BY_WIRE_FAC_SWITCH = _FlightSim_Control_FLY_BY_WIRE_FAC_SWITCH(flightSim)
        self.FLY_BY_WIRE_SEC_FAILED = _FlightSim_Control_FLY_BY_WIRE_SEC_FAILED(flightSim)
        self.FLY_BY_WIRE_SEC_SWITCH = _FlightSim_Control_FLY_BY_WIRE_SEC_SWITCH(flightSim)
        self.FOLDING_WING_HANDLE_POSITION = _FlightSim_Control_FOLDING_WING_HANDLE_POSITION(flightSim)
        self.FOLDING_WING_LEFT_PERCENT = _FlightSim_Control_FOLDING_WING_LEFT_PERCENT(flightSim)
        self.FOLDING_WING_RIGHT_PERCENT = _FlightSim_Control_FOLDING_WING_RIGHT_PERCENT(flightSim)
        self.RUDDER_DEFLECTION = _FlightSim_Control_RUDDER_DEFLECTION(flightSim)
        self.RUDDER_DEFLECTION_PCT = _FlightSim_Control_RUDDER_DEFLECTION_PCT(flightSim)
        self.RUDDER_PEDAL_INDICATOR = _FlightSim_Control_RUDDER_PEDAL_INDICATOR(flightSim)
        self.RUDDER_PEDAL_POSITION = _FlightSim_Control_RUDDER_PEDAL_POSITION(flightSim)
        self.RUDDER_POSITION = _FlightSim_Control_RUDDER_POSITION(flightSim)
        self.RUDDER_TRIM = _FlightSim_Control_RUDDER_TRIM(flightSim)
        self.RUDDER_TRIM_DISABLED = _FlightSim_Control_RUDDER_TRIM_DISABLED(flightSim)
        self.RUDDER_TRIM_PCT = _FlightSim_Control_RUDDER_TRIM_PCT(flightSim)
        self.SPOILERS_ARMED = _FlightSim_Control_SPOILERS_ARMED(flightSim)
        self.SPOILER_AVAILABLE = _FlightSim_Control_SPOILER_AVAILABLE(flightSim)
        self.SPOILERS_HANDLE_POSITION = _FlightSim_Control_SPOILERS_HANDLE_POSITION(flightSim)
        self.SPOILERS_LEFT_POSITION = _FlightSim_Control_SPOILERS_LEFT_POSITION(flightSim)
        self.SPOILERS_RIGHT_POSITION = _FlightSim_Control_SPOILERS_RIGHT_POSITION(flightSim)
        self.BLAST_SHIELD_POSITION = lambda index: _FlightSim_Control_BLAST_SHIELD_POSITION(flightSim, index)
        self.CABLE_CAUGHT_BY_TAILHOOK = lambda index: _FlightSim_Control_CABLE_CAUGHT_BY_TAILHOOK(flightSim, index)
        self.CATAPULT_STROKE_POSITION = lambda index: _FlightSim_Control_CATAPULT_STROKE_POSITION(flightSim, index)
        self.HOLDBACK_BAR_INSTALLED = _FlightSim_Control_HOLDBACK_BAR_INSTALLED(flightSim)
        self.LAUNCHBAR_HELD_EXTENDED = _FlightSim_Control_LAUNCHBAR_HELD_EXTENDED(flightSim)
        self.LAUNCHBAR_POSITION = _FlightSim_Control_LAUNCHBAR_POSITION(flightSim)
        self.LAUNCHBAR_SWITCH = _FlightSim_Control_LAUNCHBAR_SWITCH(flightSim)
        self.NUMBER_OF_CATAPULTS = _FlightSim_Control_NUMBER_OF_CATAPULTS(flightSim)
        self.CONCORDE_NOSE_ANGLE = _FlightSim_Control_CONCORDE_NOSE_ANGLE(flightSim)
        self.CONCORDE_VISOR_NOSE_HANDLE = _FlightSim_Control_CONCORDE_VISOR_NOSE_HANDLE(flightSim)
        self.CONCORDE_VISOR_POSITION_PERCENT = _FlightSim_Control_CONCORDE_VISOR_POSITION_PERCENT(flightSim)


# Angle deflection for the aileron.
class _FlightSim_Control_AILERON_AVERAGE_DEFLECTION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:AILERON AVERAGE DEFLECTION,{unit.value})")


# Angle deflection for the aileron.
class _FlightSim_Control_AILERON_LEFT_DEFLECTION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:AILERON LEFT DEFLECTION,{unit.value})")


# Percent deflection for the aileron.
# NOTE: This is available in multiplayer to all near aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_Control_AILERON_LEFT_DEFLECTION_PCT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:AILERON LEFT DEFLECTION PCT,{unit.value})")


# Percent aileron input left/right.
class _FlightSim_Control_AILERON_POSITION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION'):
        # unit: Position (-16K to 0) -16K = full left
        return self._.get(f"(A:AILERON POSITION,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION', value: str):
        # unit: Position (-16K to 0) -16K = full left
        self._.set(f"{value} (>A:AILERON POSITION,{unit.value})")


# Angle deflection.
class _FlightSim_Control_AILERON_RIGHT_DEFLECTION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:AILERON RIGHT DEFLECTION,{unit.value})")


# Percent deflection.
# NOTE: This is available in multiplayer to all near aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_Control_AILERON_RIGHT_DEFLECTION_PCT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:AILERON RIGHT DEFLECTION PCT,{unit.value})")


# Angle deflection.
class _FlightSim_Control_AILERON_TRIM:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:AILERON TRIM,{unit.value})")


# Whether or not the Aileron Trim has been disabled.
class _FlightSim_Control_AILERON_TRIM_DISABLED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AILERON TRIM DISABLED,{unit.value})")


# The trim position of the ailerons. Zero is fully retracted.
# NOTE: This is available in multiplayer to all near aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_Control_AILERON_TRIM_PCT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:AILERON TRIM PCT,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100', value: str):
        self._.set(f"{value} (>A:AILERON TRIM PCT,{unit.value})")


# Angle deflection.
class _FlightSim_Control_ELEVATOR_DEFLECTION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:ELEVATOR DEFLECTION,{unit.value})")


# Percent deflection.
# NOTE: This is available in multiplayer. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_Control_ELEVATOR_DEFLECTION_PCT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:ELEVATOR DEFLECTION PCT,{unit.value})")


# Percent elevator input deflection.
class _FlightSim_Control_ELEVATOR_POSITION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION'):
        # unit: Position (-16K to 0) -16K = full down
        return self._.get(f"(A:ELEVATOR POSITION,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION', value: str):
        # unit: Position (-16K to 0) -16K = full down
        self._.set(f"{value} (>A:ELEVATOR POSITION,{unit.value})")


# Whether or not the Elevator Trim has been disabled.
class _FlightSim_Control_ELEVATOR_TRIM_DISABLED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:ELEVATOR TRIM DISABLED,{unit.value})")


# Returns the maximum elevator trim value. This corresponds to the elevator_trim_down_limit in the Flight Model Config file.
class _FlightSim_Control_ELEVATOR_TRIM_DOWN_LIMIT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:ELEVATOR TRIM DOWN LIMIT,{unit.value})")


# Percent elevator trim (for indication).
class _FlightSim_Control_ELEVATOR_TRIM_INDICATOR:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION'):
        # unit: Position (-16K to 0) -16K = full down
        return self._.get(f"(A:ELEVATOR TRIM INDICATOR,{unit.value})")


# Elevator trim neutral.
class _FlightSim_Control_ELEVATOR_TRIM_NEUTRAL:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:ELEVATOR TRIM NEUTRAL,{unit.value})")


# Percent elevator trim.
class _FlightSim_Control_ELEVATOR_TRIM_PCT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:ELEVATOR TRIM PCT,{unit.value})")


# Elevator trim deflection.
class _FlightSim_Control_ELEVATOR_TRIM_POSITION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:ELEVATOR TRIM POSITION,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Angle.RADIAN', value: str):
        self._.set(f"{value} (>A:ELEVATOR TRIM POSITION,{unit.value})")


# Returns the maximum elevator trim value. This corresponds to the elevator_trim_up_limit in the Flight Model Config file.
class _FlightSim_Control_ELEVATOR_TRIM_UP_LIMIT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:ELEVATOR TRIM UP LIMIT,{unit.value})")


# Elevon deflection.
class _FlightSim_Control_ELEVON_DEFLECTION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:ELEVON DEFLECTION,{unit.value})")


# True if flaps are damaged by excessive speed.
class _FlightSim_Control_FLAP_DAMAGE_BY_SPEED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:FLAP DAMAGE BY SPEED,{unit.value})")


# Set the position of the flaps control.
class _FlightSim_Control_FLAP_POSITION_SET:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION'):
        return self._.get(f"(A:FLAP POSITION SET,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION', value: str):
        self._.set(f"{value} (>A:FLAP POSITION SET,{unit.value})")


# True if safe speed limit for flaps exceeded.
class _FlightSim_Control_FLAP_SPEED_EXCEEDED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:FLAP SPEED EXCEEDED,{unit.value})")


# True if flaps available.
class _FlightSim_Control_FLAPS_AVAILABLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:FLAPS AVAILABLE,{unit.value})")


# This returns the effective flaps handle index, after some of the conditions have potentially forced the state to change.
class _FlightSim_Control_FLAPS_EFFECTIVE_HANDLE_INDEX:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:FLAPS EFFECTIVE HANDLE INDEX:{self._index},{unit.value})")


# Index of current flap position.
class _FlightSim_Control_FLAPS_HANDLE_INDEX:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:FLAPS HANDLE INDEX:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER', value: str):
        self._.set(f"{value} (>A:FLAPS HANDLE INDEX:{self._index},{unit.value})")


# Percent flap handle extended.
# NOTE: This is available in multiplayer to all near aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_Control_FLAPS_HANDLE_PERCENT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:FLAPS HANDLE PERCENT,{unit.value})")


# Number of available flap positions.
class _FlightSim_Control_FLAPS_NUM_HANDLE_POSITIONS:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:FLAPS NUM HANDLE POSITIONS,{unit.value})")


# Angle left leading edge flap extended. Use LEADING_EDGE_FLAPS_LEFT_PERCENT to set a value.
class _FlightSim_Control_LEADING_EDGE_FLAPS_LEFT_ANGLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:LEADING EDGE FLAPS LEFT ANGLE,{unit.value})")


# Index of left leading edge flap position.
class _FlightSim_Control_LEADING_EDGE_FLAPS_LEFT_INDEX:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:LEADING EDGE FLAPS LEFT INDEX,{unit.value})")


# Percent left leading edge flap extended.
# NOTE: This is available in multiplayer to all near aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_Control_LEADING_EDGE_FLAPS_LEFT_PERCENT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:LEADING EDGE FLAPS LEFT PERCENT,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100', value: str):
        self._.set(f"{value} (>A:LEADING EDGE FLAPS LEFT PERCENT,{unit.value})")


# Angle right leading edge flap extended. Use LEADING_EDGE_FLAPS_RIGHT_PERCENT to set a value.
class _FlightSim_Control_LEADING_EDGE_FLAPS_RIGHT_ANGLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:LEADING EDGE FLAPS RIGHT ANGLE,{unit.value})")


# Index of right leading edge flap position.
class _FlightSim_Control_LEADING_EDGE_FLAPS_RIGHT_INDEX:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:LEADING EDGE FLAPS RIGHT INDEX,{unit.value})")


# Percent right leading edge flap extended.
# NOTE: This is available in multiplayer to all near aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_Control_LEADING_EDGE_FLAPS_RIGHT_PERCENT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:LEADING EDGE FLAPS RIGHT PERCENT,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100', value: str):
        self._.set(f"{value} (>A:LEADING EDGE FLAPS RIGHT PERCENT,{unit.value})")


# Angle left trailing edge flap extended. Use TRAILING_EDGE_FLAPS_LEFT_PERCENT to set a value.
class _FlightSim_Control_TRAILING_EDGE_FLAPS_LEFT_ANGLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:TRAILING EDGE FLAPS LEFT ANGLE,{unit.value})")


# Index of left trailing edge flap position.
class _FlightSim_Control_TRAILING_EDGE_FLAPS_LEFT_INDEX:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:TRAILING EDGE FLAPS LEFT INDEX,{unit.value})")


# Percent left trailing edge flap extended.
# NOTE: This is available in multiplayer to all near aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_Control_TRAILING_EDGE_FLAPS_LEFT_PERCENT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:TRAILING EDGE FLAPS LEFT PERCENT,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100', value: str):
        self._.set(f"{value} (>A:TRAILING EDGE FLAPS LEFT PERCENT,{unit.value})")


# Angle right trailing edge flap extended. Use TRAILING_EDGE_FLAPS_RIGHT_PERCENT to set a value.
class _FlightSim_Control_TRAILING_EDGE_FLAPS_RIGHT_ANGLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:TRAILING EDGE FLAPS RIGHT ANGLE,{unit.value})")


# Index of right trailing edge flap position.
class _FlightSim_Control_TRAILING_EDGE_FLAPS_RIGHT_INDEX:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:TRAILING EDGE FLAPS RIGHT INDEX,{unit.value})")


# Percent right trailing edge flap extended.
# NOTE: This is available in multiplayer to all near aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_Control_TRAILING_EDGE_FLAPS_RIGHT_PERCENT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:TRAILING EDGE FLAPS RIGHT PERCENT,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100', value: str):
        self._.set(f"{value} (>A:TRAILING EDGE FLAPS RIGHT PERCENT,{unit.value})")


# Returns true if the fly-by-wire alpha protection is enabled or false otherwise.
class _FlightSim_Control_FLY_BY_WIRE_ALPHA_PROTECTION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:FLY BY WIRE ALPHA PROTECTION,{unit.value})")


# True if the Elevators and Ailerons computer has failed.
class _FlightSim_Control_FLY_BY_WIRE_ELAC_FAILED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:FLY BY WIRE ELAC FAILED,{unit.value})")


# True if the fly by wire Elevators and Ailerons computer is on.
class _FlightSim_Control_FLY_BY_WIRE_ELAC_SWITCH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:FLY BY WIRE ELAC SWITCH,{unit.value})")


# True if the Flight Augmentation computer has failed.
class _FlightSim_Control_FLY_BY_WIRE_FAC_FAILED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:FLY BY WIRE FAC FAILED,{unit.value})")


# True if the fly by wire Flight Augmentation computer is on.
class _FlightSim_Control_FLY_BY_WIRE_FAC_SWITCH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:FLY BY WIRE FAC SWITCH,{unit.value})")


# True if the Spoilers and Elevators computer has failed.
class _FlightSim_Control_FLY_BY_WIRE_SEC_FAILED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:FLY BY WIRE SEC FAILED,{unit.value})")


# True if the fly by wire Spoilers and Elevators computer is on.
class _FlightSim_Control_FLY_BY_WIRE_SEC_SWITCH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:FLY BY WIRE SEC SWITCH,{unit.value})")


# True if the folding wing handle is engaged.
class _FlightSim_Control_FOLDING_WING_HANDLE_POSITION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:FOLDING WING HANDLE POSITION,{unit.value})")


# Left folding wing position, 1.0 is fully folded.
class _FlightSim_Control_FOLDING_WING_LEFT_PERCENT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:FOLDING WING LEFT PERCENT,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100', value: str):
        self._.set(f"{value} (>A:FOLDING WING LEFT PERCENT,{unit.value})")


# Right folding wing position, 1.0 is fully folded.
class _FlightSim_Control_FOLDING_WING_RIGHT_PERCENT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:FOLDING WING RIGHT PERCENT,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100', value: str):
        self._.set(f"{value} (>A:FOLDING WING RIGHT PERCENT,{unit.value})")


# Angle deflection.
class _FlightSim_Control_RUDDER_DEFLECTION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:RUDDER DEFLECTION,{unit.value})")


# Percent deflection.
# NOTE: This is available in multiplayer. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_Control_RUDDER_DEFLECTION_PCT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:RUDDER DEFLECTION PCT,{unit.value})")


# Rudder pedal position.
class _FlightSim_Control_RUDDER_PEDAL_INDICATOR:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION'):
        return self._.get(f"(A:RUDDER PEDAL INDICATOR,{unit.value})")


# Percent rudder pedal deflection (for animation).
class _FlightSim_Control_RUDDER_PEDAL_POSITION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION'):
        # unit: Position (-16K to 0) -16K = left pedal pushed full in
        return self._.get(f"(A:RUDDER PEDAL POSITION,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION', value: str):
        # unit: Position (-16K to 0) -16K = left pedal pushed full in
        self._.set(f"{value} (>A:RUDDER PEDAL POSITION,{unit.value})")


# Percent rudder input deflection.
class _FlightSim_Control_RUDDER_POSITION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION'):
        # unit: Position (-16K to 0) -16K = full left
        return self._.get(f"(A:RUDDER POSITION,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION', value: str):
        # unit: Position (-16K to 0) -16K = full left
        self._.set(f"{value} (>A:RUDDER POSITION,{unit.value})")


# Angle deflection.
class _FlightSim_Control_RUDDER_TRIM:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:RUDDER TRIM,{unit.value})")


# Whether or not the Rudder Trim has been disabled.
class _FlightSim_Control_RUDDER_TRIM_DISABLED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:RUDDER TRIM DISABLED,{unit.value})")


# The trim position of the rudder. Zero is no trim.
class _FlightSim_Control_RUDDER_TRIM_PCT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:RUDDER TRIM PCT,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100', value: str):
        self._.set(f"{value} (>A:RUDDER TRIM PCT,{unit.value})")


# Checks if autospoilers are armed (true) or not (false).
class _FlightSim_Control_SPOILERS_ARMED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:SPOILERS ARMED,{unit.value})")


# True if spoiler system available.
class _FlightSim_Control_SPOILER_AVAILABLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:SPOILER AVAILABLE,{unit.value})")


# Spoiler handle position.
class _FlightSim_Control_SPOILERS_HANDLE_POSITION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100 | FlightSim.Unit.Miscellaneous.POSITION'):
        # unit: Percent Over 100 or Position (16K = down, 0 = up)
        return self._.get(f"(A:SPOILERS HANDLE POSITION,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100 | FlightSim.Unit.Miscellaneous.POSITION', value: str):
        # unit: Percent Over 100 or Position (16K = down, 0 = up)
        self._.set(f"{value} (>A:SPOILERS HANDLE POSITION,{unit.value})")


# Percent left spoiler deflected.
# NOTE: This is available in multiplayer. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_Control_SPOILERS_LEFT_POSITION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100 | FlightSim.Unit.Miscellaneous.POSITION'):
        # unit: Percent Over 100 or Position (0 = retracted, 16K fully extended)
        return self._.get(f"(A:SPOILERS LEFT POSITION,{unit.value})")


# Percent right spoiler deflected.
# NOTE: This is available in multiplayer. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_Control_SPOILERS_RIGHT_POSITION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100 | FlightSim.Unit.Miscellaneous.POSITION'):
        # unit: Percent Over 100 or Position (0 = retracted, 16K fully extended)
        return self._.get(f"(A:SPOILERS RIGHT POSITION,{unit.value})")


# Indexed from 1, 100 is fully deployed, 0 flat on deck
class _FlightSim_Control_BLAST_SHIELD_POSITION:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:BLAST SHIELD POSITION:{self._index},{unit.value})")


# A number 1 through 4 for the cable number caught by the tailhook. Cable 1 is the one closest to the stern of the carrier. A value of 0 indicates no cable was caught.
class _FlightSim_Control_CABLE_CAUGHT_BY_TAILHOOK:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:CABLE CAUGHT BY TAILHOOK:{self._index},{unit.value})")


# Catapults are indexed from 1. This value will be 0 before the catapult fires, and then up to 100 as the aircraft is propelled down the catapult. The aircraft may takeoff before the value reaches 100 (depending on the aircraft weight, power applied, and other factors), in which case this value will not be further updated. This value could be used to drive a bogie animation.
class _FlightSim_Control_CATAPULT_STROKE_POSITION:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:CATAPULT STROKE POSITION:{self._index},{unit.value})")


# Holdback bars allow build up of thrust before takeoff from a catapult, and are installed by the deck crew of an aircraft carrier.
class _FlightSim_Control_HOLDBACK_BAR_INSTALLED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:HOLDBACK BAR INSTALLED,{unit.value})")


# This will be True if the launchbar is fully extended, and can be used, for example, to change the color of an instrument light.
class _FlightSim_Control_LAUNCHBAR_HELD_EXTENDED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:LAUNCHBAR HELD EXTENDED,{unit.value})")


# Installed on aircraft before takeoff from a carrier catapult. Note that gear cannot retract with this extended. 100 = fully extended.
class _FlightSim_Control_LAUNCHBAR_POSITION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:LAUNCHBAR POSITION,{unit.value})")


# If this is set to True the launch bar switch has been engaged.
class _FlightSim_Control_LAUNCHBAR_SWITCH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:LAUNCHBAR SWITCH,{unit.value})")


# Maximum of 4. A model can contain more than 4 catapults, but only the first four will be read and recognized by the simulation.
class _FlightSim_Control_NUMBER_OF_CATAPULTS:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:NUMBER OF CATAPULTS,{unit.value})")


# The nose angle, where 0 is fully up.
class _FlightSim_Control_CONCORDE_NOSE_ANGLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:CONCORDE NOSE ANGLE,{unit.value})")


# The visor nose handle position.
class _FlightSim_Control_CONCORDE_VISOR_NOSE_HANDLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        VISOR_UP_NOSE_DOWN = 0
        VISOR_DOWN_NOSE_UP = 1
        VISOR_DOWN_NOSE_5_DEGREES = 2
        VISOR_DOWN_NOSE_12_5_DEGREES = 3

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:CONCORDE VISOR NOSE HANDLE,{unit.value})")


# The visor position expressed as a percentage where 0.0 = up and 1.0 = extended/down.
class _FlightSim_Control_CONCORDE_VISOR_POSITION_PERCENT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:CONCORDE VISOR POSITION PERCENT,{unit.value})")


class _FlightSim_Electrics:
    def __init__(self, flightSim):
        self._ = flightSim
        self.BUS_LOOKUP_INDEX = _FlightSim_Electrics_BUS_LOOKUP_INDEX(flightSim)
        self.BUS_BREAKER_PULLED = _FlightSim_Electrics_BUS_BREAKER_PULLED(flightSim)
        self.BUS_CONNECTION_ON = _FlightSim_Electrics_BUS_CONNECTION_ON(flightSim)
        self.ELECTRICAL_GENALT_LOAD = _FlightSim_Electrics_ELECTRICAL_GENALT_LOAD(flightSim)
        self.ELECTRICAL_GENALT_BUS_AMPS = _FlightSim_Electrics_ELECTRICAL_GENALT_BUS_AMPS(flightSim)
        self.ELECTRICAL_GENALT_BUS_VOLTAGE = _FlightSim_Electrics_ELECTRICAL_GENALT_BUS_VOLTAGE(flightSim)
        self.ELECTRICAL_MAIN_BUS_VOLTAGE = _FlightSim_Electrics_ELECTRICAL_MAIN_BUS_VOLTAGE(flightSim)
        self.ELECTRICAL_AVIONICS_BUS_AMPS = _FlightSim_Electrics_ELECTRICAL_AVIONICS_BUS_AMPS(flightSim)
        self.ELECTRICAL_AVIONICS_BUS_VOLTAGE = _FlightSim_Electrics_ELECTRICAL_AVIONICS_BUS_VOLTAGE(flightSim)
        self.ELECTRICAL_MAIN_BUS_AMPS = _FlightSim_Electrics_ELECTRICAL_MAIN_BUS_AMPS(flightSim)
        self.ELECTRICAL_OLD_CHARGING_AMPS = _FlightSim_Electrics_ELECTRICAL_OLD_CHARGING_AMPS(flightSim)
        self.ELECTRICAL_TOTAL_LOAD_AMPS = _FlightSim_Electrics_ELECTRICAL_TOTAL_LOAD_AMPS(flightSim)
        self.NEW_ELECTRICAL_SYSTEM = _FlightSim_Electrics_NEW_ELECTRICAL_SYSTEM(flightSim)
        self.ALTERNATOR_BREAKER_PULLED = _FlightSim_Electrics_ALTERNATOR_BREAKER_PULLED(flightSim)
        self.ALTERNATOR_CONNECTION_ON = _FlightSim_Electrics_ALTERNATOR_CONNECTION_ON(flightSim)
        self.GENERAL_ENG_MASTER_ALTERNATOR = lambda index: _FlightSim_Electrics_GENERAL_ENG_MASTER_ALTERNATOR(flightSim, index)
        self.APU_BLEED_PRESSURE_RECEIVED_BY_ENGINE = _FlightSim_Electrics_APU_BLEED_PRESSURE_RECEIVED_BY_ENGINE(flightSim)
        self.APU_GENERATOR_ACTIVE = lambda index: _FlightSim_Electrics_APU_GENERATOR_ACTIVE(flightSim, index)
        self.APU_GENERATOR_SWITCH = lambda index: _FlightSim_Electrics_APU_GENERATOR_SWITCH(flightSim, index)
        self.APU_ON_FIRE_DETECTED = _FlightSim_Electrics_APU_ON_FIRE_DETECTED(flightSim)
        self.APU_PCT_RPM = _FlightSim_Electrics_APU_PCT_RPM(flightSim)
        self.APU_PCT_STARTER = _FlightSim_Electrics_APU_PCT_STARTER(flightSim)
        self.APU_SWITCH = _FlightSim_Electrics_APU_SWITCH(flightSim)
        self.APU_VOLTS = lambda index: _FlightSim_Electrics_APU_VOLTS(flightSim, index)
        self.BLEED_AIR_APU = _FlightSim_Electrics_BLEED_AIR_APU(flightSim)
        self.BATTERY_BREAKER_PULLED = _FlightSim_Electrics_BATTERY_BREAKER_PULLED(flightSim)
        self.BATTERY_CONNECTION_ON = _FlightSim_Electrics_BATTERY_CONNECTION_ON(flightSim)
        self.ELECTRICAL_BATTERY_BUS_AMPS = _FlightSim_Electrics_ELECTRICAL_BATTERY_BUS_AMPS(flightSim)
        self.ELECTRICAL_BATTERY_BUS_VOLTAGE = _FlightSim_Electrics_ELECTRICAL_BATTERY_BUS_VOLTAGE(flightSim)
        self.ELECTRICAL_BATTERY_ESTIMATED_CAPACITY_PCT = _FlightSim_Electrics_ELECTRICAL_BATTERY_ESTIMATED_CAPACITY_PCT(flightSim)
        self.ELECTRICAL_BATTERY_LOAD = _FlightSim_Electrics_ELECTRICAL_BATTERY_LOAD(flightSim)
        self.ELECTRICAL_BATTERY_VOLTAGE = _FlightSim_Electrics_ELECTRICAL_BATTERY_VOLTAGE(flightSim)
        self.ELECTRICAL_HOT_BATTERY_BUS_AMPS = _FlightSim_Electrics_ELECTRICAL_HOT_BATTERY_BUS_AMPS(flightSim)
        self.ELECTRICAL_HOT_BATTERY_BUS_VOLTAGE = _FlightSim_Electrics_ELECTRICAL_HOT_BATTERY_BUS_VOLTAGE(flightSim)
        self.ELECTRICAL_MASTER_BATTERY = _FlightSim_Electrics_ELECTRICAL_MASTER_BATTERY(flightSim)
        self.BREAKER_ADF = _FlightSim_Electrics_BREAKER_ADF(flightSim)
        self.BREAKER_ALTFLD = _FlightSim_Electrics_BREAKER_ALTFLD(flightSim)
        self.BREAKER_AUTOPILOT = _FlightSim_Electrics_BREAKER_AUTOPILOT(flightSim)
        self.BREAKER_AVNBUS1 = _FlightSim_Electrics_BREAKER_AVNBUS1(flightSim)
        self.BREAKER_AVNBUS2 = _FlightSim_Electrics_BREAKER_AVNBUS2(flightSim)
        self.BREAKER_AVNFAN = _FlightSim_Electrics_BREAKER_AVNFAN(flightSim)
        self.BREAKER_FLAP = _FlightSim_Electrics_BREAKER_FLAP(flightSim)
        self.BREAKER_GPS = _FlightSim_Electrics_BREAKER_GPS(flightSim)
        self.BREAKER_INST = _FlightSim_Electrics_BREAKER_INST(flightSim)
        self.BREAKER_INSTLTS = _FlightSim_Electrics_BREAKER_INSTLTS(flightSim)
        self.BREAKER_LTS_PWR = _FlightSim_Electrics_BREAKER_LTS_PWR(flightSim)
        self.BREAKER_NAVCOM1 = _FlightSim_Electrics_BREAKER_NAVCOM1(flightSim)
        self.BREAKER_NAVCOM2 = _FlightSim_Electrics_BREAKER_NAVCOM2(flightSim)
        self.BREAKER_NAVCOM3 = _FlightSim_Electrics_BREAKER_NAVCOM3(flightSim)
        self.BREAKER_TURNCOORD = _FlightSim_Electrics_BREAKER_TURNCOORD(flightSim)
        self.BREAKER_WARN = _FlightSim_Electrics_BREAKER_WARN(flightSim)
        self.BREAKER_XPNDR = _FlightSim_Electrics_BREAKER_XPNDR(flightSim)
        self.CIRCUIT_AUTOPILOT_ON = _FlightSim_Electrics_CIRCUIT_AUTOPILOT_ON(flightSim)
        self.CIRCUIT_AUTO_BRAKES_ON = _FlightSim_Electrics_CIRCUIT_AUTO_BRAKES_ON(flightSim)
        self.CIRCUIT_AUTO_FEATHER_ON = _FlightSim_Electrics_CIRCUIT_AUTO_FEATHER_ON(flightSim)
        self.CIRCUIT_AVIONICS_ON = _FlightSim_Electrics_CIRCUIT_AVIONICS_ON(flightSim)
        self.CIRCUIT_BREAKER_PULLED = _FlightSim_Electrics_CIRCUIT_BREAKER_PULLED(flightSim)
        self.CIRCUIT_CONNECTION_ON = _FlightSim_Electrics_CIRCUIT_CONNECTION_ON(flightSim)
        self.CIRCUIT_FLAP_MOTOR_ON = _FlightSim_Electrics_CIRCUIT_FLAP_MOTOR_ON(flightSim)
        self.CIRCUIT_GEAR_MOTOR_ON = _FlightSim_Electrics_CIRCUIT_GEAR_MOTOR_ON(flightSim)
        self.CIRCUIT_GEAR_WARNING_ON = _FlightSim_Electrics_CIRCUIT_GEAR_WARNING_ON(flightSim)
        self.CIRCUIT_GENERAL_PANEL_ON = _FlightSim_Electrics_CIRCUIT_GENERAL_PANEL_ON(flightSim)
        self.CIRCUIT_HYDRAULIC_PUMP_ON = _FlightSim_Electrics_CIRCUIT_HYDRAULIC_PUMP_ON(flightSim)
        self.CIRCUIT_MARKER_BEACON_ON = _FlightSim_Electrics_CIRCUIT_MARKER_BEACON_ON(flightSim)
        self.CIRCUIT_NAVCOM1_ON = _FlightSim_Electrics_CIRCUIT_NAVCOM1_ON(flightSim)
        self.CIRCUIT_NAVCOM2_ON = _FlightSim_Electrics_CIRCUIT_NAVCOM2_ON(flightSim)
        self.CIRCUIT_NAVCOM3_ON = _FlightSim_Electrics_CIRCUIT_NAVCOM3_ON(flightSim)
        self.CIRCUIT_ON = _FlightSim_Electrics_CIRCUIT_ON(flightSim)
        self.CIRCUIT_PITOT_HEAT_ON = _FlightSim_Electrics_CIRCUIT_PITOT_HEAT_ON(flightSim)
        self.CIRCUIT_POWER_SETTING = _FlightSim_Electrics_CIRCUIT_POWER_SETTING(flightSim)
        self.CIRCUIT_PROP_SYNC_ON = _FlightSim_Electrics_CIRCUIT_PROP_SYNC_ON(flightSim)
        self.CIRCUIT_STANDBY_VACUUM_ON = _FlightSim_Electrics_CIRCUIT_STANDBY_VACUUM_ON(flightSim)
        self.CIRCUIT_SWITCH_ON = _FlightSim_Electrics_CIRCUIT_SWITCH_ON(flightSim)
        self.EXTERNAL_POWER_AVAILABLE = _FlightSim_Electrics_EXTERNAL_POWER_AVAILABLE(flightSim)
        self.EXTERNAL_POWER_BREAKER_PULLED = _FlightSim_Electrics_EXTERNAL_POWER_BREAKER_PULLED(flightSim)
        self.EXTERNAL_POWER_CONNECTION_ON = _FlightSim_Electrics_EXTERNAL_POWER_CONNECTION_ON(flightSim)
        self.EXTERNAL_POWER_ON = _FlightSim_Electrics_EXTERNAL_POWER_ON(flightSim)


# This is a settable simvar meaning that it can both be read and set. Some of the simvars in this list are using this to lookup a value using two arguments (one argument in addition to the component index). For example to check the state of the connection between a "circuit.45" and the "bus.2" it would be written as follows:
# 2 (>A:BUS LOOKUP INDEX, Number) (A:CIRCUIT CONNECTION ON:45, Bool)
# It should be notes that when BUS_LOOKUP_INDEX is not set (ie: it is 0) then TRUE will be returned if any of your bus connections are on.
#! -
class _FlightSim_Electrics_BUS_LOOKUP_INDEX:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: ''):
        return self._.get(f"(A:BUS LOOKUP INDEX,{unit.value})")

    def set(self, unit: '', value: str):
        self._.set(f"{value} (>A:BUS LOOKUP INDEX,{unit.value})")


# This will be true if the bus breaker is pulled. Requires a BUS_LOOKUP_INDEX and a bus index.
class _FlightSim_Electrics_BUS_BREAKER_PULLED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:BUS BREAKER PULLED,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:BUS BREAKER PULLED,{unit.value})")


# This will be true if the bus is connected. Requires a BUS_LOOKUP_INDEX and a bus index.
class _FlightSim_Electrics_BUS_CONNECTION_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:BUS CONNECTION ON,{unit.value})")


# This returns the percentage of the load output that is being consumed. This requires an alternator index when referencing.
class _FlightSim_Electrics_ELECTRICAL_GENALT_LOAD:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:ELECTRICAL GENALT LOAD,{unit.value})")


# The load handled by the alternator. This requires an alternator index when referencing.
class _FlightSim_Electrics_ELECTRICAL_GENALT_BUS_AMPS:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.ElectricalCurrent.AMPERE'):
        return self._.get(f"(A:ELECTRICAL GENALT BUS AMPS,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.ElectricalCurrent.AMPERE', value: str):
        self._.set(f"{value} (>A:ELECTRICAL GENALT BUS AMPS,{unit.value})")


# General alternator voltage. This requires an alternator index when referencing.
class _FlightSim_Electrics_ELECTRICAL_GENALT_BUS_VOLTAGE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.ElectricalPotential.VOLT'):
        return self._.get(f"(A:ELECTRICAL GENALT BUS VOLTAGE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.ElectricalPotential.VOLT', value: str):
        self._.set(f"{value} (>A:ELECTRICAL GENALT BUS VOLTAGE,{unit.value})")


# The main bus voltage. Use a bus index when referencing.
class _FlightSim_Electrics_ELECTRICAL_MAIN_BUS_VOLTAGE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.ElectricalPotential.VOLT'):
        return self._.get(f"(A:ELECTRICAL MAIN BUS VOLTAGE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.ElectricalPotential.VOLT', value: str):
        self._.set(f"{value} (>A:ELECTRICAL MAIN BUS VOLTAGE,{unit.value})")


# Avionics bus current
class _FlightSim_Electrics_ELECTRICAL_AVIONICS_BUS_AMPS:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.ElectricalCurrent.AMPERE'):
        return self._.get(f"(A:ELECTRICAL AVIONICS BUS AMPS,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.ElectricalCurrent.AMPERE', value: str):
        self._.set(f"{value} (>A:ELECTRICAL AVIONICS BUS AMPS,{unit.value})")


# Avionics bus voltage
class _FlightSim_Electrics_ELECTRICAL_AVIONICS_BUS_VOLTAGE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.ElectricalPotential.VOLT'):
        return self._.get(f"(A:ELECTRICAL AVIONICS BUS VOLTAGE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.ElectricalPotential.VOLT', value: str):
        self._.set(f"{value} (>A:ELECTRICAL AVIONICS BUS VOLTAGE,{unit.value})")


# Main bus current
class _FlightSim_Electrics_ELECTRICAL_MAIN_BUS_AMPS:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.ElectricalCurrent.AMPERE'):
        return self._.get(f"(A:ELECTRICAL MAIN BUS AMPS,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.ElectricalCurrent.AMPERE', value: str):
        self._.set(f"{value} (>A:ELECTRICAL MAIN BUS AMPS,{unit.value})")


# Deprecated, do not use!
# Use ELECTRICAL BATTERY LOAD.
class _FlightSim_Electrics_ELECTRICAL_OLD_CHARGING_AMPS:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.ElectricalCurrent.AMPERE'):
        return self._.get(f"(A:ELECTRICAL OLD CHARGING AMPS,{unit.value})")


# Total load amps
class _FlightSim_Electrics_ELECTRICAL_TOTAL_LOAD_AMPS:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.ElectricalCurrent.AMPERE'):
        return self._.get(f"(A:ELECTRICAL TOTAL LOAD AMPS,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.ElectricalCurrent.AMPERE', value: str):
        self._.set(f"{value} (>A:ELECTRICAL TOTAL LOAD AMPS,{unit.value})")


# Is the aircraft using the new Electrical System or the legacy FSX one.
class _FlightSim_Electrics_NEW_ELECTRICAL_SYSTEM:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:NEW ELECTRICAL SYSTEM,{unit.value})")


# This will be true if the alternator breaker is pulled. Requires a BUS_LOOKUP_INDEX and an alternator index.
class _FlightSim_Electrics_ALTERNATOR_BREAKER_PULLED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:ALTERNATOR BREAKER PULLED,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:ALTERNATOR BREAKER PULLED,{unit.value})")


# This will be true if the alternator is connected. Requires a BUS_LOOKUP_INDEX and an alternator index.
class _FlightSim_Electrics_ALTERNATOR_CONNECTION_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:ALTERNATOR CONNECTION ON,{unit.value})")


# The alternator (generator) switch position, true if the switch is ON. Requires an engine index, and the use of an alternator index when referencing.
class _FlightSim_Electrics_GENERAL_ENG_MASTER_ALTERNATOR:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GENERAL ENG MASTER ALTERNATOR:{self._index},{unit.value})")


# Bleed air pressure received by the engine from the APU.
class _FlightSim_Electrics_APU_BLEED_PRESSURE_RECEIVED_BY_ENGINE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Pressure.POUND_FORCE_PER_SQUARE_INCH'):
        return self._.get(f"(A:APU BLEED PRESSURE RECEIVED BY ENGINE,{unit.value})")


# Set or get whether an APU is active (true) or not (false). Takes an index to be able to have multiple generators on a single APU.
class _FlightSim_Electrics_APU_GENERATOR_ACTIVE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:APU GENERATOR ACTIVE:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:APU GENERATOR ACTIVE:{self._index},{unit.value})")


# Enables or disables the APU for an engine. Takes an index to be able to have multiple generators on a single APU
class _FlightSim_Electrics_APU_GENERATOR_SWITCH:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:APU GENERATOR SWITCH:{self._index},{unit.value})")


# Will return true if the APU is on fire, or false otherwise.
class _FlightSim_Electrics_APU_ON_FIRE_DETECTED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:APU ON FIRE DETECTED,{unit.value})")


# Auxiliary power unit RPM, as a percentage
class _FlightSim_Electrics_APU_PCT_RPM:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:APU PCT RPM,{unit.value})")


# Auxiliary power unit starter, as a percentage
class _FlightSim_Electrics_APU_PCT_STARTER:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:APU PCT STARTER,{unit.value})")


# Boolean, whether or not the APU is switched on.
class _FlightSim_Electrics_APU_SWITCH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:APU SWITCH,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:APU SWITCH,{unit.value})")


# The volts from the APU to the selected engine. Takes an index to be able to have multiple generators on a single APU.
class _FlightSim_Electrics_APU_VOLTS:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.ElectricalPotential.VOLT'):
        return self._.get(f"(A:APU VOLTS:{self._index},{unit.value})")


# Boolean, returns whether or not the APU attempts to provide Bleed Air.
class _FlightSim_Electrics_BLEED_AIR_APU:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:BLEED AIR APU,{unit.value})")


# This will be true if the battery breaker is pulled. Requires a BUS LOOKUP INDEX and a battery index.
class _FlightSim_Electrics_BATTERY_BREAKER_PULLED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:BATTERY BREAKER PULLED,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:BATTERY BREAKER PULLED,{unit.value})")


# This will be true if the battery is connected. Requires a BUS_LOOKUP_INDEX and a battery index.
class _FlightSim_Electrics_BATTERY_CONNECTION_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:BATTERY CONNECTION ON,{unit.value})")


# Battery bus current
class _FlightSim_Electrics_ELECTRICAL_BATTERY_BUS_AMPS:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.ElectricalCurrent.AMPERE'):
        return self._.get(f"(A:ELECTRICAL BATTERY BUS AMPS,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.ElectricalCurrent.AMPERE', value: str):
        self._.set(f"{value} (>A:ELECTRICAL BATTERY BUS AMPS,{unit.value})")


# Battery bus voltage
class _FlightSim_Electrics_ELECTRICAL_BATTERY_BUS_VOLTAGE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.ElectricalPotential.VOLT'):
        return self._.get(f"(A:ELECTRICAL BATTERY BUS VOLTAGE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.ElectricalPotential.VOLT', value: str):
        self._.set(f"{value} (>A:ELECTRICAL BATTERY BUS VOLTAGE,{unit.value})")


# Battery capacity over max capacity, 100 is full.
class _FlightSim_Electrics_ELECTRICAL_BATTERY_ESTIMATED_CAPACITY_PCT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:ELECTRICAL BATTERY ESTIMATED CAPACITY PCT,{unit.value})")


# The load handled by the battery (negative values mean the battery is receiving current). Use a battery index when referencing.
class _FlightSim_Electrics_ELECTRICAL_BATTERY_LOAD:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.ElectricalCurrent.AMPERE'):
        return self._.get(f"(A:ELECTRICAL BATTERY LOAD,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.ElectricalCurrent.AMPERE', value: str):
        self._.set(f"{value} (>A:ELECTRICAL BATTERY LOAD,{unit.value})")


# The battery voltage. Use a battery index when referencing.
class _FlightSim_Electrics_ELECTRICAL_BATTERY_VOLTAGE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.ElectricalPotential.VOLT'):
        return self._.get(f"(A:ELECTRICAL BATTERY VOLTAGE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.ElectricalPotential.VOLT', value: str):
        self._.set(f"{value} (>A:ELECTRICAL BATTERY VOLTAGE,{unit.value})")


# Current available when battery switch is turned off
class _FlightSim_Electrics_ELECTRICAL_HOT_BATTERY_BUS_AMPS:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.ElectricalCurrent.AMPERE'):
        return self._.get(f"(A:ELECTRICAL HOT BATTERY BUS AMPS,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.ElectricalCurrent.AMPERE', value: str):
        self._.set(f"{value} (>A:ELECTRICAL HOT BATTERY BUS AMPS,{unit.value})")


# Voltage available when battery switch is turned off
class _FlightSim_Electrics_ELECTRICAL_HOT_BATTERY_BUS_VOLTAGE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.ElectricalPotential.VOLT'):
        return self._.get(f"(A:ELECTRICAL HOT BATTERY BUS VOLTAGE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.ElectricalPotential.VOLT', value: str):
        self._.set(f"{value} (>A:ELECTRICAL HOT BATTERY BUS VOLTAGE,{unit.value})")


# The battery switch position, true if the switch is ON. Use a battery index when referencing.
class _FlightSim_Electrics_ELECTRICAL_MASTER_BATTERY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:ELECTRICAL MASTER BATTERY,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:ELECTRICAL MASTER BATTERY,{unit.value})")


# All these SimVars can be used to get or set the breaker state for the electrical system (either true or false).
# If the breaker is popped (set to false), then the associated circuit will not receive electricity.
class _FlightSim_Electrics_BREAKER_ADF:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:BREAKER ADF,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:BREAKER ADF,{unit.value})")


# All these SimVars can be used to get or set the breaker state for the electrical system (either true or false).
# If the breaker is popped (set to false), then the associated circuit will not receive electricity.
class _FlightSim_Electrics_BREAKER_ALTFLD:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:BREAKER ALTFLD,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:BREAKER ALTFLD,{unit.value})")


# All these SimVars can be used to get or set the breaker state for the electrical system (either true or false).
# If the breaker is popped (set to false), then the associated circuit will not receive electricity.
class _FlightSim_Electrics_BREAKER_AUTOPILOT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:BREAKER AUTOPILOT,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:BREAKER AUTOPILOT,{unit.value})")


# All these SimVars can be used to get or set the breaker state for the electrical system (either true or false).
# If the breaker is popped (set to false), then the associated circuit will not receive electricity.
class _FlightSim_Electrics_BREAKER_AVNBUS1:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:BREAKER AVNBUS1,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:BREAKER AVNBUS1,{unit.value})")


# All these SimVars can be used to get or set the breaker state for the electrical system (either true or false).
# If the breaker is popped (set to false), then the associated circuit will not receive electricity.
class _FlightSim_Electrics_BREAKER_AVNBUS2:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:BREAKER AVNBUS2,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:BREAKER AVNBUS2,{unit.value})")


# All these SimVars can be used to get or set the breaker state for the electrical system (either true or false).
# If the breaker is popped (set to false), then the associated circuit will not receive electricity.
class _FlightSim_Electrics_BREAKER_AVNFAN:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:BREAKER AVNFAN,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:BREAKER AVNFAN,{unit.value})")


# All these SimVars can be used to get or set the breaker state for the electrical system (either true or false).
# If the breaker is popped (set to false), then the associated circuit will not receive electricity.
class _FlightSim_Electrics_BREAKER_FLAP:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:BREAKER FLAP,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:BREAKER FLAP,{unit.value})")


# All these SimVars can be used to get or set the breaker state for the electrical system (either true or false).
# If the breaker is popped (set to false), then the associated circuit will not receive electricity.
class _FlightSim_Electrics_BREAKER_GPS:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:BREAKER GPS,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:BREAKER GPS,{unit.value})")


# All these SimVars can be used to get or set the breaker state for the electrical system (either true or false).
# If the breaker is popped (set to false), then the associated circuit will not receive electricity.
class _FlightSim_Electrics_BREAKER_INST:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:BREAKER INST,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:BREAKER INST,{unit.value})")


# All these SimVars can be used to get or set the breaker state for the electrical system (either true or false).
# If the breaker is popped (set to false), then the associated circuit will not receive electricity.
class _FlightSim_Electrics_BREAKER_INSTLTS:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:BREAKER INSTLTS,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:BREAKER INSTLTS,{unit.value})")


# All these SimVars can be used to get or set the breaker state for the electrical system (either true or false).
# If the breaker is popped (set to false), then the associated circuit will not receive electricity.
class _FlightSim_Electrics_BREAKER_LTS_PWR:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:BREAKER LTS PWR,{unit.value})")


# All these SimVars can be used to get or set the breaker state for the electrical system (either true or false).
# If the breaker is popped (set to false), then the associated circuit will not receive electricity.
class _FlightSim_Electrics_BREAKER_NAVCOM1:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:BREAKER NAVCOM1,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:BREAKER NAVCOM1,{unit.value})")


# All these SimVars can be used to get or set the breaker state for the electrical system (either true or false).
# If the breaker is popped (set to false), then the associated circuit will not receive electricity.
class _FlightSim_Electrics_BREAKER_NAVCOM2:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:BREAKER NAVCOM2,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:BREAKER NAVCOM2,{unit.value})")


# All these SimVars can be used to get or set the breaker state for the electrical system (either true or false).
# If the breaker is popped (set to false), then the associated circuit will not receive electricity.
class _FlightSim_Electrics_BREAKER_NAVCOM3:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:BREAKER NAVCOM3,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:BREAKER NAVCOM3,{unit.value})")


# All these SimVars can be used to get or set the breaker state for the electrical system (either true or false).
# If the breaker is popped (set to false), then the associated circuit will not receive electricity.
class _FlightSim_Electrics_BREAKER_TURNCOORD:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:BREAKER TURNCOORD,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:BREAKER TURNCOORD,{unit.value})")


# All these SimVars can be used to get or set the breaker state for the electrical system (either true or false).
# If the breaker is popped (set to false), then the associated circuit will not receive electricity.
class _FlightSim_Electrics_BREAKER_WARN:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:BREAKER WARN,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:BREAKER WARN,{unit.value})")


# All these SimVars can be used to get or set the breaker state for the electrical system (either true or false).
# If the breaker is popped (set to false), then the associated circuit will not receive electricity.
class _FlightSim_Electrics_BREAKER_XPNDR:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:BREAKER XPNDR,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:BREAKER XPNDR,{unit.value})")


# Is electrical power available to this circuit
class _FlightSim_Electrics_CIRCUIT_AUTOPILOT_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:CIRCUIT AUTOPILOT ON,{unit.value})")


# Is electrical power available to this circuit
class _FlightSim_Electrics_CIRCUIT_AUTO_BRAKES_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:CIRCUIT AUTO BRAKES ON,{unit.value})")


# Is electrical power available to this circuit. Please see the Note On Autofeathering for more information.
class _FlightSim_Electrics_CIRCUIT_AUTO_FEATHER_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:CIRCUIT AUTO FEATHER ON,{unit.value})")


# Is electrical power available to this circuit
class _FlightSim_Electrics_CIRCUIT_AVIONICS_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:CIRCUIT AVIONICS ON,{unit.value})")


# This will be true if the circuit breaker is pulled. Requires a BUS_LOOKUP_INDEX and a circuit index.
class _FlightSim_Electrics_CIRCUIT_BREAKER_PULLED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:CIRCUIT BREAKER PULLED,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:CIRCUIT BREAKER PULLED,{unit.value})")


# This will be true if the circuit is connected. Requires a BUS_LOOKUP_INDEX and a circuit index.
class _FlightSim_Electrics_CIRCUIT_CONNECTION_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:CIRCUIT CONNECTION ON,{unit.value})")


# Is electrical power available to the flap motor circuit
class _FlightSim_Electrics_CIRCUIT_FLAP_MOTOR_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:CIRCUIT FLAP MOTOR ON,{unit.value})")


# Is electrical power available to the gear motor circuit
class _FlightSim_Electrics_CIRCUIT_GEAR_MOTOR_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:CIRCUIT GEAR MOTOR ON,{unit.value})")


# Is electrical power available to gear warning circuit
class _FlightSim_Electrics_CIRCUIT_GEAR_WARNING_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:CIRCUIT GEAR WARNING ON,{unit.value})")


# Is electrical power available to the general panel circuit
class _FlightSim_Electrics_CIRCUIT_GENERAL_PANEL_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:CIRCUIT GENERAL PANEL ON,{unit.value})")


# Is electrical power available to the hydraulic pump circuit
class _FlightSim_Electrics_CIRCUIT_HYDRAULIC_PUMP_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:CIRCUIT HYDRAULIC PUMP ON,{unit.value})")


# Is electrical power available to the marker beacon circuit
class _FlightSim_Electrics_CIRCUIT_MARKER_BEACON_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:CIRCUIT MARKER BEACON ON,{unit.value})")


# Whether or not power is available to the NAVCOM1 circuit.
class _FlightSim_Electrics_CIRCUIT_NAVCOM1_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:CIRCUIT NAVCOM1 ON,{unit.value})")


# Whether or not power is available to the NAVCOM2 circuit.
class _FlightSim_Electrics_CIRCUIT_NAVCOM2_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:CIRCUIT NAVCOM2 ON,{unit.value})")


# Whether or not power is available to the NAVCOM3 circuit.
class _FlightSim_Electrics_CIRCUIT_NAVCOM3_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:CIRCUIT NAVCOM3 ON,{unit.value})")


# This will be true if the given circuit is functioning. Use a circuit index when referencing.
class _FlightSim_Electrics_CIRCUIT_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:CIRCUIT ON,{unit.value})")


# Is electrical power available to the pitot heat circuit
class _FlightSim_Electrics_CIRCUIT_PITOT_HEAT_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:CIRCUIT PITOT HEAT ON,{unit.value})")


# This returns the percentage of use that the circuit is getting. This requires a circuit index when referencing.
class _FlightSim_Electrics_CIRCUIT_POWER_SETTING:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:CIRCUIT POWER SETTING,{unit.value})")


# Is electrical power available to the propeller sync circuit
class _FlightSim_Electrics_CIRCUIT_PROP_SYNC_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:CIRCUIT PROP SYNC ON,{unit.value})")


# Is electrical power available to the vacuum circuit
class _FlightSim_Electrics_CIRCUIT_STANDBY_VACUUM_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:CIRCUIT STANDBY VACUUM ON,{unit.value})")


# The circuit switch position, true if the switch is ON. Use a circuit index when referencing.
class _FlightSim_Electrics_CIRCUIT_SWITCH_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:CIRCUIT SWITCH ON,{unit.value})")


# This will be true if the given external power source is available. Use an external power index when referencing.
class _FlightSim_Electrics_EXTERNAL_POWER_AVAILABLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:EXTERNAL POWER AVAILABLE,{unit.value})")


# Boolean, The state of the breaker of an external power source
class _FlightSim_Electrics_EXTERNAL_POWER_BREAKER_PULLED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:EXTERNAL POWER BREAKER PULLED,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:EXTERNAL POWER BREAKER PULLED,{unit.value})")


# Boolean, The state of the connection between a bus and an external power source
class _FlightSim_Electrics_EXTERNAL_POWER_CONNECTION_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:EXTERNAL POWER CONNECTION ON,{unit.value})")


# The external power switch position, true if the switch is ON. Use an external power index when referencing.
class _FlightSim_Electrics_EXTERNAL_POWER_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:EXTERNAL POWER ON,{unit.value})")


class _FlightSim_Engine:
    def __init__(self, flightSim):
        self._ = flightSim
        self.BLEED_AIR_ENGINE = lambda index: _FlightSim_Engine_BLEED_AIR_ENGINE(flightSim, index)
        self.BLEED_AIR_SOURCE_CONTROL = lambda index: _FlightSim_Engine_BLEED_AIR_SOURCE_CONTROL(flightSim, index)
        self.COWL_FLAPS = _FlightSim_Engine_COWL_FLAPS(flightSim)
        self.ENGINE_CONTROL_SELECT = _FlightSim_Engine_ENGINE_CONTROL_SELECT(flightSim)
        self.ENGINE_MIXURE_AVAILABLE = _FlightSim_Engine_ENGINE_MIXURE_AVAILABLE(flightSim)
        self.ENGINE_PRIMER = _FlightSim_Engine_ENGINE_PRIMER(flightSim)
        self.ENGINE_TYPE = _FlightSim_Engine_ENGINE_TYPE(flightSim)
        self.ENG_ANTI_ICE = lambda index: _FlightSim_Engine_ENG_ANTI_ICE(flightSim, index)
        self.ENG_COMBUSTION = lambda index: _FlightSim_Engine_ENG_COMBUSTION(flightSim, index)
        self.ENG_CYLINDER_HEAD_TEMPERATURE = lambda index: _FlightSim_Engine_ENG_CYLINDER_HEAD_TEMPERATURE(flightSim, index)
        self.ENG_EXHAUST_GAS_TEMPERATURE = lambda index: _FlightSim_Engine_ENG_EXHAUST_GAS_TEMPERATURE(flightSim, index)
        self.ENG_EXHAUST_GAS_TEMPERATURE_GES = lambda index: _FlightSim_Engine_ENG_EXHAUST_GAS_TEMPERATURE_GES(flightSim, index)
        self.ENG_FAILED = lambda index: _FlightSim_Engine_ENG_FAILED(flightSim, index)
        self.ENG_FUEL_FLOW_BUG_POSITION = lambda index: _FlightSim_Engine_ENG_FUEL_FLOW_BUG_POSITION(flightSim, index)
        self.ENG_FUEL_FLOW_GPH = lambda index: _FlightSim_Engine_ENG_FUEL_FLOW_GPH(flightSim, index)
        self.ENG_FUEL_FLOW_PPH = lambda index: _FlightSim_Engine_ENG_FUEL_FLOW_PPH(flightSim, index)
        self.ENG_FUEL_FLOW_PPH_SSL = lambda index: _FlightSim_Engine_ENG_FUEL_FLOW_PPH_SSL(flightSim, index)
        self.ENG_HYDRAULIC_PRESSURE = lambda index: _FlightSim_Engine_ENG_HYDRAULIC_PRESSURE(flightSim, index)
        self.ENG_HYDRAULIC_QUANTITY = lambda index: _FlightSim_Engine_ENG_HYDRAULIC_QUANTITY(flightSim, index)
        self.ENG_MANIFOLD_PRESSURE = lambda index: _FlightSim_Engine_ENG_MANIFOLD_PRESSURE(flightSim, index)
        self.ENG_MAX_RPM = _FlightSim_Engine_ENG_MAX_RPM(flightSim)
        self.ENG_N1_RPM = lambda index: _FlightSim_Engine_ENG_N1_RPM(flightSim, index)
        self.ENG_N2_RPM = lambda index: _FlightSim_Engine_ENG_N2_RPM(flightSim, index)
        self.ENG_OIL_PRESSURE = lambda index: _FlightSim_Engine_ENG_OIL_PRESSURE(flightSim, index)
        self.ENG_OIL_QUANTITY = lambda index: _FlightSim_Engine_ENG_OIL_QUANTITY(flightSim, index)
        self.ENG_OIL_TEMPERATURE = lambda index: _FlightSim_Engine_ENG_OIL_TEMPERATURE(flightSim, index)
        self.ENG_ON_FIRE = lambda index: _FlightSim_Engine_ENG_ON_FIRE(flightSim, index)
        self.ENG_PRESSURE_RATIO = lambda index: _FlightSim_Engine_ENG_PRESSURE_RATIO(flightSim, index)
        self.ENG_PRESSURE_RATIO_GES = lambda index: _FlightSim_Engine_ENG_PRESSURE_RATIO_GES(flightSim, index)
        self.ENG_RPM_ANIMATION_PERCENT = lambda index: _FlightSim_Engine_ENG_RPM_ANIMATION_PERCENT(flightSim, index)
        self.ENG_RPM_SCALER = lambda index: _FlightSim_Engine_ENG_RPM_SCALER(flightSim, index)
        self.ENG_TORQUE = lambda index: _FlightSim_Engine_ENG_TORQUE(flightSim, index)
        self.ENG_VIBRATION = lambda index: _FlightSim_Engine_ENG_VIBRATION(flightSim, index)
        self.ESTIMATED_FUEL_FLOW = lambda index: _FlightSim_Engine_ESTIMATED_FUEL_FLOW(flightSim, index)
        self.FULL_THROTTLE_THRUST_TO_WEIGHT_RATIO = _FlightSim_Engine_FULL_THROTTLE_THRUST_TO_WEIGHT_RATIO(flightSim)
        self.GENERAL_ENG_ANTI_ICE_POSITION = lambda index: _FlightSim_Engine_GENERAL_ENG_ANTI_ICE_POSITION(flightSim, index)
        self.GENERAL_ENG_COMBUSTION = lambda index: _FlightSim_Engine_GENERAL_ENG_COMBUSTION(flightSim, index)
        self.GENERAL_ENG_COMBUSTION_EX1 = lambda index: _FlightSim_Engine_GENERAL_ENG_COMBUSTION_EX1(flightSim, index)
        self.GENERAL_ENG_COMBUSTION_SOUND_PERCENT = lambda index: _FlightSim_Engine_GENERAL_ENG_COMBUSTION_SOUND_PERCENT(flightSim, index)
        self.GENERAL_ENG_DAMAGE_PERCENT = lambda index: _FlightSim_Engine_GENERAL_ENG_DAMAGE_PERCENT(flightSim, index)
        self.GENERAL_ENG_ELAPSED_TIME = lambda index: _FlightSim_Engine_GENERAL_ENG_ELAPSED_TIME(flightSim, index)
        self.GENERAL_ENG_EXHAUST_GAS_TEMPERATURE = lambda index: _FlightSim_Engine_GENERAL_ENG_EXHAUST_GAS_TEMPERATURE(flightSim, index)
        self.GENERAL_ENG_FAILED = lambda index: _FlightSim_Engine_GENERAL_ENG_FAILED(flightSim, index)
        self.GENERAL_ENG_FIRE_DETECTED = lambda index: _FlightSim_Engine_GENERAL_ENG_FIRE_DETECTED(flightSim, index)
        self.GENERAL_ENG_FUEL_PRESSURE = lambda index: _FlightSim_Engine_GENERAL_ENG_FUEL_PRESSURE(flightSim, index)
        self.GENERAL_ENG_FUEL_PUMP_ON = lambda index: _FlightSim_Engine_GENERAL_ENG_FUEL_PUMP_ON(flightSim, index)
        self.GENERAL_ENG_FUEL_PUMP_SWITCH = lambda index: _FlightSim_Engine_GENERAL_ENG_FUEL_PUMP_SWITCH(flightSim, index)
        self.GENERAL_ENG_FUEL_PUMP_SWITCH_EX1 = lambda index: _FlightSim_Engine_GENERAL_ENG_FUEL_PUMP_SWITCH_EX1(flightSim, index)
        self.GENERAL_ENG_FUEL_USED_SINCE_START = lambda index: _FlightSim_Engine_GENERAL_ENG_FUEL_USED_SINCE_START(flightSim, index)
        self.GENERAL_ENG_FUEL_VALVE = lambda index: _FlightSim_Engine_GENERAL_ENG_FUEL_VALVE(flightSim, index)
        self.GENERAL_ENG_GENERATOR_ACTIVE = lambda index: _FlightSim_Engine_GENERAL_ENG_GENERATOR_ACTIVE(flightSim, index)
        self.GENERAL_ENG_GENERATOR_SWITCH = lambda index: _FlightSim_Engine_GENERAL_ENG_GENERATOR_SWITCH(flightSim, index)
        self.GENERAL_ENG_HOBBS_ELAPSED_TIME = lambda index: _FlightSim_Engine_GENERAL_ENG_HOBBS_ELAPSED_TIME(flightSim, index)
        self.GENERAL_ENG_MASTER_ALTERNATOR = _FlightSim_Engine_GENERAL_ENG_MASTER_ALTERNATOR(flightSim)
        self.GENERAL_ENG_MAX_REACHED_RPM = lambda index: _FlightSim_Engine_GENERAL_ENG_MAX_REACHED_RPM(flightSim, index)
        self.GENERAL_ENG_MIXTURE_LEVER_POSITION = lambda index: _FlightSim_Engine_GENERAL_ENG_MIXTURE_LEVER_POSITION(flightSim, index)
        self.GENERAL_ENG_OIL_LEAKED_PERCENT = lambda index: _FlightSim_Engine_GENERAL_ENG_OIL_LEAKED_PERCENT(flightSim, index)
        self.GENERAL_ENG_OIL_PRESSURE = lambda index: _FlightSim_Engine_GENERAL_ENG_OIL_PRESSURE(flightSim, index)
        self.GENERAL_ENG_OIL_TEMPERATURE = lambda index: _FlightSim_Engine_GENERAL_ENG_OIL_TEMPERATURE(flightSim, index)
        self.GENERAL_ENG_PCT_MAX_RPM = lambda index: _FlightSim_Engine_GENERAL_ENG_PCT_MAX_RPM(flightSim, index)
        self.GENERAL_ENG_PROPELLER_LEVER_POSITION = lambda index: _FlightSim_Engine_GENERAL_ENG_PROPELLER_LEVER_POSITION(flightSim, index)
        self.GENERAL_ENG_REVERSE_THRUST_ENGAGED = _FlightSim_Engine_GENERAL_ENG_REVERSE_THRUST_ENGAGED(flightSim)
        self.GENERAL_ENG_RPM = lambda index: _FlightSim_Engine_GENERAL_ENG_RPM(flightSim, index)
        self.GENERAL_ENG_STARTER = lambda index: _FlightSim_Engine_GENERAL_ENG_STARTER(flightSim, index)
        self.GENERAL_ENG_STARTER_ACTIVE = lambda index: _FlightSim_Engine_GENERAL_ENG_STARTER_ACTIVE(flightSim, index)
        self.GENERAL_ENG_THROTTLE_LEVER_POSITION = lambda index: _FlightSim_Engine_GENERAL_ENG_THROTTLE_LEVER_POSITION(flightSim, index)
        self.GENERAL_ENG_THROTTLE_MANAGED_MODE = lambda index: _FlightSim_Engine_GENERAL_ENG_THROTTLE_MANAGED_MODE(flightSim, index)
        self.MASTER_IGNITION_SWITCH = _FlightSim_Engine_MASTER_IGNITION_SWITCH(flightSim)
        self.MAX_EGT = _FlightSim_Engine_MAX_EGT(flightSim)
        self.MAX_OIL_TEMPERATURE = _FlightSim_Engine_MAX_OIL_TEMPERATURE(flightSim)
        self.MAX_RATED_ENGINE_RPM = _FlightSim_Engine_MAX_RATED_ENGINE_RPM(flightSim)
        self.NUMBER_OF_ENGINES = _FlightSim_Engine_NUMBER_OF_ENGINES(flightSim)
        self.OIL_AMOUNT = _FlightSim_Engine_OIL_AMOUNT(flightSim)
        self.PANEL_AUTO_FEATHER_SWITCH = lambda index: _FlightSim_Engine_PANEL_AUTO_FEATHER_SWITCH(flightSim, index)
        self.PROP_AUTO_CRUISE_ACTIVE = _FlightSim_Engine_PROP_AUTO_CRUISE_ACTIVE(flightSim)
        self.PROP_AUTO_FEATHER_ARMED = lambda index: _FlightSim_Engine_PROP_AUTO_FEATHER_ARMED(flightSim, index)
        self.PROP_BETA = lambda index: _FlightSim_Engine_PROP_BETA(flightSim, index)
        self.PROP_BETA_FORCED_ACTIVE = _FlightSim_Engine_PROP_BETA_FORCED_ACTIVE(flightSim)
        self.PROP_BETA_FORCED_POSITION = _FlightSim_Engine_PROP_BETA_FORCED_POSITION(flightSim)
        self.PROP_BETA_MAX = _FlightSim_Engine_PROP_BETA_MAX(flightSim)
        self.PROP_BETA_MIN = _FlightSim_Engine_PROP_BETA_MIN(flightSim)
        self.PROP_BETA_MIN_REVERSE = _FlightSim_Engine_PROP_BETA_MIN_REVERSE(flightSim)
        self.PROP_DEICE_SWITCH = lambda index: _FlightSim_Engine_PROP_DEICE_SWITCH(flightSim, index)
        self.PROP_FEATHERED = lambda index: _FlightSim_Engine_PROP_FEATHERED(flightSim, index)
        self.PROP_FEATHERING_INHIBIT = lambda index: _FlightSim_Engine_PROP_FEATHERING_INHIBIT(flightSim, index)
        self.PROP_FEATHER_SWITCH = lambda index: _FlightSim_Engine_PROP_FEATHER_SWITCH(flightSim, index)
        self.PROP_MAX_RPM_PERCENT = lambda index: _FlightSim_Engine_PROP_MAX_RPM_PERCENT(flightSim, index)
        self.PROP_ROTATION_ANGLE = _FlightSim_Engine_PROP_ROTATION_ANGLE(flightSim)
        self.PROP_RPM = lambda index: _FlightSim_Engine_PROP_RPM(flightSim, index)
        self.PROP_SYNC_ACTIVE = lambda index: _FlightSim_Engine_PROP_SYNC_ACTIVE(flightSim, index)
        self.PROP_SYNC_DELTA_LEVER = lambda index: _FlightSim_Engine_PROP_SYNC_DELTA_LEVER(flightSim, index)
        self.PROP_THRUST = lambda index: _FlightSim_Engine_PROP_THRUST(flightSim, index)
        self.PROPELLER_ADVANCED_SELECTION = _FlightSim_Engine_PROPELLER_ADVANCED_SELECTION(flightSim)
        self.SHUTOFF_VALVE_PULLED = _FlightSim_Engine_SHUTOFF_VALVE_PULLED(flightSim)
        self.THROTTLE_LOWER_LIMIT = _FlightSim_Engine_THROTTLE_LOWER_LIMIT(flightSim)
        self.TURB_ENG_AFTERBURNER = lambda index: _FlightSim_Engine_TURB_ENG_AFTERBURNER(flightSim, index)
        self.TURB_ENG_AFTERBURNER_PCT_ACTIVE = lambda index: _FlightSim_Engine_TURB_ENG_AFTERBURNER_PCT_ACTIVE(flightSim, index)
        self.TURB_ENG_AFTERBURNER_STAGE_ACTIVE = lambda index: _FlightSim_Engine_TURB_ENG_AFTERBURNER_STAGE_ACTIVE(flightSim, index)
        self.TURB_ENG_BLEED_AIR = lambda index: _FlightSim_Engine_TURB_ENG_BLEED_AIR(flightSim, index)
        self.TURB_ENG_COMMANDED_N1 = lambda index: _FlightSim_Engine_TURB_ENG_COMMANDED_N1(flightSim, index)
        self.TURB_ENG_CONDITION_LEVER_POSITION = lambda index: _FlightSim_Engine_TURB_ENG_CONDITION_LEVER_POSITION(flightSim, index)
        self.TURB_ENG_CORRECTED_FF = lambda index: _FlightSim_Engine_TURB_ENG_CORRECTED_FF(flightSim, index)
        self.TURB_ENG_CORRECTED_N1 = lambda index: _FlightSim_Engine_TURB_ENG_CORRECTED_N1(flightSim, index)
        self.TURB_ENG_CORRECTED_N2 = lambda index: _FlightSim_Engine_TURB_ENG_CORRECTED_N2(flightSim, index)
        self.TURB_ENG_FREE_TURBINE_TORQUE = lambda index: _FlightSim_Engine_TURB_ENG_FREE_TURBINE_TORQUE(flightSim, index)
        self.TURB_ENG_FUEL_AVAILABLE = lambda index: _FlightSim_Engine_TURB_ENG_FUEL_AVAILABLE(flightSim, index)
        self.TURB_ENG_FUEL_EFFICIENCY_LOSS = lambda index: _FlightSim_Engine_TURB_ENG_FUEL_EFFICIENCY_LOSS(flightSim, index)
        self.TURB_ENG_FUEL_FLOW_PPH = lambda index: _FlightSim_Engine_TURB_ENG_FUEL_FLOW_PPH(flightSim, index)
        self.TURB_ENG_HIGH_IDLE = lambda index: _FlightSim_Engine_TURB_ENG_HIGH_IDLE(flightSim, index)
        self.TURB_ENG_IGNITION_SWITCH = lambda index: _FlightSim_Engine_TURB_ENG_IGNITION_SWITCH(flightSim, index)
        self.TURB_ENG_IGNITION_SWITCH_EX1 = lambda index: _FlightSim_Engine_TURB_ENG_IGNITION_SWITCH_EX1(flightSim, index)
        self.TURB_ENG_IS_IGNITING = lambda index: _FlightSim_Engine_TURB_ENG_IS_IGNITING(flightSim, index)
        self.TURB_ENG_ITT = lambda index: _FlightSim_Engine_TURB_ENG_ITT(flightSim, index)
        self.TURB_ENG_ITT_COOLING_EFFICIENCY_LOSS = lambda index: _FlightSim_Engine_TURB_ENG_ITT_COOLING_EFFICIENCY_LOSS(flightSim, index)
        self.TURB_ENG_JET_THRUST = lambda index: _FlightSim_Engine_TURB_ENG_JET_THRUST(flightSim, index)
        self.TURB_ENG_LOW_IDLE = lambda index: _FlightSim_Engine_TURB_ENG_LOW_IDLE(flightSim, index)
        self.TURB_ENG_MASTER_STARTER_SWITCH = _FlightSim_Engine_TURB_ENG_MASTER_STARTER_SWITCH(flightSim)
        self.TURB_ENG_MAX_TORQUE_PERCENT = lambda index: _FlightSim_Engine_TURB_ENG_MAX_TORQUE_PERCENT(flightSim, index)
        self.TURB_ENG_N1 = lambda index: _FlightSim_Engine_TURB_ENG_N1(flightSim, index)
        self.TURB_ENG_N1_LOSS = lambda index: _FlightSim_Engine_TURB_ENG_N1_LOSS(flightSim, index)
        self.TURB_ENG_N2 = lambda index: _FlightSim_Engine_TURB_ENG_N2(flightSim, index)
        self.TURB_ENG_NUM_TANKS_USED = lambda index: _FlightSim_Engine_TURB_ENG_NUM_TANKS_USED(flightSim, index)
        self.TURB_ENG_PRESSURE_RATIO = lambda index: _FlightSim_Engine_TURB_ENG_PRESSURE_RATIO(flightSim, index)
        self.TURB_ENG_PRIMARY_NOZZLE_PERCENT = lambda index: _FlightSim_Engine_TURB_ENG_PRIMARY_NOZZLE_PERCENT(flightSim, index)
        self.TURB_ENG_REVERSE_NOZZLE_PERCENT = lambda index: _FlightSim_Engine_TURB_ENG_REVERSE_NOZZLE_PERCENT(flightSim, index)
        self.TURB_ENG_TANKS_USED = lambda index: _FlightSim_Engine_TURB_ENG_TANKS_USED(flightSim, index)
        self.TURB_ENG_TANK_SELECTOR = lambda index: _FlightSim_Engine_TURB_ENG_TANK_SELECTOR(flightSim, index)
        self.TURB_ENG_THROTTLE_COMMANDED_N1 = lambda index: _FlightSim_Engine_TURB_ENG_THROTTLE_COMMANDED_N1(flightSim, index)
        self.TURB_ENG_THRUST_EFFICIENCY_LOSS = lambda index: _FlightSim_Engine_TURB_ENG_THRUST_EFFICIENCY_LOSS(flightSim, index)
        self.TURB_ENG_VIBRATION = lambda index: _FlightSim_Engine_TURB_ENG_VIBRATION(flightSim, index)
        self.TURB_MAX_ITT = _FlightSim_Engine_TURB_MAX_ITT(flightSim)
        self.RECIP_CARBURETOR_TEMPERATURE = lambda index: _FlightSim_Engine_RECIP_CARBURETOR_TEMPERATURE(flightSim, index)
        self.RECIP_ENG_ALTERNATE_AIR_POSITION = lambda index: _FlightSim_Engine_RECIP_ENG_ALTERNATE_AIR_POSITION(flightSim, index)
        self.RECIP_ENG_ANTIDETONATION_TANK_MAX_QUANTITY = lambda index: _FlightSim_Engine_RECIP_ENG_ANTIDETONATION_TANK_MAX_QUANTITY(flightSim, index)
        self.RECIP_ENG_ANTIDETONATION_TANK_QUANTITY = lambda index: _FlightSim_Engine_RECIP_ENG_ANTIDETONATION_TANK_QUANTITY(flightSim, index)
        self.RECIP_ENG_ANTIDETONATION_TANK_VALVE = lambda index: _FlightSim_Engine_RECIP_ENG_ANTIDETONATION_TANK_VALVE(flightSim, index)
        self.RECIP_ENG_ANTIDETONATION_FLOW_RATE = lambda index: _FlightSim_Engine_RECIP_ENG_ANTIDETONATION_FLOW_RATE(flightSim, index)
        self.RECIP_ENG_BRAKE_POWER = lambda index: _FlightSim_Engine_RECIP_ENG_BRAKE_POWER(flightSim, index)
        self.RECIP_ENG_COOLANT_RESERVOIR_PERCENT = lambda index: _FlightSim_Engine_RECIP_ENG_COOLANT_RESERVOIR_PERCENT(flightSim, index)
        self.RECIP_ENG_COWL_FLAP_POSITION = lambda index: _FlightSim_Engine_RECIP_ENG_COWL_FLAP_POSITION(flightSim, index)
        self.RECIP_ENG_CYLINDER_HEAD_TEMPERATURE = lambda index: _FlightSim_Engine_RECIP_ENG_CYLINDER_HEAD_TEMPERATURE(flightSim, index)
        self.RECIP_ENG_CYLINDER_HEALTH = lambda index: _FlightSim_Engine_RECIP_ENG_CYLINDER_HEALTH(flightSim, index)
        self.RECIP_ENG_DETONATING = lambda index: _FlightSim_Engine_RECIP_ENG_DETONATING(flightSim, index)
        self.RECIP_ENG_EMERGENCY_BOOST_ACTIVE = lambda index: _FlightSim_Engine_RECIP_ENG_EMERGENCY_BOOST_ACTIVE(flightSim, index)
        self.RECIP_ENG_EMERGENCY_BOOST_ELAPSED_TIME = lambda index: _FlightSim_Engine_RECIP_ENG_EMERGENCY_BOOST_ELAPSED_TIME(flightSim, index)
        self.RECIP_ENG_ENGINE_MASTER_SWITCH = lambda index: _FlightSim_Engine_RECIP_ENG_ENGINE_MASTER_SWITCH(flightSim, index)
        self.RECIP_ENG_FUEL_AVAILABLE = lambda index: _FlightSim_Engine_RECIP_ENG_FUEL_AVAILABLE(flightSim, index)
        self.RECIP_ENG_FUEL_FLOW = lambda index: _FlightSim_Engine_RECIP_ENG_FUEL_FLOW(flightSim, index)
        self.RECIP_ENG_FUEL_NUMBER_TANKS_USED = lambda index: _FlightSim_Engine_RECIP_ENG_FUEL_NUMBER_TANKS_USED(flightSim, index)
        self.RECIP_ENG_FUEL_TANKS_USED = lambda index: _FlightSim_Engine_RECIP_ENG_FUEL_TANKS_USED(flightSim, index)
        self.RECIP_ENG_FUEL_TANK_SELECTOR = lambda index: _FlightSim_Engine_RECIP_ENG_FUEL_TANK_SELECTOR(flightSim, index)
        self.RECIP_ENG_GLOW_PLUG_ACTIVE = lambda index: _FlightSim_Engine_RECIP_ENG_GLOW_PLUG_ACTIVE(flightSim, index)
        self.RECIP_ENG_LEFT_MAGNETO = lambda index: _FlightSim_Engine_RECIP_ENG_LEFT_MAGNETO(flightSim, index)
        self.RECIP_ENG_MANIFOLD_PRESSURE = lambda index: _FlightSim_Engine_RECIP_ENG_MANIFOLD_PRESSURE(flightSim, index)
        self.RECIP_ENG_NITROUS_TANK_MAX_QUANTITY = lambda index: _FlightSim_Engine_RECIP_ENG_NITROUS_TANK_MAX_QUANTITY(flightSim, index)
        self.RECIP_ENG_NITROUS_TANK_QUANTITY = lambda index: _FlightSim_Engine_RECIP_ENG_NITROUS_TANK_QUANTITY(flightSim, index)
        self.RECIP_ENG_NITROUS_TANK_VALVE = _FlightSim_Engine_RECIP_ENG_NITROUS_TANK_VALVE(flightSim)
        self.RECIP_ENG_NUM_CYLINDERS = lambda index: _FlightSim_Engine_RECIP_ENG_NUM_CYLINDERS(flightSim, index)
        self.RECIP_ENG_NUM_CYLINDERS_FAILED = lambda index: _FlightSim_Engine_RECIP_ENG_NUM_CYLINDERS_FAILED(flightSim, index)
        self.RECIP_ENG_PRIMER = lambda index: _FlightSim_Engine_RECIP_ENG_PRIMER(flightSim, index)
        self.RECIP_ENG_RADIATOR_TEMPERATURE = lambda index: _FlightSim_Engine_RECIP_ENG_RADIATOR_TEMPERATURE(flightSim, index)
        self.RECIP_ENG_RIGHT_MAGNETO = lambda index: _FlightSim_Engine_RECIP_ENG_RIGHT_MAGNETO(flightSim, index)
        self.RECIP_ENG_STARTER_TORQUE = lambda index: _FlightSim_Engine_RECIP_ENG_STARTER_TORQUE(flightSim, index)
        self.RECIP_ENG_SUPERCHARGER_ACTIVE_GEAR = lambda index: _FlightSim_Engine_RECIP_ENG_SUPERCHARGER_ACTIVE_GEAR(flightSim, index)
        self.RECIP_ENG_TURBINE_INLET_TEMPERATURE = lambda index: _FlightSim_Engine_RECIP_ENG_TURBINE_INLET_TEMPERATURE(flightSim, index)
        self.RECIP_ENG_TURBOCHARGER_FAILED = lambda index: _FlightSim_Engine_RECIP_ENG_TURBOCHARGER_FAILED(flightSim, index)
        self.RECIP_ENG_WASTEGATE_POSITION = lambda index: _FlightSim_Engine_RECIP_ENG_WASTEGATE_POSITION(flightSim, index)
        self.RECIP_MAX_CHT = _FlightSim_Engine_RECIP_MAX_CHT(flightSim)
        self.RECIP_MIXTURE_RATIO = lambda index: _FlightSim_Engine_RECIP_MIXTURE_RATIO(flightSim, index)


# Returns whether or not the indexed engine (see note) attempts to provide bleed air.
class _FlightSim_Engine_BLEED_AIR_ENGINE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:BLEED AIR ENGINE:{self._index},{unit.value})")


# The bleed air system source controller for an indexed engine (see note). This will work as follows:
class _FlightSim_Engine_BLEED_AIR_SOURCE_CONTROL:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    class Unit(Enum):
        AUTO = 0
        OFF = 1
        APU = 2
        ENGINES = 3

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:BLEED AIR SOURCE CONTROL:{self._index},{unit.value})")


# Deprecated, do not use!
class _FlightSim_Engine_COWL_FLAPS:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:COWL FLAPS,{unit.value})")


# Selected engines (combination of bit flags)
#! Flags:
# 
# 1 = Engine 1
# 2 = Engine 2
# 4 = Engine 3
# 8 = Engine 4
class _FlightSim_Engine_ENGINE_CONTROL_SELECT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: ''):
        return self._.get(f"(A:ENGINE CONTROL SELECT,{unit.value})")

    def set(self, unit: '', value: str):
        self._.set(f"{value} (>A:ENGINE CONTROL SELECT,{unit.value})")


# True if engine mixture is available for prop engines. Deprecated, do not use (mixture is always available)!
class _FlightSim_Engine_ENGINE_MIXURE_AVAILABLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:ENGINE MIXURE AVAILABLE,{unit.value})")


# The engine primer position.
class _FlightSim_Engine_ENGINE_PRIMER:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION'):
        return self._.get(f"(A:ENGINE PRIMER,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION', value: str):
        self._.set(f"{value} (>A:ENGINE PRIMER,{unit.value})")


# Engine type.
class _FlightSim_Engine_ENGINE_TYPE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        PISTON = 0
        JET = 1
        NONE = 2
        HELO_BELL_TURBINE = 3
        UNSUPPORTED = 4
        TURBOPROP = 5

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:ENGINE TYPE,{unit.value})")


# Anti-ice switch for the indexed engine (see note), true if enabled false otherwise.
class _FlightSim_Engine_ENG_ANTI_ICE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:ENG ANTI ICE:{self._index},{unit.value})")


# True if the indexed engine (see note) is running, false otherwise.
class _FlightSim_Engine_ENG_COMBUSTION:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:ENG COMBUSTION:{self._index},{unit.value})")


# The indexed engine (see note) cylinder head temperature.
class _FlightSim_Engine_ENG_CYLINDER_HEAD_TEMPERATURE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Temperature.RANKINE'):
        return self._.get(f"(A:ENG CYLINDER HEAD TEMPERATURE:{self._index},{unit.value})")


# Exhaust gas temperature for the indexed engine (see note).
class _FlightSim_Engine_ENG_EXHAUST_GAS_TEMPERATURE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Temperature.RANKINE'):
        return self._.get(f"(A:ENG EXHAUST GAS TEMPERATURE:{self._index},{unit.value})")


# Governed engine setting exhaust gas temperature for the indexed engine (see note).
class _FlightSim_Engine_ENG_EXHAUST_GAS_TEMPERATURE_GES:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:ENG EXHAUST GAS TEMPERATURE GES:{self._index},{unit.value})")


# Failure flag for the indexed engine (see note) that has failed.
class _FlightSim_Engine_ENG_FAILED:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:ENG FAILED:{self._index},{unit.value})")


# Fuel flow reference in pounds per hour for the indexed engine (see note).
class _FlightSim_Engine_ENG_FUEL_FLOW_BUG_POSITION:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.POUND_PER_HOUR'):
        return self._.get(f"(A:ENG FUEL FLOW BUG POSITION:{self._index},{unit.value})")


# Engine fuel flow in gallons per hour for the indexed engine (see note).
class _FlightSim_Engine_ENG_FUEL_FLOW_GPH:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.VolumeRate.GALLON_PER_HOUR'):
        return self._.get(f"(A:ENG FUEL FLOW GPH:{self._index},{unit.value})")


# The indexed engine (see note) fuel flow in pounds per hour.
class _FlightSim_Engine_ENG_FUEL_FLOW_PPH:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.POUND_PER_HOUR'):
        return self._.get(f"(A:ENG FUEL FLOW PPH:{self._index},{unit.value})")


# Engine fuel flow in pounds per hour.
# Deprecated in favour of ENG FUEL FLOW PPH.
class _FlightSim_Engine_ENG_FUEL_FLOW_PPH_SSL:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.POUND_PER_HOUR'):
        return self._.get(f"(A:ENG FUEL FLOW PPH SSL:{self._index},{unit.value})")


# The indexed engine (see note) hydraulic pressure.
class _FlightSim_Engine_ENG_HYDRAULIC_PRESSURE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Pressure.POUND_FORCE_PER_SQUARE_FOOT'):
        return self._.get(f"(A:ENG HYDRAULIC PRESSURE:{self._index},{unit.value})")


# The indexed engine (see note)hydraulic fluid quantity, as a percentage of total capacity
class _FlightSim_Engine_ENG_HYDRAULIC_QUANTITY:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:ENG HYDRAULIC QUANTITY:{self._index},{unit.value})")


# The indexed engine (see note) manifold pressure.
class _FlightSim_Engine_ENG_MANIFOLD_PRESSURE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Pressure.INCH_OF_MERCURY'):
        return self._.get(f"(A:ENG MANIFOLD PRESSURE:{self._index},{unit.value})")


# The indexed engine (see note) Maximum rpm.
class _FlightSim_Engine_ENG_MAX_RPM:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.AngularVelocity.REVOLUTION_PER_MINUTE'):
        return self._.get(f"(A:ENG MAX RPM,{unit.value})")


# The indexed engine (see note) N1 rpm.
class _FlightSim_Engine_ENG_N1_RPM:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.AngularVelocity.REVOLUTION_PER_MINUTE'):
        # unit: RPM (0 to 16384 = 0 to 100%)
        return self._.get(f"(A:ENG N1 RPM:{self._index},{unit.value})")


# The indexed engine (see note) N2 rpm.
class _FlightSim_Engine_ENG_N2_RPM:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.AngularVelocity.REVOLUTION_PER_MINUTE'):
        # unit: RPM (0 to 16384 = 0 to 100%)
        return self._.get(f"(A:ENG N2 RPM:{self._index},{unit.value})")


# The indexed engine (see note) oil pressure.
class _FlightSim_Engine_ENG_OIL_PRESSURE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Pressure.POUND_FORCE_PER_SQUARE_FOOT'):
        return self._.get(f"(A:ENG OIL PRESSURE:{self._index},{unit.value})")


# The indexed engine (see note) oil quantity as a percentage of full capacity.
class _FlightSim_Engine_ENG_OIL_QUANTITY:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:ENG OIL QUANTITY:{self._index},{unit.value})")


# The indexed engine (see note) oil temperature.
class _FlightSim_Engine_ENG_OIL_TEMPERATURE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Temperature.RANKINE'):
        return self._.get(f"(A:ENG OIL TEMPERATURE:{self._index},{unit.value})")


# The indexed engine (see note) on fire state.
class _FlightSim_Engine_ENG_ON_FIRE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:ENG ON FIRE:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:ENG ON FIRE:{self._index},{unit.value})")


# The indexed engine (see note) pressure ratio.
class _FlightSim_Engine_ENG_PRESSURE_RATIO:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.RATIO'):
        # unit: Ratio (0-16384)
        return self._.get(f"(A:ENG PRESSURE RATIO:{self._index},{unit.value})")


# Engine pressure ratio. Deprecated, do not use!
class _FlightSim_Engine_ENG_PRESSURE_RATIO_GES:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.SCALER'):
        return self._.get(f"(A:ENG PRESSURE RATIO GES:{self._index},{unit.value})")


# The indexed engine (see note) percentage maximum rated rpm - used for visual animation.
# NOTE: This is available in multiplayer to all near aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_Engine_ENG_RPM_ANIMATION_PERCENT:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:ENG RPM ANIMATION PERCENT:{self._index},{unit.value})")


# RPM scalar value. Deprecated, do not use!
class _FlightSim_Engine_ENG_RPM_SCALER:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.SCALER'):
        return self._.get(f"(A:ENG RPM SCALER:{self._index},{unit.value})")


# The indexed engine (see note) torque.
class _FlightSim_Engine_ENG_TORQUE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Torque.FOOT_POUND'):
        return self._.get(f"(A:ENG TORQUE:{self._index},{unit.value})")


# The indexed engine (see note) vibration.
class _FlightSim_Engine_ENG_VIBRATION:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:ENG VIBRATION:{self._index},{unit.value})")


# Estimated fuel flow to the indexed engine (see note) at cruise speed.
class _FlightSim_Engine_ESTIMATED_FUEL_FLOW:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.POUND_PER_HOUR'):
        return self._.get(f"(A:ESTIMATED FUEL FLOW:{self._index},{unit.value})")


# Full throttle thrust to weight ratio
class _FlightSim_Engine_FULL_THROTTLE_THRUST_TO_WEIGHT_RATIO:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:FULL THROTTLE THRUST TO WEIGHT RATIO,{unit.value})")


# The indexed engine (see note) anti-ice switch state - 0 (FALSE) is off and 1 (TRUE) is on.
class _FlightSim_Engine_GENERAL_ENG_ANTI_ICE_POSITION:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GENERAL ENG ANTI ICE POSITION:{self._index},{unit.value})")


# Set the indexed engine (see note) combustion flag to TRUE or FALSE. Note that this will not only stop all combustion, but it will also set the engine RPM to 0, regardless of the actual state of the simulation.
# NOTE: This is available in multiplayer to all far aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_Engine_GENERAL_ENG_COMBUSTION:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GENERAL ENG COMBUSTION:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:GENERAL ENG COMBUSTION:{self._index},{unit.value})")


# This SimVar is similar to GENERAL ENG COMBUSTION, in that it can also be used to enable or disable engine combustion. However this SimVar will not interfere with the current state of ths simulation. For example, if the aircraft has a turbine engine with auto_ignition enabled or it's a propeller engine with magnetos, then in the subsequent simulation frames this SimVar may be set to 1 (TRUE) again as the engine restarts automatically.
class _FlightSim_Engine_GENERAL_ENG_COMBUSTION_EX1:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GENERAL ENG COMBUSTION EX1:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:GENERAL ENG COMBUSTION EX1:{self._index},{unit.value})")


# Percent of maximum sound being created by the indexed engine (see note).
# NOTE: This is available in multiplayer to all far aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_Engine_GENERAL_ENG_COMBUSTION_SOUND_PERCENT:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:GENERAL ENG COMBUSTION SOUND PERCENT:{self._index},{unit.value})")


# Percent of total damage to the indexed engine (see note).
class _FlightSim_Engine_GENERAL_ENG_DAMAGE_PERCENT:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:GENERAL ENG DAMAGE PERCENT:{self._index},{unit.value})")


# Total elapsed time since the indexed engine (see note) was started.
class _FlightSim_Engine_GENERAL_ENG_ELAPSED_TIME:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Time.HOUR'):
        return self._.get(f"(A:GENERAL ENG ELAPSED TIME:{self._index},{unit.value})")


# The indexed engine (see note) exhaust gas temperature.
class _FlightSim_Engine_GENERAL_ENG_EXHAUST_GAS_TEMPERATURE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Temperature.RANKINE'):
        return self._.get(f"(A:GENERAL ENG EXHAUST GAS TEMPERATURE:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Temperature.RANKINE', value: str):
        self._.set(f"{value} (>A:GENERAL ENG EXHAUST GAS TEMPERATURE:{self._index},{unit.value})")


# The indexed engine (see note) fail flag.
class _FlightSim_Engine_GENERAL_ENG_FAILED:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GENERAL ENG FAILED:{self._index},{unit.value})")


# Detects if a fire has been detected in an indexed engine (see note) or not. If 0 (FALSE) no fire has been detected and if 1 (TRUE) then it has.
class _FlightSim_Engine_GENERAL_ENG_FIRE_DETECTED:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GENERAL ENG FIRE DETECTED:{self._index},{unit.value})")


# The indexed engine (see note) fuel pressure.
class _FlightSim_Engine_GENERAL_ENG_FUEL_PRESSURE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Pressure.POUND_FORCE_PER_SQUARE_INCH'):
        return self._.get(f"(A:GENERAL ENG FUEL PRESSURE:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Pressure.POUND_FORCE_PER_SQUARE_INCH', value: str):
        self._.set(f"{value} (>A:GENERAL ENG FUEL PRESSURE:{self._index},{unit.value})")


# Whether the indexed engine (see note) fuel pump on (1, TRUE) or off (0, FALSE).
class _FlightSim_Engine_GENERAL_ENG_FUEL_PUMP_ON:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GENERAL ENG FUEL PUMP ON:{self._index},{unit.value})")


# Fuel pump switch state the indexed engine (see note). If 0 (FALSE) the pump is off and if 1 (TRUE) then it is on.
class _FlightSim_Engine_GENERAL_ENG_FUEL_PUMP_SWITCH:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GENERAL ENG FUEL PUMP SWITCH:{self._index},{unit.value})")


# Equivalent to GENERAL ENG FUEL PUMP SWITCH but differentiates between ON and AUTO
class _FlightSim_Engine_GENERAL_ENG_FUEL_PUMP_SWITCH_EX1:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GENERAL ENG FUEL PUMP SWITCH EX1:{self._index},{unit.value})")


# Fuel used since the indexed engine (see note) was last started.
class _FlightSim_Engine_GENERAL_ENG_FUEL_USED_SINCE_START:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Weight.POUND'):
        return self._.get(f"(A:GENERAL ENG FUEL USED SINCE START:{self._index},{unit.value})")


# Fuel valve state for the indexed engine (see note). If 0 (FALSE) then the valve is closed and if 1 (TRUE) then it is open.
class _FlightSim_Engine_GENERAL_ENG_FUEL_VALVE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GENERAL ENG FUEL VALVE:{self._index},{unit.value})")


# Settable alternator (generator) on/off switch for the indexed engine (see note).
class _FlightSim_Engine_GENERAL_ENG_GENERATOR_ACTIVE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GENERAL ENG GENERATOR ACTIVE:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:GENERAL ENG GENERATOR ACTIVE:{self._index},{unit.value})")


# Alternator (generator) on/off switch state for the indexed engine (see note).
class _FlightSim_Engine_GENERAL_ENG_GENERATOR_SWITCH:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GENERAL ENG GENERATOR SWITCH:{self._index},{unit.value})")


# This can be used to find the time since the indexed engine (see note) started running. Similar to ElapsedTachometerTime, this records the time the engine has been running, but instead of taking a % of the time based on the Pct/RPM this takes the full time, but only if a threshold RPM/speed is reached. You can set the thresholds using the accumulated_time_hobbs_min_pct_rpm and accumulated_time_hobbs_min_knots parameters in the [GENERALENGINEDATA] section of the engines.cfg file.
class _FlightSim_Engine_GENERAL_ENG_HOBBS_ELAPSED_TIME:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Time.SECOND'):
        return self._.get(f"(A:GENERAL ENG HOBBS ELAPSED TIME:{self._index},{unit.value})")


# The alternator switch for a specific engine. Requires an engine index (1 - 4) when used.
class _FlightSim_Engine_GENERAL_ENG_MASTER_ALTERNATOR:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GENERAL ENG MASTER ALTERNATOR,{unit.value})")


# Maximum attained rpm for the indexed engine (see note).
class _FlightSim_Engine_GENERAL_ENG_MAX_REACHED_RPM:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.AngularVelocity.REVOLUTION_PER_MINUTE'):
        return self._.get(f"(A:GENERAL ENG MAX REACHED RPM:{self._index},{unit.value})")


# Percent of max mixture lever position for the indexed engine (see note).
class _FlightSim_Engine_GENERAL_ENG_MIXTURE_LEVER_POSITION:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:GENERAL ENG MIXTURE LEVER POSITION:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT', value: str):
        self._.set(f"{value} (>A:GENERAL ENG MIXTURE LEVER POSITION:{self._index},{unit.value})")


# Percent of max oil capacity leaked for the indexed engine (see note).
class _FlightSim_Engine_GENERAL_ENG_OIL_LEAKED_PERCENT:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:GENERAL ENG OIL LEAKED PERCENT:{self._index},{unit.value})")


# The indexed engine (see note) oil pressure.
class _FlightSim_Engine_GENERAL_ENG_OIL_PRESSURE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Pressure.POUND_FORCE_PER_SQUARE_FOOT'):
        return self._.get(f"(A:GENERAL ENG OIL PRESSURE:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Pressure.POUND_FORCE_PER_SQUARE_FOOT', value: str):
        self._.set(f"{value} (>A:GENERAL ENG OIL PRESSURE:{self._index},{unit.value})")


# The indexed engine (see note) oil temperature.
class _FlightSim_Engine_GENERAL_ENG_OIL_TEMPERATURE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Temperature.RANKINE'):
        return self._.get(f"(A:GENERAL ENG OIL TEMPERATURE:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Temperature.RANKINE', value: str):
        self._.set(f"{value} (>A:GENERAL ENG OIL TEMPERATURE:{self._index},{unit.value})")


# Percent of max rated rpm for the indexed engine (see note).
# NOTE: This is available in multiplayer to all far aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_Engine_GENERAL_ENG_PCT_MAX_RPM:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:GENERAL ENG PCT MAX RPM:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT', value: str):
        self._.set(f"{value} (>A:GENERAL ENG PCT MAX RPM:{self._index},{unit.value})")


# Percent of max prop lever position for the indexed engine (see note).
class _FlightSim_Engine_GENERAL_ENG_PROPELLER_LEVER_POSITION:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:GENERAL ENG PROPELLER LEVER POSITION:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT', value: str):
        self._.set(f"{value} (>A:GENERAL ENG PROPELLER LEVER POSITION:{self._index},{unit.value})")


# This will return 1 (TRUE) if the reverse thruster is engaged, or 0 (FALSE) otherwise.
class _FlightSim_Engine_GENERAL_ENG_REVERSE_THRUST_ENGAGED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GENERAL ENG REVERSE THRUST ENGAGED,{unit.value})")


# The RPM for an indexed engine (see note).
# NOTE: This is available in multiplayer to all far aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_Engine_GENERAL_ENG_RPM:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.AngularVelocity.REVOLUTION_PER_MINUTE'):
        return self._.get(f"(A:GENERAL ENG RPM:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.AngularVelocity.REVOLUTION_PER_MINUTE', value: str):
        self._.set(f"{value} (>A:GENERAL ENG RPM:{self._index},{unit.value})")


# The indexed engine (see note) starter on/off state.
class _FlightSim_Engine_GENERAL_ENG_STARTER:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GENERAL ENG STARTER:{self._index},{unit.value})")


# True if the indexed engine (see note) starter is active.
# NOTE: This is available in multiplayer to all near aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_Engine_GENERAL_ENG_STARTER_ACTIVE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GENERAL ENG STARTER ACTIVE:{self._index},{unit.value})")


# Percent of max throttle position for the indexed engine (see note).
class _FlightSim_Engine_GENERAL_ENG_THROTTLE_LEVER_POSITION:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:GENERAL ENG THROTTLE LEVER POSITION:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT', value: str):
        self._.set(f"{value} (>A:GENERAL ENG THROTTLE LEVER POSITION:{self._index},{unit.value})")


# Current mode of the managed throttle for the indexed engine (see note).
class _FlightSim_Engine_GENERAL_ENG_THROTTLE_MANAGED_MODE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:GENERAL ENG THROTTLE MANAGED MODE:{self._index},{unit.value})")


# Aircraft master ignition switch (grounds all engines magnetos).
class _FlightSim_Engine_MASTER_IGNITION_SWITCH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:MASTER IGNITION SWITCH,{unit.value})")


# The maximum EGT, as set using the egt_peak_temperature parameter in the engines.cfg file.
class _FlightSim_Engine_MAX_EGT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Temperature.RANKINE'):
        return self._.get(f"(A:MAX EGT,{unit.value})")


# The maximum oil temperature, as set using the parameter oil_temp_heating_constant in the engines.cfg file.
class _FlightSim_Engine_MAX_OIL_TEMPERATURE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Temperature.RANKINE'):
        return self._.get(f"(A:MAX OIL TEMPERATURE,{unit.value})")


# Maximum rated rpm for the indexed engine (see note).
class _FlightSim_Engine_MAX_RATED_ENGINE_RPM:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.AngularVelocity.REVOLUTION_PER_MINUTE'):
        return self._.get(f"(A:MAX RATED ENGINE RPM,{unit.value})")


# Number of engines (minimum 0, maximum 4)
class _FlightSim_Engine_NUMBER_OF_ENGINES:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:NUMBER OF ENGINES,{unit.value})")


# Deprecated, do not use!
class _FlightSim_Engine_OIL_AMOUNT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Volume.FS7_OIL_QUANTITY'):
        # unit: FS7 Oil Quantity (Deprecated)
        return self._.get(f"(A:OIL AMOUNT,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Volume.FS7_OIL_QUANTITY', value: str):
        # unit: FS7 Oil Quantity (Deprecated)
        self._.set(f"{value} (>A:OIL AMOUNT,{unit.value})")


# Auto-feather arming switch for the indexed engine (see note). Please see the Note On Autofeathering for more information.
class _FlightSim_Engine_PANEL_AUTO_FEATHER_SWITCH:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:PANEL AUTO FEATHER SWITCH:{self._index},{unit.value})")


# True if prop auto cruise active
class _FlightSim_Engine_PROP_AUTO_CRUISE_ACTIVE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:PROP AUTO CRUISE ACTIVE,{unit.value})")


# Auto-feather armed state for the indexed engine (see note).
class _FlightSim_Engine_PROP_AUTO_FEATHER_ARMED:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:PROP AUTO FEATHER ARMED:{self._index},{unit.value})")


# The "prop beta" is the pitch of the blades of the propeller, and this can be used to retrieve the current pitch setting, per indexed engine (see note).
class _FlightSim_Engine_PROP_BETA:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:PROP BETA:{self._index},{unit.value})")


# This can be used to enable the propeller forced beta mode (1, TRUE) or disable it (0, FALSE), when being written to. When being read from, it will return TRUE (1) if the forced beta mode is enabled or FALSE (0) if it isn't. When enabled, the PROP BETA FORCED POSITION value will be used to drive the prop beta, while the internal coded simulation logic is used when this is disabled.
class _FlightSim_Engine_PROP_BETA_FORCED_ACTIVE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:PROP BETA FORCED ACTIVE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:PROP BETA FORCED ACTIVE,{unit.value})")


# Get or set the beta at which the prop is forced. Only valid when PROP BETA FORCED ACTIVE is TRUE (1).
class _FlightSim_Engine_PROP_BETA_FORCED_POSITION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:PROP BETA FORCED POSITION,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Angle.RADIAN', value: str):
        self._.set(f"{value} (>A:PROP BETA FORCED POSITION,{unit.value})")


# The "prop beta" is the pitch of the blades of the propeller. This retrieves the maximum possible pitch value for all engines.
class _FlightSim_Engine_PROP_BETA_MAX:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:PROP BETA MAX,{unit.value})")


# The "prop beta" is the pitch of the blades of the propeller. This retrieves the minimum possible pitch value for all engines.
class _FlightSim_Engine_PROP_BETA_MIN:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:PROP BETA MIN,{unit.value})")


# The "prop beta" is the pitch of the blades of the propeller. This retrieves the minimum possible pitch value when the propeller is in reverse for all engines.
class _FlightSim_Engine_PROP_BETA_MIN_REVERSE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:PROP BETA MIN REVERSE,{unit.value})")


# True if prop deice switch on for the indexed engine (see note).
class _FlightSim_Engine_PROP_DEICE_SWITCH:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:PROP DEICE SWITCH:{self._index},{unit.value})")


# This will return the feathered state of the propeller for an indexed engine (see note). The state is either feathered (true) or not (false).
class _FlightSim_Engine_PROP_FEATHERED:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:PROP FEATHERED:{self._index},{unit.value})")


# Feathering inhibit flag for the indexed engine (see note).
class _FlightSim_Engine_PROP_FEATHERING_INHIBIT:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:PROP FEATHERING INHIBIT:{self._index},{unit.value})")


# Prop feather switch for the indexed engine (see note).
class _FlightSim_Engine_PROP_FEATHER_SWITCH:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:PROP FEATHER SWITCH:{self._index},{unit.value})")


# Percent of max rated rpm for the indexed engine (see note).
# NOTE: This is available in multiplayer to all near aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_Engine_PROP_MAX_RPM_PERCENT:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:PROP MAX RPM PERCENT:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT', value: str):
        self._.set(f"{value} (>A:PROP MAX RPM PERCENT:{self._index},{unit.value})")


# Prop rotation angle.
# NOTE: This is available in multiplayer to all near aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_Engine_PROP_ROTATION_ANGLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:PROP ROTATION ANGLE,{unit.value})")


# Propeller rpm for the indexed engine (see note).
class _FlightSim_Engine_PROP_RPM:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.AngularVelocity.REVOLUTION_PER_MINUTE'):
        return self._.get(f"(A:PROP RPM:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.AngularVelocity.REVOLUTION_PER_MINUTE', value: str):
        self._.set(f"{value} (>A:PROP RPM:{self._index},{unit.value})")


# True if prop sync is active the indexed engine (see note).
class _FlightSim_Engine_PROP_SYNC_ACTIVE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:PROP SYNC ACTIVE:{self._index},{unit.value})")


# Corrected prop correction input on slaved engine for the indexed engine (see note).
class _FlightSim_Engine_PROP_SYNC_DELTA_LEVER:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION'):
        return self._.get(f"(A:PROP SYNC DELTA LEVER:{self._index},{unit.value})")


# Propeller thrust for the indexed engine (see note).
# NOTE: This is available in multiplayer to all near aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_Engine_PROP_THRUST:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Weight.POUND'):
        return self._.get(f"(A:PROP THRUST:{self._index},{unit.value})")


# Deprecated, do not use!
class _FlightSim_Engine_PROPELLER_ADVANCED_SELECTION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:PROPELLER ADVANCED SELECTION,{unit.value})")


# This checks if the shutoff valve to the engine has been pulled (true) or not (false). When pulled piston engines will be blocked from getting any fuel.
class _FlightSim_Engine_SHUTOFF_VALVE_PULLED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:SHUTOFF VALVE PULLED,{unit.value})")


# Percent throttle defining lower limit (negative for reverse thrust equipped airplanes).
class _FlightSim_Engine_THROTTLE_LOWER_LIMIT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:THROTTLE LOWER LIMIT,{unit.value})")


# Afterburner state for the indexed engine (see note).
# NOTE: This is available in multiplayer to all near aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_Engine_TURB_ENG_AFTERBURNER:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:TURB ENG AFTERBURNER:{self._index},{unit.value})")


# The percentage that the afterburner is running at.
# NOTE: This is available in multiplayer to all near aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_Engine_TURB_ENG_AFTERBURNER_PCT_ACTIVE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:TURB ENG AFTERBURNER PCT ACTIVE:{self._index},{unit.value})")


# The stage of the afterburner, or 0 if the afterburner is not active.
# NOTE: This is available in multiplayer to all near aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_Engine_TURB_ENG_AFTERBURNER_STAGE_ACTIVE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:TURB ENG AFTERBURNER STAGE ACTIVE:{self._index},{unit.value})")


# Bleed air pressure for the indexed engine (see note).
class _FlightSim_Engine_TURB_ENG_BLEED_AIR:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Pressure.POUND_FORCE_PER_SQUARE_INCH'):
        return self._.get(f"(A:TURB ENG BLEED AIR:{self._index},{unit.value})")


# Effective commanded N1 for the indexed turbine engine (see note).
class _FlightSim_Engine_TURB_ENG_COMMANDED_N1:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:TURB ENG COMMANDED N1:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT', value: str):
        self._.set(f"{value} (>A:TURB ENG COMMANDED N1:{self._index},{unit.value})")


# When the throttle is on idle position, this sets the condition levers to one of 3 positions to define the idle N1 target for the indexed engine (see note):
# Note that this option requires several settings from the engines.cfg file to be set to specific values before working correctly:
class _FlightSim_Engine_TURB_ENG_CONDITION_LEVER_POSITION:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    class Unit(Enum):
        FUEL_CUT_OFF = 0
        LOW_IDLE = 1
        HIGH_IDLE = 2

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:TURB ENG CONDITION LEVER POSITION:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM', value: str):
        self._.set(f"{value} (>A:TURB ENG CONDITION LEVER POSITION:{self._index},{unit.value})")


# Corrected fuel flow for the indexed engine (see note).
class _FlightSim_Engine_TURB_ENG_CORRECTED_FF:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.POUND_PER_HOUR'):
        return self._.get(f"(A:TURB ENG CORRECTED FF:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.POUND_PER_HOUR', value: str):
        self._.set(f"{value} (>A:TURB ENG CORRECTED FF:{self._index},{unit.value})")


# The indexed turbine engine (see note) corrected N1.
class _FlightSim_Engine_TURB_ENG_CORRECTED_N1:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:TURB ENG CORRECTED N1:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT', value: str):
        self._.set(f"{value} (>A:TURB ENG CORRECTED N1:{self._index},{unit.value})")


# The indexed turbine engine (see note) corrected N2.
class _FlightSim_Engine_TURB_ENG_CORRECTED_N2:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:TURB ENG CORRECTED N2:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT', value: str):
        self._.set(f"{value} (>A:TURB ENG CORRECTED N2:{self._index},{unit.value})")


# The amount of free torque for the indexed turbine engine (see note).
class _FlightSim_Engine_TURB_ENG_FREE_TURBINE_TORQUE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Torque.FOOT_POUND'):
        return self._.get(f"(A:TURB ENG FREE TURBINE TORQUE:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Torque.FOOT_POUND', value: str):
        self._.set(f"{value} (>A:TURB ENG FREE TURBINE TORQUE:{self._index},{unit.value})")


# True if fuel is available for the indexed engine (see note).
class _FlightSim_Engine_TURB_ENG_FUEL_AVAILABLE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:TURB ENG FUEL AVAILABLE:{self._index},{unit.value})")


# This is used to control the fuel efficiency loss of the indexed engine, from 0 - no fuel efficiency loss - to 100 - double the fuel consumption.
class _FlightSim_Engine_TURB_ENG_FUEL_EFFICIENCY_LOSS:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:TURB ENG FUEL EFFICIENCY LOSS:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT', value: str):
        self._.set(f"{value} (>A:TURB ENG FUEL EFFICIENCY LOSS:{self._index},{unit.value})")


# The indexed engine (see note) fuel flow rate.
class _FlightSim_Engine_TURB_ENG_FUEL_FLOW_PPH:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.POUND_PER_HOUR'):
        return self._.get(f"(A:TURB ENG FUEL FLOW PPH:{self._index},{unit.value})")


# Retrieves the high idle N1 value to be reached by the the indexed turboprop engine (see note) with throttle in idle position and condition lever in high idle position (condition lever position can be checked or set using the TURB_ENG_CONDITION_LEVER_POSITION SimVar).
class _FlightSim_Engine_TURB_ENG_HIGH_IDLE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:TURB ENG HIGH IDLE:{self._index},{unit.value})")


# True if the the indexed turbine engine (see note) ignition switch is on.
class _FlightSim_Engine_TURB_ENG_IGNITION_SWITCH:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:TURB ENG IGNITION SWITCH:{self._index},{unit.value})")


# Position of the the indexed turbine engine (see note) Ignition Switch. Similar to TURB_ENG_IGNITION_SWITCH but differentiates between ON and AUTO.
class _FlightSim_Engine_TURB_ENG_IGNITION_SWITCH_EX1:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    class Unit(Enum):
        OFF = 0
        AUTO = 1
        ON = 2

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:TURB ENG IGNITION SWITCH EX1:{self._index},{unit.value})")


# Whether or not the ignition system is currently running for the indexed engine (see note). Depends on TURB_ENG_IGNITION_SWITCH_EX1 Enum, the cfg var ignition_auto_type and current state of the plane.
class _FlightSim_Engine_TURB_ENG_IS_IGNITING:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:TURB ENG IS IGNITING:{self._index},{unit.value})")


# Retrieve or set the ITT for the indexed engine (see note).
class _FlightSim_Engine_TURB_ENG_ITT:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Temperature.RANKINE'):
        return self._.get(f"(A:TURB ENG ITT:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Temperature.RANKINE', value: str):
        self._.set(f"{value} (>A:TURB ENG ITT:{self._index},{unit.value})")


# This is used to control the ITT cooling efficiency loss of the indexed engine, from 0 - no cooling efficiency loss - to 100 -engine recieves no ITT cooling.
class _FlightSim_Engine_TURB_ENG_ITT_COOLING_EFFICIENCY_LOSS:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:TURB ENG ITT COOLING EFFICIENCY LOSS:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT', value: str):
        self._.set(f"{value} (>A:TURB ENG ITT COOLING EFFICIENCY LOSS:{self._index},{unit.value})")


# The indexed engine (see note) jet thrust.
class _FlightSim_Engine_TURB_ENG_JET_THRUST:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Weight.POUND'):
        return self._.get(f"(A:TURB ENG JET THRUST:{self._index},{unit.value})")


# Retrieves the low idle N1 value to be reached by the the indexed turboprop engine (see note) with throttle in idle position and condition lever in low idle position (condition lever position can be checked or set using the TURB_ENG_CONDITION_LEVER_POSITION SimVar).
class _FlightSim_Engine_TURB_ENG_LOW_IDLE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:TURB ENG LOW IDLE:{self._index},{unit.value})")


# True if the turbine engine master starter switch is on, false otherwise.
class _FlightSim_Engine_TURB_ENG_MASTER_STARTER_SWITCH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:TURB ENG MASTER STARTER SWITCH,{unit.value})")


# Percent of max rated torque for the indexed engine (see note).
class _FlightSim_Engine_TURB_ENG_MAX_TORQUE_PERCENT:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:TURB ENG MAX TORQUE PERCENT:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT', value: str):
        self._.set(f"{value} (>A:TURB ENG MAX TORQUE PERCENT:{self._index},{unit.value})")


# The indexed turbine engine (see note) N1 value.
# NOTE: This is available in multiplayer to all far aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_Engine_TURB_ENG_N1:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:TURB ENG N1:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT', value: str):
        self._.set(f"{value} (>A:TURB ENG N1:{self._index},{unit.value})")


# This is used to control the N1 loss of the indexed engine, from 0 - no N1 loss - to 100 - 100% N1 loss.
class _FlightSim_Engine_TURB_ENG_N1_LOSS:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:TURB ENG N1 LOSS:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT', value: str):
        self._.set(f"{value} (>A:TURB ENG N1 LOSS:{self._index},{unit.value})")


# The indexed turbine engine (see note) N2 value.
# NOTE: This is available in multiplayer to all far aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_Engine_TURB_ENG_N2:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:TURB ENG N2:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT', value: str):
        self._.set(f"{value} (>A:TURB ENG N2:{self._index},{unit.value})")


# Number of tanks currently being used by the indexed engine (see note).
class _FlightSim_Engine_TURB_ENG_NUM_TANKS_USED:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:TURB ENG NUM TANKS USED:{self._index},{unit.value})")


# The indexed engine (see note) pressure ratio.
class _FlightSim_Engine_TURB_ENG_PRESSURE_RATIO:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.RATIO'):
        return self._.get(f"(A:TURB ENG PRESSURE RATIO:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.RATIO', value: str):
        self._.set(f"{value} (>A:TURB ENG PRESSURE RATIO:{self._index},{unit.value})")


# Percent thrust of primary nozzle for the indexed engine (see note).
class _FlightSim_Engine_TURB_ENG_PRIMARY_NOZZLE_PERCENT:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:TURB ENG PRIMARY NOZZLE PERCENT:{self._index},{unit.value})")


# Percent thrust reverser nozzles deployed for the indexed engine (see note).
# NOTE: This is available in multiplayer to all far aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_Engine_TURB_ENG_REVERSE_NOZZLE_PERCENT:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:TURB ENG REVERSE NOZZLE PERCENT:{self._index},{unit.value})")


# Fuel tanks used by the indexed engine (see note), one or more of the following bit flags: Center 1 Bit 0 Center 2 Bit 1 Center 3 Bit 2 Left Main Bit 3 Left Aux Bit 4 Left Tip Bit 5 Right Main Bit 6 Right Aux Bit 7 Right Tip Bit 8 External 1 Bit 9 External 2 Bit 10
class _FlightSim_Engine_TURB_ENG_TANKS_USED:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.MASK'):
        return self._.get(f"(A:TURB ENG TANKS USED:{self._index},{unit.value})")


# Fuel tank selected for the indexed engine (see note). See Fuel Tank Selection for a list of values.
class _FlightSim_Engine_TURB_ENG_TANK_SELECTOR:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:TURB ENG TANK SELECTOR:{self._index},{unit.value})")


# The indexed turbine engine (see note) commanded N1 for current throttle position.
class _FlightSim_Engine_TURB_ENG_THROTTLE_COMMANDED_N1:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:TURB ENG THROTTLE COMMANDED N1:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT', value: str):
        self._.set(f"{value} (>A:TURB ENG THROTTLE COMMANDED N1:{self._index},{unit.value})")


# This can be used to control the thrust efficiency loss of the indexed engine, where a value of 0 is 100% of available thrust, and 100 is 0% available thrust.
class _FlightSim_Engine_TURB_ENG_THRUST_EFFICIENCY_LOSS:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:TURB ENG THRUST EFFICIENCY LOSS:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT', value: str):
        self._.set(f"{value} (>A:TURB ENG THRUST EFFICIENCY LOSS:{self._index},{unit.value})")


# The indexed turbine engine (see note) vibration value.
class _FlightSim_Engine_TURB_ENG_VIBRATION:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:TURB ENG VIBRATION:{self._index},{unit.value})")


# Retrieve the itt_peak_temperature as set in the engines.cfg file.
class _FlightSim_Engine_TURB_MAX_ITT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Temperature.RANKINE'):
        return self._.get(f"(A:TURB MAX ITT,{unit.value})")


# Carburetor temperature the indexed engine (see note).
class _FlightSim_Engine_RECIP_CARBURETOR_TEMPERATURE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Temperature.CELSIUS'):
        return self._.get(f"(A:RECIP CARBURETOR TEMPERATURE:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Temperature.CELSIUS', value: str):
        self._.set(f"{value} (>A:RECIP CARBURETOR TEMPERATURE:{self._index},{unit.value})")


# Alternate air control the indexed engine (see note).
class _FlightSim_Engine_RECIP_ENG_ALTERNATE_AIR_POSITION:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION'):
        return self._.get(f"(A:RECIP ENG ALTERNATE AIR POSITION:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION', value: str):
        self._.set(f"{value} (>A:RECIP ENG ALTERNATE AIR POSITION:{self._index},{unit.value})")


# The maximum quantity of water/methanol mixture in the ADI tank for the indexed engine (see note). This value is set as part of the [ANTIDETONATION_SYSTEM.N] section in the aircraft configuration files.
class _FlightSim_Engine_RECIP_ENG_ANTIDETONATION_TANK_MAX_QUANTITY:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Volume.GALLON'):
        return self._.get(f"(A:RECIP ENG ANTIDETONATION TANK MAX QUANTITY:{self._index},{unit.value})")


# The quantity of water/methanol mixture currently in the ADI tank for the indexed engine (see note).
class _FlightSim_Engine_RECIP_ENG_ANTIDETONATION_TANK_QUANTITY:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Volume.GALLON'):
        return self._.get(f"(A:RECIP ENG ANTIDETONATION TANK QUANTITY:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Volume.GALLON', value: str):
        self._.set(f"{value} (>A:RECIP ENG ANTIDETONATION TANK QUANTITY:{self._index},{unit.value})")


# The status of the ADI tank valve for the indexed engine (see note).
class _FlightSim_Engine_RECIP_ENG_ANTIDETONATION_TANK_VALVE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:RECIP ENG ANTIDETONATION TANK VALVE:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:RECIP ENG ANTIDETONATION TANK VALVE:{self._index},{unit.value})")


# This gives the actual flow rate of the Anti Detonation system for the indexed engine (see note).
class _FlightSim_Engine_RECIP_ENG_ANTIDETONATION_FLOW_RATE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.VolumeRate.GALLON_PER_HOUR'):
        return self._.get(f"(A:RECIP ENG ANTIDETONATION FLOW RATE:{self._index},{unit.value})")


# Brake power produced by the indexed engine (see note).
class _FlightSim_Engine_RECIP_ENG_BRAKE_POWER:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Power.FOOT_POUND_PER_SECOND'):
        return self._.get(f"(A:RECIP ENG BRAKE POWER:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Power.FOOT_POUND_PER_SECOND', value: str):
        self._.set(f"{value} (>A:RECIP ENG BRAKE POWER:{self._index},{unit.value})")


# Percent coolant available for the indexed engine (see note).
class _FlightSim_Engine_RECIP_ENG_COOLANT_RESERVOIR_PERCENT:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:RECIP ENG COOLANT RESERVOIR PERCENT:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT', value: str):
        self._.set(f"{value} (>A:RECIP ENG COOLANT RESERVOIR PERCENT:{self._index},{unit.value})")


# Percent cowl flap opened for the indexed engine (see note).
class _FlightSim_Engine_RECIP_ENG_COWL_FLAP_POSITION:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:RECIP ENG COWL FLAP POSITION:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT', value: str):
        self._.set(f"{value} (>A:RECIP ENG COWL FLAP POSITION:{self._index},{unit.value})")


# Engine cylinder head temperature for the indexed engine (see note).
class _FlightSim_Engine_RECIP_ENG_CYLINDER_HEAD_TEMPERATURE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Temperature.CELSIUS'):
        return self._.get(f"(A:RECIP ENG CYLINDER HEAD TEMPERATURE:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Temperature.CELSIUS', value: str):
        self._.set(f"{value} (>A:RECIP ENG CYLINDER HEAD TEMPERATURE:{self._index},{unit.value})")


# Index high 16 bits is engine number, low16 cylinder number, both indexed from 1.
class _FlightSim_Engine_RECIP_ENG_CYLINDER_HEALTH:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:RECIP ENG CYLINDER HEALTH:{self._index},{unit.value})")


# Set to 1 (TRUE) if the indexed engine (see note) is detonating.
class _FlightSim_Engine_RECIP_ENG_DETONATING:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:RECIP ENG DETONATING:{self._index},{unit.value})")


# Whether emergency boost is active (1, TRUE) or not (0, FALSE) for the indexed engine (see note).
class _FlightSim_Engine_RECIP_ENG_EMERGENCY_BOOST_ACTIVE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:RECIP ENG EMERGENCY BOOST ACTIVE:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:RECIP ENG EMERGENCY BOOST ACTIVE:{self._index},{unit.value})")


# The elapsed time that emergency boost has been active on the indexed engine (see note). The timer will start when boost is first activated.
# IMPORTANT! This timer does not reset. So if you set your time limit in the engines.cfg file to 315s and you spend 2 minutes with boost active, then pull back on the throttle for 1 minute, then engage boost again for 2 minutes, the simulation will consider that you spent 4 minutes with boost active. The 1 minute pause is not taken into account.
class _FlightSim_Engine_RECIP_ENG_EMERGENCY_BOOST_ELAPSED_TIME:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Time.HOUR'):
        return self._.get(f"(A:RECIP ENG EMERGENCY BOOST ELAPSED TIME:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Time.HOUR', value: str):
        self._.set(f"{value} (>A:RECIP ENG EMERGENCY BOOST ELAPSED TIME:{self._index},{unit.value})")


# Whether or not the Engine Master switch is active on an indexed engine (see note).
class _FlightSim_Engine_RECIP_ENG_ENGINE_MASTER_SWITCH:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:RECIP ENG ENGINE MASTER SWITCH:{self._index},{unit.value})")


# True if fuel is available for the indexed engine (see note).
class _FlightSim_Engine_RECIP_ENG_FUEL_AVAILABLE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:RECIP ENG FUEL AVAILABLE:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:RECIP ENG FUEL AVAILABLE:{self._index},{unit.value})")


# The indexed engine (see note) fuel flow.
class _FlightSim_Engine_RECIP_ENG_FUEL_FLOW:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.POUND_PER_HOUR'):
        return self._.get(f"(A:RECIP ENG FUEL FLOW:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.POUND_PER_HOUR', value: str):
        self._.set(f"{value} (>A:RECIP ENG FUEL FLOW:{self._index},{unit.value})")


# Number of tanks currently being used by the indexed engine (see note).
class _FlightSim_Engine_RECIP_ENG_FUEL_NUMBER_TANKS_USED:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:RECIP ENG FUEL NUMBER TANKS USED:{self._index},{unit.value})")


# Fuel tanks used by the indexed engine (see note), one or more of the following bit flags: Center 1 Bit 0 Center 2 Bit 1 Center 3 Bit 2 Left Main Bit 3 Left Aux Bit 4 Left Tip Bit 5 Right Main Bit 6 Right Aux Bit 7 Right Tip Bit 8 External 1 Bit 9 External 2 Bit 10
class _FlightSim_Engine_RECIP_ENG_FUEL_TANKS_USED:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.MASK'):
        return self._.get(f"(A:RECIP ENG FUEL TANKS USED:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.MASK', value: str):
        self._.set(f"{value} (>A:RECIP ENG FUEL TANKS USED:{self._index},{unit.value})")


# Fuel tank selected for the indexed engine (see note). See Fuel Tank Selection for a list of values.
class _FlightSim_Engine_RECIP_ENG_FUEL_TANK_SELECTOR:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:RECIP ENG FUEL TANK SELECTOR:{self._index},{unit.value})")


# Whether or not the Glow Plug is active on the indexed engine (see note)..
class _FlightSim_Engine_RECIP_ENG_GLOW_PLUG_ACTIVE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:RECIP ENG GLOW PLUG ACTIVE:{self._index},{unit.value})")


# Left magneto state for the indexed engine (see note).
class _FlightSim_Engine_RECIP_ENG_LEFT_MAGNETO:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:RECIP ENG LEFT MAGNETO:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:RECIP ENG LEFT MAGNETO:{self._index},{unit.value})")


# The indexed engine (see note) manifold pressure.
class _FlightSim_Engine_RECIP_ENG_MANIFOLD_PRESSURE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Pressure.POUND_FORCE_PER_SQUARE_INCH'):
        return self._.get(f"(A:RECIP ENG MANIFOLD PRESSURE:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Pressure.POUND_FORCE_PER_SQUARE_INCH', value: str):
        self._.set(f"{value} (>A:RECIP ENG MANIFOLD PRESSURE:{self._index},{unit.value})")


# The maximum quantity of nitrous permitted per indexed engine (see note).
class _FlightSim_Engine_RECIP_ENG_NITROUS_TANK_MAX_QUANTITY:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Volume.GALLON'):
        return self._.get(f"(A:RECIP ENG NITROUS TANK MAX QUANTITY:{self._index},{unit.value})")


# The quantity of nitrous per indexed engine (see note).
class _FlightSim_Engine_RECIP_ENG_NITROUS_TANK_QUANTITY:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Volume.GALLON'):
        return self._.get(f"(A:RECIP ENG NITROUS TANK QUANTITY:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Volume.GALLON', value: str):
        self._.set(f"{value} (>A:RECIP ENG NITROUS TANK QUANTITY:{self._index},{unit.value})")


# The statte of the nitrous tank valve for the indexed engine (see note). Either 1 (TRUE) for open or 0 (FALSE) for closed.
class _FlightSim_Engine_RECIP_ENG_NITROUS_TANK_VALVE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:RECIP ENG NITROUS TANK VALVE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:RECIP ENG NITROUS TANK VALVE,{unit.value})")


# The number of cylinders for the indexed engine (see note).
class _FlightSim_Engine_RECIP_ENG_NUM_CYLINDERS:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:RECIP ENG NUM CYLINDERS:{self._index},{unit.value})")


# The number of cylinders that have failed in the indexed engine (see note).
class _FlightSim_Engine_RECIP_ENG_NUM_CYLINDERS_FAILED:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:RECIP ENG NUM CYLINDERS FAILED:{self._index},{unit.value})")


# The indexed engine (see note) primer state.
class _FlightSim_Engine_RECIP_ENG_PRIMER:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:RECIP ENG PRIMER:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:RECIP ENG PRIMER:{self._index},{unit.value})")


# The indexed engine (see note) radiator temperature.
class _FlightSim_Engine_RECIP_ENG_RADIATOR_TEMPERATURE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Temperature.CELSIUS'):
        return self._.get(f"(A:RECIP ENG RADIATOR TEMPERATURE:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Temperature.CELSIUS', value: str):
        self._.set(f"{value} (>A:RECIP ENG RADIATOR TEMPERATURE:{self._index},{unit.value})")


# The indexed engine (see note) right magneto state.
class _FlightSim_Engine_RECIP_ENG_RIGHT_MAGNETO:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:RECIP ENG RIGHT MAGNETO:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:RECIP ENG RIGHT MAGNETO:{self._index},{unit.value})")


# Torque produced by the indexed engine (see note).
class _FlightSim_Engine_RECIP_ENG_STARTER_TORQUE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Torque.FOOT_POUND'):
        return self._.get(f"(A:RECIP ENG STARTER TORQUE:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Torque.FOOT_POUND', value: str):
        self._.set(f"{value} (>A:RECIP ENG STARTER TORQUE:{self._index},{unit.value})")


# Returns which of the supercharger gears is engaged for the indexed engine (see note).
class _FlightSim_Engine_RECIP_ENG_SUPERCHARGER_ACTIVE_GEAR:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:RECIP ENG SUPERCHARGER ACTIVE GEAR:{self._index},{unit.value})")


# The indexed engine (see note) turbine inlet temperature.
class _FlightSim_Engine_RECIP_ENG_TURBINE_INLET_TEMPERATURE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Temperature.CELSIUS'):
        return self._.get(f"(A:RECIP ENG TURBINE INLET TEMPERATURE:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Temperature.CELSIUS', value: str):
        self._.set(f"{value} (>A:RECIP ENG TURBINE INLET TEMPERATURE:{self._index},{unit.value})")


# The indexed engine (see note) turbo failed state.
class _FlightSim_Engine_RECIP_ENG_TURBOCHARGER_FAILED:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:RECIP ENG TURBOCHARGER FAILED:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:RECIP ENG TURBOCHARGER FAILED:{self._index},{unit.value})")


# When the engines.cfg parameter turbocharged is TRUE, this SimVar will return the percentage that the turbo waste gate is closed for the indexed engine (see note). If the turbocharged variable is FALSE and the manifold_pressure_regulator parameter is TRUE, then this will return the percentage that the manifold pressure regulator is closed for the indexed engine.
class _FlightSim_Engine_RECIP_ENG_WASTEGATE_POSITION:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:RECIP ENG WASTEGATE POSITION:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT', value: str):
        self._.set(f"{value} (>A:RECIP ENG WASTEGATE POSITION:{self._index},{unit.value})")


# This will return the cylinder head temperature value set by the cht_heating_constant parameter in the engines.cfg file.
class _FlightSim_Engine_RECIP_MAX_CHT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Temperature.RANKINE'):
        return self._.get(f"(A:RECIP MAX CHT,{unit.value})")


# Fuel / Air mixture ratio for the indexed engine (see note).
class _FlightSim_Engine_RECIP_MIXTURE_RATIO:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.RATIO'):
        return self._.get(f"(A:RECIP MIXTURE RATIO:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.RATIO', value: str):
        self._.set(f"{value} (>A:RECIP MIXTURE RATIO:{self._index},{unit.value})")


class _FlightSim_FlightModel:
    def __init__(self, flightSim):
        self._ = flightSim
        self.BETA_DOT = _FlightSim_FlightModel_BETA_DOT(flightSim)
        self.DECISION_ALTITUDE_MSL = _FlightSim_FlightModel_DECISION_ALTITUDE_MSL(flightSim)
        self.DECISION_HEIGHT = _FlightSim_FlightModel_DECISION_HEIGHT(flightSim)
        self.DESIGN_CRUISE_ALT = _FlightSim_FlightModel_DESIGN_CRUISE_ALT(flightSim)
        self.DESIGN_SPAWN_ALTITUDE_CRUISE = _FlightSim_FlightModel_DESIGN_SPAWN_ALTITUDE_CRUISE(flightSim)
        self.DESIGN_SPAWN_ALTITUDE_DESCENT = _FlightSim_FlightModel_DESIGN_SPAWN_ALTITUDE_DESCENT(flightSim)
        self.DESIGN_SPEED_CLIMB = _FlightSim_FlightModel_DESIGN_SPEED_CLIMB(flightSim)
        self.DESIGN_SPEED_MIN_ROTATION = _FlightSim_FlightModel_DESIGN_SPEED_MIN_ROTATION(flightSim)
        self.DESIGN_SPEED_VC = _FlightSim_FlightModel_DESIGN_SPEED_VC(flightSim)
        self.DESIGN_SPEED_VS0 = _FlightSim_FlightModel_DESIGN_SPEED_VS0(flightSim)
        self.DESIGN_SPEED_VS1 = _FlightSim_FlightModel_DESIGN_SPEED_VS1(flightSim)
        self.DESIGN_TAKEOFF_SPEED = _FlightSim_FlightModel_DESIGN_TAKEOFF_SPEED(flightSim)
        self.DYNAMIC_PRESSURE = _FlightSim_FlightModel_DYNAMIC_PRESSURE(flightSim)
        self.ESTIMATED_CRUISE_SPEED = _FlightSim_FlightModel_ESTIMATED_CRUISE_SPEED(flightSim)
        self.G_FORCE = _FlightSim_FlightModel_G_FORCE(flightSim)
        self.G_LIMITER_SETTING = _FlightSim_FlightModel_G_LIMITER_SETTING(flightSim)
        self.INCIDENCE_ALPHA = _FlightSim_FlightModel_INCIDENCE_ALPHA(flightSim)
        self.INCIDENCE_BETA = _FlightSim_FlightModel_INCIDENCE_BETA(flightSim)
        self.IS_TAIL_DRAGGER = _FlightSim_FlightModel_IS_TAIL_DRAGGER(flightSim)
        self.LINEAR_CL_ALPHA = _FlightSim_FlightModel_LINEAR_CL_ALPHA(flightSim)
        self.MACH_MAX_OPERATE = _FlightSim_FlightModel_MACH_MAX_OPERATE(flightSim)
        self.MAX_G_FORCE = _FlightSim_FlightModel_MAX_G_FORCE(flightSim)
        self.MIN_DRAG_VELOCITY = _FlightSim_FlightModel_MIN_DRAG_VELOCITY(flightSim)
        self.MIN_G_FORCE = _FlightSim_FlightModel_MIN_G_FORCE(flightSim)
        self.SEMIBODY_LOADFACTOR_X = _FlightSim_FlightModel_SEMIBODY_LOADFACTOR_X(flightSim)
        self.SEMIBODY_LOADFACTOR_Y = _FlightSim_FlightModel_SEMIBODY_LOADFACTOR_Y(flightSim)
        self.SEMIBODY_LOADFACTOR_YDOT = _FlightSim_FlightModel_SEMIBODY_LOADFACTOR_YDOT(flightSim)
        self.SEMIBODY_LOADFACTOR_Z = _FlightSim_FlightModel_SEMIBODY_LOADFACTOR_Z(flightSim)
        self.SIGMA_SQRT = _FlightSim_FlightModel_SIGMA_SQRT(flightSim)
        self.SIMULATED_RADIUS = _FlightSim_FlightModel_SIMULATED_RADIUS(flightSim)
        self.STALL_ALPHA = _FlightSim_FlightModel_STALL_ALPHA(flightSim)
        self.STATIC_PITCH = _FlightSim_FlightModel_STATIC_PITCH(flightSim)
        self.TYPICAL_DESCENT_RATE = _FlightSim_FlightModel_TYPICAL_DESCENT_RATE(flightSim)
        self.WING_AREA = _FlightSim_FlightModel_WING_AREA(flightSim)
        self.WING_FLEX_PCT = lambda index: _FlightSim_FlightModel_WING_FLEX_PCT(flightSim, index)
        self.WING_SPAN = _FlightSim_FlightModel_WING_SPAN(flightSim)
        self.YAW_STRING_ANGLE = _FlightSim_FlightModel_YAW_STRING_ANGLE(flightSim)
        self.YAW_STRING_PCT_EXTENDED = _FlightSim_FlightModel_YAW_STRING_PCT_EXTENDED(flightSim)
        self.ZERO_LIFT_ALPHA = _FlightSim_FlightModel_ZERO_LIFT_ALPHA(flightSim)
        self.CG_AFT_LIMIT = _FlightSim_FlightModel_CG_AFT_LIMIT(flightSim)
        self.CG_FEET = _FlightSim_FlightModel_CG_FEET(flightSim)
        self.CG_FEET_AFT_LIMIT = _FlightSim_FlightModel_CG_FEET_AFT_LIMIT(flightSim)
        self.CG_FEET_LATERAL = _FlightSim_FlightModel_CG_FEET_LATERAL(flightSim)
        self.CG_FEET_LATERAL_LEFT_LIMIT = _FlightSim_FlightModel_CG_FEET_LATERAL_LEFT_LIMIT(flightSim)
        self.CG_FEET_LATERAL_RIGHT_LIMIT = _FlightSim_FlightModel_CG_FEET_LATERAL_RIGHT_LIMIT(flightSim)
        self.CG_FEET_FWD_LIMIT = _FlightSim_FlightModel_CG_FEET_FWD_LIMIT(flightSim)
        self.CG_FWD_LIMIT = _FlightSim_FlightModel_CG_FWD_LIMIT(flightSim)
        self.CG_MAX_MACH = _FlightSim_FlightModel_CG_MAX_MACH(flightSim)
        self.CG_MIN_MACH = _FlightSim_FlightModel_CG_MIN_MACH(flightSim)
        self.CG_PERCENT = _FlightSim_FlightModel_CG_PERCENT(flightSim)
        self.CG_PERCENT_LATERAL = _FlightSim_FlightModel_CG_PERCENT_LATERAL(flightSim)
        self.STATIC_CG_TO_GROUND = _FlightSim_FlightModel_STATIC_CG_TO_GROUND(flightSim)
        self.INTERACTIVE_POINT_BANK = _FlightSim_FlightModel_INTERACTIVE_POINT_BANK(flightSim)
        self.INTERACTIVE_POINT_HEADING = _FlightSim_FlightModel_INTERACTIVE_POINT_HEADING(flightSim)
        self.INTERACTIVE_POINT_JETWAY_LEFT_BEND = _FlightSim_FlightModel_INTERACTIVE_POINT_JETWAY_LEFT_BEND(flightSim)
        self.INTERACTIVE_POINT_JETWAY_LEFT_DEPLOYMENT = _FlightSim_FlightModel_INTERACTIVE_POINT_JETWAY_LEFT_DEPLOYMENT(flightSim)
        self.INTERACTIVE_POINT_JETWAY_RIGHT_BEND = _FlightSim_FlightModel_INTERACTIVE_POINT_JETWAY_RIGHT_BEND(flightSim)
        self.INTERACTIVE_POINT_JETWAY_RIGHT_DEPLOYMENT = _FlightSim_FlightModel_INTERACTIVE_POINT_JETWAY_RIGHT_DEPLOYMENT(flightSim)
        self.INTERACTIVE_POINT_JETWAY_TOP_HORIZONTAL = _FlightSim_FlightModel_INTERACTIVE_POINT_JETWAY_TOP_HORIZONTAL(flightSim)
        self.INTERACTIVE_POINT_JETWAY_TOP_VERTICAL = _FlightSim_FlightModel_INTERACTIVE_POINT_JETWAY_TOP_VERTICAL(flightSim)
        self.INTERACTIVE_POINT_GOAL = _FlightSim_FlightModel_INTERACTIVE_POINT_GOAL(flightSim)
        self.INTERACTIVE_POINT_OPEN = _FlightSim_FlightModel_INTERACTIVE_POINT_OPEN(flightSim)
        self.INTERACTIVE_POINT_PITCH = _FlightSim_FlightModel_INTERACTIVE_POINT_PITCH(flightSim)
        self.INTERACTIVE_POINT_POSX = _FlightSim_FlightModel_INTERACTIVE_POINT_POSX(flightSim)
        self.INTERACTIVE_POINT_POSY = _FlightSim_FlightModel_INTERACTIVE_POINT_POSY(flightSim)
        self.INTERACTIVE_POINT_POSZ = _FlightSim_FlightModel_INTERACTIVE_POINT_POSZ(flightSim)
        self.INTERACTIVE_POINT_TYPE = _FlightSim_FlightModel_INTERACTIVE_POINT_TYPE(flightSim)
        self.EMPTY_WEIGHT = _FlightSim_FlightModel_EMPTY_WEIGHT(flightSim)
        self.EMPTY_WEIGHT_CROSS_COUPLED_MOI = _FlightSim_FlightModel_EMPTY_WEIGHT_CROSS_COUPLED_MOI(flightSim)
        self.EMPTY_WEIGHT_PITCH_MOI = _FlightSim_FlightModel_EMPTY_WEIGHT_PITCH_MOI(flightSim)
        self.EMPTY_WEIGHT_ROLL_MOI = _FlightSim_FlightModel_EMPTY_WEIGHT_ROLL_MOI(flightSim)
        self.EMPTY_WEIGHT_YAW_MOI = _FlightSim_FlightModel_EMPTY_WEIGHT_YAW_MOI(flightSim)
        self.MAX_GROSS_WEIGHT = _FlightSim_FlightModel_MAX_GROSS_WEIGHT(flightSim)
        self.TOTAL_WEIGHT = _FlightSim_FlightModel_TOTAL_WEIGHT(flightSim)
        self.TOTAL_WEIGHT_CROSS_COUPLED_MOI = _FlightSim_FlightModel_TOTAL_WEIGHT_CROSS_COUPLED_MOI(flightSim)
        self.TOTAL_WEIGHT_PITCH_MOI = _FlightSim_FlightModel_TOTAL_WEIGHT_PITCH_MOI(flightSim)
        self.TOTAL_WEIGHT_ROLL_MOI = _FlightSim_FlightModel_TOTAL_WEIGHT_ROLL_MOI(flightSim)
        self.TOTAL_WEIGHT_YAW_MOI = _FlightSim_FlightModel_TOTAL_WEIGHT_YAW_MOI(flightSim)


# Beta dot
class _FlightSim_FlightModel_BETA_DOT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.AngularVelocity.RADIAN_PER_SECOND'):
        return self._.get(f"(A:BETA DOT,{unit.value})")


# Design decision altitude above mean sea level
class _FlightSim_FlightModel_DECISION_ALTITUDE_MSL:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.FOOT'):
        return self._.get(f"(A:DECISION ALTITUDE MSL,{unit.value})")


# Design decision height
class _FlightSim_FlightModel_DECISION_HEIGHT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.FOOT'):
        return self._.get(f"(A:DECISION HEIGHT,{unit.value})")


# This design constant represents the optimal altitude the aircraft should maintain when in cruise. It is derived from the cruise_alt setting in the [REFERENCE SPEEDS] section of the flightmodel.cfg. Default is 1500ft.
class _FlightSim_FlightModel_DESIGN_CRUISE_ALT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.FOOT'):
        return self._.get(f"(A:DESIGN CRUISE ALT,{unit.value})")


# This design constant represents the spawn altitude for the aircraft when spawning in cruise. It is derived from the spawn_cruise_altitude setting in the [REFERENCE SPEEDS] section of the flightmodel.cfg. Default is 1500ft.
class _FlightSim_FlightModel_DESIGN_SPAWN_ALTITUDE_CRUISE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.FOOT'):
        return self._.get(f"(A:DESIGN SPAWN ALTITUDE CRUISE,{unit.value})")


# This design constant represents the spawn altitude for the aircraft when spawning in descent. It is derived from the spawn_descent_altitude setting in the [REFERENCE SPEEDS] section of the flightmodel.cfg. Default is 500ft.
class _FlightSim_FlightModel_DESIGN_SPAWN_ALTITUDE_DESCENT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.FOOT'):
        return self._.get(f"(A:DESIGN SPAWN ALTITUDE DESCENT,{unit.value})")


# This design constant represents the optimal climb speed for the aircraft. It is derived from the climb_speed setting in the [REFERENCE SPEEDS] section of the flightmodel.cfg. Default value is -1.
class _FlightSim_FlightModel_DESIGN_SPEED_CLIMB:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.FEET_PER_SECOND'):
        return self._.get(f"(A:DESIGN SPEED CLIMB,{unit.value})")


# This design constant represents the minimum speed required for aircraft rotation. It is derived from the rotation_speed_min setting in the [REFERENCE SPEEDS] section of the flightmodel.cfg. Default value is -1.
class _FlightSim_FlightModel_DESIGN_SPEED_MIN_ROTATION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.FEET_PER_SECOND'):
        return self._.get(f"(A:DESIGN SPEED MIN ROTATION,{unit.value})")


# This design constant represents the aircraft ideal cruising speed. It is derived from the cruise_speed setting in the [REFERENCE SPEEDS] section of the flightmodel.cfg. The default value is computed an internal function that uses the estimated cruise altitude and estimated cruise percent power, according of the engine type, the number of engines, the density, the wing area and some drag parameters. Normally this value is set in the CFG file and the default value is never used.
class _FlightSim_FlightModel_DESIGN_SPEED_VC:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.FEET_PER_SECOND'):
        return self._.get(f"(A:DESIGN SPEED VC,{unit.value})")


# This design constant represents the the stall speed when flaps are fully extended. It is derived from the full_flaps_stall_speed setting in the [REFERENCE SPEEDS] section of the flightmodel.cfg. Default value is 0.8 x VS.
class _FlightSim_FlightModel_DESIGN_SPEED_VS0:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.KNOT'):
        return self._.get(f"(A:DESIGN SPEED VS0,{unit.value})")


# This design constant represents the stall speed when flaps are fully retracted. It is derived from the flaps_up_stall_speed setting in the [REFERENCE SPEEDS] section of the flightmodel.cfg. Default value is 0.
class _FlightSim_FlightModel_DESIGN_SPEED_VS1:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.KNOT'):
        return self._.get(f"(A:DESIGN SPEED VS1,{unit.value})")


# This design constant represents the aircraft ideal takoff speed. It is derived from the takeoff_speed setting in the [REFERENCE SPEEDS] section of the flightmodel.cfg.
class _FlightSim_FlightModel_DESIGN_TAKEOFF_SPEED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.KNOT'):
        return self._.get(f"(A:DESIGN TAKEOFF SPEED,{unit.value})")


# Dynamic pressure
class _FlightSim_FlightModel_DYNAMIC_PRESSURE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Pressure.POUND_FORCE_PER_SQUARE_FOOT'):
        return self._.get(f"(A:DYNAMIC PRESSURE,{unit.value})")


# Estimated cruise speed
class _FlightSim_FlightModel_ESTIMATED_CRUISE_SPEED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.FEET_PER_SECOND'):
        return self._.get(f"(A:ESTIMATED CRUISE SPEED,{unit.value})")


# Current g force
class _FlightSim_FlightModel_G_FORCE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Acceleration.G_FORCE'):
        return self._.get(f"(A:G FORCE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Acceleration.G_FORCE', value: str):
        self._.set(f"{value} (>A:G FORCE,{unit.value})")


# This returns the setting of the G-limiter, as set using the GLimiterSetting parameter.
class _FlightSim_FlightModel_G_LIMITER_SETTING:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        OFF = 0
        ON = 1
        OVERRIDE = 2

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:G LIMITER SETTING,{unit.value})")


# Angle of attack
class _FlightSim_FlightModel_INCIDENCE_ALPHA:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:INCIDENCE ALPHA,{unit.value})")


# Sideslip angle
class _FlightSim_FlightModel_INCIDENCE_BETA:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:INCIDENCE BETA,{unit.value})")


# True if the aircraft is a taildragger
class _FlightSim_FlightModel_IS_TAIL_DRAGGER:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:IS TAIL DRAGGER,{unit.value})")


# Linear CL alpha
class _FlightSim_FlightModel_LINEAR_CL_ALPHA:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PER_RADIAN'):
        return self._.get(f"(A:LINEAR CL ALPHA,{unit.value})")


# Maximum design mach
class _FlightSim_FlightModel_MACH_MAX_OPERATE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.MACH'):
        return self._.get(f"(A:MACH MAX OPERATE,{unit.value})")


# Maximum G force attained
class _FlightSim_FlightModel_MAX_G_FORCE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Acceleration.G_FORCE'):
        return self._.get(f"(A:MAX G FORCE,{unit.value})")


# Minimum drag velocity, in clean, with no input and no gears, when at 10000ft.
class _FlightSim_FlightModel_MIN_DRAG_VELOCITY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.FEET_PER_SECOND'):
        return self._.get(f"(A:MIN DRAG VELOCITY,{unit.value})")


# Minimum G force attained
class _FlightSim_FlightModel_MIN_G_FORCE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Acceleration.G_FORCE'):
        return self._.get(f"(A:MIN G FORCE,{unit.value})")


# Deprecated, do not use!
class _FlightSim_FlightModel_SEMIBODY_LOADFACTOR_X:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:SEMIBODY LOADFACTOR X,{unit.value})")


# Acceleration along the axis Y divided by the gravity constant g (usually around 9.81m.s²)
class _FlightSim_FlightModel_SEMIBODY_LOADFACTOR_Y:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:SEMIBODY LOADFACTOR Y,{unit.value})")


# Derivative of SEMIBODY LOADFACTOR Y in relation to time.
#! Per second
class _FlightSim_FlightModel_SEMIBODY_LOADFACTOR_YDOT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: ''):
        return self._.get(f"(A:SEMIBODY LOADFACTOR YDOT,{unit.value})")


# Deprecated, do not use!
class _FlightSim_FlightModel_SEMIBODY_LOADFACTOR_Z:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:SEMIBODY LOADFACTOR Z,{unit.value})")


# Sigma sqrt
class _FlightSim_FlightModel_SIGMA_SQRT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:SIGMA SQRT,{unit.value})")


# Simulated radius
class _FlightSim_FlightModel_SIMULATED_RADIUS:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.FOOT'):
        return self._.get(f"(A:SIMULATED RADIUS,{unit.value})")


# The angle of attack which produces the maximum lift coefficient before entering into stall conditions.
class _FlightSim_FlightModel_STALL_ALPHA:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:STALL ALPHA,{unit.value})")


# The angle at which static pitch stability is achieved.
class _FlightSim_FlightModel_STATIC_PITCH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:STATIC PITCH,{unit.value})")


# the typical (normal) descent rate for the aircraft.
class _FlightSim_FlightModel_TYPICAL_DESCENT_RATE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.FEET_PER_MINUTE'):
        return self._.get(f"(A:TYPICAL DESCENT RATE,{unit.value})")


# Total wing area
class _FlightSim_FlightModel_WING_AREA:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Area.SQUARE_FOOT'):
        return self._.get(f"(A:WING AREA,{unit.value})")


# The current wing flex. Different values can be set for each wing (for example, during banking). Set an index of 1 for the left wing, and 2 for the right wing.
class _FlightSim_FlightModel_WING_FLEX_PCT:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:WING FLEX PCT:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100', value: str):
        self._.set(f"{value} (>A:WING FLEX PCT:{self._index},{unit.value})")


# Total wing span
class _FlightSim_FlightModel_WING_SPAN:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.FOOT'):
        return self._.get(f"(A:WING SPAN,{unit.value})")


# The yaw string angle. Yaw strings are attached to gliders as visible indicators of the yaw angle. An animation of this is not implemented in ESP.
class _FlightSim_FlightModel_YAW_STRING_ANGLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:YAW STRING ANGLE,{unit.value})")


# Yaw string angle as a percentage
class _FlightSim_FlightModel_YAW_STRING_PCT_EXTENDED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:YAW STRING PCT EXTENDED,{unit.value})")


# The angle of attack at which the wing has zero lift.
class _FlightSim_FlightModel_ZERO_LIFT_ALPHA:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:ZERO LIFT ALPHA,{unit.value})")


# Most backward authorized position of the CG according to the POH.
# NOTE: This is only valid for airplanes.
class _FlightSim_FlightModel_CG_AFT_LIMIT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:CG AFT LIMIT,{unit.value})")


# The longitudinal CG position relative to the Reference Datum Position.
# NOTE: This is only valid for helicopters.
class _FlightSim_FlightModel_CG_FEET:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.FOOT'):
        return self._.get(f"(A:CG FEET,{unit.value})")


# The aft CG limit position relative to the Reference Datum Position.
# NOTE: This is only valid for helicopters.
class _FlightSim_FlightModel_CG_FEET_AFT_LIMIT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.FOOT'):
        return self._.get(f"(A:CG FEET AFT LIMIT,{unit.value})")


# The lateral CG position relative to the Reference Datum Position.
# NOTE: This is only valid for helicopters.
class _FlightSim_FlightModel_CG_FEET_LATERAL:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.FOOT'):
        return self._.get(f"(A:CG FEET LATERAL,{unit.value})")


# The left hand lateral CG position relative to the Reference Datum Position.
# NOTE: This is only valid for helicopters.
class _FlightSim_FlightModel_CG_FEET_LATERAL_LEFT_LIMIT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.FOOT'):
        return self._.get(f"(A:CG FEET LATERAL LEFT LIMIT,{unit.value})")


# The right hand lateral CG position relative to the Reference Datum Position.
# NOTE: This is only valid for helicopters.
class _FlightSim_FlightModel_CG_FEET_LATERAL_RIGHT_LIMIT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.FOOT'):
        return self._.get(f"(A:CG FEET LATERAL RIGHT LIMIT,{unit.value})")


# The forward CG limit position relative to the Reference Datum Position.
# NOTE: This is only valid for helicopters.
class _FlightSim_FlightModel_CG_FEET_FWD_LIMIT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.FOOT'):
        return self._.get(f"(A:CG FEET FWD LIMIT,{unit.value})")


# Most forward authorized position of the CG according to the POH.
# NOTE: This is only valid for airplanes.
class _FlightSim_FlightModel_CG_FWD_LIMIT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:CG FWD LIMIT,{unit.value})")


# Deprecated, do not use!
class _FlightSim_FlightModel_CG_MAX_MACH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.MACH'):
        return self._.get(f"(A:CG MAX MACH,{unit.value})")


# Deprecated, do not use!
class _FlightSim_FlightModel_CG_MIN_MACH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.MACH'):
        return self._.get(f"(A:CG MIN MACH,{unit.value})")


# Longitudinal CG position as a percent of reference Chord.
# NOTE: This is only valid for airplanes.
class _FlightSim_FlightModel_CG_PERCENT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:CG PERCENT,{unit.value})")


# Lateral CG position as a percent of reference Chord.
# NOTE: This is only valid for airplanes.
class _FlightSim_FlightModel_CG_PERCENT_LATERAL:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:CG PERCENT LATERAL,{unit.value})")


# Static CG position with reference to the ground.
# NOTE: This is only valid for airplanes.
class _FlightSim_FlightModel_STATIC_CG_TO_GROUND:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.FOOT'):
        return self._.get(f"(A:STATIC CG TO GROUND,{unit.value})")


# Interactive Point orientation: Bank
class _FlightSim_FlightModel_INTERACTIVE_POINT_BANK:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:INTERACTIVE POINT BANK,{unit.value})")


# Interactive Point orientation: Heading
class _FlightSim_FlightModel_INTERACTIVE_POINT_HEADING:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:INTERACTIVE POINT HEADING,{unit.value})")


# Interactive Point Jetway constant, determining the desired left bend ratio of jetway hood
class _FlightSim_FlightModel_INTERACTIVE_POINT_JETWAY_LEFT_BEND:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:INTERACTIVE POINT JETWAY LEFT BEND,{unit.value})")


# Interactive Point Jetway constant, determining the desired left deployment angle of jetway hood
class _FlightSim_FlightModel_INTERACTIVE_POINT_JETWAY_LEFT_DEPLOYMENT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:INTERACTIVE POINT JETWAY LEFT DEPLOYMENT,{unit.value})")


# Interactive Point Jetway constant, determining the desired right bend ratio of jetway hood
class _FlightSim_FlightModel_INTERACTIVE_POINT_JETWAY_RIGHT_BEND:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:INTERACTIVE POINT JETWAY RIGHT BEND,{unit.value})")


# Interactive Point Jetway constant, determining the desired right deployment angle of jetway hood
class _FlightSim_FlightModel_INTERACTIVE_POINT_JETWAY_RIGHT_DEPLOYMENT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:INTERACTIVE POINT JETWAY RIGHT DEPLOYMENT,{unit.value})")


# Interactive Point Jetway constant, determining the desired top horizontal ratio of displacement of jetway hood
class _FlightSim_FlightModel_INTERACTIVE_POINT_JETWAY_TOP_HORIZONTAL:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:INTERACTIVE POINT JETWAY TOP HORIZONTAL,{unit.value})")


# Interactive Point Jetway constant, determining the desired top vertical ratio of displacement of jetway hood
class _FlightSim_FlightModel_INTERACTIVE_POINT_JETWAY_TOP_VERTICAL:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:INTERACTIVE POINT JETWAY TOP VERTICAL,{unit.value})")


# The Interactive Point goal percentage of opening (if it's for a door) or percentage of deployment (if it's for a hose or cable).
class _FlightSim_FlightModel_INTERACTIVE_POINT_GOAL:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:INTERACTIVE POINT GOAL,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100', value: str):
        self._.set(f"{value} (>A:INTERACTIVE POINT GOAL,{unit.value})")


# Interactive Point current percentage of opening (if door) or deployment (if hose/cable)
class _FlightSim_FlightModel_INTERACTIVE_POINT_OPEN:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:INTERACTIVE POINT OPEN,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100', value: str):
        self._.set(f"{value} (>A:INTERACTIVE POINT OPEN,{unit.value})")


# Interactive Point orientation: Pitch
class _FlightSim_FlightModel_INTERACTIVE_POINT_PITCH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:INTERACTIVE POINT PITCH,{unit.value})")


# Interactive Point X position relative to datum reference point
class _FlightSim_FlightModel_INTERACTIVE_POINT_POSX:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.FOOT'):
        return self._.get(f"(A:INTERACTIVE POINT POSX,{unit.value})")


# Interactive Point Y position relative to datum reference point
class _FlightSim_FlightModel_INTERACTIVE_POINT_POSY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.FOOT'):
        return self._.get(f"(A:INTERACTIVE POINT POSY,{unit.value})")


# Interactive Point Z position relative to datum reference point
class _FlightSim_FlightModel_INTERACTIVE_POINT_POSZ:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.FOOT'):
        return self._.get(f"(A:INTERACTIVE POINT POSZ,{unit.value})")


# The type of interactive point
class _FlightSim_FlightModel_INTERACTIVE_POINT_TYPE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        MAIN_EXIT = 0
        CARGO_EXIT = 1
        EMERGENCY_EXIT = 2
        FUEL_HOSE = 3
        GROUND_POWER_CABLE = 4
        UNKNOWN_FOR_ERROR_HANDLING = 99

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:INTERACTIVE POINT TYPE,{unit.value})")


# Empty weight of the aircraft
class _FlightSim_FlightModel_EMPTY_WEIGHT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Weight.POUND'):
        return self._.get(f"(A:EMPTY WEIGHT,{unit.value})")


# Empty weight cross coupled moment of inertia
class _FlightSim_FlightModel_EMPTY_WEIGHT_CROSS_COUPLED_MOI:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Pressure.SLUG_FEET_SQUARED'):
        return self._.get(f"(A:EMPTY WEIGHT CROSS COUPLED MOI,{unit.value})")


# Empty weight pitch moment of inertia
class _FlightSim_FlightModel_EMPTY_WEIGHT_PITCH_MOI:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Pressure.SLUG_FEET_SQUARED'):
        return self._.get(f"(A:EMPTY WEIGHT PITCH MOI,{unit.value})")


# Empty weight roll moment of inertia
class _FlightSim_FlightModel_EMPTY_WEIGHT_ROLL_MOI:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Pressure.SLUG_FEET_SQUARED'):
        return self._.get(f"(A:EMPTY WEIGHT ROLL MOI,{unit.value})")


# Empty weight yaw moment of inertia
class _FlightSim_FlightModel_EMPTY_WEIGHT_YAW_MOI:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Pressure.SLUG_FEET_SQUARED'):
        return self._.get(f"(A:EMPTY WEIGHT YAW MOI,{unit.value})")


# Maximum gross weight of the aircaft
class _FlightSim_FlightModel_MAX_GROSS_WEIGHT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Weight.POUND'):
        return self._.get(f"(A:MAX GROSS WEIGHT,{unit.value})")


# Total weight of the aircraft
class _FlightSim_FlightModel_TOTAL_WEIGHT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Weight.POUND'):
        return self._.get(f"(A:TOTAL WEIGHT,{unit.value})")


# Total weight cross coupled moment of inertia
class _FlightSim_FlightModel_TOTAL_WEIGHT_CROSS_COUPLED_MOI:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Pressure.SLUG_FEET_SQUARED'):
        return self._.get(f"(A:TOTAL WEIGHT CROSS COUPLED MOI,{unit.value})")


# Total weight pitch moment of inertia
class _FlightSim_FlightModel_TOTAL_WEIGHT_PITCH_MOI:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Pressure.SLUG_FEET_SQUARED'):
        return self._.get(f"(A:TOTAL WEIGHT PITCH MOI,{unit.value})")


# Total weight roll moment of inertia
class _FlightSim_FlightModel_TOTAL_WEIGHT_ROLL_MOI:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Pressure.SLUG_FEET_SQUARED'):
        return self._.get(f"(A:TOTAL WEIGHT ROLL MOI,{unit.value})")


# Total weight yaw moment of inertia
class _FlightSim_FlightModel_TOTAL_WEIGHT_YAW_MOI:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Pressure.SLUG_FEET_SQUARED'):
        return self._.get(f"(A:TOTAL WEIGHT YAW MOI,{unit.value})")


class _FlightSim_Fuel:
    def __init__(self, flightSim):
        self._ = flightSim
        self.FUEL_CROSS_FEED = lambda index: _FlightSim_Fuel_FUEL_CROSS_FEED(flightSim, index)
        self.FUEL_DUMP_ACTIVE = _FlightSim_Fuel_FUEL_DUMP_ACTIVE(flightSim)
        self.FUEL_DUMP_SWITCH = _FlightSim_Fuel_FUEL_DUMP_SWITCH(flightSim)
        self.FUEL_LEFT_CAPACITY = _FlightSim_Fuel_FUEL_LEFT_CAPACITY(flightSim)
        self.FUEL_LEFT_QUANTITY = _FlightSim_Fuel_FUEL_LEFT_QUANTITY(flightSim)
        self.FUEL_PUMP = _FlightSim_Fuel_FUEL_PUMP(flightSim)
        self.FUEL_RIGHT_CAPACITY = _FlightSim_Fuel_FUEL_RIGHT_CAPACITY(flightSim)
        self.FUEL_RIGHT_QUANTITY = _FlightSim_Fuel_FUEL_RIGHT_QUANTITY(flightSim)
        self.FUEL_SELECTED_QUANTITY = lambda index: _FlightSim_Fuel_FUEL_SELECTED_QUANTITY(flightSim, index)
        self.FUEL_SELECTED_QUANTITY_PERCENT = lambda index: _FlightSim_Fuel_FUEL_SELECTED_QUANTITY_PERCENT(flightSim, index)
        self.FUEL_SELECTED_TRANSFER_MODE = _FlightSim_Fuel_FUEL_SELECTED_TRANSFER_MODE(flightSim)
        self.FUEL_TOTAL_CAPACITY = _FlightSim_Fuel_FUEL_TOTAL_CAPACITY(flightSim)
        self.FUEL_TOTAL_QUANTITY = _FlightSim_Fuel_FUEL_TOTAL_QUANTITY(flightSim)
        self.FUEL_TOTAL_QUANTITY_WEIGHT = _FlightSim_Fuel_FUEL_TOTAL_QUANTITY_WEIGHT(flightSim)
        self.FUEL_TRANSFER_PUMP_ON = lambda index: _FlightSim_Fuel_FUEL_TRANSFER_PUMP_ON(flightSim, index)
        self.FUEL_WEIGHT_PER_GALLON = _FlightSim_Fuel_FUEL_WEIGHT_PER_GALLON(flightSim)
        self.NEW_FUEL_SYSTEM = _FlightSim_Fuel_NEW_FUEL_SYSTEM(flightSim)
        self.NUM_FUEL_SELECTORS = _FlightSim_Fuel_NUM_FUEL_SELECTORS(flightSim)
        self.UNLIMITED_FUEL = _FlightSim_Fuel_UNLIMITED_FUEL(flightSim)
        self.UNUSABLE_FUEL_TOTAL_QUANTITY = _FlightSim_Fuel_UNUSABLE_FUEL_TOTAL_QUANTITY(flightSim)
        self.FUELSYSTEM_ENGINE_PRESSURE = lambda index: _FlightSim_Fuel_FUELSYSTEM_ENGINE_PRESSURE(flightSim, index)
        self.FUELSYSTEM_JUNCTION_SETTING = lambda index: _FlightSim_Fuel_FUELSYSTEM_JUNCTION_SETTING(flightSim, index)
        self.FUELSYSTEM_LINE_FUEL_FLOW = lambda index: _FlightSim_Fuel_FUELSYSTEM_LINE_FUEL_FLOW(flightSim, index)
        self.FUELSYSTEM_LINE_FUEL_LEVEL = lambda index: _FlightSim_Fuel_FUELSYSTEM_LINE_FUEL_LEVEL(flightSim, index)
        self.FUELSYSTEM_LINE_FUEL_PRESSURE = lambda index: _FlightSim_Fuel_FUELSYSTEM_LINE_FUEL_PRESSURE(flightSim, index)
        self.FUELSYSTEM_PUMP_ACTIVE = lambda index: _FlightSim_Fuel_FUELSYSTEM_PUMP_ACTIVE(flightSim, index)
        self.FUELSYSTEM_PUMP_SWITCH = lambda index: _FlightSim_Fuel_FUELSYSTEM_PUMP_SWITCH(flightSim, index)
        self.FUELSYSTEM_TANK_CAPACITY = lambda index: _FlightSim_Fuel_FUELSYSTEM_TANK_CAPACITY(flightSim, index)
        self.FUELSYSTEM_TANK_LEVEL = lambda index: _FlightSim_Fuel_FUELSYSTEM_TANK_LEVEL(flightSim, index)
        self.FUELSYSTEM_TANK_QUANTITY = lambda index: _FlightSim_Fuel_FUELSYSTEM_TANK_QUANTITY(flightSim, index)
        self.FUELSYSTEM_TANK_TOTAL_QUANTITY = lambda index: _FlightSim_Fuel_FUELSYSTEM_TANK_TOTAL_QUANTITY(flightSim, index)
        self.FUELSYSTEM_TANK_WEIGHT = lambda index: _FlightSim_Fuel_FUELSYSTEM_TANK_WEIGHT(flightSim, index)
        self.FUELSYSTEM_TRIGGER_STATUS = lambda index: _FlightSim_Fuel_FUELSYSTEM_TRIGGER_STATUS(flightSim, index)
        self.FUELSYSTEM_VALVE_OPEN = lambda index: _FlightSim_Fuel_FUELSYSTEM_VALVE_OPEN(flightSim, index)
        self.FUELSYSTEM_VALVE_SWITCH = lambda index: _FlightSim_Fuel_FUELSYSTEM_VALVE_SWITCH(flightSim, index)
        self.FUEL_TANK_CENTER_CAPACITY = _FlightSim_Fuel_FUEL_TANK_CENTER_CAPACITY(flightSim)
        self.FUEL_TANK_CENTER_LEVEL = _FlightSim_Fuel_FUEL_TANK_CENTER_LEVEL(flightSim)
        self.FUEL_TANK_CENTER_QUANTITY = _FlightSim_Fuel_FUEL_TANK_CENTER_QUANTITY(flightSim)
        self.FUEL_TANK_EXTERNAL1_CAPACITY = _FlightSim_Fuel_FUEL_TANK_EXTERNAL1_CAPACITY(flightSim)
        self.FUEL_TANK_EXTERNAL1_LEVEL = _FlightSim_Fuel_FUEL_TANK_EXTERNAL1_LEVEL(flightSim)
        self.FUEL_TANK_EXTERNAL1_QUANTITY = _FlightSim_Fuel_FUEL_TANK_EXTERNAL1_QUANTITY(flightSim)
        self.FUEL_TANK_LEFT_AUX_CAPACITY = _FlightSim_Fuel_FUEL_TANK_LEFT_AUX_CAPACITY(flightSim)
        self.FUEL_TANK_LEFT_AUX_LEVEL = _FlightSim_Fuel_FUEL_TANK_LEFT_AUX_LEVEL(flightSim)
        self.FUEL_TANK_LEFT_AUX_QUANTITY = _FlightSim_Fuel_FUEL_TANK_LEFT_AUX_QUANTITY(flightSim)
        self.FUEL_TANK_LEFT_MAIN_CAPACITY = _FlightSim_Fuel_FUEL_TANK_LEFT_MAIN_CAPACITY(flightSim)
        self.FUEL_TANK_LEFT_MAIN_LEVEL = _FlightSim_Fuel_FUEL_TANK_LEFT_MAIN_LEVEL(flightSim)
        self.FUEL_TANK_LEFT_MAIN_QUANTITY = _FlightSim_Fuel_FUEL_TANK_LEFT_MAIN_QUANTITY(flightSim)
        self.FUEL_TANK_LEFT_TIP_CAPACITY = _FlightSim_Fuel_FUEL_TANK_LEFT_TIP_CAPACITY(flightSim)
        self.FUEL_TANK_LEFT_TIP_LEVEL = _FlightSim_Fuel_FUEL_TANK_LEFT_TIP_LEVEL(flightSim)
        self.FUEL_TANK_LEFT_TIP_QUANTITY = _FlightSim_Fuel_FUEL_TANK_LEFT_TIP_QUANTITY(flightSim)
        self.FUEL_TANK_RIGHT_AUX_CAPACITY = _FlightSim_Fuel_FUEL_TANK_RIGHT_AUX_CAPACITY(flightSim)
        self.FUEL_TANK_RIGHT_AUX_LEVEL = _FlightSim_Fuel_FUEL_TANK_RIGHT_AUX_LEVEL(flightSim)
        self.FUEL_TANK_RIGHT_AUX_QUANTITY = _FlightSim_Fuel_FUEL_TANK_RIGHT_AUX_QUANTITY(flightSim)
        self.FUEL_TANK_RIGHT_MAIN_CAPACITY = _FlightSim_Fuel_FUEL_TANK_RIGHT_MAIN_CAPACITY(flightSim)
        self.FUEL_TANK_RIGHT_MAIN_LEVEL = _FlightSim_Fuel_FUEL_TANK_RIGHT_MAIN_LEVEL(flightSim)
        self.FUEL_TANK_RIGHT_MAIN_QUANTITY = _FlightSim_Fuel_FUEL_TANK_RIGHT_MAIN_QUANTITY(flightSim)
        self.FUEL_TANK_RIGHT_TIP_CAPACITY = _FlightSim_Fuel_FUEL_TANK_RIGHT_TIP_CAPACITY(flightSim)
        self.FUEL_TANK_RIGHT_TIP_LEVEL = _FlightSim_Fuel_FUEL_TANK_RIGHT_TIP_LEVEL(flightSim)
        self.FUEL_TANK_RIGHT_TIP_QUANTITY = _FlightSim_Fuel_FUEL_TANK_RIGHT_TIP_QUANTITY(flightSim)
        self.FUEL_TANK_SELECTOR = lambda index: _FlightSim_Fuel_FUEL_TANK_SELECTOR(flightSim, index)


# Cross feed valve setting. This will return the current setting for the fuel crossfeed for the indexed engine, based on the current status of the simulation and the Cross Feed key events.
class _FlightSim_Fuel_FUEL_CROSS_FEED:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    class Unit(Enum):
        CLOSED = 0
        OPEN = 1
        LEFT_TO_RIGHT = 2
        RIGHT_TO_LEFT = 3

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:FUEL CROSS FEED:{self._index},{unit.value})")


# If 1 (TRUE) then the aircraft can dump fuel.
class _FlightSim_Fuel_FUEL_DUMP_ACTIVE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:FUEL DUMP ACTIVE,{unit.value})")


# If set to 1 (TRUE) then the aircraft will dump fuel at the rate set by fuel_dump_rate parameter in the flight_model.cfg file.
class _FlightSim_Fuel_FUEL_DUMP_SWITCH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:FUEL DUMP SWITCH,{unit.value})")


# Maximum capacity in volume of all the tanks on the left side of the aircraft.
class _FlightSim_Fuel_FUEL_LEFT_CAPACITY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Volume.GALLON'):
        return self._.get(f"(A:FUEL LEFT CAPACITY,{unit.value})")


# Current quantity in volume of all the tanks on the left side of the aircraft.
class _FlightSim_Fuel_FUEL_LEFT_QUANTITY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Volume.GALLON'):
        return self._.get(f"(A:FUEL LEFT QUANTITY,{unit.value})")


# Currently not used within the simulation.
class _FlightSim_Fuel_FUEL_PUMP:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:FUEL PUMP,{unit.value})")


# Maximum capacity in volume of all the tanks on the right side of the aircraft.
class _FlightSim_Fuel_FUEL_RIGHT_CAPACITY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Volume.GALLON'):
        return self._.get(f"(A:FUEL RIGHT CAPACITY,{unit.value})")


# Current quantity in volume of all the tanks on the right side of the aircraft.
class _FlightSim_Fuel_FUEL_RIGHT_QUANTITY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Volume.GALLON'):
        return self._.get(f"(A:FUEL RIGHT QUANTITY,{unit.value})")


# Quantity of fuel in the tank referenced by the indexed selector. When using the legacy fuel system, this SimVar will return the quantity of fuel in the tank pointed to by the selector you chose with the index. If passing an index higher than the number of selectors - or when using the modern fuel system - it will return the total fuel quantity available.
class _FlightSim_Fuel_FUEL_SELECTED_QUANTITY:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Volume.GALLON'):
        return self._.get(f"(A:FUEL SELECTED QUANTITY:{self._index},{unit.value})")


# Percent or capacity for the tank referenced by the indexed selector. When using the legacy fuel system, this SimVar will return the percentage of fuel in the tank pointed to by the selector you chose with the index. If passing an index higher than the number of selectors available - or when using the modern fuel system - it will return the percentage of total fuel quantity available.
class _FlightSim_Fuel_FUEL_SELECTED_QUANTITY_PERCENT:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:FUEL SELECTED QUANTITY PERCENT:{self._index},{unit.value})")


# The method of transfer for the fuel. Each of the available transfer options are explained below:
class _FlightSim_Fuel_FUEL_SELECTED_TRANSFER_MODE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        OFF = 0
        AUTO = 1
        FORWARD = 2
        AFT = 3
        MANUAL = 4
        CUSTOM = 5

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:FUEL SELECTED TRANSFER MODE,{unit.value})")


# Total fuel capacity of the aircraft for all tanks.
class _FlightSim_Fuel_FUEL_TOTAL_CAPACITY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Volume.GALLON'):
        return self._.get(f"(A:FUEL TOTAL CAPACITY,{unit.value})")


# Current total quantity of fuel in volume for all tanks of the aircraft.
class _FlightSim_Fuel_FUEL_TOTAL_QUANTITY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Volume.GALLON'):
        return self._.get(f"(A:FUEL TOTAL QUANTITY,{unit.value})")


# Current total fuel weight for all tanks of the aircraft
class _FlightSim_Fuel_FUEL_TOTAL_QUANTITY_WEIGHT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Weight.POUND'):
        return self._.get(f"(A:FUEL TOTAL QUANTITY WEIGHT,{unit.value})")


# Returns 1 (TRUE) if the indexed pump is active.
class _FlightSim_Fuel_FUEL_TRANSFER_PUMP_ON:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:FUEL TRANSFER PUMP ON:{self._index},{unit.value})")


# The weight of the fuel, per gallon.
class _FlightSim_Fuel_FUEL_WEIGHT_PER_GALLON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Weight.POUND'):
        return self._.get(f"(A:FUEL WEIGHT PER GALLON,{unit.value})")


# Will return 1 (TRUE) if the aircraft is using the modern [FUEL_SYSTEM] or 0 (FALSE) for the legacy [FUEL].
class _FlightSim_Fuel_NEW_FUEL_SYSTEM:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:NEW FUEL SYSTEM,{unit.value})")


# The number of fuel selectors on the aircraft.
class _FlightSim_Fuel_NUM_FUEL_SELECTORS:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:NUM FUEL SELECTORS,{unit.value})")


# Will return 1 (TRUE) if the unlimited fuel flag has been enabled, or 0 (FALSE) otherwise.
class _FlightSim_Fuel_UNLIMITED_FUEL:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:UNLIMITED FUEL,{unit.value})")


# The total amount of fuel in all tanks of the aircraft which is not usable.
class _FlightSim_Fuel_UNUSABLE_FUEL_TOTAL_QUANTITY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Volume.GALLON'):
        return self._.get(f"(A:UNUSABLE FUEL TOTAL QUANTITY,{unit.value})")


# The pressure of the fuel coming to the indexed engine. The index is the number of the engine N component as defined by the Engine.N parameter.
class _FlightSim_Fuel_FUELSYSTEM_ENGINE_PRESSURE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Pressure.KILOPASCAL'):
        return self._.get(f"(A:FUELSYSTEM ENGINE PRESSURE:{self._index},{unit.value})")


# This will return the current Option for the indexed junction. The index is the number of the line N component as defined by the Junction.N parameter.
class _FlightSim_Fuel_FUELSYSTEM_JUNCTION_SETTING:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:FUELSYSTEM JUNCTION SETTING:{self._index},{unit.value})")


# The fuel flowing through the indexed line in Gallons per Hour. The index is the number of the line N component as defined by the Line.N parameter.
class _FlightSim_Fuel_FUELSYSTEM_LINE_FUEL_FLOW:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.VolumeRate.GALLON_PER_HOUR'):
        return self._.get(f"(A:FUELSYSTEM LINE FUEL FLOW:{self._index},{unit.value})")


# The level of fuel in the indexed line in Gallons. The index is the number of the line N component as defined by the Line.N parameter.
class _FlightSim_Fuel_FUELSYSTEM_LINE_FUEL_LEVEL:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Volume.GALLON'):
        return self._.get(f"(A:FUELSYSTEM LINE FUEL LEVEL:{self._index},{unit.value})")


# The pressure in the indexed fuel line, measured in KiloPascal. The index is the number of the line N component as defined by the Line.N parameter.
class _FlightSim_Fuel_FUELSYSTEM_LINE_FUEL_PRESSURE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Pressure.KILOPASCAL'):
        return self._.get(f"(A:FUELSYSTEM LINE FUEL PRESSURE:{self._index},{unit.value})")


# Whether or not the indexed pump is actually active. The index is the number of the pump N component as defined by the Pump.N parameter.
class _FlightSim_Fuel_FUELSYSTEM_PUMP_ACTIVE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:FUELSYSTEM PUMP ACTIVE:{self._index},{unit.value})")


# Whether or not the indexed pump is enabled. The index is the number of the pump N component as defined by the Pump.N parameter.
class _FlightSim_Fuel_FUELSYSTEM_PUMP_SWITCH:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:FUELSYSTEM PUMP SWITCH:{self._index},{unit.value})")


# Total capacity of the indexed fuel tank. The index is the number of the tank N component as defined by the Tank.N parameter.
# NOTE: This SimVar can only be used with the modern Fuel System.
class _FlightSim_Fuel_FUELSYSTEM_TANK_CAPACITY:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Volume.GALLON'):
        return self._.get(f"(A:FUELSYSTEM TANK CAPACITY:{self._index},{unit.value})")


# Quantity of fuel available in the indexed fuel tank. The index is the number of the tank N component as defined by the Tank.N parameter.
# NOTE: This SimVar can only be used with the modern Fuel System.
class _FlightSim_Fuel_FUELSYSTEM_TANK_LEVEL:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:FUELSYSTEM TANK LEVEL:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100', value: str):
        self._.set(f"{value} (>A:FUELSYSTEM TANK LEVEL:{self._index},{unit.value})")


# Quantity of fuel currently available in the indexed fuel tank. The index is the number of the tank N component as defined by the Tank.N parameter.
# NOTE: If the fuel system Version is 2 or below, the index value will be one of the Fuel Tank Selection indices.
class _FlightSim_Fuel_FUELSYSTEM_TANK_QUANTITY:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Volume.GALLON'):
        return self._.get(f"(A:FUELSYSTEM TANK QUANTITY:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Volume.GALLON', value: str):
        self._.set(f"{value} (>A:FUELSYSTEM TANK QUANTITY:{self._index},{unit.value})")


# Total quantity of fuel available in the indexed fuel tank, including any unusable fuel. The index is the number of the tank N component as defined by the Tank.N parameter.
# NOTE: If the fuel system Version is 2 or below, the index value will be one of the Fuel Tank Selection indices.
class _FlightSim_Fuel_FUELSYSTEM_TANK_TOTAL_QUANTITY:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Volume.GALLON'):
        return self._.get(f"(A:FUELSYSTEM TANK TOTAL QUANTITY:{self._index},{unit.value})")


# Weight of fuel available in the indexed fuel tank. The index is the number of the tank N component as defined by the Tank.N parameter.
# NOTE: If the fuel system Version is 2 or below, the index value will be one of the Fuel Tank Selection indices.
class _FlightSim_Fuel_FUELSYSTEM_TANK_WEIGHT:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Weight.POUND'):
        return self._.get(f"(A:FUELSYSTEM TANK WEIGHT:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Weight.POUND', value: str):
        self._.set(f"{value} (>A:FUELSYSTEM TANK WEIGHT:{self._index},{unit.value})")


# Whether or not the indexed trigger is active. The index is the number of the trigger N component as defined by the Trigger.N parameter.
class _FlightSim_Fuel_FUELSYSTEM_TRIGGER_STATUS:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:FUELSYSTEM TRIGGER STATUS:{self._index},{unit.value})")


# Whether or not the indexed valve is actually fully opened. The index is the number of the valve N component as defined by the Valve.N parameter.
class _FlightSim_Fuel_FUELSYSTEM_VALVE_OPEN:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:FUELSYSTEM VALVE OPEN:{self._index},{unit.value})")


# Whether or not the indexed valve is set to be opened. The index is the number of the valve N component as defined by the Valve.N parameter.
class _FlightSim_Fuel_FUELSYSTEM_VALVE_SWITCH:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:FUELSYSTEM VALVE SWITCH:{self._index},{unit.value})")


# Maximum capacity in volume of center tank 1/2/3.
class _FlightSim_Fuel_FUEL_TANK_CENTER_CAPACITY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Volume.GALLON'):
        return self._.get(f"(A:FUEL TANK CENTER CAPACITY,{unit.value})")


# Percent of maximum capacity of center tank 1/2/3.
class _FlightSim_Fuel_FUEL_TANK_CENTER_LEVEL:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:FUEL TANK CENTER LEVEL,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100', value: str):
        self._.set(f"{value} (>A:FUEL TANK CENTER LEVEL,{unit.value})")


# Current quantity in volume of center tank 1/2/3.
class _FlightSim_Fuel_FUEL_TANK_CENTER_QUANTITY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Volume.GALLON'):
        return self._.get(f"(A:FUEL TANK CENTER QUANTITY,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Volume.GALLON', value: str):
        self._.set(f"{value} (>A:FUEL TANK CENTER QUANTITY,{unit.value})")


# Maximum capacity in volume of external tank 1/2.
class _FlightSim_Fuel_FUEL_TANK_EXTERNAL1_CAPACITY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Volume.GALLON'):
        return self._.get(f"(A:FUEL TANK EXTERNAL1 CAPACITY,{unit.value})")


# Percent of maximum capacity of texternal tank 1/2.
class _FlightSim_Fuel_FUEL_TANK_EXTERNAL1_LEVEL:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:FUEL TANK EXTERNAL1 LEVEL,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100', value: str):
        self._.set(f"{value} (>A:FUEL TANK EXTERNAL1 LEVEL,{unit.value})")


# Current quantity in volume of external tank 1/2.
class _FlightSim_Fuel_FUEL_TANK_EXTERNAL1_QUANTITY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Volume.GALLON'):
        return self._.get(f"(A:FUEL TANK EXTERNAL1 QUANTITY,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Volume.GALLON', value: str):
        self._.set(f"{value} (>A:FUEL TANK EXTERNAL1 QUANTITY,{unit.value})")


# Maximum capacity in volume of the left auxiliary tank.
class _FlightSim_Fuel_FUEL_TANK_LEFT_AUX_CAPACITY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Volume.GALLON'):
        return self._.get(f"(A:FUEL TANK LEFT AUX CAPACITY,{unit.value})")


# Percent of maximum capacity of the left auxiliary tank.
class _FlightSim_Fuel_FUEL_TANK_LEFT_AUX_LEVEL:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:FUEL TANK LEFT AUX LEVEL,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100', value: str):
        self._.set(f"{value} (>A:FUEL TANK LEFT AUX LEVEL,{unit.value})")


# Current quantity in volume of the left auxiliary tank.
class _FlightSim_Fuel_FUEL_TANK_LEFT_AUX_QUANTITY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Volume.GALLON'):
        return self._.get(f"(A:FUEL TANK LEFT AUX QUANTITY,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Volume.GALLON', value: str):
        self._.set(f"{value} (>A:FUEL TANK LEFT AUX QUANTITY,{unit.value})")


# Maximum capacity in volume of the left main tank.
class _FlightSim_Fuel_FUEL_TANK_LEFT_MAIN_CAPACITY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Volume.GALLON'):
        return self._.get(f"(A:FUEL TANK LEFT MAIN CAPACITY,{unit.value})")


# Percent of maximum capacity of the left main tank.
class _FlightSim_Fuel_FUEL_TANK_LEFT_MAIN_LEVEL:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:FUEL TANK LEFT MAIN LEVEL,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100', value: str):
        self._.set(f"{value} (>A:FUEL TANK LEFT MAIN LEVEL,{unit.value})")


# Current quantity in volume of the left main tank.
class _FlightSim_Fuel_FUEL_TANK_LEFT_MAIN_QUANTITY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Volume.GALLON'):
        return self._.get(f"(A:FUEL TANK LEFT MAIN QUANTITY,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Volume.GALLON', value: str):
        self._.set(f"{value} (>A:FUEL TANK LEFT MAIN QUANTITY,{unit.value})")


# Maximum capacity in volume of the left tip tank.
class _FlightSim_Fuel_FUEL_TANK_LEFT_TIP_CAPACITY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Volume.GALLON'):
        return self._.get(f"(A:FUEL TANK LEFT TIP CAPACITY,{unit.value})")


# Percent of maximum capacity of the left tip tank.
class _FlightSim_Fuel_FUEL_TANK_LEFT_TIP_LEVEL:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:FUEL TANK LEFT TIP LEVEL,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100', value: str):
        self._.set(f"{value} (>A:FUEL TANK LEFT TIP LEVEL,{unit.value})")


# Current quantity in volume of the left tip tank.
class _FlightSim_Fuel_FUEL_TANK_LEFT_TIP_QUANTITY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Volume.GALLON'):
        return self._.get(f"(A:FUEL TANK LEFT TIP QUANTITY,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Volume.GALLON', value: str):
        self._.set(f"{value} (>A:FUEL TANK LEFT TIP QUANTITY,{unit.value})")


# Maximum capacity in volume of the right auxiliary tank.
class _FlightSim_Fuel_FUEL_TANK_RIGHT_AUX_CAPACITY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Volume.GALLON'):
        return self._.get(f"(A:FUEL TANK RIGHT AUX CAPACITY,{unit.value})")


# Percent of maximum capacity of the right auxiliary tank.
class _FlightSim_Fuel_FUEL_TANK_RIGHT_AUX_LEVEL:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:FUEL TANK RIGHT AUX LEVEL,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100', value: str):
        self._.set(f"{value} (>A:FUEL TANK RIGHT AUX LEVEL,{unit.value})")


# Current quantity in volume of the right auxiliary tank.
class _FlightSim_Fuel_FUEL_TANK_RIGHT_AUX_QUANTITY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Volume.GALLON'):
        return self._.get(f"(A:FUEL TANK RIGHT AUX QUANTITY,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Volume.GALLON', value: str):
        self._.set(f"{value} (>A:FUEL TANK RIGHT AUX QUANTITY,{unit.value})")


# Maximum capacity in volume of the right main tank.
class _FlightSim_Fuel_FUEL_TANK_RIGHT_MAIN_CAPACITY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Volume.GALLON'):
        return self._.get(f"(A:FUEL TANK RIGHT MAIN CAPACITY,{unit.value})")


# Percent of maximum capacity of the right main tank.
class _FlightSim_Fuel_FUEL_TANK_RIGHT_MAIN_LEVEL:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:FUEL TANK RIGHT MAIN LEVEL,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100', value: str):
        self._.set(f"{value} (>A:FUEL TANK RIGHT MAIN LEVEL,{unit.value})")


# Current quantity in volume of the right main tank.
class _FlightSim_Fuel_FUEL_TANK_RIGHT_MAIN_QUANTITY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Volume.GALLON'):
        return self._.get(f"(A:FUEL TANK RIGHT MAIN QUANTITY,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Volume.GALLON', value: str):
        self._.set(f"{value} (>A:FUEL TANK RIGHT MAIN QUANTITY,{unit.value})")


# Maximum capacity in volume of the right tip tank.
class _FlightSim_Fuel_FUEL_TANK_RIGHT_TIP_CAPACITY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Volume.GALLON'):
        return self._.get(f"(A:FUEL TANK RIGHT TIP CAPACITY,{unit.value})")


# Percent of maximum capacity of the right tip tank.
class _FlightSim_Fuel_FUEL_TANK_RIGHT_TIP_LEVEL:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:FUEL TANK RIGHT TIP LEVEL,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100', value: str):
        self._.set(f"{value} (>A:FUEL TANK RIGHT TIP LEVEL,{unit.value})")


# Current quantity in volume of the right tip tank.
class _FlightSim_Fuel_FUEL_TANK_RIGHT_TIP_QUANTITY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Volume.GALLON'):
        return self._.get(f"(A:FUEL TANK RIGHT TIP QUANTITY,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Volume.GALLON', value: str):
        self._.set(f"{value} (>A:FUEL TANK RIGHT TIP QUANTITY,{unit.value})")


# Which tank the indexed selector is set to. The index is the selector to check (from 1 to 4), and the return value will be the Fuel Tank Selection index.
# NOTE: This SimVar is only valid for the legacy [FUEL] setup.
class _FlightSim_Fuel_FUEL_TANK_SELECTOR:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:FUEL TANK SELECTOR:{self._index},{unit.value})")


class _FlightSim_Misc:
    def __init__(self, flightSim):
        self._ = flightSim
        self.AMBIENT_IN_CLOUD = _FlightSim_Misc_AMBIENT_IN_CLOUD(flightSim)
        self.CONTRAILS_CONDITIONS_MET = _FlightSim_Misc_CONTRAILS_CONDITIONS_MET(flightSim)
        self.IS_SLEW_ACTIVE = _FlightSim_Misc_IS_SLEW_ACTIVE(flightSim)
        self.IS_SLEW_ALLOWED = _FlightSim_Misc_IS_SLEW_ALLOWED(flightSim)
        self.IS_USER_SIM = _FlightSim_Misc_IS_USER_SIM(flightSim)
        self.ON_ANY_RUNWAY = _FlightSim_Misc_ON_ANY_RUNWAY(flightSim)
        self.PLANE_IN_PARKING_STATE = _FlightSim_Misc_PLANE_IN_PARKING_STATE(flightSim)
        self.SURFACE_CONDITION = _FlightSim_Misc_SURFACE_CONDITION(flightSim)
        self.SURFACE_INFO_VALID = _FlightSim_Misc_SURFACE_INFO_VALID(flightSim)
        self.SURFACE_TYPE = _FlightSim_Misc_SURFACE_TYPE(flightSim)
        self.STRUCTURAL_ICE_PCT = _FlightSim_Misc_STRUCTURAL_ICE_PCT(flightSim)
        self.TITLE = _FlightSim_Misc_TITLE(flightSim)
        self.TOW_CONNECTION = _FlightSim_Misc_TOW_CONNECTION(flightSim)
        self.WINDSHIELD_RAIN_EFFECT_AVAILABLE = _FlightSim_Misc_WINDSHIELD_RAIN_EFFECT_AVAILABLE(flightSim)
        self.ACCELERATION_BODY_X = _FlightSim_Misc_ACCELERATION_BODY_X(flightSim)
        self.ACCELERATION_BODY_Y = _FlightSim_Misc_ACCELERATION_BODY_Y(flightSim)
        self.ACCELERATION_BODY_Z = _FlightSim_Misc_ACCELERATION_BODY_Z(flightSim)
        self.ACCELERATION_WORLD_X = _FlightSim_Misc_ACCELERATION_WORLD_X(flightSim)
        self.ACCELERATION_WORLD_Y = _FlightSim_Misc_ACCELERATION_WORLD_Y(flightSim)
        self.ACCELERATION_WORLD_Z = _FlightSim_Misc_ACCELERATION_WORLD_Z(flightSim)
        self.SURFACE_RELATIVE_GROUND_SPEED = _FlightSim_Misc_SURFACE_RELATIVE_GROUND_SPEED(flightSim)
        self.GROUND_VELOCITY = _FlightSim_Misc_GROUND_VELOCITY(flightSim)
        self.PLANE_ALTITUDE = _FlightSim_Misc_PLANE_ALTITUDE(flightSim)
        self.PLANE_ALT_ABOVE_GROUND = _FlightSim_Misc_PLANE_ALT_ABOVE_GROUND(flightSim)
        self.PLANE_ALT_ABOVE_GROUND_MINUS_CG = _FlightSim_Misc_PLANE_ALT_ABOVE_GROUND_MINUS_CG(flightSim)
        self.PLANE_BANK_DEGREES = _FlightSim_Misc_PLANE_BANK_DEGREES(flightSim)
        self.PLANE_HEADING_DEGREES_GYRO = _FlightSim_Misc_PLANE_HEADING_DEGREES_GYRO(flightSim)
        self.PLANE_HEADING_DEGREES_MAGNETIC = _FlightSim_Misc_PLANE_HEADING_DEGREES_MAGNETIC(flightSim)
        self.PLANE_HEADING_DEGREES_TRUE = _FlightSim_Misc_PLANE_HEADING_DEGREES_TRUE(flightSim)
        self.PLANE_LATITUDE = _FlightSim_Misc_PLANE_LATITUDE(flightSim)
        self.PLANE_LONGITUDE = _FlightSim_Misc_PLANE_LONGITUDE(flightSim)
        self.PLANE_PITCH_DEGREES = _FlightSim_Misc_PLANE_PITCH_DEGREES(flightSim)
        self.PLANE_TOUCHDOWN_BANK_DEGREES = _FlightSim_Misc_PLANE_TOUCHDOWN_BANK_DEGREES(flightSim)
        self.PLANE_TOUCHDOWN_HEADING_DEGREES_MAGNETIC = _FlightSim_Misc_PLANE_TOUCHDOWN_HEADING_DEGREES_MAGNETIC(flightSim)
        self.PLANE_TOUCHDOWN_HEADING_DEGREES_TRUE = _FlightSim_Misc_PLANE_TOUCHDOWN_HEADING_DEGREES_TRUE(flightSim)
        self.PLANE_TOUCHDOWN_LATITUDE = _FlightSim_Misc_PLANE_TOUCHDOWN_LATITUDE(flightSim)
        self.PLANE_TOUCHDOWN_LONGITUDE = _FlightSim_Misc_PLANE_TOUCHDOWN_LONGITUDE(flightSim)
        self.PLANE_TOUCHDOWN_NORMAL_VELOCITY = _FlightSim_Misc_PLANE_TOUCHDOWN_NORMAL_VELOCITY(flightSim)
        self.PLANE_TOUCHDOWN_PITCH_DEGREES = _FlightSim_Misc_PLANE_TOUCHDOWN_PITCH_DEGREES(flightSim)
        self.RELATIVE_WIND_VELOCITY_BODY_X = _FlightSim_Misc_RELATIVE_WIND_VELOCITY_BODY_X(flightSim)
        self.RELATIVE_WIND_VELOCITY_BODY_Y = _FlightSim_Misc_RELATIVE_WIND_VELOCITY_BODY_Y(flightSim)
        self.RELATIVE_WIND_VELOCITY_BODY_Z = _FlightSim_Misc_RELATIVE_WIND_VELOCITY_BODY_Z(flightSim)
        self.ROTATION_ACCELERATION_BODY_X = _FlightSim_Misc_ROTATION_ACCELERATION_BODY_X(flightSim)
        self.ROTATION_ACCELERATION_BODY_Y = _FlightSim_Misc_ROTATION_ACCELERATION_BODY_Y(flightSim)
        self.ROTATION_ACCELERATION_BODY_Z = _FlightSim_Misc_ROTATION_ACCELERATION_BODY_Z(flightSim)
        self.ROTATION_VELOCITY_BODY_X = _FlightSim_Misc_ROTATION_VELOCITY_BODY_X(flightSim)
        self.ROTATION_VELOCITY_BODY_Y = _FlightSim_Misc_ROTATION_VELOCITY_BODY_Y(flightSim)
        self.ROTATION_VELOCITY_BODY_Z = _FlightSim_Misc_ROTATION_VELOCITY_BODY_Z(flightSim)
        self.SLOPE_TO_ATC_RUNWAY = _FlightSim_Misc_SLOPE_TO_ATC_RUNWAY(flightSim)
        self.VELOCITY_BODY_X = _FlightSim_Misc_VELOCITY_BODY_X(flightSim)
        self.VELOCITY_BODY_Y = _FlightSim_Misc_VELOCITY_BODY_Y(flightSim)
        self.VELOCITY_BODY_Z = _FlightSim_Misc_VELOCITY_BODY_Z(flightSim)
        self.VERTICAL_SPEED = _FlightSim_Misc_VERTICAL_SPEED(flightSim)
        self.EYEPOINT_POSITION = _FlightSim_Misc_EYEPOINT_POSITION(flightSim)
        self.STRUC_AIRSPEED_HOLD_PID_CONSTS = _FlightSim_Misc_STRUC_AIRSPEED_HOLD_PID_CONSTS(flightSim)
        self.STRUC_HEADING_HOLD_PID_CONSTS = _FlightSim_Misc_STRUC_HEADING_HOLD_PID_CONSTS(flightSim)
        self.STRUCT_BODY_ROTATION_ACCELERATION = _FlightSim_Misc_STRUCT_BODY_ROTATION_ACCELERATION(flightSim)
        self.STRUCT_BODY_ROTATION_VELOCITY = _FlightSim_Misc_STRUCT_BODY_ROTATION_VELOCITY(flightSim)
        self.STRUCT_BODY_VELOCITY = _FlightSim_Misc_STRUCT_BODY_VELOCITY(flightSim)
        self.STRUCT_ENGINE_POSITION = lambda index: _FlightSim_Misc_STRUCT_ENGINE_POSITION(flightSim, index)
        self.STRUCT_EYEPOINT_DYNAMIC_ANGLE = _FlightSim_Misc_STRUCT_EYEPOINT_DYNAMIC_ANGLE(flightSim)
        self.STRUCT_EYEPOINT_DYNAMIC_OFFSET = _FlightSim_Misc_STRUCT_EYEPOINT_DYNAMIC_OFFSET(flightSim)
        self.STRUCT_LATLONALT = _FlightSim_Misc_STRUCT_LATLONALT(flightSim)
        self.STRUCT_LATLONALTPBH = _FlightSim_Misc_STRUCT_LATLONALTPBH(flightSim)
        self.AIRCRAFT_WIND_X = _FlightSim_Misc_AIRCRAFT_WIND_X(flightSim)
        self.AIRCRAFT_WIND_Y = _FlightSim_Misc_AIRCRAFT_WIND_Y(flightSim)
        self.AIRCRAFT_WIND_Z = _FlightSim_Misc_AIRCRAFT_WIND_Z(flightSim)
        self.AIRSPEED_BARBER_POLE = _FlightSim_Misc_AIRSPEED_BARBER_POLE(flightSim)
        self.AIRSPEED_INDICATED = _FlightSim_Misc_AIRSPEED_INDICATED(flightSim)
        self.AIRSPEED_MACH = _FlightSim_Misc_AIRSPEED_MACH(flightSim)
        self.AIRSPEED_SELECT_INDICATED_OR_TRUE = _FlightSim_Misc_AIRSPEED_SELECT_INDICATED_OR_TRUE(flightSim)
        self.AIRSPEED_TRUE = _FlightSim_Misc_AIRSPEED_TRUE(flightSim)
        self.AIRSPEED_TRUE_RAW = _FlightSim_Misc_AIRSPEED_TRUE_RAW(flightSim)
        self.BARBER_POLE_MACH = _FlightSim_Misc_BARBER_POLE_MACH(flightSim)
        self.TOTAL_VELOCITY = _FlightSim_Misc_TOTAL_VELOCITY(flightSim)
        self.WINDSHIELD_WIND_VELOCITY = _FlightSim_Misc_WINDSHIELD_WIND_VELOCITY(flightSim)
        self.STANDARD_ATM_TEMPERATURE = _FlightSim_Misc_STANDARD_ATM_TEMPERATURE(flightSim)
        self.TOTAL_AIR_TEMPERATURE = _FlightSim_Misc_TOTAL_AIR_TEMPERATURE(flightSim)


# True if the aircraft is in a cloud.
class _FlightSim_Misc_AMBIENT_IN_CLOUD:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AMBIENT IN CLOUD,{unit.value})")


# True if the aircraft has met the conditions required to spawn the contrail VFX.
class _FlightSim_Misc_CONTRAILS_CONDITIONS_MET:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:CONTRAILS CONDITIONS MET,{unit.value})")


# True if slew is active.
class _FlightSim_Misc_IS_SLEW_ACTIVE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:IS SLEW ACTIVE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:IS SLEW ACTIVE,{unit.value})")


# True if slew is enabled.
class _FlightSim_Misc_IS_SLEW_ALLOWED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:IS SLEW ALLOWED,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:IS SLEW ALLOWED,{unit.value})")


# Is this the user loaded aircraft.
class _FlightSim_Misc_IS_USER_SIM:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:IS USER SIM,{unit.value})")


# Whether or not the plane is currently on a runway.
class _FlightSim_Misc_ON_ANY_RUNWAY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:ON ANY RUNWAY,{unit.value})")


# Whether or not the plane is currently parked (true) or not (false).
class _FlightSim_Misc_PLANE_IN_PARKING_STATE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:PLANE IN PARKING STATE,{unit.value})")


# The state of the surface directly under the aircraft.
class _FlightSim_Misc_SURFACE_CONDITION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        NORMAL = 0
        WET = 1
        ICY = 2
        SNOW = 3

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:SURFACE CONDITION,{unit.value})")


# True indicates that the SURFACE CONDITION return value is meaningful.
class _FlightSim_Misc_SURFACE_INFO_VALID:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:SURFACE INFO VALID,{unit.value})")


# The type of surface under the aircraft.
class _FlightSim_Misc_SURFACE_TYPE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        CONCRETE = 0
        GRASS = 1
        WATER = 2
        GRASS_BUMPY = 3
        ASPHALT = 4
        SHORT_GRASS = 5
        LONG_GRASS = 6
        HARD_TURF = 7
        SNOW = 8
        ICE = 9
        URBAN = 10
        FOREST = 11
        DIRT = 12
        CORAL = 13
        GRAVEL = 14
        OIL_TREATED = 15
        STEEL_MATS = 16
        BITUMINUS = 17
        BRICK = 18
        MACADAM = 19
        PLANKS = 20
        SAND = 21
        SHALE = 22
        TARMAC = 23
        WRIGHT_FLYER_TRACK = 24

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:SURFACE TYPE,{unit.value})")


# Amount of ice on aircraft structure. 100 is fully iced.
class _FlightSim_Misc_STRUCTURAL_ICE_PCT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:STRUCTURAL ICE PCT,{unit.value})")


# Title from aircraft.cfg.
class _FlightSim_Misc_TITLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.STRING'):
        # unit: String (max 128 chars)
        return self._.get(f"(A:TITLE,{unit.value})")


# True if a towline is connected to both tow plane and glider.
class _FlightSim_Misc_TOW_CONNECTION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:TOW CONNECTION,{unit.value})")


# Is visual effect available on this aircraft.
class _FlightSim_Misc_WINDSHIELD_RAIN_EFFECT_AVAILABLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:WINDSHIELD RAIN EFFECT AVAILABLE,{unit.value})")


# Acceleration relative to aircraft X axis, in east/west direction.
class _FlightSim_Misc_ACCELERATION_BODY_X:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Acceleration.FEET_PER_SECOND_SQUARED'):
        return self._.get(f"(A:ACCELERATION BODY X,{unit.value})")


# Acceleration relative to aircraft Y axis, in vertical direction.
class _FlightSim_Misc_ACCELERATION_BODY_Y:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Acceleration.FEET_PER_SECOND_SQUARED'):
        return self._.get(f"(A:ACCELERATION BODY Y,{unit.value})")


# Acceleration relative to aircraft Z axis, in north/south direction.
class _FlightSim_Misc_ACCELERATION_BODY_Z:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Acceleration.FEET_PER_SECOND_SQUARED'):
        return self._.get(f"(A:ACCELERATION BODY Z,{unit.value})")


# Acceleration relative to the earth X axis, in east/west direction.
class _FlightSim_Misc_ACCELERATION_WORLD_X:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Acceleration.FEET_PER_SECOND_SQUARED'):
        return self._.get(f"(A:ACCELERATION WORLD X,{unit.value})")


# Acceleration relative to the earth Y axis, in vertical direction.
class _FlightSim_Misc_ACCELERATION_WORLD_Y:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Acceleration.FEET_PER_SECOND_SQUARED'):
        return self._.get(f"(A:ACCELERATION WORLD Y,{unit.value})")


# Acceleration relative to the earth Z axis, in north/south direction.
class _FlightSim_Misc_ACCELERATION_WORLD_Z:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Acceleration.FEET_PER_SECOND_SQUARED'):
        return self._.get(f"(A:ACCELERATION WORLD Z,{unit.value})")


# The speed of the aircraft relative to the speed of the first surface directly underneath it. Use this to retrieve, for example, an aircraft's taxiing speed while it is moving on a moving carrier. It also applies to airborne aircraft, for example when a helicopter is successfully hovering above a moving ship, this value should be zero. The returned value will be the same as GROUND VELOCITY if the first surface beneath it is not moving.
class _FlightSim_Misc_SURFACE_RELATIVE_GROUND_SPEED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.FEET_PER_SECOND'):
        return self._.get(f"(A:SURFACE RELATIVE GROUND SPEED,{unit.value})")


# Speed relative to the earths surface.
# NOTE: This is available in multiplayer to all far aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_Misc_GROUND_VELOCITY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.KNOT'):
        return self._.get(f"(A:GROUND VELOCITY,{unit.value})")


# Altitude of aircraft.
class _FlightSim_Misc_PLANE_ALTITUDE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.FOOT'):
        return self._.get(f"(A:PLANE ALTITUDE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Length.FOOT', value: str):
        self._.set(f"{value} (>A:PLANE ALTITUDE,{unit.value})")


# Altitude above the surface.
class _FlightSim_Misc_PLANE_ALT_ABOVE_GROUND:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.FOOT'):
        return self._.get(f"(A:PLANE ALT ABOVE GROUND,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Length.FOOT', value: str):
        self._.set(f"{value} (>A:PLANE ALT ABOVE GROUND,{unit.value})")


# Altitude above the surface minus CG.
class _FlightSim_Misc_PLANE_ALT_ABOVE_GROUND_MINUS_CG:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.FOOT'):
        return self._.get(f"(A:PLANE ALT ABOVE GROUND MINUS CG,{unit.value})")


# Bank angle, although the name mentions degrees the units used are radians.
class _FlightSim_Misc_PLANE_BANK_DEGREES:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:PLANE BANK DEGREES,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Angle.RADIAN', value: str):
        self._.set(f"{value} (>A:PLANE BANK DEGREES,{unit.value})")


# Heading indicator taken from the aircraft gyro.
class _FlightSim_Misc_PLANE_HEADING_DEGREES_GYRO:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:PLANE HEADING DEGREES GYRO,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Angle.DEGREE', value: str):
        self._.set(f"{value} (>A:PLANE HEADING DEGREES GYRO,{unit.value})")


# Heading relative to magnetic north - although the name mentions degrees the units used are radians.
class _FlightSim_Misc_PLANE_HEADING_DEGREES_MAGNETIC:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:PLANE HEADING DEGREES MAGNETIC,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Angle.RADIAN', value: str):
        self._.set(f"{value} (>A:PLANE HEADING DEGREES MAGNETIC,{unit.value})")


# Heading relative to true north - although the name mentions degrees the units used are radians.
class _FlightSim_Misc_PLANE_HEADING_DEGREES_TRUE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:PLANE HEADING DEGREES TRUE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Angle.RADIAN', value: str):
        self._.set(f"{value} (>A:PLANE HEADING DEGREES TRUE,{unit.value})")


# Latitude of aircraft, North is positive, South negative.
class _FlightSim_Misc_PLANE_LATITUDE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:PLANE LATITUDE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Angle.RADIAN', value: str):
        self._.set(f"{value} (>A:PLANE LATITUDE,{unit.value})")


# Longitude of aircraft, East is positive, West negative.
class _FlightSim_Misc_PLANE_LONGITUDE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:PLANE LONGITUDE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Angle.RADIAN', value: str):
        self._.set(f"{value} (>A:PLANE LONGITUDE,{unit.value})")


# Pitch angle, although the name mentions degrees the units used are radians.
class _FlightSim_Misc_PLANE_PITCH_DEGREES:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:PLANE PITCH DEGREES,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Angle.RADIAN', value: str):
        self._.set(f"{value} (>A:PLANE PITCH DEGREES,{unit.value})")


# This float represents the bank of the player's plane from the last touchdown.
class _FlightSim_Misc_PLANE_TOUCHDOWN_BANK_DEGREES:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:PLANE TOUCHDOWN BANK DEGREES,{unit.value})")


# This float represents the magnetic heading of the player's plane from the last touchdown.
class _FlightSim_Misc_PLANE_TOUCHDOWN_HEADING_DEGREES_MAGNETIC:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:PLANE TOUCHDOWN HEADING DEGREES MAGNETIC,{unit.value})")


# This float represents the true heading of the player's plane from the last touchdown.
class _FlightSim_Misc_PLANE_TOUCHDOWN_HEADING_DEGREES_TRUE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:PLANE TOUCHDOWN HEADING DEGREES TRUE,{unit.value})")


# This float represents the plane latitude for the last touchdown.
class _FlightSim_Misc_PLANE_TOUCHDOWN_LATITUDE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:PLANE TOUCHDOWN LATITUDE,{unit.value})")


# This float represents the plane longitude for the last touchdown.
class _FlightSim_Misc_PLANE_TOUCHDOWN_LONGITUDE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:PLANE TOUCHDOWN LONGITUDE,{unit.value})")


# This float represents the player's plane speed according to ground normal from the last touchdown.
class _FlightSim_Misc_PLANE_TOUCHDOWN_NORMAL_VELOCITY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.FEET_PER_SECOND'):
        return self._.get(f"(A:PLANE TOUCHDOWN NORMAL VELOCITY,{unit.value})")


# This float represents the pitch of the player's plane from the last touchdown.
class _FlightSim_Misc_PLANE_TOUCHDOWN_PITCH_DEGREES:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:PLANE TOUCHDOWN PITCH DEGREES,{unit.value})")


# Lateral (X axis) speed relative to wind.
class _FlightSim_Misc_RELATIVE_WIND_VELOCITY_BODY_X:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.FEET_PER_SECOND'):
        return self._.get(f"(A:RELATIVE WIND VELOCITY BODY X,{unit.value})")


# Vertical (Y axis) speed relative to wind.
class _FlightSim_Misc_RELATIVE_WIND_VELOCITY_BODY_Y:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.FEET_PER_SECOND'):
        return self._.get(f"(A:RELATIVE WIND VELOCITY BODY Y,{unit.value})")


# Longitudinal (Z axis) speed relative to wind.
class _FlightSim_Misc_RELATIVE_WIND_VELOCITY_BODY_Z:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.FEET_PER_SECOND'):
        return self._.get(f"(A:RELATIVE WIND VELOCITY BODY Z,{unit.value})")


# Rotation acceleration relative to aircraft X axis.
class _FlightSim_Misc_ROTATION_ACCELERATION_BODY_X:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.AngularAcceleration.RADIAN_PER_SECOND_SQUARED'):
        return self._.get(f"(A:ROTATION ACCELERATION BODY X,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.AngularAcceleration.RADIAN_PER_SECOND_SQUARED', value: str):
        self._.set(f"{value} (>A:ROTATION ACCELERATION BODY X,{unit.value})")


# Rotation acceleration relative to aircraft Y axis.
class _FlightSim_Misc_ROTATION_ACCELERATION_BODY_Y:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.AngularAcceleration.RADIAN_PER_SECOND_SQUARED'):
        return self._.get(f"(A:ROTATION ACCELERATION BODY Y,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.AngularAcceleration.RADIAN_PER_SECOND_SQUARED', value: str):
        self._.set(f"{value} (>A:ROTATION ACCELERATION BODY Y,{unit.value})")


# Rotation acceleration relative to aircraft Z axis.
class _FlightSim_Misc_ROTATION_ACCELERATION_BODY_Z:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.AngularAcceleration.RADIAN_PER_SECOND_SQUARED'):
        return self._.get(f"(A:ROTATION ACCELERATION BODY Z,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.AngularAcceleration.RADIAN_PER_SECOND_SQUARED', value: str):
        self._.set(f"{value} (>A:ROTATION ACCELERATION BODY Z,{unit.value})")


# Rotation velocity relative to aircraft X axis.
class _FlightSim_Misc_ROTATION_VELOCITY_BODY_X:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.FEET_PER_SECOND'):
        return self._.get(f"(A:ROTATION VELOCITY BODY X,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Speed.FEET_PER_SECOND', value: str):
        self._.set(f"{value} (>A:ROTATION VELOCITY BODY X,{unit.value})")


# Rotation velocity relative to aircraft Y axis.
class _FlightSim_Misc_ROTATION_VELOCITY_BODY_Y:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.FEET_PER_SECOND'):
        return self._.get(f"(A:ROTATION VELOCITY BODY Y,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Speed.FEET_PER_SECOND', value: str):
        self._.set(f"{value} (>A:ROTATION VELOCITY BODY Y,{unit.value})")


# Rotation velocity relative to aircraft Z axis.
class _FlightSim_Misc_ROTATION_VELOCITY_BODY_Z:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.FEET_PER_SECOND'):
        return self._.get(f"(A:ROTATION VELOCITY BODY Z,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Speed.FEET_PER_SECOND', value: str):
        self._.set(f"{value} (>A:ROTATION VELOCITY BODY Z,{unit.value})")


# The slope between the plane and the expected landing position of the runway. Returns 0 if no runway is assigned.
class _FlightSim_Misc_SLOPE_TO_ATC_RUNWAY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:SLOPE TO ATC RUNWAY,{unit.value})")


# True lateral speed, relative to aircraft X axis.
class _FlightSim_Misc_VELOCITY_BODY_X:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.FEET_PER_SECOND'):
        return self._.get(f"(A:VELOCITY BODY X,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Speed.FEET_PER_SECOND', value: str):
        self._.set(f"{value} (>A:VELOCITY BODY X,{unit.value})")


# True vertical speed, relative to aircraft Y axis.
class _FlightSim_Misc_VELOCITY_BODY_Y:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.FEET_PER_SECOND'):
        return self._.get(f"(A:VELOCITY BODY Y,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Speed.FEET_PER_SECOND', value: str):
        self._.set(f"{value} (>A:VELOCITY BODY Y,{unit.value})")


# True longitudinal speed, relative to aircraft Z axis.
class _FlightSim_Misc_VELOCITY_BODY_Z:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.FEET_PER_SECOND'):
        return self._.get(f"(A:VELOCITY BODY Z,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Speed.FEET_PER_SECOND', value: str):
        self._.set(f"{value} (>A:VELOCITY BODY Z,{unit.value})")


# The current indicated vertical speed for the aircraft.
class _FlightSim_Misc_VERTICAL_SPEED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.FEET_PER_SECOND'):
        return self._.get(f"(A:VERTICAL SPEED,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Speed.FEET_PER_SECOND', value: str):
        self._.set(f"{value} (>A:VERTICAL SPEED,{unit.value})")


# The eyepoint position relative to the reference datum position for the aircraft.
#! SIMCONNECT_DATA_XYZ
# feet
class _FlightSim_Misc_EYEPOINT_POSITION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: ''):
        return self._.get(f"(A:EYEPOINT POSITION,{unit.value})")


# Returns the various airspeed PID constants. This is generally only used for AI controlled aircraft and boats, although it may be useful when working with RTCs and the user aircraft.
#! PID_STRUCT
class _FlightSim_Misc_STRUC_AIRSPEED_HOLD_PID_CONSTS:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: ''):
        return self._.get(f"(A:STRUC AIRSPEED HOLD PID CONSTS,{unit.value})")


# Returns the various airspeed PID constants. This is generally only used for AI controlled aircraft and boats, although it may be useful when working with RTCs and the user aircraft.
#! PID_STRUCT
class _FlightSim_Misc_STRUC_HEADING_HOLD_PID_CONSTS:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: ''):
        return self._.get(f"(A:STRUC HEADING HOLD PID CONSTS,{unit.value})")


# The body rotation acceleration.
#! SIMCONNECT_DATA_XYZ
# radians per second
class _FlightSim_Misc_STRUCT_BODY_ROTATION_ACCELERATION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: ''):
        return self._.get(f"(A:STRUCT BODY ROTATION ACCELERATION,{unit.value})")


# The body rotation velocity.
#! SIMCONNECT_DATA_XYZ
# radians per second
class _FlightSim_Misc_STRUCT_BODY_ROTATION_VELOCITY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: ''):
        return self._.get(f"(A:STRUCT BODY ROTATION VELOCITY,{unit.value})")


# The object body velocity.
#! SIMCONNECT_DATA_XYZ
# feet per second
class _FlightSim_Misc_STRUCT_BODY_VELOCITY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: ''):
        return self._.get(f"(A:STRUCT BODY VELOCITY,{unit.value})")


# The position of the indexed engine relative to the Datum Reference Point for the aircraft.
#! SIMCONNECT_DATA_XYZ
# feet.
class _FlightSim_Misc_STRUCT_ENGINE_POSITION:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: ''):
        return self._.get(f"(A:STRUCT ENGINE POSITION:{self._index},{unit.value})")


# The angle of the eyepoint view. Zero, zero, zero is straight ahead.
#! SIMCONNECT_DATA_XYZ
# radians
class _FlightSim_Misc_STRUCT_EYEPOINT_DYNAMIC_ANGLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: ''):
        return self._.get(f"(A:STRUCT EYEPOINT DYNAMIC ANGLE,{unit.value})")


# A variable offset away from the EYEPOINT POSITION.
#! SIMCONNECT_DATA_XYZ
# feet
class _FlightSim_Misc_STRUCT_EYEPOINT_DYNAMIC_OFFSET:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: ''):
        return self._.get(f"(A:STRUCT EYEPOINT DYNAMIC OFFSET,{unit.value})")


# Returns the latitude, longitude and altitude of the user aircraft.
#! SIMCONNECT_DATA_LATLONALT
class _FlightSim_Misc_STRUCT_LATLONALT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: ''):
        return self._.get(f"(A:STRUCT LATLONALT,{unit.value})")


# Returns the lattitude, longitude, altitude, pitch, bank and heading of the user aircraft.
#! Returns a struct with 6 values: lat, lon, alt, pitch, bank, heading
class _FlightSim_Misc_STRUCT_LATLONALTPBH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: ''):
        return self._.get(f"(A:STRUCT LATLONALTPBH,{unit.value})")


# Wind component in aircraft lateral (X) axis.
class _FlightSim_Misc_AIRCRAFT_WIND_X:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.KNOT'):
        return self._.get(f"(A:AIRCRAFT WIND X,{unit.value})")


# Wind component in aircraft vertical (Y) axis.
class _FlightSim_Misc_AIRCRAFT_WIND_Y:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.KNOT'):
        return self._.get(f"(A:AIRCRAFT WIND Y,{unit.value})")


# Wind component in aircraft longitudinal (Z) axis.
class _FlightSim_Misc_AIRCRAFT_WIND_Z:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.KNOT'):
        return self._.get(f"(A:AIRCRAFT WIND Z,{unit.value})")


# Redline airspeed (dynamic on some aircraft).
class _FlightSim_Misc_AIRSPEED_BARBER_POLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.KNOT'):
        return self._.get(f"(A:AIRSPEED BARBER POLE,{unit.value})")


# Indicated airspeed.
class _FlightSim_Misc_AIRSPEED_INDICATED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.KNOT'):
        return self._.get(f"(A:AIRSPEED INDICATED,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Speed.KNOT', value: str):
        self._.set(f"{value} (>A:AIRSPEED INDICATED,{unit.value})")


# Current mach.
class _FlightSim_Misc_AIRSPEED_MACH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.MACH'):
        return self._.get(f"(A:AIRSPEED MACH,{unit.value})")


# The airspeed, whether true or indicated airspeed has been selected.
class _FlightSim_Misc_AIRSPEED_SELECT_INDICATED_OR_TRUE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.KNOT'):
        return self._.get(f"(A:AIRSPEED SELECT INDICATED OR TRUE,{unit.value})")


# True airspeed.
class _FlightSim_Misc_AIRSPEED_TRUE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.KNOT'):
        return self._.get(f"(A:AIRSPEED TRUE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Speed.KNOT', value: str):
        self._.set(f"{value} (>A:AIRSPEED TRUE,{unit.value})")


# Equivalent to AIRSPEED TRUE, but does not account for wind when used to Set Airspeed value
class _FlightSim_Misc_AIRSPEED_TRUE_RAW:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.KNOT'):
        return self._.get(f"(A:AIRSPEED TRUE RAW,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Speed.KNOT', value: str):
        self._.set(f"{value} (>A:AIRSPEED TRUE RAW,{unit.value})")


# Mach associated with maximum airspeed.
class _FlightSim_Misc_BARBER_POLE_MACH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.MACH'):
        return self._.get(f"(A:BARBER POLE MACH,{unit.value})")


# Velocity regardless of direction. For example, if a helicopter is ascending vertically at 100 fps, getting this variable will return 100.
class _FlightSim_Misc_TOTAL_VELOCITY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.FEET_PER_SECOND'):
        return self._.get(f"(A:TOTAL VELOCITY,{unit.value})")


# Longitudinal speed of wind on the windshield.
class _FlightSim_Misc_WINDSHIELD_WIND_VELOCITY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.FEET_PER_SECOND'):
        return self._.get(f"(A:WINDSHIELD WIND VELOCITY,{unit.value})")


# Outside temperature on the standard ATM scale.
class _FlightSim_Misc_STANDARD_ATM_TEMPERATURE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Temperature.RANKINE'):
        return self._.get(f"(A:STANDARD ATM TEMPERATURE,{unit.value})")


# Total air temperature is the air temperature at the front of the aircraft where the ram pressure from the speed of the aircraft is taken into account.
class _FlightSim_Misc_TOTAL_AIR_TEMPERATURE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Temperature.CELSIUS'):
        return self._.get(f"(A:TOTAL AIR TEMPERATURE,{unit.value})")


class _FlightSim_Radio:
    def __init__(self, flightSim):
        self._ = flightSim
        self.ADF_ACTIVE_FREQUENCY = lambda index: _FlightSim_Radio_ADF_ACTIVE_FREQUENCY(flightSim, index)
        self.ADF_AVAILABLE = lambda index: _FlightSim_Radio_ADF_AVAILABLE(flightSim, index)
        self.ADF_CARD = _FlightSim_Radio_ADF_CARD(flightSim)
        self.ADF_EXT_FREQUENCY = _FlightSim_Radio_ADF_EXT_FREQUENCY(flightSim)
        self.ADF_FREQUENCY = _FlightSim_Radio_ADF_FREQUENCY(flightSim)
        self.ADF_IDENT = _FlightSim_Radio_ADF_IDENT(flightSim)
        self.ADF_LATLONALT = lambda index: _FlightSim_Radio_ADF_LATLONALT(flightSim, index)
        self.ADF_NAME = lambda index: _FlightSim_Radio_ADF_NAME(flightSim, index)
        self.ADF_RADIAL = lambda index: _FlightSim_Radio_ADF_RADIAL(flightSim, index)
        self.ADF_RADIAL_MAG = lambda index: _FlightSim_Radio_ADF_RADIAL_MAG(flightSim, index)
        self.ADF_SIGNAL = lambda index: _FlightSim_Radio_ADF_SIGNAL(flightSim, index)
        self.ADF_SOUND = lambda index: _FlightSim_Radio_ADF_SOUND(flightSim, index)
        self.ADF_STANDBY_AVAILABLE = lambda index: _FlightSim_Radio_ADF_STANDBY_AVAILABLE(flightSim, index)
        self.ADF_STANDBY_FREQUENCY = lambda index: _FlightSim_Radio_ADF_STANDBY_FREQUENCY(flightSim, index)
        self.ADF_VOLUME = _FlightSim_Radio_ADF_VOLUME(flightSim)
        self.ATC_AIRLINE = _FlightSim_Radio_ATC_AIRLINE(flightSim)
        self.ATC_AIRPORT_IS_TOWERED = _FlightSim_Radio_ATC_AIRPORT_IS_TOWERED(flightSim)
        self.ATC_CLEARED_IFR = _FlightSim_Radio_ATC_CLEARED_IFR(flightSim)
        self.ATC_CLEARED_LANDING = _FlightSim_Radio_ATC_CLEARED_LANDING(flightSim)
        self.ATC_CLEARED_TAKEOFF = _FlightSim_Radio_ATC_CLEARED_TAKEOFF(flightSim)
        self.ATC_CLEARED_TAXI = _FlightSim_Radio_ATC_CLEARED_TAXI(flightSim)
        self.ATC_CURRENT_WAYPOINT_ALTITUDE = _FlightSim_Radio_ATC_CURRENT_WAYPOINT_ALTITUDE(flightSim)
        self.ATC_FLIGHT_NUMBER = _FlightSim_Radio_ATC_FLIGHT_NUMBER(flightSim)
        self.ATC_FLIGHTPLAN_DIFF_ALT = _FlightSim_Radio_ATC_FLIGHTPLAN_DIFF_ALT(flightSim)
        self.ATC_FLIGHTPLAN_DIFF_DISTANCE = _FlightSim_Radio_ATC_FLIGHTPLAN_DIFF_DISTANCE(flightSim)
        self.ATC_FLIGHTPLAN_DIFF_HEADING = _FlightSim_Radio_ATC_FLIGHTPLAN_DIFF_HEADING(flightSim)
        self.ATC_HEAVY = _FlightSim_Radio_ATC_HEAVY(flightSim)
        self.ATC_ID = _FlightSim_Radio_ATC_ID(flightSim)
        self.ATC_IFR_FP_TO_REQUEST = _FlightSim_Radio_ATC_IFR_FP_TO_REQUEST(flightSim)
        self.ATC_MODEL = _FlightSim_Radio_ATC_MODEL(flightSim)
        self.ATC_ON_PARKING_SPOT = _FlightSim_Radio_ATC_ON_PARKING_SPOT(flightSim)
        self.ATC_PREVIOUS_WAYPOINT_ALTITUDE = _FlightSim_Radio_ATC_PREVIOUS_WAYPOINT_ALTITUDE(flightSim)
        self.ATC_RUNWAY_AIRPORT_NAME = _FlightSim_Radio_ATC_RUNWAY_AIRPORT_NAME(flightSim)
        self.ATC_RUNWAY_DISTANCE = _FlightSim_Radio_ATC_RUNWAY_DISTANCE(flightSim)
        self.ATC_RUNWAY_END_DISTANCE = _FlightSim_Radio_ATC_RUNWAY_END_DISTANCE(flightSim)
        self.ATC_RUNWAY_HEADING_DEGREES_TRUE = _FlightSim_Radio_ATC_RUNWAY_HEADING_DEGREES_TRUE(flightSim)
        self.ATC_RUNWAY_LENGTH = _FlightSim_Radio_ATC_RUNWAY_LENGTH(flightSim)
        self.ATC_RUNWAY_RELATIVE_POSITION_X = _FlightSim_Radio_ATC_RUNWAY_RELATIVE_POSITION_X(flightSim)
        self.ATC_RUNWAY_RELATIVE_POSITION_Y = _FlightSim_Radio_ATC_RUNWAY_RELATIVE_POSITION_Y(flightSim)
        self.ATC_RUNWAY_RELATIVE_POSITION_Z = _FlightSim_Radio_ATC_RUNWAY_RELATIVE_POSITION_Z(flightSim)
        self.ATC_RUNWAY_SELECTED = _FlightSim_Radio_ATC_RUNWAY_SELECTED(flightSim)
        self.ATC_RUNWAY_START_DISTANCE = _FlightSim_Radio_ATC_RUNWAY_START_DISTANCE(flightSim)
        self.ATC_RUNWAY_TDPOINT_RELATIVE_POSITION_X = _FlightSim_Radio_ATC_RUNWAY_TDPOINT_RELATIVE_POSITION_X(flightSim)
        self.ATC_RUNWAY_TDPOINT_RELATIVE_POSITION_Y = _FlightSim_Radio_ATC_RUNWAY_TDPOINT_RELATIVE_POSITION_Y(flightSim)
        self.ATC_RUNWAY_TDPOINT_RELATIVE_POSITION_Z = _FlightSim_Radio_ATC_RUNWAY_TDPOINT_RELATIVE_POSITION_Z(flightSim)
        self.ATC_RUNWAY_WIDTH = _FlightSim_Radio_ATC_RUNWAY_WIDTH(flightSim)
        self.ATC_SUGGESTED_MIN_RWY_LANDING = _FlightSim_Radio_ATC_SUGGESTED_MIN_RWY_LANDING(flightSim)
        self.ATC_SUGGESTED_MIN_RWY_TAKEOFF = _FlightSim_Radio_ATC_SUGGESTED_MIN_RWY_TAKEOFF(flightSim)
        self.ATC_TAXIPATH_DISTANCE = _FlightSim_Radio_ATC_TAXIPATH_DISTANCE(flightSim)
        self.ATC_TYPE = _FlightSim_Radio_ATC_TYPE(flightSim)
        self.COM1_STORED_FREQUENCY = _FlightSim_Radio_COM1_STORED_FREQUENCY(flightSim)
        self.COM_ACTIVE_BEARING = lambda index: _FlightSim_Radio_COM_ACTIVE_BEARING(flightSim, index)
        self.COM_ACTIVE_DISTANCE = lambda index: _FlightSim_Radio_COM_ACTIVE_DISTANCE(flightSim, index)
        self.COM_ACTIVE_FREQUENCY = lambda index: _FlightSim_Radio_COM_ACTIVE_FREQUENCY(flightSim, index)
        self.COM_ACTIVE_FREQ_IDENT = lambda index: _FlightSim_Radio_COM_ACTIVE_FREQ_IDENT(flightSim, index)
        self.COM_ACTIVE_FREQ_TYPE = lambda index: _FlightSim_Radio_COM_ACTIVE_FREQ_TYPE(flightSim, index)
        self.COM_ACTIVE_LATLONALT = lambda index: _FlightSim_Radio_COM_ACTIVE_LATLONALT(flightSim, index)
        self.COM_AVAILABLE = lambda index: _FlightSim_Radio_COM_AVAILABLE(flightSim, index)
        self.COM_LATLONALT = lambda index: _FlightSim_Radio_COM_LATLONALT(flightSim, index)
        self.COM_RECEIVE = lambda index: _FlightSim_Radio_COM_RECEIVE(flightSim, index)
        self.COM_RECEIVE_ALL = _FlightSim_Radio_COM_RECEIVE_ALL(flightSim)
        self.COM_RECEIVE_EX1 = lambda index: _FlightSim_Radio_COM_RECEIVE_EX1(flightSim, index)
        self.COM_SPACING_MODE = lambda index: _FlightSim_Radio_COM_SPACING_MODE(flightSim, index)
        self.COM_STANDBY_FREQUENCY = lambda index: _FlightSim_Radio_COM_STANDBY_FREQUENCY(flightSim, index)
        self.COM_STANDBY_FREQ_IDENT = lambda index: _FlightSim_Radio_COM_STANDBY_FREQ_IDENT(flightSim, index)
        self.COM_STANDBY_FREQ_TYPE = lambda index: _FlightSim_Radio_COM_STANDBY_FREQ_TYPE(flightSim, index)
        self.COM_STATUS = lambda index: _FlightSim_Radio_COM_STATUS(flightSim, index)
        self.COM_TEST = lambda index: _FlightSim_Radio_COM_TEST(flightSim, index)
        self.COM_TRANSMIT = lambda index: _FlightSim_Radio_COM_TRANSMIT(flightSim, index)
        self.COM_VOLUME = _FlightSim_Radio_COM_VOLUME(flightSim)
        self.FLARM_AVAILABLE = _FlightSim_Radio_FLARM_AVAILABLE(flightSim)
        self.FLARM_THREAT_BEARING = _FlightSim_Radio_FLARM_THREAT_BEARING(flightSim)
        self.FLARM_THREAT_DATA = _FlightSim_Radio_FLARM_THREAT_DATA(flightSim)
        self.FLARM_THREAT_DISTANCE = _FlightSim_Radio_FLARM_THREAT_DISTANCE(flightSim)
        self.FLARM_THREAT_HEADING = _FlightSim_Radio_FLARM_THREAT_HEADING(flightSim)
        self.FLARM_THREAT_RELATIVE_ALTITUDE = _FlightSim_Radio_FLARM_THREAT_RELATIVE_ALTITUDE(flightSim)
        self.FLARM_THREAT_TIME_TO_COLLISION = _FlightSim_Radio_FLARM_THREAT_TIME_TO_COLLISION(flightSim)
        self.FLARM_THREAT_VERTICAL_BEARING = _FlightSim_Radio_FLARM_THREAT_VERTICAL_BEARING(flightSim)
        self.GPS_APPROACH_AIRPORT_ID = _FlightSim_Radio_GPS_APPROACH_AIRPORT_ID(flightSim)
        self.GPS_APPROACH_APPROACH_ID = _FlightSim_Radio_GPS_APPROACH_APPROACH_ID(flightSim)
        self.GPS_APPROACH_APPROACH_INDEX = _FlightSim_Radio_GPS_APPROACH_APPROACH_INDEX(flightSim)
        self.GPS_APPROACH_APPROACH_TYPE = _FlightSim_Radio_GPS_APPROACH_APPROACH_TYPE(flightSim)
        self.GPS_APPROACH_IS_FINAL = _FlightSim_Radio_GPS_APPROACH_IS_FINAL(flightSim)
        self.GPS_APPROACH_IS_MISSED = _FlightSim_Radio_GPS_APPROACH_IS_MISSED(flightSim)
        self.GPS_APPROACH_IS_WP_RUNWAY = _FlightSim_Radio_GPS_APPROACH_IS_WP_RUNWAY(flightSim)
        self.GPS_APPROACH_MODE = _FlightSim_Radio_GPS_APPROACH_MODE(flightSim)
        self.GPS_APPROACH_SEGMENT_TYPE = _FlightSim_Radio_GPS_APPROACH_SEGMENT_TYPE(flightSim)
        self.GPS_APPROACH_TIMEZONE_DEVIATION = _FlightSim_Radio_GPS_APPROACH_TIMEZONE_DEVIATION(flightSim)
        self.GPS_APPROACH_TRANSITION_ID = _FlightSim_Radio_GPS_APPROACH_TRANSITION_ID(flightSim)
        self.GPS_APPROACH_TRANSITION_INDEX = _FlightSim_Radio_GPS_APPROACH_TRANSITION_INDEX(flightSim)
        self.GPS_APPROACH_WP_COUNT = _FlightSim_Radio_GPS_APPROACH_WP_COUNT(flightSim)
        self.GPS_APPROACH_WP_INDEX = _FlightSim_Radio_GPS_APPROACH_WP_INDEX(flightSim)
        self.GPS_APPROACH_WP_TYPE = _FlightSim_Radio_GPS_APPROACH_WP_TYPE(flightSim)
        self.GPS_CDI_NEEDLE = _FlightSim_Radio_GPS_CDI_NEEDLE(flightSim)
        self.GPS_CDI_SCALING = _FlightSim_Radio_GPS_CDI_SCALING(flightSim)
        self.GPS_COURSE_TO_STEER = _FlightSim_Radio_GPS_COURSE_TO_STEER(flightSim)
        self.GPS_DRIVES_NAV1 = _FlightSim_Radio_GPS_DRIVES_NAV1(flightSim)
        self.GPS_ETA = _FlightSim_Radio_GPS_ETA(flightSim)
        self.GPS_ETE = _FlightSim_Radio_GPS_ETE(flightSim)
        self.GPS_FLIGHTPLAN_TOTAL_DISTANCE = _FlightSim_Radio_GPS_FLIGHTPLAN_TOTAL_DISTANCE(flightSim)
        self.GPS_FLIGHT_PLAN_WP_COUNT = _FlightSim_Radio_GPS_FLIGHT_PLAN_WP_COUNT(flightSim)
        self.GPS_FLIGHT_PLAN_WP_INDEX = _FlightSim_Radio_GPS_FLIGHT_PLAN_WP_INDEX(flightSim)
        self.GPS_GROUND_MAGNETIC_TRACK = _FlightSim_Radio_GPS_GROUND_MAGNETIC_TRACK(flightSim)
        self.GPS_GROUND_SPEED = _FlightSim_Radio_GPS_GROUND_SPEED(flightSim)
        self.GPS_GROUND_TRUE_HEADING = _FlightSim_Radio_GPS_GROUND_TRUE_HEADING(flightSim)
        self.GPS_GROUND_TRUE_TRACK = _FlightSim_Radio_GPS_GROUND_TRUE_TRACK(flightSim)
        self.GPS_GSI_SCALING = _FlightSim_Radio_GPS_GSI_SCALING(flightSim)
        self.GPS_HAS_GLIDEPATH = _FlightSim_Radio_GPS_HAS_GLIDEPATH(flightSim)
        self.GPS_HSI_NEEDLE = _FlightSim_Radio_GPS_HSI_NEEDLE(flightSim)
        self.GPS_IS_ACTIVE_FLIGHT_PLAN = _FlightSim_Radio_GPS_IS_ACTIVE_FLIGHT_PLAN(flightSim)
        self.GPS_IS_ACTIVE_WAY_POINT = _FlightSim_Radio_GPS_IS_ACTIVE_WAY_POINT(flightSim)
        self.GPS_IS_ACTIVE_WP_LOCKED = _FlightSim_Radio_GPS_IS_ACTIVE_WP_LOCKED(flightSim)
        self.GPS_IS_APPROACH_ACTIVE = _FlightSim_Radio_GPS_IS_APPROACH_ACTIVE(flightSim)
        self.GPS_IS_APPROACH_LOADED = _FlightSim_Radio_GPS_IS_APPROACH_LOADED(flightSim)
        self.GPS_IS_ARRIVED = _FlightSim_Radio_GPS_IS_ARRIVED(flightSim)
        self.GPS_IS_DIRECTTO_FLIGHTPLAN = _FlightSim_Radio_GPS_IS_DIRECTTO_FLIGHTPLAN(flightSim)
        self.GPS_MAGVAR = _FlightSim_Radio_GPS_MAGVAR(flightSim)
        self.GPS_OBS_ACTIVE = _FlightSim_Radio_GPS_OBS_ACTIVE(flightSim)
        self.GPS_OBS_VALUE = _FlightSim_Radio_GPS_OBS_VALUE(flightSim)
        self.GPS_OVERRIDDEN = _FlightSim_Radio_GPS_OVERRIDDEN(flightSim)
        self.GPS_POSITION_ALT = _FlightSim_Radio_GPS_POSITION_ALT(flightSim)
        self.GPS_POSITION_LAT = _FlightSim_Radio_GPS_POSITION_LAT(flightSim)
        self.GPS_POSITION_LON = _FlightSim_Radio_GPS_POSITION_LON(flightSim)
        self.GPS_TARGET_ALTITUDE = _FlightSim_Radio_GPS_TARGET_ALTITUDE(flightSim)
        self.GPS_TARGET_DISTANCE = _FlightSim_Radio_GPS_TARGET_DISTANCE(flightSim)
        self.GPS_VERTICAL_ANGLE = _FlightSim_Radio_GPS_VERTICAL_ANGLE(flightSim)
        self.GPS_VERTICAL_ANGLE_ERROR = _FlightSim_Radio_GPS_VERTICAL_ANGLE_ERROR(flightSim)
        self.GPS_VERTICAL_ERROR = _FlightSim_Radio_GPS_VERTICAL_ERROR(flightSim)
        self.GPS_WP_BEARING = _FlightSim_Radio_GPS_WP_BEARING(flightSim)
        self.GPS_WP_CROSS_TRK = _FlightSim_Radio_GPS_WP_CROSS_TRK(flightSim)
        self.GPS_WP_DESIRED_TRACK = _FlightSim_Radio_GPS_WP_DESIRED_TRACK(flightSim)
        self.GPS_WP_DISTANCE = _FlightSim_Radio_GPS_WP_DISTANCE(flightSim)
        self.GPS_WP_ETA = _FlightSim_Radio_GPS_WP_ETA(flightSim)
        self.GPS_WP_ETE = _FlightSim_Radio_GPS_WP_ETE(flightSim)
        self.GPS_WP_NEXT_ALT = _FlightSim_Radio_GPS_WP_NEXT_ALT(flightSim)
        self.GPS_WP_NEXT_ID = _FlightSim_Radio_GPS_WP_NEXT_ID(flightSim)
        self.GPS_WP_NEXT_LAT = _FlightSim_Radio_GPS_WP_NEXT_LAT(flightSim)
        self.GPS_WP_NEXT_LON = _FlightSim_Radio_GPS_WP_NEXT_LON(flightSim)
        self.GPS_WP_PREV_ALT = _FlightSim_Radio_GPS_WP_PREV_ALT(flightSim)
        self.GPS_WP_PREV_ID = _FlightSim_Radio_GPS_WP_PREV_ID(flightSim)
        self.GPS_WP_PREV_LAT = _FlightSim_Radio_GPS_WP_PREV_LAT(flightSim)
        self.GPS_WP_PREV_LON = _FlightSim_Radio_GPS_WP_PREV_LON(flightSim)
        self.GPS_WP_PREV_VALID = _FlightSim_Radio_GPS_WP_PREV_VALID(flightSim)
        self.GPS_WP_TRACK_ANGLE_ERROR = _FlightSim_Radio_GPS_WP_TRACK_ANGLE_ERROR(flightSim)
        self.GPS_WP_TRUE_BEARING = _FlightSim_Radio_GPS_WP_TRUE_BEARING(flightSim)
        self.GPS_WP_TRUE_REQ_HDG = _FlightSim_Radio_GPS_WP_TRUE_REQ_HDG(flightSim)
        self.GPS_WP_VERTICAL_SPEED = _FlightSim_Radio_GPS_WP_VERTICAL_SPEED(flightSim)
        self.HSI_BEARING = _FlightSim_Radio_HSI_BEARING(flightSim)
        self.HSI_BEARING_VALID = _FlightSim_Radio_HSI_BEARING_VALID(flightSim)
        self.HSI_CDI_NEEDLE = _FlightSim_Radio_HSI_CDI_NEEDLE(flightSim)
        self.HSI_CDI_NEEDLE_VALID = _FlightSim_Radio_HSI_CDI_NEEDLE_VALID(flightSim)
        self.HSI_DISTANCE = _FlightSim_Radio_HSI_DISTANCE(flightSim)
        self.HSI_GSI_NEEDLE = _FlightSim_Radio_HSI_GSI_NEEDLE(flightSim)
        self.HSI_GSI_NEEDLE_VALID = _FlightSim_Radio_HSI_GSI_NEEDLE_VALID(flightSim)
        self.HSI_HAS_LOCALIZER = _FlightSim_Radio_HSI_HAS_LOCALIZER(flightSim)
        self.HSI_SPEED = _FlightSim_Radio_HSI_SPEED(flightSim)
        self.HSI_STATION_IDENT = _FlightSim_Radio_HSI_STATION_IDENT(flightSim)
        self.HSI_TF_FLAGS = _FlightSim_Radio_HSI_TF_FLAGS(flightSim)
        self.INNER_MARKER = _FlightSim_Radio_INNER_MARKER(flightSim)
        self.INNER_MARKER_LATLONALT = _FlightSim_Radio_INNER_MARKER_LATLONALT(flightSim)
        self.MARKER_AVAILABLE = _FlightSim_Radio_MARKER_AVAILABLE(flightSim)
        self.MARKER_BEACON_SENSITIVITY_HIGH = _FlightSim_Radio_MARKER_BEACON_SENSITIVITY_HIGH(flightSim)
        self.MARKER_BEACON_STATE = _FlightSim_Radio_MARKER_BEACON_STATE(flightSim)
        self.MARKER_BEACON_TEST_MUTE = _FlightSim_Radio_MARKER_BEACON_TEST_MUTE(flightSim)
        self.MARKER_SOUND = _FlightSim_Radio_MARKER_SOUND(flightSim)
        self.MIDDLE_MARKER = _FlightSim_Radio_MIDDLE_MARKER(flightSim)
        self.MIDDLE_MARKER_LATLONALT = _FlightSim_Radio_MIDDLE_MARKER_LATLONALT(flightSim)
        self.OUTER_MARKER = _FlightSim_Radio_OUTER_MARKER(flightSim)
        self.OUTER_MARKER_LATLONALT = _FlightSim_Radio_OUTER_MARKER_LATLONALT(flightSim)
        self.NAV_ACTIVE_FREQUENCY = lambda index: _FlightSim_Radio_NAV_ACTIVE_FREQUENCY(flightSim, index)
        self.NAV_AVAILABLE = lambda index: _FlightSim_Radio_NAV_AVAILABLE(flightSim, index)
        self.NAV_BACK_COURSE_FLAGS = lambda index: _FlightSim_Radio_NAV_BACK_COURSE_FLAGS(flightSim, index)
        self.NAV_CDI = lambda index: _FlightSim_Radio_NAV_CDI(flightSim, index)
        self.NAV_CLOSE_DME = lambda index: _FlightSim_Radio_NAV_CLOSE_DME(flightSim, index)
        self.NAV_CLOSE_FREQUENCY = lambda index: _FlightSim_Radio_NAV_CLOSE_FREQUENCY(flightSim, index)
        self.NAV_CLOSE_IDENT = lambda index: _FlightSim_Radio_NAV_CLOSE_IDENT(flightSim, index)
        self.NAV_CLOSE_LOCALIZER = lambda index: _FlightSim_Radio_NAV_CLOSE_LOCALIZER(flightSim, index)
        self.NAV_CLOSE_NAME = lambda index: _FlightSim_Radio_NAV_CLOSE_NAME(flightSim, index)
        self.NAV_CODES = _FlightSim_Radio_NAV_CODES(flightSim)
        self.NAV_DME = _FlightSim_Radio_NAV_DME(flightSim)
        self.NAV_DMESPEED = _FlightSim_Radio_NAV_DMESPEED(flightSim)
        self.NAV_DME_LATLONALT = lambda index: _FlightSim_Radio_NAV_DME_LATLONALT(flightSim, index)
        self.NAV_FREQUENCY = _FlightSim_Radio_NAV_FREQUENCY(flightSim)
        self.NAV_GLIDE_SLOPE = _FlightSim_Radio_NAV_GLIDE_SLOPE(flightSim)
        self.NAV_GLIDE_SLOPE_ERROR = _FlightSim_Radio_NAV_GLIDE_SLOPE_ERROR(flightSim)
        self.NAV_GLIDE_SLOPE_LENGTH = _FlightSim_Radio_NAV_GLIDE_SLOPE_LENGTH(flightSim)
        self.NAV_GSI = _FlightSim_Radio_NAV_GSI(flightSim)
        self.NAV_GS_FLAG = _FlightSim_Radio_NAV_GS_FLAG(flightSim)
        self.NAV_GS_LATLONALT = lambda index: _FlightSim_Radio_NAV_GS_LATLONALT(flightSim, index)
        self.NAV_GS_LLAF64 = _FlightSim_Radio_NAV_GS_LLAF64(flightSim)
        self.NAV_HAS_CLOSE_DME = _FlightSim_Radio_NAV_HAS_CLOSE_DME(flightSim)
        self.NAV_HAS_CLOSE_LOCALIZER = _FlightSim_Radio_NAV_HAS_CLOSE_LOCALIZER(flightSim)
        self.NAV_HAS_DME = _FlightSim_Radio_NAV_HAS_DME(flightSim)
        self.NAV_HAS_GLIDE_SLOPE = _FlightSim_Radio_NAV_HAS_GLIDE_SLOPE(flightSim)
        self.NAV_HAS_LOCALIZER = _FlightSim_Radio_NAV_HAS_LOCALIZER(flightSim)
        self.NAV_HAS_NAV = _FlightSim_Radio_NAV_HAS_NAV(flightSim)
        self.NAV_HAS_TACAN = _FlightSim_Radio_NAV_HAS_TACAN(flightSim)
        self.NAV_IDENT = _FlightSim_Radio_NAV_IDENT(flightSim)
        self.NAV_LOCALIZER = _FlightSim_Radio_NAV_LOCALIZER(flightSim)
        self.NAV_LOC_AIRPORT_IDENT = _FlightSim_Radio_NAV_LOC_AIRPORT_IDENT(flightSim)
        self.NAV_LOC_RUNWAY_DESIGNATOR = _FlightSim_Radio_NAV_LOC_RUNWAY_DESIGNATOR(flightSim)
        self.NAV_LOC_RUNWAY_NUMBER = _FlightSim_Radio_NAV_LOC_RUNWAY_NUMBER(flightSim)
        self.NAV_MAGVAR = _FlightSim_Radio_NAV_MAGVAR(flightSim)
        self.NAV_NAME = _FlightSim_Radio_NAV_NAME(flightSim)
        self.NAV_OBS = _FlightSim_Radio_NAV_OBS(flightSim)
        self.NAV_RADIAL = _FlightSim_Radio_NAV_RADIAL(flightSim)
        self.NAV_RADIAL_ERROR = _FlightSim_Radio_NAV_RADIAL_ERROR(flightSim)
        self.NAV_RAW_GLIDE_SLOPE = _FlightSim_Radio_NAV_RAW_GLIDE_SLOPE(flightSim)
        self.NAV_RELATIVE_BEARING_TO_STATION = _FlightSim_Radio_NAV_RELATIVE_BEARING_TO_STATION(flightSim)
        self.NAV_SIGNAL = _FlightSim_Radio_NAV_SIGNAL(flightSim)
        self.NAV_SOUND = lambda index: _FlightSim_Radio_NAV_SOUND(flightSim, index)
        self.NAV_STANDBY_FREQUENCY = lambda index: _FlightSim_Radio_NAV_STANDBY_FREQUENCY(flightSim, index)
        self.NAV_TOFROM = _FlightSim_Radio_NAV_TOFROM(flightSim)
        self.NAV_VOLUME = _FlightSim_Radio_NAV_VOLUME(flightSim)
        self.NAV_VOR_DISTANCE = _FlightSim_Radio_NAV_VOR_DISTANCE(flightSim)
        self.NAV_VOR_LATLONALT = lambda index: _FlightSim_Radio_NAV_VOR_LATLONALT(flightSim, index)
        self.NAV_VOR_LLAF64 = _FlightSim_Radio_NAV_VOR_LLAF64(flightSim)
        self.TACAN_ACTIVE_CHANNEL = lambda index: _FlightSim_Radio_TACAN_ACTIVE_CHANNEL(flightSim, index)
        self.TACAN_ACTIVE_MODE = lambda index: _FlightSim_Radio_TACAN_ACTIVE_MODE(flightSim, index)
        self.TACAN_AVAILABLE = lambda index: _FlightSim_Radio_TACAN_AVAILABLE(flightSim, index)
        self.TACAN_DRIVES_NAV1 = lambda index: _FlightSim_Radio_TACAN_DRIVES_NAV1(flightSim, index)
        self.TACAN_OBS = lambda index: _FlightSim_Radio_TACAN_OBS(flightSim, index)
        self.TACAN_STANDBY_CHANNEL = lambda index: _FlightSim_Radio_TACAN_STANDBY_CHANNEL(flightSim, index)
        self.TACAN_STANDBY_MODE = lambda index: _FlightSim_Radio_TACAN_STANDBY_MODE(flightSim, index)
        self.TACAN_STATION_CDI = lambda index: _FlightSim_Radio_TACAN_STATION_CDI(flightSim, index)
        self.TACAN_STATION_DISTANCE = lambda index: _FlightSim_Radio_TACAN_STATION_DISTANCE(flightSim, index)
        self.TACAN_STATION_IDENT = lambda index: _FlightSim_Radio_TACAN_STATION_IDENT(flightSim, index)
        self.TACAN_STATION_LATLONALT = lambda index: _FlightSim_Radio_TACAN_STATION_LATLONALT(flightSim, index)
        self.TACAN_STATION_RADIAL = lambda index: _FlightSim_Radio_TACAN_STATION_RADIAL(flightSim, index)
        self.TACAN_STATION_RADIAL_ERROR = lambda index: _FlightSim_Radio_TACAN_STATION_RADIAL_ERROR(flightSim, index)
        self.TACAN_STATION_TOFROM = lambda index: _FlightSim_Radio_TACAN_STATION_TOFROM(flightSim, index)
        self.TACAN_VOLUME = lambda index: _FlightSim_Radio_TACAN_VOLUME(flightSim, index)
        self.COPILOT_TRANSMITTER_TYPE = _FlightSim_Radio_COPILOT_TRANSMITTER_TYPE(flightSim)
        self.COPILOT_TRANSMITTING = _FlightSim_Radio_COPILOT_TRANSMITTING(flightSim)
        self.PILOT_TRANSMITTER_TYPE = _FlightSim_Radio_PILOT_TRANSMITTER_TYPE(flightSim)
        self.PILOT_TRANSMITTING = _FlightSim_Radio_PILOT_TRANSMITTING(flightSim)
        self.RADIOS_AVAILABLE = _FlightSim_Radio_RADIOS_AVAILABLE(flightSim)
        self.RADIO_HEIGHT = _FlightSim_Radio_RADIO_HEIGHT(flightSim)
        self.TRANSPONDER_AVAILABLE = _FlightSim_Radio_TRANSPONDER_AVAILABLE(flightSim)
        self.TRANSPONDER_CODE = lambda index: _FlightSim_Radio_TRANSPONDER_CODE(flightSim, index)
        self.TRANSPONDER_IDENT = _FlightSim_Radio_TRANSPONDER_IDENT(flightSim)
        self.TRANSPONDER_STATE = _FlightSim_Radio_TRANSPONDER_STATE(flightSim)


# ADF frequency. Index of 1 or 2.
class _FlightSim_Radio_ADF_ACTIVE_FREQUENCY:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Frequency.ADF_BCD32'):
        return self._.get(f"(A:ADF ACTIVE FREQUENCY:{self._index},{unit.value})")


# True if ADF is available
class _FlightSim_Radio_ADF_AVAILABLE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:ADF AVAILABLE:{self._index},{unit.value})")


# ADF compass rose setting
class _FlightSim_Radio_ADF_CARD:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:ADF CARD,{unit.value})")


# Deprecated, use ADF ACTIVE FREQUENCY
class _FlightSim_Radio_ADF_EXT_FREQUENCY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Frequency.BCD16'):
        return self._.get(f"(A:ADF EXT FREQUENCY,{unit.value})")


# Deprecated, use ADF ACTIVE FREQUENCY
class _FlightSim_Radio_ADF_FREQUENCY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Frequency.BCD16'):
        return self._.get(f"(A:ADF FREQUENCY,{unit.value})")


# ICAO code
class _FlightSim_Radio_ADF_IDENT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.STRING'):
        return self._.get(f"(A:ADF IDENT,{unit.value})")


# Returns the latitude, longitude and altitude of the station the radio equipment is currently tuned to, or zeros if the radio is not tuned to any ADF station. Index of 1 or 2 for ADF 1 and ADF 2.
#! SIMCONNECT_DATA_LATLONALT
# structure
class _FlightSim_Radio_ADF_LATLONALT:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: ''):
        return self._.get(f"(A:ADF LATLONALT:{self._index},{unit.value})")


# Descriptive name
class _FlightSim_Radio_ADF_NAME:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.STRING'):
        return self._.get(f"(A:ADF NAME:{self._index},{unit.value})")


# Current direction from NDB station
class _FlightSim_Radio_ADF_RADIAL:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:ADF RADIAL:{self._index},{unit.value})")


# Returns the magnetic bearing to the currently tuned ADF transmitter.
class _FlightSim_Radio_ADF_RADIAL_MAG:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:ADF RADIAL MAG:{self._index},{unit.value})")


# Signal strength
class _FlightSim_Radio_ADF_SIGNAL:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:ADF SIGNAL:{self._index},{unit.value})")


# ADF audio flag. Index of 0 or 1.
class _FlightSim_Radio_ADF_SOUND:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:ADF SOUND:{self._index},{unit.value})")


# True if ADF Standby is available
class _FlightSim_Radio_ADF_STANDBY_AVAILABLE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:ADF STANDBY AVAILABLE:{self._index},{unit.value})")


# ADF standby frequency
class _FlightSim_Radio_ADF_STANDBY_FREQUENCY:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Frequency.HERTZ'):
        return self._.get(f"(A:ADF STANDBY FREQUENCY:{self._index},{unit.value})")


# Returns the volume of the ADF
class _FlightSim_Radio_ADF_VOLUME:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:ADF VOLUME,{unit.value})")


# The name of the Airline used by ATC, as a string with a maximum length of 50 characters.
class _FlightSim_Radio_ATC_AIRLINE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.STRING'):
        return self._.get(f"(A:ATC AIRLINE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.STRING', value: str):
        self._.set(f"{value} (>A:ATC AIRLINE,{unit.value})")


# If the airport is controlled, this boolean is true.
class _FlightSim_Radio_ATC_AIRPORT_IS_TOWERED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:ATC AIRPORT IS TOWERED,{unit.value})")


# Returns whether or not the user has filed an IFR flightplan that has been cleared by the sim ATC
class _FlightSim_Radio_ATC_CLEARED_IFR:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:ATC CLEARED IFR,{unit.value})")


# Whether the ATC has cleared the plane for landing.
class _FlightSim_Radio_ATC_CLEARED_LANDING:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:ATC CLEARED LANDING,{unit.value})")


# Whether the ATC has cleared the plane for takeoff.
class _FlightSim_Radio_ATC_CLEARED_TAKEOFF:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:ATC CLEARED TAKEOFF,{unit.value})")


# Whether the ATC has cleared the plane for taxi.
class _FlightSim_Radio_ATC_CLEARED_TAXI:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:ATC CLEARED TAXI,{unit.value})")


# Returns the target altitude for the current ATC flightplan waypoint.
class _FlightSim_Radio_ATC_CURRENT_WAYPOINT_ALTITUDE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:ATC CURRENT WAYPOINT ALTITUDE,{unit.value})")


# Flight Number used by ATC, as a string with a maximum number of 6 characters.
class _FlightSim_Radio_ATC_FLIGHT_NUMBER:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.STRING'):
        return self._.get(f"(A:ATC FLIGHT NUMBER,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.STRING', value: str):
        self._.set(f"{value} (>A:ATC FLIGHT NUMBER,{unit.value})")


# Altitude between the position of the aircraft and his closest waypoints in the flightplan.
class _FlightSim_Radio_ATC_FLIGHTPLAN_DIFF_ALT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.METER'):
        return self._.get(f"(A:ATC FLIGHTPLAN DIFF ALT,{unit.value})")


# Returns the lateral distance the user's plane is from the ATC flight plan track.
class _FlightSim_Radio_ATC_FLIGHTPLAN_DIFF_DISTANCE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.METER'):
        return self._.get(f"(A:ATC FLIGHTPLAN DIFF DISTANCE,{unit.value})")


# Heading between the position of the aircraft and his closest waypoints in the flightplan.
class _FlightSim_Radio_ATC_FLIGHTPLAN_DIFF_HEADING:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:ATC FLIGHTPLAN DIFF HEADING,{unit.value})")


# Is this aircraft recognized by ATC as heavy.
class _FlightSim_Radio_ATC_HEAVY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:ATC HEAVY,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:ATC HEAVY,{unit.value})")


# ID used by ATC, as a string with a maximum number of 10 characters.
class _FlightSim_Radio_ATC_ID:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.STRING'):
        return self._.get(f"(A:ATC ID,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.STRING', value: str):
        self._.set(f"{value} (>A:ATC ID,{unit.value})")


# Returns true if the user has a valid IFR flight plan they can as for clearance for with ATC at the airport they are currently at.
class _FlightSim_Radio_ATC_IFR_FP_TO_REQUEST:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:ATC IFR FP TO REQUEST,{unit.value})")


# Model used by ATC, as a string with a maximum number of 10 characters.
class _FlightSim_Radio_ATC_MODEL:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.STRING'):
        return self._.get(f"(A:ATC MODEL,{unit.value})")


# Is ATC aircraft on parking spot.
class _FlightSim_Radio_ATC_ON_PARKING_SPOT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:ATC ON PARKING SPOT,{unit.value})")


# Returns the target altitude for the previous ATC flightplan waypoint.
class _FlightSim_Radio_ATC_PREVIOUS_WAYPOINT_ALTITUDE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.METER'):
        return self._.get(f"(A:ATC PREVIOUS WAYPOINT ALTITUDE,{unit.value})")


# The name of the airport of the runway assigned by the ATC. Returns "" if no runway is assigned.
class _FlightSim_Radio_ATC_RUNWAY_AIRPORT_NAME:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.STRING'):
        return self._.get(f"(A:ATC RUNWAY AIRPORT NAME,{unit.value})")


# This float represents the distance between the player's plane and the center of the runway selected by the ATC.
class _FlightSim_Radio_ATC_RUNWAY_DISTANCE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.METER'):
        return self._.get(f"(A:ATC RUNWAY DISTANCE,{unit.value})")


# This is a float corresponding to the horizontal distance between the player's plane and the end of the runway selected by the ATC.
class _FlightSim_Radio_ATC_RUNWAY_END_DISTANCE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.METER'):
        return self._.get(f"(A:ATC RUNWAY END DISTANCE,{unit.value})")


# This float represents the true heading of the runway selected by the ATC.
class _FlightSim_Radio_ATC_RUNWAY_HEADING_DEGREES_TRUE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:ATC RUNWAY HEADING DEGREES TRUE,{unit.value})")


# The length of the runway assigned by the ATC. Returns -1 if no runway is assigned.
class _FlightSim_Radio_ATC_RUNWAY_LENGTH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.METER'):
        return self._.get(f"(A:ATC RUNWAY LENGTH,{unit.value})")


# This is a float corresponding to the player's main gear relative X (transverse) position on the runway selected by the ATC.
class _FlightSim_Radio_ATC_RUNWAY_RELATIVE_POSITION_X:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.METER'):
        return self._.get(f"(A:ATC RUNWAY RELATIVE POSITION X,{unit.value})")


# This is a float corresponding to the player's main gear relative Y (height) position on the runway selected by the ATC.
class _FlightSim_Radio_ATC_RUNWAY_RELATIVE_POSITION_Y:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.METER'):
        return self._.get(f"(A:ATC RUNWAY RELATIVE POSITION Y,{unit.value})")


# This is a float corresponding to the player's main gear relative Z (longitudinal) position on the runway selected by the ATC.
class _FlightSim_Radio_ATC_RUNWAY_RELATIVE_POSITION_Z:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.METER'):
        return self._.get(f"(A:ATC RUNWAY RELATIVE POSITION Z,{unit.value})")


# This is a boolean corresponding to whether or not the ATC has pre-selected a runway for the player's plane. If this is false, every other ATC RUNWAY * SimVar will return default values.
class _FlightSim_Radio_ATC_RUNWAY_SELECTED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:ATC RUNWAY SELECTED,{unit.value})")


# This is a float corresponding to the horizontal distance between the player's plane and the start of the runway selected by the ATC.
class _FlightSim_Radio_ATC_RUNWAY_START_DISTANCE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.METER'):
        return self._.get(f"(A:ATC RUNWAY START DISTANCE,{unit.value})")


# This float represents the player's main gear relative X (transverse) position according to the aiming point of the runway selected by the ATC.
class _FlightSim_Radio_ATC_RUNWAY_TDPOINT_RELATIVE_POSITION_X:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.METER'):
        return self._.get(f"(A:ATC RUNWAY TDPOINT RELATIVE POSITION X,{unit.value})")


# This float represents the player's main gear relative Y (height) position according to the aiming point of the runway selected by the ATC.
class _FlightSim_Radio_ATC_RUNWAY_TDPOINT_RELATIVE_POSITION_Y:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.METER'):
        return self._.get(f"(A:ATC RUNWAY TDPOINT RELATIVE POSITION Y,{unit.value})")


# This float represents the player's main relative Z (longitudinal) position according to the aiming point of the runway selected by the ATC.
class _FlightSim_Radio_ATC_RUNWAY_TDPOINT_RELATIVE_POSITION_Z:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.METER'):
        return self._.get(f"(A:ATC RUNWAY TDPOINT RELATIVE POSITION Z,{unit.value})")


# The width of the runway assigned by the ATC. Returns -1 if no runway is assigned.
class _FlightSim_Radio_ATC_RUNWAY_WIDTH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.METER'):
        return self._.get(f"(A:ATC RUNWAY WIDTH,{unit.value})")


# Suggested minimum runway length for landing. Used by ATC.
class _FlightSim_Radio_ATC_SUGGESTED_MIN_RWY_LANDING:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.FOOT'):
        return self._.get(f"(A:ATC SUGGESTED MIN RWY LANDING,{unit.value})")


# Suggested minimum runway length for takeoff. Used by ATC.
class _FlightSim_Radio_ATC_SUGGESTED_MIN_RWY_TAKEOFF:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.FOOT'):
        return self._.get(f"(A:ATC SUGGESTED MIN RWY TAKEOFF,{unit.value})")


# Returns the lateral distance the user's plane is from the path of the currently issued ATC taxi instructions.
class _FlightSim_Radio_ATC_TAXIPATH_DISTANCE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.METER'):
        return self._.get(f"(A:ATC TAXIPATH DISTANCE,{unit.value})")


# Type used by ATC.
#! String (30)
class _FlightSim_Radio_ATC_TYPE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: ''):
        return self._.get(f"(A:ATC TYPE,{unit.value})")


# The stored COM 1/2/3 frequency value.
class _FlightSim_Radio_COM1_STORED_FREQUENCY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Frequency.BCD16'):
        return self._.get(f"(A:COM1 STORED FREQUENCY,{unit.value})")


# Gives the bearing (in degrees) of the active COM station (airport) or a value less than 0 if the station does not belong to an airport. Index is 1, 2 or 3.
class _FlightSim_Radio_COM_ACTIVE_BEARING:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:COM ACTIVE BEARING:{self._index},{unit.value})")


# Gives the distance (in meters) to the active COM station (airport) or a value less than -180° if the station does not belong to an airport. Index is 1, 2 or 3.
class _FlightSim_Radio_COM_ACTIVE_DISTANCE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Length.METER'):
        return self._.get(f"(A:COM ACTIVE DISTANCE:{self._index},{unit.value})")


# Com frequency. Index is 1, 2 or 3.
class _FlightSim_Radio_COM_ACTIVE_FREQUENCY:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Frequency.BCD16'):
        return self._.get(f"(A:COM ACTIVE FREQUENCY:{self._index},{unit.value})")


# The identity of the station that is tuned on the indexed active COM radio. Index is 1, 2, or 3.
class _FlightSim_Radio_COM_ACTIVE_FREQ_IDENT:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.STRING'):
        return self._.get(f"(A:COM ACTIVE FREQ IDENT:{self._index},{unit.value})")


# The type of COM frequency for the active indexed COM system. Index is 1, 2, or 3.
#! String:
# 
# "ATIS" - Atis
# "UNI" - Unicom
# "CTAF" - CTAF
# "GND" - Ground
# "TWR" - Tower
# "CLR" - Clearance
# 
#                             Delivery
#                         
# "APPR" - Approach
# "DEP" - Departure
# "FSS" - FSS
# "AWS" - AWOS
class _FlightSim_Radio_COM_ACTIVE_FREQ_TYPE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: ''):
        return self._.get(f"(A:COM ACTIVE FREQ TYPE:{self._index},{unit.value})")


# This will return the latitude, longitude and altitude corresponding to the indexed COM station associated with the active COM frequency. If the station is not associated with an airport, then the lat/lon/alt values returned will be -15943°, 80°, -10000 (this means that you can simply check that the altitude value is greater than 0 to assure the validity of the returned struct).
# Index is 1, 2 or 3.
#! Struct:
# SIMCONNECT_DATA_LATLONALT
class _FlightSim_Radio_COM_ACTIVE_LATLONALT:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: ''):
        return self._.get(f"(A:COM ACTIVE LATLONALT:{self._index},{unit.value})")


# True if COM1, COM2 or COM3 is available (depending on the index, either 1, 2, or 3)
class _FlightSim_Radio_COM_AVAILABLE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:COM AVAILABLE:{self._index},{unit.value})")


# Not currently used in the simulation.
#! Struct:
# SIMCONNECT_DATA_LATLONALT
class _FlightSim_Radio_COM_LATLONALT:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: ''):
        return self._.get(f"(A:COM LATLONALT:{self._index},{unit.value})")


# Whether or not the plane is receiving on the indexed com channel or not (either 1, 2, or 3 for the index).
class _FlightSim_Radio_COM_RECEIVE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:COM RECEIVE:{self._index},{unit.value})")


# Toggles all COM radios to receive on
class _FlightSim_Radio_COM_RECEIVE_ALL:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:COM RECEIVE ALL,{unit.value})")


# Whether or not the plane is receiving on the indexed com channel. Index is 1, 2 or 3.
class _FlightSim_Radio_COM_RECEIVE_EX1:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:COM RECEIVE EX1:{self._index},{unit.value})")


# The COM radio frequency step. Index is 1, 2 or 3.
class _FlightSim_Radio_COM_SPACING_MODE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    class Unit(Enum):
        25KHZ = 0
        8_33KHZ = 1

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:COM SPACING MODE:{self._index},{unit.value})")


# Com standby frequency. Index is 1, 2 or 3.
class _FlightSim_Radio_COM_STANDBY_FREQUENCY:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Frequency.BCD16'):
        return self._.get(f"(A:COM STANDBY FREQUENCY:{self._index},{unit.value})")


# The identity of the station that is tuned on the indexed standby COM radio. Index is 1, 2, or 3.
class _FlightSim_Radio_COM_STANDBY_FREQ_IDENT:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.STRING'):
        return self._.get(f"(A:COM STANDBY FREQ IDENT:{self._index},{unit.value})")


# The type of COM frequency for the standby indexed COM system. Index is 1, 2, or 3.
#! String:
# 
# "ATIS" - Atis
# "UNI" - Unicom
# "CTAF" - CTAF
# "GND" - Ground
# "TWR" - Tower
# "CLR" - Clearance
# 
#                             Delivery
#                         
# "APPR" - Approach
# "DEP" - Departure
# "FSS" - FSS
# "AWS" - AWOS
class _FlightSim_Radio_COM_STANDBY_FREQ_TYPE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: ''):
        return self._.get(f"(A:COM STANDBY FREQ TYPE:{self._index},{unit.value})")


# Radio status flag for the indexed com channel. Index is 1, 2 or 3.
class _FlightSim_Radio_COM_STATUS:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    class Unit(Enum):
        INVALID = -1
        OK = 0
        DOES_NOT_EXIST = 1
        NO_ELECTRICITY = 2
        FAILED = 3

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:COM STATUS:{self._index},{unit.value})")


# Enter an index of 1, 2 or 3. Will return TRUE if the COM system is working, FALSE otherwise.
class _FlightSim_Radio_COM_TEST:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:COM TEST:{self._index},{unit.value})")


# Audio panel com transmit state. Index of 1, 2 or 3.
class _FlightSim_Radio_COM_TRANSMIT:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:COM TRANSMIT:{self._index},{unit.value})")


# The volume of the COM Radio.
class _FlightSim_Radio_COM_VOLUME:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:COM VOLUME,{unit.value})")


# Whether the FLARM is available (TRUE, 1) or not (FALSE, 0).
class _FlightSim_Radio_FLARM_AVAILABLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:FLARM AVAILABLE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:FLARM AVAILABLE,{unit.value})")


# The bearing of the FLARM threat aircraft, relative to track.
class _FlightSim_Radio_FLARM_THREAT_BEARING:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:FLARM THREAT BEARING,{unit.value})")


# The FLARM threat aircraft data structure, which contains data about the perceived threat, returned as a struct. Struct member variables are as follows:
#! Struct
class _FlightSim_Radio_FLARM_THREAT_DATA:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: ''):
        return self._.get(f"(A:FLARM THREAT DATA,{unit.value})")


# The distance to the FLARM threat object.
class _FlightSim_Radio_FLARM_THREAT_DISTANCE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.METER'):
        return self._.get(f"(A:FLARM THREAT DISTANCE,{unit.value})")


# The heading to the FLARM threat object.
class _FlightSim_Radio_FLARM_THREAT_HEADING:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:FLARM THREAT HEADING,{unit.value})")


# The relative altitude of the threat object.
class _FlightSim_Radio_FLARM_THREAT_RELATIVE_ALTITUDE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.METER'):
        return self._.get(f"(A:FLARM THREAT RELATIVE ALTITUDE,{unit.value})")


# The estimated time to a collision.
class _FlightSim_Radio_FLARM_THREAT_TIME_TO_COLLISION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Time.SECOND'):
        return self._.get(f"(A:FLARM THREAT TIME TO COLLISION,{unit.value})")


# The vertical bearing towards the threat.
class _FlightSim_Radio_FLARM_THREAT_VERTICAL_BEARING:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:FLARM THREAT VERTICAL BEARING,{unit.value})")


# ID of airport.
class _FlightSim_Radio_GPS_APPROACH_AIRPORT_ID:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.STRING'):
        return self._.get(f"(A:GPS APPROACH AIRPORT ID,{unit.value})")


# ID of approach.
class _FlightSim_Radio_GPS_APPROACH_APPROACH_ID:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.STRING'):
        return self._.get(f"(A:GPS APPROACH APPROACH ID,{unit.value})")


# Index of approach for given airport.
class _FlightSim_Radio_GPS_APPROACH_APPROACH_INDEX:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:GPS APPROACH APPROACH INDEX,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER', value: str):
        self._.set(f"{value} (>A:GPS APPROACH APPROACH INDEX,{unit.value})")


# Approach type.
class _FlightSim_Radio_GPS_APPROACH_APPROACH_TYPE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        NONE = 0
        GPS = 1
        VOR = 2
        NDB = 3
        ILS = 4
        LOCALIZER = 5
        SDF = 6
        LDA = 7
        VOR_DME = 8
        NDB_DME = 9
        RNAV = 10
        BACKCOURSE = 11

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:GPS APPROACH APPROACH TYPE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM', value: str):
        self._.set(f"{value} (>A:GPS APPROACH APPROACH TYPE,{unit.value})")


# Is approach transition final approach segment.
class _FlightSim_Radio_GPS_APPROACH_IS_FINAL:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GPS APPROACH IS FINAL,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:GPS APPROACH IS FINAL,{unit.value})")


# Is approach segment missed approach segment.
class _FlightSim_Radio_GPS_APPROACH_IS_MISSED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GPS APPROACH IS MISSED,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:GPS APPROACH IS MISSED,{unit.value})")


# Waypoint is the runway.
class _FlightSim_Radio_GPS_APPROACH_IS_WP_RUNWAY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GPS APPROACH IS WP RUNWAY,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:GPS APPROACH IS WP RUNWAY,{unit.value})")


# Sub mode within approach mode.
class _FlightSim_Radio_GPS_APPROACH_MODE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        NONE = 0
        TRANSITION = 1
        FINAL = 2
        MISSED = 3

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:GPS APPROACH MODE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM', value: str):
        self._.set(f"{value} (>A:GPS APPROACH MODE,{unit.value})")


# Segment type within approach.
class _FlightSim_Radio_GPS_APPROACH_SEGMENT_TYPE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        LINE = 0
        ARC_CLOCKWISE = 1
        ARC_COUNTER_CLOCKWISE = 2

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:GPS APPROACH SEGMENT TYPE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM', value: str):
        self._.set(f"{value} (>A:GPS APPROACH SEGMENT TYPE,{unit.value})")


# Deviation of local time from GMT.
class _FlightSim_Radio_GPS_APPROACH_TIMEZONE_DEVIATION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Time.SECOND'):
        return self._.get(f"(A:GPS APPROACH TIMEZONE DEVIATION,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Time.SECOND', value: str):
        self._.set(f"{value} (>A:GPS APPROACH TIMEZONE DEVIATION,{unit.value})")


# ID of approach transition.
class _FlightSim_Radio_GPS_APPROACH_TRANSITION_ID:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.STRING'):
        return self._.get(f"(A:GPS APPROACH TRANSITION ID,{unit.value})")


# Index of approach transition.
class _FlightSim_Radio_GPS_APPROACH_TRANSITION_INDEX:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:GPS APPROACH TRANSITION INDEX,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER', value: str):
        self._.set(f"{value} (>A:GPS APPROACH TRANSITION INDEX,{unit.value})")


# Number of waypoints.
class _FlightSim_Radio_GPS_APPROACH_WP_COUNT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:GPS APPROACH WP COUNT,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER', value: str):
        self._.set(f"{value} (>A:GPS APPROACH WP COUNT,{unit.value})")


# Index of current waypoint.
class _FlightSim_Radio_GPS_APPROACH_WP_INDEX:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:GPS APPROACH WP INDEX,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER', value: str):
        self._.set(f"{value} (>A:GPS APPROACH WP INDEX,{unit.value})")


# Waypoint type within approach mode.
class _FlightSim_Radio_GPS_APPROACH_WP_TYPE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        NONE = 0
        FIX = 1
        PROCEDURE_TURN_LEFT = 2
        PROCEDURE_TURN_RIGHT = 3
        DME_ARC_LEFT = 4
        DME_ARC_RIGHT = 5
        HOLDING_LEFT = 6
        HOLDING_RIGHT = 7
        DISTANCE = 8
        ALTITUDE = 9
        MANUAL_SEQUENCE = 10
        VECTOR_TO_FINAL = 11

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:GPS APPROACH WP TYPE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM', value: str):
        self._.set(f"{value} (>A:GPS APPROACH WP TYPE,{unit.value})")


# The course deviation of the needle for a CDI instrument. The SimVar displays the deviation from -127 to +127. It returns a value if a flight plan is set (otherwise it will return 0) even if the autopilot isn't on GPS mode. Scaling can also be set through the GPS CDI SCALING simvar.
class _FlightSim_Radio_GPS_CDI_NEEDLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:GPS CDI NEEDLE,{unit.value})")


# The full scale deflection of the CDI due to GPS cross-track error, in meters.
class _FlightSim_Radio_GPS_CDI_SCALING:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.METER'):
        return self._.get(f"(A:GPS CDI SCALING,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Length.METER', value: str):
        self._.set(f"{value} (>A:GPS CDI SCALING,{unit.value})")


# Suggested heading to steer (for autopilot).
class _FlightSim_Radio_GPS_COURSE_TO_STEER:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:GPS COURSE TO STEER,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Angle.RADIAN', value: str):
        self._.set(f"{value} (>A:GPS COURSE TO STEER,{unit.value})")


# GPS is driving Nav 1 indicator. Note this setting will also affect the SimVars HSI_STATION_IDENT and HSI_BEARING.
class _FlightSim_Radio_GPS_DRIVES_NAV1:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GPS DRIVES NAV1,{unit.value})")


# Estimated time of arrival at destination.
class _FlightSim_Radio_GPS_ETA:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Time.SECOND'):
        return self._.get(f"(A:GPS ETA,{unit.value})")


# Estimated time en route to destination.
class _FlightSim_Radio_GPS_ETE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Time.SECOND'):
        return self._.get(f"(A:GPS ETE,{unit.value})")


# This is the complete flightplan length from start to end. Essentially the cumulative length of all the flight plan legs added together.
class _FlightSim_Radio_GPS_FLIGHTPLAN_TOTAL_DISTANCE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.METER'):
        return self._.get(f"(A:GPS FLIGHTPLAN TOTAL DISTANCE,{unit.value})")


# Number of waypoints.
class _FlightSim_Radio_GPS_FLIGHT_PLAN_WP_COUNT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:GPS FLIGHT PLAN WP COUNT,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER', value: str):
        self._.set(f"{value} (>A:GPS FLIGHT PLAN WP COUNT,{unit.value})")


# Index of waypoint.
class _FlightSim_Radio_GPS_FLIGHT_PLAN_WP_INDEX:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:GPS FLIGHT PLAN WP INDEX,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER', value: str):
        self._.set(f"{value} (>A:GPS FLIGHT PLAN WP INDEX,{unit.value})")


# Current magnetic ground track.
class _FlightSim_Radio_GPS_GROUND_MAGNETIC_TRACK:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:GPS GROUND MAGNETIC TRACK,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Angle.RADIAN', value: str):
        self._.set(f"{value} (>A:GPS GROUND MAGNETIC TRACK,{unit.value})")


# Current ground speed.
class _FlightSim_Radio_GPS_GROUND_SPEED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.METER_PER_SECOND'):
        return self._.get(f"(A:GPS GROUND SPEED,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Length.METER_PER_SECOND', value: str):
        self._.set(f"{value} (>A:GPS GROUND SPEED,{unit.value})")


# Current true heading.
class _FlightSim_Radio_GPS_GROUND_TRUE_HEADING:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:GPS GROUND TRUE HEADING,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Angle.RADIAN', value: str):
        self._.set(f"{value} (>A:GPS GROUND TRUE HEADING,{unit.value})")


# Current true ground track.
class _FlightSim_Radio_GPS_GROUND_TRUE_TRACK:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:GPS GROUND TRUE TRACK,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Angle.RADIAN', value: str):
        self._.set(f"{value} (>A:GPS GROUND TRUE TRACK,{unit.value})")


# The full scale deflection of the vertical GSI due to GPS glidepath deviation, in meters.
class _FlightSim_Radio_GPS_GSI_SCALING:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.METER'):
        return self._.get(f"(A:GPS GSI SCALING,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Length.METER', value: str):
        self._.set(f"{value} (>A:GPS GSI SCALING,{unit.value})")


# Whether or not the GPS system has a presently available glidepath for guidance. Only applicable with GPS_OVERRIDDEN. When true and in GPS OVERRIDDEN, HSI_GSI_NEEDLE_VALID will also be true.
class _FlightSim_Radio_GPS_HAS_GLIDEPATH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GPS HAS GLIDEPATH,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:GPS HAS GLIDEPATH,{unit.value})")


# The glide deviation of the needle for a CDI instrument. The simvar displays the deviation from -127 to +127. It returns a value if a flight plan is set (otherwise it will return 0) even if the autopilot isn't on GPS mode. Scaling can also be set through the GPS CDI SCALING simvar.
class _FlightSim_Radio_GPS_HSI_NEEDLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:GPS HSI NEEDLE,{unit.value})")


# Flight plan mode active.
class _FlightSim_Radio_GPS_IS_ACTIVE_FLIGHT_PLAN:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GPS IS ACTIVE FLIGHT PLAN,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:GPS IS ACTIVE FLIGHT PLAN,{unit.value})")


# Waypoint mode active.
class _FlightSim_Radio_GPS_IS_ACTIVE_WAY_POINT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GPS IS ACTIVE WAY POINT,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:GPS IS ACTIVE WAY POINT,{unit.value})")


# Is switching to next waypoint locked.
class _FlightSim_Radio_GPS_IS_ACTIVE_WP_LOCKED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GPS IS ACTIVE WP LOCKED,{unit.value})")


# Is approach mode active.
class _FlightSim_Radio_GPS_IS_APPROACH_ACTIVE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GPS IS APPROACH ACTIVE,{unit.value})")


# Is approach loaded.
class _FlightSim_Radio_GPS_IS_APPROACH_LOADED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GPS IS APPROACH LOADED,{unit.value})")


# Is flight plan destination reached.
class _FlightSim_Radio_GPS_IS_ARRIVED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GPS IS ARRIVED,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:GPS IS ARRIVED,{unit.value})")


# Is Direct To Waypoint mode active.
class _FlightSim_Radio_GPS_IS_DIRECTTO_FLIGHTPLAN:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GPS IS DIRECTTO FLIGHTPLAN,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:GPS IS DIRECTTO FLIGHTPLAN,{unit.value})")


# Current GPS magnetic variation.
class _FlightSim_Radio_GPS_MAGVAR:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:GPS MAGVAR,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Angle.RADIAN', value: str):
        self._.set(f"{value} (>A:GPS MAGVAR,{unit.value})")


# Whether or not the OBS mode is currently active (disable the automatic sequencing of waypoints in GPS flight plan).
class _FlightSim_Radio_GPS_OBS_ACTIVE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GPS OBS ACTIVE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:GPS OBS ACTIVE,{unit.value})")


# This is the currently selected OBS course in degrees, from 0 to 360.
class _FlightSim_Radio_GPS_OBS_VALUE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:GPS OBS VALUE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Angle.DEGREE', value: str):
        self._.set(f"{value} (>A:GPS OBS VALUE,{unit.value})")


# When it is active, all sim GPS system updates are suspended. This must be set to TRUE to be able to correctly set to any other GPS SimVar.
class _FlightSim_Radio_GPS_OVERRIDDEN:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GPS OVERRIDDEN,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:GPS OVERRIDDEN,{unit.value})")


# Current GPS altitude.
class _FlightSim_Radio_GPS_POSITION_ALT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.METER'):
        return self._.get(f"(A:GPS POSITION ALT,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Length.METER', value: str):
        self._.set(f"{value} (>A:GPS POSITION ALT,{unit.value})")


# Current GPS latitude.
class _FlightSim_Radio_GPS_POSITION_LAT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:GPS POSITION LAT,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Angle.DEGREE', value: str):
        self._.set(f"{value} (>A:GPS POSITION LAT,{unit.value})")


# Current GPS longitude.
class _FlightSim_Radio_GPS_POSITION_LON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:GPS POSITION LON,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Angle.DEGREE', value: str):
        self._.set(f"{value} (>A:GPS POSITION LON,{unit.value})")


# Altitude of GPS target.
class _FlightSim_Radio_GPS_TARGET_ALTITUDE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.METER'):
        return self._.get(f"(A:GPS TARGET ALTITUDE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Length.METER', value: str):
        self._.set(f"{value} (>A:GPS TARGET ALTITUDE,{unit.value})")


# Distance to target.
class _FlightSim_Radio_GPS_TARGET_DISTANCE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.METER'):
        return self._.get(f"(A:GPS TARGET DISTANCE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Length.METER', value: str):
        self._.set(f"{value} (>A:GPS TARGET DISTANCE,{unit.value})")


# Glidepath in degrees.
class _FlightSim_Radio_GPS_VERTICAL_ANGLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:GPS VERTICAL ANGLE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Angle.DEGREE', value: str):
        self._.set(f"{value} (>A:GPS VERTICAL ANGLE,{unit.value})")


# Vertical error in degrees from GlidePath.
class _FlightSim_Radio_GPS_VERTICAL_ANGLE_ERROR:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:GPS VERTICAL ANGLE ERROR,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Angle.DEGREE', value: str):
        self._.set(f"{value} (>A:GPS VERTICAL ANGLE ERROR,{unit.value})")


# Vertical deviation in meters from GlidePath.
class _FlightSim_Radio_GPS_VERTICAL_ERROR:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.METER'):
        return self._.get(f"(A:GPS VERTICAL ERROR,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Length.METER', value: str):
        self._.set(f"{value} (>A:GPS VERTICAL ERROR,{unit.value})")


# Magnetic bearing to waypoint.
class _FlightSim_Radio_GPS_WP_BEARING:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:GPS WP BEARING,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Angle.RADIAN', value: str):
        self._.set(f"{value} (>A:GPS WP BEARING,{unit.value})")


# Cross track distance.
class _FlightSim_Radio_GPS_WP_CROSS_TRK:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.METER'):
        return self._.get(f"(A:GPS WP CROSS TRK,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Length.METER', value: str):
        self._.set(f"{value} (>A:GPS WP CROSS TRK,{unit.value})")


# The required heading (magnetic) from the previous waypoint to the next waypoint.
class _FlightSim_Radio_GPS_WP_DESIRED_TRACK:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:GPS WP DESIRED TRACK,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Angle.RADIAN', value: str):
        self._.set(f"{value} (>A:GPS WP DESIRED TRACK,{unit.value})")


# Distance to waypoint.
class _FlightSim_Radio_GPS_WP_DISTANCE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.METER'):
        return self._.get(f"(A:GPS WP DISTANCE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Length.METER', value: str):
        self._.set(f"{value} (>A:GPS WP DISTANCE,{unit.value})")


# Estimated time of arrival at waypoint.
class _FlightSim_Radio_GPS_WP_ETA:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Time.SECOND'):
        return self._.get(f"(A:GPS WP ETA,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Time.SECOND', value: str):
        self._.set(f"{value} (>A:GPS WP ETA,{unit.value})")


# Estimated time en route to waypoint.
class _FlightSim_Radio_GPS_WP_ETE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Time.SECOND'):
        return self._.get(f"(A:GPS WP ETE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Time.SECOND', value: str):
        self._.set(f"{value} (>A:GPS WP ETE,{unit.value})")


# Altitude of next waypoint.
class _FlightSim_Radio_GPS_WP_NEXT_ALT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.METER'):
        return self._.get(f"(A:GPS WP NEXT ALT,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Length.METER', value: str):
        self._.set(f"{value} (>A:GPS WP NEXT ALT,{unit.value})")


# ID of next GPS waypoint.
class _FlightSim_Radio_GPS_WP_NEXT_ID:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.STRING'):
        return self._.get(f"(A:GPS WP NEXT ID,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.STRING', value: str):
        self._.set(f"{value} (>A:GPS WP NEXT ID,{unit.value})")


# Latitude of next waypoint.
class _FlightSim_Radio_GPS_WP_NEXT_LAT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:GPS WP NEXT LAT,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Angle.DEGREE', value: str):
        self._.set(f"{value} (>A:GPS WP NEXT LAT,{unit.value})")


# Longitude of next waypoint.
class _FlightSim_Radio_GPS_WP_NEXT_LON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:GPS WP NEXT LON,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Angle.DEGREE', value: str):
        self._.set(f"{value} (>A:GPS WP NEXT LON,{unit.value})")


# Altitude of previous waypoint.
class _FlightSim_Radio_GPS_WP_PREV_ALT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.METER'):
        return self._.get(f"(A:GPS WP PREV ALT,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Length.METER', value: str):
        self._.set(f"{value} (>A:GPS WP PREV ALT,{unit.value})")


# ID of previous GPS waypoint.
class _FlightSim_Radio_GPS_WP_PREV_ID:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.STRING'):
        return self._.get(f"(A:GPS WP PREV ID,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.STRING', value: str):
        self._.set(f"{value} (>A:GPS WP PREV ID,{unit.value})")


# Latitude of previous waypoint.
class _FlightSim_Radio_GPS_WP_PREV_LAT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:GPS WP PREV LAT,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Angle.DEGREE', value: str):
        self._.set(f"{value} (>A:GPS WP PREV LAT,{unit.value})")


# Longitude of previous waypoint.
class _FlightSim_Radio_GPS_WP_PREV_LON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:GPS WP PREV LON,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Angle.DEGREE', value: str):
        self._.set(f"{value} (>A:GPS WP PREV LON,{unit.value})")


# Is previous waypoint valid (i.e. current waypoint is not the first waypoint).
class _FlightSim_Radio_GPS_WP_PREV_VALID:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GPS WP PREV VALID,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:GPS WP PREV VALID,{unit.value})")


# Tracking angle error to waypoint.
class _FlightSim_Radio_GPS_WP_TRACK_ANGLE_ERROR:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:GPS WP TRACK ANGLE ERROR,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Angle.RADIAN', value: str):
        self._.set(f"{value} (>A:GPS WP TRACK ANGLE ERROR,{unit.value})")


# True bearing to waypoint.
class _FlightSim_Radio_GPS_WP_TRUE_BEARING:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:GPS WP TRUE BEARING,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Angle.RADIAN', value: str):
        self._.set(f"{value} (>A:GPS WP TRUE BEARING,{unit.value})")


# Required true heading to waypoint.
class _FlightSim_Radio_GPS_WP_TRUE_REQ_HDG:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:GPS WP TRUE REQ HDG,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Angle.RADIAN', value: str):
        self._.set(f"{value} (>A:GPS WP TRUE REQ HDG,{unit.value})")


# Vertical speed to waypoint.
class _FlightSim_Radio_GPS_WP_VERTICAL_SPEED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.METER_PER_SECOND'):
        return self._.get(f"(A:GPS WP VERTICAL SPEED,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Length.METER_PER_SECOND', value: str):
        self._.set(f"{value} (>A:GPS WP VERTICAL SPEED,{unit.value})")


# If the GPS_DRIVES_NAV1 variable is true and the HSI BEARING VALID variable is true, this variable contains the HSI needle bearing. If the GPS DRIVES NAV1 variable is false and the HSI BEARING VALID variable is true, this variable contains the ADF1 frequency.
class _FlightSim_Radio_HSI_BEARING:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:HSI BEARING,{unit.value})")


# This will return true if the HSI BEARING variable contains valid data.
class _FlightSim_Radio_HSI_BEARING_VALID:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:HSI BEARING VALID,{unit.value})")


# Needle deflection (+/- 127).
class _FlightSim_Radio_HSI_CDI_NEEDLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:HSI CDI NEEDLE,{unit.value})")


# Signal valid.
class _FlightSim_Radio_HSI_CDI_NEEDLE_VALID:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:HSI CDI NEEDLE VALID,{unit.value})")


# DME/GPS distance.
class _FlightSim_Radio_HSI_DISTANCE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.NAUTICAL_MILE'):
        return self._.get(f"(A:HSI DISTANCE,{unit.value})")


# Needle deflection (+/- 119).
class _FlightSim_Radio_HSI_GSI_NEEDLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:HSI GSI NEEDLE,{unit.value})")


# Signal valid.
class _FlightSim_Radio_HSI_GSI_NEEDLE_VALID:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:HSI GSI NEEDLE VALID,{unit.value})")


# Station is a localizer.
class _FlightSim_Radio_HSI_HAS_LOCALIZER:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:HSI HAS LOCALIZER,{unit.value})")


# DME/GPS speed.
class _FlightSim_Radio_HSI_SPEED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.KNOT'):
        return self._.get(f"(A:HSI SPEED,{unit.value})")


# Returns the ident of the the next GPS waypoint, if GPS_DRIVES_NAV1 is true. If GPS DRIVES NAV1 is false, it returns the identity of the station that is tuned on nav radio 1.
class _FlightSim_Radio_HSI_STATION_IDENT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.STRING'):
        return self._.get(f"(A:HSI STATION IDENT,{unit.value})")


# Nav TO/FROM flag.
class _FlightSim_Radio_HSI_TF_FLAGS:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        OFF = 0
        TO = 1
        FROM = 2

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:HSI TF FLAGS,{unit.value})")


# Inner marker state.
class _FlightSim_Radio_INNER_MARKER:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:INNER MARKER,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:INNER MARKER,{unit.value})")


# Returns the latitude, longitude and altitude of the inner marker of an approach to a runway, if the aircraft is within the required proximity, otherwise it will return zeros.
#! SIMCONNECT_DATA_LATLONALT
# structure
class _FlightSim_Radio_INNER_MARKER_LATLONALT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: ''):
        return self._.get(f"(A:INNER MARKER LATLONALT,{unit.value})")


# True if Marker is available.
class _FlightSim_Radio_MARKER_AVAILABLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:MARKER AVAILABLE,{unit.value})")


# Whether or not the Marker Beacon is in High Sensitivity mode.
class _FlightSim_Radio_MARKER_BEACON_SENSITIVITY_HIGH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:MARKER BEACON SENSITIVITY HIGH,{unit.value})")


# Marker beacon state.
class _FlightSim_Radio_MARKER_BEACON_STATE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        NONE = 0
        OUTER = 1
        MIDDLE = 2
        INNER = 3

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:MARKER BEACON STATE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM', value: str):
        self._.set(f"{value} (>A:MARKER BEACON STATE,{unit.value})")


# Whether or not the Marker Beacon is in Test/Mute mode.
class _FlightSim_Radio_MARKER_BEACON_TEST_MUTE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:MARKER BEACON TEST MUTE,{unit.value})")


# Marker audio flag.
class _FlightSim_Radio_MARKER_SOUND:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:MARKER SOUND,{unit.value})")


# Middle marker state.
class _FlightSim_Radio_MIDDLE_MARKER:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:MIDDLE MARKER,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:MIDDLE MARKER,{unit.value})")


# Returns the latitude, longitude and altitude of the middle marker.
#! SIMCONNECT_DATA_LATLONALT
# structure
class _FlightSim_Radio_MIDDLE_MARKER_LATLONALT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: ''):
        return self._.get(f"(A:MIDDLE MARKER LATLONALT,{unit.value})")


# Outer marker state.
class _FlightSim_Radio_OUTER_MARKER:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:OUTER MARKER,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:OUTER MARKER,{unit.value})")


# Returns the latitude, longitude and altitude of the outer marker.
#! SIMCONNECT_DATA_LATLONALT
# structure
class _FlightSim_Radio_OUTER_MARKER_LATLONALT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: ''):
        return self._.get(f"(A:OUTER MARKER LATLONALT,{unit.value})")


# Nav active frequency. Index is 1 or 2.
class _FlightSim_Radio_NAV_ACTIVE_FREQUENCY:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Frequency.MEGAHERTZ'):
        return self._.get(f"(A:NAV ACTIVE FREQUENCY:{self._index},{unit.value})")


# Flag if Nav equipped on aircraft.
class _FlightSim_Radio_NAV_AVAILABLE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:NAV AVAILABLE:{self._index},{unit.value})")


# Returns the listed bit flags.
#! Flags:
# 
# BIT0:[index] 1=back course available
# BIT1:[index] 1=localizer tuned in
# BIT2:[index] 1=on course
# BIT7:[index] 1=station active
class _FlightSim_Radio_NAV_BACK_COURSE_FLAGS:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: ''):
        return self._.get(f"(A:NAV BACK COURSE FLAGS:{self._index},{unit.value})")


# CDI needle deflection (+/- 127).
class _FlightSim_Radio_NAV_CDI:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:NAV CDI:{self._index},{unit.value})")


# Closest DME distance. Requires an index value from 1 to 4 to set which NAV to target.
# Note that this SimVar will only work if the NAV1_CLOSE_FREQ_SET key event has been set to 1 (TRUE).
class _FlightSim_Radio_NAV_CLOSE_DME:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Length.NAUTICAL_MILE'):
        return self._.get(f"(A:NAV CLOSE DME:{self._index},{unit.value})")


# Note that this SimVar will only work if the NAV1_CLOSE_FREQ_SET key event has been set to 1 (TRUE).
class _FlightSim_Radio_NAV_CLOSE_FREQUENCY:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Frequency.HERTZ'):
        return self._.get(f"(A:NAV CLOSE FREQUENCY:{self._index},{unit.value})")


# Note that this SimVar will only work if the NAV1_CLOSE_FREQ_SET key event has been set to 1 (TRUE).
class _FlightSim_Radio_NAV_CLOSE_IDENT:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.STRING'):
        return self._.get(f"(A:NAV CLOSE IDENT:{self._index},{unit.value})")


# Note that this SimVar will only work if the NAV1_CLOSE_FREQ_SET key event has been set to 1 (TRUE).
class _FlightSim_Radio_NAV_CLOSE_LOCALIZER:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:NAV CLOSE LOCALIZER:{self._index},{unit.value})")


# Note that this SimVar will only work if the NAV1_CLOSE_FREQ_SET key event has been set to 1 (TRUE).
class _FlightSim_Radio_NAV_CLOSE_NAME:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.STRING'):
        return self._.get(f"(A:NAV CLOSE NAME:{self._index},{unit.value})")


# Returns bit flags with the listed meaning.
#! Flags:
# 
# BIT7:[index] 0= VOR 1= Localizer
# BIT6:[index] 1= glideslope available
# BIT5:[index] 1= no localizer backcourse
# BIT4:[index] 1= DME transmitter at glide slope
# 
#                             transmitter
#                         
# BIT3:[index] 1= no nav signal available
# BIT2:[index] 1= voice available
# BIT1:[index] 1 = TACAN available
# BIT0:[index] 1= DME available
class _FlightSim_Radio_NAV_CODES:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: ''):
        return self._.get(f"(A:NAV CODES,{unit.value})")


# DME distance.
class _FlightSim_Radio_NAV_DME:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.NAUTICAL_MILE'):
        return self._.get(f"(A:NAV DME,{unit.value})")


# DME speed.
class _FlightSim_Radio_NAV_DMESPEED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.KNOT'):
        return self._.get(f"(A:NAV DMESPEED,{unit.value})")


# Returns the DME station.
#! SIMCONNECT_DATA_LATLONALT structure
class _FlightSim_Radio_NAV_DME_LATLONALT:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: ''):
        return self._.get(f"(A:NAV DME LATLONALT:{self._index},{unit.value})")


# Localizer course frequency
class _FlightSim_Radio_NAV_FREQUENCY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Frequency.HERTZ'):
        return self._.get(f"(A:NAV FREQUENCY,{unit.value})")


# The glide slope gradient. The value returned is an integer value formed as follows:
# So, for example, a glide slope of 2.7º would return a value of 6174. TO get the value in degrees, then use NAV_RAW_GLIDE_SLOPE instead.
class _FlightSim_Radio_NAV_GLIDE_SLOPE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:NAV GLIDE SLOPE,{unit.value})")


# Difference between current position and glideslope angle. Note that this provides 32 bit floating point precision, rather than the 8 bit integer precision of NAV GSI.
class _FlightSim_Radio_NAV_GLIDE_SLOPE_ERROR:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:NAV GLIDE SLOPE ERROR,{unit.value})")


# The distance between the plane and the Glide beacon.
class _FlightSim_Radio_NAV_GLIDE_SLOPE_LENGTH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.FOOT'):
        return self._.get(f"(A:NAV GLIDE SLOPE LENGTH,{unit.value})")


# Glideslope needle deflection (+/- 119). Note that this provides only 8 bit precision, whereas NAV GLIDE SLOPE ERROR provides 32 bit floating point precision.
class _FlightSim_Radio_NAV_GSI:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:NAV GSI,{unit.value})")


# Glideslope flag.
class _FlightSim_Radio_NAV_GS_FLAG:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:NAV GS FLAG,{unit.value})")


# Returns the glide slope.
#! SIMCONNECT_DATA_LATLONALT structure
class _FlightSim_Radio_NAV_GS_LATLONALT:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: ''):
        return self._.get(f"(A:NAV GS LATLONALT:{self._index},{unit.value})")


# Nav GS latitude, longitude, altitude.
#! SIMCONNECT_DATA_LATLONALT structure
class _FlightSim_Radio_NAV_GS_LLAF64:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: ''):
        return self._.get(f"(A:NAV GS LLAF64,{unit.value})")


# Flag if found a close station with a DME.
class _FlightSim_Radio_NAV_HAS_CLOSE_DME:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:NAV HAS CLOSE DME,{unit.value})")


# Flag if found a close localizer station.
class _FlightSim_Radio_NAV_HAS_CLOSE_LOCALIZER:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:NAV HAS CLOSE LOCALIZER,{unit.value})")


# Flag if tuned station has a DME.
class _FlightSim_Radio_NAV_HAS_DME:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:NAV HAS DME,{unit.value})")


# Flag if tuned station has a glideslope.
class _FlightSim_Radio_NAV_HAS_GLIDE_SLOPE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:NAV HAS GLIDE SLOPE,{unit.value})")


# Flag if tuned station is a localizer.
class _FlightSim_Radio_NAV_HAS_LOCALIZER:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:NAV HAS LOCALIZER,{unit.value})")


# Flag if Nav has signal.
class _FlightSim_Radio_NAV_HAS_NAV:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:NAV HAS NAV,{unit.value})")


# Flag if Nav has a Tacan.
class _FlightSim_Radio_NAV_HAS_TACAN:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:NAV HAS TACAN,{unit.value})")


# ICAO code.
class _FlightSim_Radio_NAV_IDENT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.STRING'):
        return self._.get(f"(A:NAV IDENT,{unit.value})")


# Localizer course heading.
class _FlightSim_Radio_NAV_LOCALIZER:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:NAV LOCALIZER,{unit.value})")


# The airport ICAO ident for the localizer that is currently tuned on the nav radio (like 'EGLL' or 'KJFK')
class _FlightSim_Radio_NAV_LOC_AIRPORT_IDENT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.STRING'):
        return self._.get(f"(A:NAV LOC AIRPORT IDENT,{unit.value})")


# The letter code for the runway that the currently tuned localizer is tuned to.
#! String
#                     
# 'L' - Left
# 'R' - Right
# 'C' - Center
# 'W' - Water
# 'A' - A
# 'B' - B
class _FlightSim_Radio_NAV_LOC_RUNWAY_DESIGNATOR:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: ''):
        return self._.get(f"(A:NAV LOC RUNWAY DESIGNATOR,{unit.value})")


# NAV LOC RUNWAY NUMBER - The number portion of the runway that the currently tuned localizer is tuned to (so if the runway was 15L, this would be 15).
#! String
# 
# '1' - '36'
# 'N'
# 'NE'
# 'E'
# 'SE'
# 'S'
# 'SW'
# 'W'
# 'NW'
class _FlightSim_Radio_NAV_LOC_RUNWAY_NUMBER:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: ''):
        return self._.get(f"(A:NAV LOC RUNWAY NUMBER,{unit.value})")


# Magnetic variation of tuned Nav station.
class _FlightSim_Radio_NAV_MAGVAR:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:NAV MAGVAR,{unit.value})")


# Descriptive name.
class _FlightSim_Radio_NAV_NAME:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.STRING'):
        return self._.get(f"(A:NAV NAME,{unit.value})")


# OBS setting. Index of 1 or 2.
class _FlightSim_Radio_NAV_OBS:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:NAV OBS,{unit.value})")


# Radial that aircraft is on.
class _FlightSim_Radio_NAV_RADIAL:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:NAV RADIAL,{unit.value})")


# Difference between current radial and OBS tuned radial.
class _FlightSim_Radio_NAV_RADIAL_ERROR:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:NAV RADIAL ERROR,{unit.value})")


# The glide slope angle.
class _FlightSim_Radio_NAV_RAW_GLIDE_SLOPE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:NAV RAW GLIDE SLOPE,{unit.value})")


# Relative bearing to station.
class _FlightSim_Radio_NAV_RELATIVE_BEARING_TO_STATION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:NAV RELATIVE BEARING TO STATION,{unit.value})")


# Nav signal strength.
class _FlightSim_Radio_NAV_SIGNAL:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:NAV SIGNAL,{unit.value})")


# Nav audio flag. Index of 1 or 2.
class _FlightSim_Radio_NAV_SOUND:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:NAV SOUND:{self._index},{unit.value})")


# Nav standby frequency. Index is 1 or 2.
class _FlightSim_Radio_NAV_STANDBY_FREQUENCY:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Frequency.MEGAHERTZ'):
        return self._.get(f"(A:NAV STANDBY FREQUENCY:{self._index},{unit.value})")


# Returns whether the Nav is going to or from the current radial (or is off).
class _FlightSim_Radio_NAV_TOFROM:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        OFF = 0
        TO = 1
        FROM = 2

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:NAV TOFROM,{unit.value})")


# The volume of the Nav radio.
class _FlightSim_Radio_NAV_VOLUME:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:NAV VOLUME,{unit.value})")


# Distance of the VOR beacon.
class _FlightSim_Radio_NAV_VOR_DISTANCE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.METER'):
        return self._.get(f"(A:NAV VOR DISTANCE,{unit.value})")


# Returns the VOR station latitude, longitude and altitude.
#! SIMCONNECT_DATA_LATLONALT structure
class _FlightSim_Radio_NAV_VOR_LATLONALT:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: ''):
        return self._.get(f"(A:NAV VOR LATLONALT:{self._index},{unit.value})")


# Nav VOR latitude, longitude, altitude.
#! SIMCONNECT_DATA_LATLONALT structure
class _FlightSim_Radio_NAV_VOR_LLAF64:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: ''):
        return self._.get(f"(A:NAV VOR LLAF64,{unit.value})")


# The active channel used by the indexed Tacan receiver on the aircraft, from 1 to 127.
class _FlightSim_Radio_TACAN_ACTIVE_CHANNEL:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:TACAN ACTIVE CHANNEL:{self._index},{unit.value})")


# The active mode used by the indexed Tacan receiver on the aircraft, where 0 = X and 1 = Y.
class _FlightSim_Radio_TACAN_ACTIVE_MODE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:TACAN ACTIVE MODE:{self._index},{unit.value})")


# Will be TRUE (1) if NAV1, NAV2, NAV3 or NAV4 can receive Tacan (depending on the index - 1, 2, 3, or 4), or FALSE (0) otherwise.
class _FlightSim_Radio_TACAN_AVAILABLE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:TACAN AVAILABLE:{self._index},{unit.value})")


# Tells whether the Tacan is driving the Nav 1 indicator (TRUE, 1) or not (FALSE, 0), for autopilot purposes.
class _FlightSim_Radio_TACAN_DRIVES_NAV1:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:TACAN DRIVES NAV1:{self._index},{unit.value})")


# The Tacan OBS setting, in degrees.
class _FlightSim_Radio_TACAN_OBS:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:TACAN OBS:{self._index},{unit.value})")


# The standby channel used by the indexed Tacan receiver on the aircraft, from 1 to 127.
class _FlightSim_Radio_TACAN_STANDBY_CHANNEL:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:TACAN STANDBY CHANNEL:{self._index},{unit.value})")


# Indicates the indexed Tacan receiver standby mode, where 0 = X and 1 = Y.
class _FlightSim_Radio_TACAN_STANDBY_MODE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:TACAN STANDBY MODE:{self._index},{unit.value})")


# The CDI needle deflection amount(course deviation) to the station. Can be +/- 127.
class _FlightSim_Radio_TACAN_STATION_CDI:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:TACAN STATION CDI:{self._index},{unit.value})")


# The distance between the Tacan station position and the aircraft position. The index value refers to the Tacan receiver connected to the station (1 or 2).
class _FlightSim_Radio_TACAN_STATION_DISTANCE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Length.METER'):
        return self._.get(f"(A:TACAN STATION DISTANCE:{self._index},{unit.value})")


# The tuned station identifier for the indexed Tacan.
class _FlightSim_Radio_TACAN_STATION_IDENT:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.STRING'):
        return self._.get(f"(A:TACAN STATION IDENT:{self._index},{unit.value})")


# Retrieves the latitude, longitude and altitude of the Tacan station.
#! SIMCONNECT_DATA_LATLONALT
# structure
class _FlightSim_Radio_TACAN_STATION_LATLONALT:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: ''):
        return self._.get(f"(A:TACAN STATION LATLONALT:{self._index},{unit.value})")


# The radial between the Tacan station and the aircraft.
class _FlightSim_Radio_TACAN_STATION_RADIAL:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:TACAN STATION RADIAL:{self._index},{unit.value})")


# Difference between the current radial and OBS tuned radial, in degrees.
class _FlightSim_Radio_TACAN_STATION_RADIAL_ERROR:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:TACAN STATION RADIAL ERROR:{self._index},{unit.value})")


# Returns whether the indexed Tacan is going to or from the current radial (or is off).
class _FlightSim_Radio_TACAN_STATION_TOFROM:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    class Unit(Enum):
        OFF = 0
        TO = 1
        FROM = 2

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:TACAN STATION TOFROM:{self._index},{unit.value})")


# The volume value of the indexed Tacan receiver on the aircraft.
class _FlightSim_Radio_TACAN_VOLUME:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:TACAN VOLUME:{self._index},{unit.value})")


# On which channel the copilot is transmitting.
class _FlightSim_Radio_COPILOT_TRANSMITTER_TYPE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        COM1 = 0
        COM2 = 1
        COM3 = 2
        TEL = 3
        NONE = 4

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:COPILOT TRANSMITTER TYPE,{unit.value})")


# Whether or not the copilot is transmitting.
class _FlightSim_Radio_COPILOT_TRANSMITTING:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:COPILOT TRANSMITTING,{unit.value})")


# On which channel the pilot is transmitting.
class _FlightSim_Radio_PILOT_TRANSMITTER_TYPE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        COM1 = 0
        COM2 = 1
        COM3 = 2
        TEL = 3
        NONE = 4

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:PILOT TRANSMITTER TYPE,{unit.value})")


# Whether or not the pilot is transmitting.
class _FlightSim_Radio_PILOT_TRANSMITTING:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:PILOT TRANSMITTING,{unit.value})")


# Currently not used within the simulation.
#! -
class _FlightSim_Radio_RADIOS_AVAILABLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: ''):
        return self._.get(f"(A:RADIOS AVAILABLE,{unit.value})")


# Radar altitude.
class _FlightSim_Radio_RADIO_HEIGHT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.FOOT'):
        return self._.get(f"(A:RADIO HEIGHT,{unit.value})")


# True if a transponder is available.
class _FlightSim_Radio_TRANSPONDER_AVAILABLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:TRANSPONDER AVAILABLE,{unit.value})")


# 4-digit code.
class _FlightSim_Radio_TRANSPONDER_CODE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Frequency.BCD16'):
        return self._.get(f"(A:TRANSPONDER CODE:{self._index},{unit.value})")


# This can set the Ident transponder using the KEY_XPNDR_IDENT_SET, KEY_XPNDR_IDENT_TOGGLE, KEY_XPNDR_IDENT_ON or KEY_XPNDR_IDENT_OFF Event IDs (see XPNDR (Transponder) section for more information). When set to true, it will automatically turn false after 18 seconds.
class _FlightSim_Radio_TRANSPONDER_IDENT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:TRANSPONDER IDENT,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:TRANSPONDER IDENT,{unit.value})")


# Transponder State.
class _FlightSim_Radio_TRANSPONDER_STATE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        OFF = 0
        STANDBY = 1
        TEST = 2
        ON = 3
        ALT = 4
        GROUND = 5

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:TRANSPONDER STATE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM', value: str):
        self._.set(f"{value} (>A:TRANSPONDER STATE,{unit.value})")


class _FlightSim_System:
    def __init__(self, flightSim):
        self._ = flightSim
        self.AIRSPEED_TRUE_CALIBRATE = _FlightSim_System_AIRSPEED_TRUE_CALIBRATE(flightSim)
        self.ALTERNATE_STATIC_SOURCE_OPEN = lambda index: _FlightSim_System_ALTERNATE_STATIC_SOURCE_OPEN(flightSim, index)
        self.ANEMOMETER_PCT_RPM = _FlightSim_System_ANEMOMETER_PCT_RPM(flightSim)
        self.ANGLE_OF_ATTACK_INDICATOR = _FlightSim_System_ANGLE_OF_ATTACK_INDICATOR(flightSim)
        self.ANNUNCIATOR_SWITCH = _FlightSim_System_ANNUNCIATOR_SWITCH(flightSim)
        self.APPLY_HEAT_TO_SYSTEMS = _FlightSim_System_APPLY_HEAT_TO_SYSTEMS(flightSim)
        self.AUDIO_PANEL_AVAILABLE = _FlightSim_System_AUDIO_PANEL_AVAILABLE(flightSim)
        self.AUDIO_PANEL_VOLUME = _FlightSim_System_AUDIO_PANEL_VOLUME(flightSim)
        self.AUTOTHROTTLE_ACTIVE = _FlightSim_System_AUTOTHROTTLE_ACTIVE(flightSim)
        self.AUTO_COORDINATION = _FlightSim_System_AUTO_COORDINATION(flightSim)
        self.AVIONICS_MASTER_SWITCH = lambda index: _FlightSim_System_AVIONICS_MASTER_SWITCH(flightSim, index)
        self.CABIN_NO_SMOKING_ALERT_SWITCH = _FlightSim_System_CABIN_NO_SMOKING_ALERT_SWITCH(flightSim)
        self.CABIN_SEATBELTS_ALERT_SWITCH = _FlightSim_System_CABIN_SEATBELTS_ALERT_SWITCH(flightSim)
        self.CANOPY_OPEN = _FlightSim_System_CANOPY_OPEN(flightSim)
        self.CARB_HEAT_AVAILABLE = _FlightSim_System_CARB_HEAT_AVAILABLE(flightSim)
        self.DELTA_HEADING_RATE = _FlightSim_System_DELTA_HEADING_RATE(flightSim)
        self.DME_SOUND = _FlightSim_System_DME_SOUND(flightSim)
        self.ELT_ACTIVATED = _FlightSim_System_ELT_ACTIVATED(flightSim)
        self.EXTERNAL_SYSTEM_VALUE = _FlightSim_System_EXTERNAL_SYSTEM_VALUE(flightSim)
        self.FIRE_BOTTLE_DISCHARGED = _FlightSim_System_FIRE_BOTTLE_DISCHARGED(flightSim)
        self.FIRE_BOTTLE_SWITCH = _FlightSim_System_FIRE_BOTTLE_SWITCH(flightSim)
        self.GLASSCOCKPIT_AUTOMATIC_BRIGHTNESS = _FlightSim_System_GLASSCOCKPIT_AUTOMATIC_BRIGHTNESS(flightSim)
        self.GPWS_SYSTEM_ACTIVE = _FlightSim_System_GPWS_SYSTEM_ACTIVE(flightSim)
        self.GPWS_WARNING = _FlightSim_System_GPWS_WARNING(flightSim)
        self.GYRO_DRIFT_ERROR = _FlightSim_System_GYRO_DRIFT_ERROR(flightSim)
        self.HAS_STALL_PROTECTION = _FlightSim_System_HAS_STALL_PROTECTION(flightSim)
        self.HEADING_INDICATOR = _FlightSim_System_HEADING_INDICATOR(flightSim)
        self.INDICATED_ALTITUDE = _FlightSim_System_INDICATED_ALTITUDE(flightSim)
        self.INDICATED_ALTITUDE_CALIBRATED = _FlightSim_System_INDICATED_ALTITUDE_CALIBRATED(flightSim)
        self.INDICATED_ALTITUDE_EX1 = _FlightSim_System_INDICATED_ALTITUDE_EX1(flightSim)
        self.INDUCTOR_COMPASS_HEADING_REF = _FlightSim_System_INDUCTOR_COMPASS_HEADING_REF(flightSim)
        self.INDUCTOR_COMPASS_PERCENT_DEVIATION = _FlightSim_System_INDUCTOR_COMPASS_PERCENT_DEVIATION(flightSim)
        self.INSTRUMENTS_AVAILABLE = _FlightSim_System_INSTRUMENTS_AVAILABLE(flightSim)
        self.INTERCOM_MODE = _FlightSim_System_INTERCOM_MODE(flightSim)
        self.INTERCOM_SYSTEM_ACTIVE = _FlightSim_System_INTERCOM_SYSTEM_ACTIVE(flightSim)
        self.IS_ALTITUDE_FREEZE_ON = _FlightSim_System_IS_ALTITUDE_FREEZE_ON(flightSim)
        self.IS_ATTITUDE_FREEZE_ON = _FlightSim_System_IS_ATTITUDE_FREEZE_ON(flightSim)
        self.IS_LATITUDE_LONGITUDE_FREEZE_ON = _FlightSim_System_IS_LATITUDE_LONGITUDE_FREEZE_ON(flightSim)
        self.KOHLSMAN_SETTING_HG = lambda index: _FlightSim_System_KOHLSMAN_SETTING_HG(flightSim, index)
        self.KOHLSMAN_SETTING_MB = lambda index: _FlightSim_System_KOHLSMAN_SETTING_MB(flightSim, index)
        self.KOHLSMAN_SETTING_STD = lambda index: _FlightSim_System_KOHLSMAN_SETTING_STD(flightSim, index)
        self.MAGNETIC_COMPASS = _FlightSim_System_MAGNETIC_COMPASS(flightSim)
        self.MANUAL_FUEL_PUMP_HANDLE = _FlightSim_System_MANUAL_FUEL_PUMP_HANDLE(flightSim)
        self.OVERSPEED_WARNING = _FlightSim_System_OVERSPEED_WARNING(flightSim)
        self.PANEL_ANTI_ICE_SWITCH = _FlightSim_System_PANEL_ANTI_ICE_SWITCH(flightSim)
        self.PITOT_ICE_PCT = _FlightSim_System_PITOT_ICE_PCT(flightSim)
        self.PITOT_HEAT = _FlightSim_System_PITOT_HEAT(flightSim)
        self.PITOT_HEAT_SWITCH = lambda index: _FlightSim_System_PITOT_HEAT_SWITCH(flightSim, index)
        self.PLANE_HEADING_DEGREES_GYRO = _FlightSim_System_PLANE_HEADING_DEGREES_GYRO(flightSim)
        self.PRESSURE_ALTITUDE = _FlightSim_System_PRESSURE_ALTITUDE(flightSim)
        self.PRESSURIZATION_CABIN_ALTITUDE = _FlightSim_System_PRESSURIZATION_CABIN_ALTITUDE(flightSim)
        self.PRESSURIZATION_CABIN_ALTITUDE_GOAL = _FlightSim_System_PRESSURIZATION_CABIN_ALTITUDE_GOAL(flightSim)
        self.PRESSURIZATION_CABIN_ALTITUDE_RATE = _FlightSim_System_PRESSURIZATION_CABIN_ALTITUDE_RATE(flightSim)
        self.PRESSURIZATION_DUMP_SWITCH = _FlightSim_System_PRESSURIZATION_DUMP_SWITCH(flightSim)
        self.PRESSURIZATION_PRESSURE_DIFFERENTIAL = _FlightSim_System_PRESSURIZATION_PRESSURE_DIFFERENTIAL(flightSim)
        self.RAD_INS_SWITCH = _FlightSim_System_RAD_INS_SWITCH(flightSim)
        self.SELECTED_DME = _FlightSim_System_SELECTED_DME(flightSim)
        self.SMOKESYSTEM_AVAILABLE = _FlightSim_System_SMOKESYSTEM_AVAILABLE(flightSim)
        self.SMOKE_ENABLE = _FlightSim_System_SMOKE_ENABLE(flightSim)
        self.SPEAKER_ACTIVE = _FlightSim_System_SPEAKER_ACTIVE(flightSim)
        self.STALL_HORN_AVAILABLE = _FlightSim_System_STALL_HORN_AVAILABLE(flightSim)
        self.STALL_PROTECTION_OFF_LIMIT = _FlightSim_System_STALL_PROTECTION_OFF_LIMIT(flightSim)
        self.STALL_PROTECTION_ON_GOAL = _FlightSim_System_STALL_PROTECTION_ON_GOAL(flightSim)
        self.STALL_PROTECTION_ON_LIMIT = _FlightSim_System_STALL_PROTECTION_ON_LIMIT(flightSim)
        self.STALL_WARNING = _FlightSim_System_STALL_WARNING(flightSim)
        self.STRUCTURAL_DEICE_SWITCH = _FlightSim_System_STRUCTURAL_DEICE_SWITCH(flightSim)
        self.SUCTION_PRESSURE = _FlightSim_System_SUCTION_PRESSURE(flightSim)
        self.SYSTEMS_AVAILABLE = _FlightSim_System_SYSTEMS_AVAILABLE(flightSim)
        self.TAILHOOK_HANDLE = _FlightSim_System_TAILHOOK_HANDLE(flightSim)
        self.TAILHOOK_POSITION = _FlightSim_System_TAILHOOK_POSITION(flightSim)
        self.TOW_RELEASE_HANDLE = _FlightSim_System_TOW_RELEASE_HANDLE(flightSim)
        self.TRUE_AIRSPEED_SELECTED = _FlightSim_System_TRUE_AIRSPEED_SELECTED(flightSim)
        self.TURN_COORDINATOR_BALL = _FlightSim_System_TURN_COORDINATOR_BALL(flightSim)
        self.TURN_COORDINATOR_BALL_INV = _FlightSim_System_TURN_COORDINATOR_BALL_INV(flightSim)
        self.TURN_INDICATOR_RATE = _FlightSim_System_TURN_INDICATOR_RATE(flightSim)
        self.TURN_INDICATOR_SWITCH = _FlightSim_System_TURN_INDICATOR_SWITCH(flightSim)
        self.WINDSHIELD_DEICE_SWITCH = _FlightSim_System_WINDSHIELD_DEICE_SWITCH(flightSim)
        self.WISKEY_COMPASS_INDICATION_DEGREES = _FlightSim_System_WISKEY_COMPASS_INDICATION_DEGREES(flightSim)
        self.VARIOMETER_MAC_CREADY_SETTING = _FlightSim_System_VARIOMETER_MAC_CREADY_SETTING(flightSim)
        self.VARIOMETER_NETTO = _FlightSim_System_VARIOMETER_NETTO(flightSim)
        self.VARIOMETER_RATE = _FlightSim_System_VARIOMETER_RATE(flightSim)
        self.VARIOMETER_SPEED_TO_FLY = _FlightSim_System_VARIOMETER_SPEED_TO_FLY(flightSim)
        self.VARIOMETER_SPEED_TO_FLY_GLIDE_RATIO = _FlightSim_System_VARIOMETER_SPEED_TO_FLY_GLIDE_RATIO(flightSim)
        self.VARIOMETER_SWITCH = _FlightSim_System_VARIOMETER_SWITCH(flightSim)
        self.VARIOMETER_TOTAL_ENERGY = _FlightSim_System_VARIOMETER_TOTAL_ENERGY(flightSim)
        self.WATER_BALLAST_TANK_CAPACITY = lambda index: _FlightSim_System_WATER_BALLAST_TANK_CAPACITY(flightSim, index)
        self.WATER_BALLAST_TANK_NUMBER = _FlightSim_System_WATER_BALLAST_TANK_NUMBER(flightSim)
        self.WATER_BALLAST_TANK_QUANTITY = lambda index: _FlightSim_System_WATER_BALLAST_TANK_QUANTITY(flightSim, index)
        self.WATER_BALLAST_VALVE = _FlightSim_System_WATER_BALLAST_VALVE(flightSim)
        self.WATER_BALLAST_VALVE_FLOW_RATE = _FlightSim_System_WATER_BALLAST_VALVE_FLOW_RATE(flightSim)
        self.WATER_BALLAST_EVERY_VALVE_OPEN = _FlightSim_System_WATER_BALLAST_EVERY_VALVE_OPEN(flightSim)
        self.IS_ANY_INTERIOR_LIGHT_ON = _FlightSim_System_IS_ANY_INTERIOR_LIGHT_ON(flightSim)
        self.LANDING_LIGHT_PBH = _FlightSim_System_LANDING_LIGHT_PBH(flightSim)
        self.LIGHT_BEACON = _FlightSim_System_LIGHT_BEACON(flightSim)
        self.LIGHT_BEACON_ON = _FlightSim_System_LIGHT_BEACON_ON(flightSim)
        self.LIGHT_BACKLIGHT_INTENSITY = _FlightSim_System_LIGHT_BACKLIGHT_INTENSITY(flightSim)
        self.LIGHT_BRAKE_ON = _FlightSim_System_LIGHT_BRAKE_ON(flightSim)
        self.LIGHT_CABIN = _FlightSim_System_LIGHT_CABIN(flightSim)
        self.LIGHT_CABIN_ON = _FlightSim_System_LIGHT_CABIN_ON(flightSim)
        self.LIGHT_CABIN_POWER_SETTING = _FlightSim_System_LIGHT_CABIN_POWER_SETTING(flightSim)
        self.LIGHT_GLARESHIELD = _FlightSim_System_LIGHT_GLARESHIELD(flightSim)
        self.LIGHT_GLARESHIELD_ON = _FlightSim_System_LIGHT_GLARESHIELD_ON(flightSim)
        self.LIGHT_GLARESHIELD_POWER_SETTING = _FlightSim_System_LIGHT_GLARESHIELD_POWER_SETTING(flightSim)
        self.LIGHT_GYROLIGHT_INTENSITY = _FlightSim_System_LIGHT_GYROLIGHT_INTENSITY(flightSim)
        self.LIGHT_HEAD_ON = _FlightSim_System_LIGHT_HEAD_ON(flightSim)
        self.LIGHT_HEADLIGHT_INTENSITY = _FlightSim_System_LIGHT_HEADLIGHT_INTENSITY(flightSim)
        self.LIGHT_LANDING_ON = _FlightSim_System_LIGHT_LANDING_ON(flightSim)
        self.LIGHT_LANDING = _FlightSim_System_LIGHT_LANDING(flightSim)
        self.LIGHT_LOGO = _FlightSim_System_LIGHT_LOGO(flightSim)
        self.LIGHT_LOGO_ON = _FlightSim_System_LIGHT_LOGO_ON(flightSim)
        self.LIGHT_NAV_ON = _FlightSim_System_LIGHT_NAV_ON(flightSim)
        self.LIGHT_NAV = _FlightSim_System_LIGHT_NAV(flightSim)
        self.LIGHT_ON_STATES = _FlightSim_System_LIGHT_ON_STATES(flightSim)
        self.LIGHT_PANEL = _FlightSim_System_LIGHT_PANEL(flightSim)
        self.LIGHT_PANEL_ON = _FlightSim_System_LIGHT_PANEL_ON(flightSim)
        self.LIGHT_PANEL_POWER_SETTING = _FlightSim_System_LIGHT_PANEL_POWER_SETTING(flightSim)
        self.LIGHT_PEDESTRAL = _FlightSim_System_LIGHT_PEDESTRAL(flightSim)
        self.LIGHT_PEDESTRAL_ON = _FlightSim_System_LIGHT_PEDESTRAL_ON(flightSim)
        self.LIGHT_PEDESTRAL_POWER_SETTING = _FlightSim_System_LIGHT_PEDESTRAL_POWER_SETTING(flightSim)
        self.LIGHT_POTENTIOMETER = lambda index: _FlightSim_System_LIGHT_POTENTIOMETER(flightSim, index)
        self.LIGHT_RECOGNITION = _FlightSim_System_LIGHT_RECOGNITION(flightSim)
        self.LIGHT_RECOGNITION_ON = _FlightSim_System_LIGHT_RECOGNITION_ON(flightSim)
        self.LIGHT_STATES = _FlightSim_System_LIGHT_STATES(flightSim)
        self.LIGHT_STROBE = _FlightSim_System_LIGHT_STROBE(flightSim)
        self.LIGHT_STROBE_ON = _FlightSim_System_LIGHT_STROBE_ON(flightSim)
        self.LIGHT_TAXI = _FlightSim_System_LIGHT_TAXI(flightSim)
        self.LIGHT_TAXI_ON = _FlightSim_System_LIGHT_TAXI_ON(flightSim)
        self.LIGHT_WING = _FlightSim_System_LIGHT_WING(flightSim)
        self.LIGHT_WING_ON = _FlightSim_System_LIGHT_WING_ON(flightSim)
        self.MANUAL_INSTRUMENT_LIGHTS = _FlightSim_System_MANUAL_INSTRUMENT_LIGHTS(flightSim)
        self.STROBES_AVAILABLE = _FlightSim_System_STROBES_AVAILABLE(flightSim)
        self.STROBE_FLASH = _FlightSim_System_STROBE_FLASH(flightSim)
        self.HYDRAULIC_PRESSURE = lambda index: _FlightSim_System_HYDRAULIC_PRESSURE(flightSim, index)
        self.HYDRAULIC_RESERVOIR_PERCENT = lambda index: _FlightSim_System_HYDRAULIC_RESERVOIR_PERCENT(flightSim, index)
        self.HYDRAULIC_SWITCH = _FlightSim_System_HYDRAULIC_SWITCH(flightSim)
        self.HYDRAULIC_SYSTEM_INTEGRITY = _FlightSim_System_HYDRAULIC_SYSTEM_INTEGRITY(flightSim)
        self.PARTIAL_PANEL_ADF = _FlightSim_System_PARTIAL_PANEL_ADF(flightSim)
        self.PARTIAL_PANEL_AIRSPEED = _FlightSim_System_PARTIAL_PANEL_AIRSPEED(flightSim)
        self.PARTIAL_PANEL_ALTIMETER = _FlightSim_System_PARTIAL_PANEL_ALTIMETER(flightSim)
        self.PARTIAL_PANEL_ATTITUDE = _FlightSim_System_PARTIAL_PANEL_ATTITUDE(flightSim)
        self.PARTIAL_PANEL_AVIONICS = _FlightSim_System_PARTIAL_PANEL_AVIONICS(flightSim)
        self.PARTIAL_PANEL_COMM = _FlightSim_System_PARTIAL_PANEL_COMM(flightSim)
        self.PARTIAL_PANEL_COMPASS = _FlightSim_System_PARTIAL_PANEL_COMPASS(flightSim)
        self.PARTIAL_PANEL_ELECTRICAL = _FlightSim_System_PARTIAL_PANEL_ELECTRICAL(flightSim)
        self.PARTIAL_PANEL_ENGINE = _FlightSim_System_PARTIAL_PANEL_ENGINE(flightSim)
        self.PARTIAL_PANEL_FUEL_INDICATOR = _FlightSim_System_PARTIAL_PANEL_FUEL_INDICATOR(flightSim)
        self.PARTIAL_PANEL_HEADING = _FlightSim_System_PARTIAL_PANEL_HEADING(flightSim)
        self.PARTIAL_PANEL_NAV = _FlightSim_System_PARTIAL_PANEL_NAV(flightSim)
        self.PARTIAL_PANEL_PITOT = _FlightSim_System_PARTIAL_PANEL_PITOT(flightSim)
        self.PARTIAL_PANEL_TRANSPONDER = _FlightSim_System_PARTIAL_PANEL_TRANSPONDER(flightSim)
        self.PARTIAL_PANEL_TURN_COORDINATOR = _FlightSim_System_PARTIAL_PANEL_TURN_COORDINATOR(flightSim)
        self.PARTIAL_PANEL_VACUUM = _FlightSim_System_PARTIAL_PANEL_VACUUM(flightSim)
        self.PARTIAL_PANEL_VERTICAL_VELOCITY = _FlightSim_System_PARTIAL_PANEL_VERTICAL_VELOCITY(flightSim)
        self.DROPPABLE_OBJECTS_COUNT = lambda index: _FlightSim_System_DROPPABLE_OBJECTS_COUNT(flightSim, index)
        self.DROPPABLE_OBJECTS_TYPE = lambda index: _FlightSim_System_DROPPABLE_OBJECTS_TYPE(flightSim, index)
        self.DROPPABLE_OBJECTS_UI_NAME = lambda index: _FlightSim_System_DROPPABLE_OBJECTS_UI_NAME(flightSim, index)
        self.PAYLOAD_STATION_COUNT = _FlightSim_System_PAYLOAD_STATION_COUNT(flightSim)
        self.PAYLOAD_STATION_NAME = lambda index: _FlightSim_System_PAYLOAD_STATION_NAME(flightSim, index)
        self.PAYLOAD_STATION_NUM_SIMOBJECTS = lambda index: _FlightSim_System_PAYLOAD_STATION_NUM_SIMOBJECTS(flightSim, index)
        self.PAYLOAD_STATION_OBJECT = lambda index: _FlightSim_System_PAYLOAD_STATION_OBJECT(flightSim, index)
        self.PAYLOAD_STATION_WEIGHT = lambda index: _FlightSim_System_PAYLOAD_STATION_WEIGHT(flightSim, index)
        self.WARNING_FUEL = _FlightSim_System_WARNING_FUEL(flightSim)
        self.WARNING_FUEL_LEFT = _FlightSim_System_WARNING_FUEL_LEFT(flightSim)
        self.WARNING_FUEL_RIGHT = _FlightSim_System_WARNING_FUEL_RIGHT(flightSim)
        self.WARNING_LOW_HEIGHT = _FlightSim_System_WARNING_LOW_HEIGHT(flightSim)
        self.WARNING_OIL_PRESSURE = _FlightSim_System_WARNING_OIL_PRESSURE(flightSim)
        self.WARNING_VACUUM = _FlightSim_System_WARNING_VACUUM(flightSim)
        self.WARNING_VACUUM_LEFT = _FlightSim_System_WARNING_VACUUM_LEFT(flightSim)
        self.WARNING_VACUUM_RIGHT = _FlightSim_System_WARNING_VACUUM_RIGHT(flightSim)
        self.WARNING_VOLTAGE = _FlightSim_System_WARNING_VOLTAGE(flightSim)
        self.YOKE_X_INIDICATOR = _FlightSim_System_YOKE_X_INIDICATOR(flightSim)
        self.YOKE_X_POSITION = _FlightSim_System_YOKE_X_POSITION(flightSim)
        self.YOKE_X_POSITION_WITH_AP = _FlightSim_System_YOKE_X_POSITION_WITH_AP(flightSim)
        self.YOKE_Y_INIDICATOR = _FlightSim_System_YOKE_Y_INIDICATOR(flightSim)
        self.YOKE_Y_POSITION = _FlightSim_System_YOKE_Y_POSITION(flightSim)
        self.YOKE_Y_POSITION_WITH_AP = _FlightSim_System_YOKE_Y_POSITION_WITH_AP(flightSim)
        self.EXIT_OPEN = lambda index: _FlightSim_System_EXIT_OPEN(flightSim, index)
        self.EXIT_POSX = lambda index: _FlightSim_System_EXIT_POSX(flightSim, index)
        self.EXIT_POSY = lambda index: _FlightSim_System_EXIT_POSY(flightSim, index)
        self.EXIT_POSZ = lambda index: _FlightSim_System_EXIT_POSZ(flightSim, index)
        self.EXIT_TYPE = lambda index: _FlightSim_System_EXIT_TYPE(flightSim, index)


# Angle of True calibration scale on airspeed indicator.
class _FlightSim_System_AIRSPEED_TRUE_CALIBRATE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:AIRSPEED TRUE CALIBRATE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Angle.DEGREE', value: str):
        self._.set(f"{value} (>A:AIRSPEED TRUE CALIBRATE,{unit.value})")


# Alternate static air source.
class _FlightSim_System_ALTERNATE_STATIC_SOURCE_OPEN:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:ALTERNATE STATIC SOURCE OPEN:{self._index},{unit.value})")


# Anemometer rpm as a percentage.
class _FlightSim_System_ANEMOMETER_PCT_RPM:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:ANEMOMETER PCT RPM,{unit.value})")


# AoA indication.
class _FlightSim_System_ANGLE_OF_ATTACK_INDICATOR:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:ANGLE OF ATTACK INDICATOR,{unit.value})")


# Currently not used in the simulation.
class _FlightSim_System_ANNUNCIATOR_SWITCH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:ANNUNCIATOR SWITCH,{unit.value})")


# Used when too close to a fire.
class _FlightSim_System_APPLY_HEAT_TO_SYSTEMS:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:APPLY HEAT TO SYSTEMS,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:APPLY HEAT TO SYSTEMS,{unit.value})")


# True if the audio panel is available.
class _FlightSim_System_AUDIO_PANEL_AVAILABLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUDIO PANEL AVAILABLE,{unit.value})")


# The Volume of the Audio Panel.
class _FlightSim_System_AUDIO_PANEL_VOLUME:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:AUDIO PANEL VOLUME,{unit.value})")


# Auto-throttle active.
class _FlightSim_System_AUTOTHROTTLE_ACTIVE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTOTHROTTLE ACTIVE,{unit.value})")


# Is auto-coordination active.
class _FlightSim_System_AUTO_COORDINATION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AUTO COORDINATION,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:AUTO COORDINATION,{unit.value})")


# The avionics master switch position, true if the switch is ON. Use an avionics circuit index when referencing.
class _FlightSim_System_AVIONICS_MASTER_SWITCH:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:AVIONICS MASTER SWITCH:{self._index},{unit.value})")


# True if the No Smoking switch is on.
class _FlightSim_System_CABIN_NO_SMOKING_ALERT_SWITCH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:CABIN NO SMOKING ALERT SWITCH,{unit.value})")


# True if the Seatbelts switch is on.
class _FlightSim_System_CABIN_SEATBELTS_ALERT_SWITCH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:CABIN SEATBELTS ALERT SWITCH,{unit.value})")


# Percent primary door/exit open.
class _FlightSim_System_CANOPY_OPEN:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:CANOPY OPEN,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100', value: str):
        self._.set(f"{value} (>A:CANOPY OPEN,{unit.value})")


# True if carburetor heat available.
class _FlightSim_System_CARB_HEAT_AVAILABLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:CARB HEAT AVAILABLE,{unit.value})")


# Rate of turn of heading indicator.
class _FlightSim_System_DELTA_HEADING_RATE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.AngularVelocity.RADIAN_PER_SECOND'):
        return self._.get(f"(A:DELTA HEADING RATE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.AngularVelocity.RADIAN_PER_SECOND', value: str):
        self._.set(f"{value} (>A:DELTA HEADING RATE,{unit.value})")


# DME audio flag.
class _FlightSim_System_DME_SOUND:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:DME SOUND,{unit.value})")


# Whether or not the Emergency Locator Transmitter is active.
class _FlightSim_System_ELT_ACTIVATED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:ELT ACTIVATED,{unit.value})")


# Generic SimVar.
class _FlightSim_System_EXTERNAL_SYSTEM_VALUE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:EXTERNAL SYSTEM VALUE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER', value: str):
        self._.set(f"{value} (>A:EXTERNAL SYSTEM VALUE,{unit.value})")


# True if the fire bottle is discharged.
class _FlightSim_System_FIRE_BOTTLE_DISCHARGED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:FIRE BOTTLE DISCHARGED,{unit.value})")


# True if the fire bottle switch is on.
class _FlightSim_System_FIRE_BOTTLE_SWITCH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:FIRE BOTTLE SWITCH,{unit.value})")


# This variable will return a value between 0 and 1 for the automatic brightness setting for glass cockpit displays, where 0 is the dimmest and 1 is the brightest. This value will vary depending on the time of day.
class _FlightSim_System_GLASSCOCKPIT_AUTOMATIC_BRIGHTNESS:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:GLASSCOCKPIT AUTOMATIC BRIGHTNESS,{unit.value})")


# True if the Ground Proximity Warning System is active.
class _FlightSim_System_GPWS_SYSTEM_ACTIVE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GPWS SYSTEM ACTIVE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:GPWS SYSTEM ACTIVE,{unit.value})")


# True if Ground Proximity Warning System installed.
class _FlightSim_System_GPWS_WARNING:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:GPWS WARNING,{unit.value})")


# Angular error of heading indicator.
class _FlightSim_System_GYRO_DRIFT_ERROR:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:GYRO DRIFT ERROR,{unit.value})")


# Will return whether the aircraft has stall protection (true) or not (false).
class _FlightSim_System_HAS_STALL_PROTECTION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:HAS STALL PROTECTION,{unit.value})")


# Heading indicator (directional gyro) indication.
class _FlightSim_System_HEADING_INDICATOR:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:HEADING INDICATOR,{unit.value})")


# The indicated altitude.
class _FlightSim_System_INDICATED_ALTITUDE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.FOOT'):
        return self._.get(f"(A:INDICATED ALTITUDE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Length.FOOT', value: str):
        self._.set(f"{value} (>A:INDICATED ALTITUDE,{unit.value})")


# Indicated altitude with the altimeter calibrated to current sea level pressure.
class _FlightSim_System_INDICATED_ALTITUDE_CALIBRATED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.FOOT'):
        return self._.get(f"(A:INDICATED ALTITUDE CALIBRATED,{unit.value})")


# Similar to INDICATED_ALTITUDE but doesn't affect actual plane position when setting this variable.
class _FlightSim_System_INDICATED_ALTITUDE_EX1:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.FOOT'):
        return self._.get(f"(A:INDICATED ALTITUDE EX1,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Length.FOOT', value: str):
        self._.set(f"{value} (>A:INDICATED ALTITUDE EX1,{unit.value})")


# Inductor compass heading.
class _FlightSim_System_INDUCTOR_COMPASS_HEADING_REF:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:INDUCTOR COMPASS HEADING REF,{unit.value})")


# Inductor compass deviation reading.
class _FlightSim_System_INDUCTOR_COMPASS_PERCENT_DEVIATION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:INDUCTOR COMPASS PERCENT DEVIATION,{unit.value})")


# Deprecated, do not use!
class _FlightSim_System_INSTRUMENTS_AVAILABLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.MASK'):
        return self._.get(f"(A:INSTRUMENTS AVAILABLE,{unit.value})")


# Intercom Mode
class _FlightSim_System_INTERCOM_MODE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        ALL = 1
        CREW = 2

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:INTERCOM MODE,{unit.value})")


# Whether or not the intercom system is active.
class _FlightSim_System_INTERCOM_SYSTEM_ACTIVE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:INTERCOM SYSTEM ACTIVE,{unit.value})")


# True if the altitude of the aircraft is frozen.
class _FlightSim_System_IS_ALTITUDE_FREEZE_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:IS ALTITUDE FREEZE ON,{unit.value})")


# True if the attitude (pitch, bank and heading) of the aircraft is frozen.
class _FlightSim_System_IS_ATTITUDE_FREEZE_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:IS ATTITUDE FREEZE ON,{unit.value})")


# True if the lat/lon of the aircraft (either user or AI controlled) is frozen. If this variable returns true, it means that the latitude and longitude of the aircraft are not being controlled by ESP, so enabling, for example, a SimConnect client to control the position of the aircraft. This can also apply to altitude and attitude. Also refer to the range of KEY_FREEZE..... Event IDs.
class _FlightSim_System_IS_LATITUDE_LONGITUDE_FREEZE_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:IS LATITUDE LONGITUDE FREEZE ON,{unit.value})")


# The value for the given altimeter index in inches of mercury.
# IMPORTANT! In the system.cfg file, altimeters are indexed from 0, but the SimVar indexes from 1. So, altimeter 0 in that file is accessed using KOHLSMAN SETTING HG:1, 1 by KOHLSMAN SETTING HG:2, etc...
class _FlightSim_System_KOHLSMAN_SETTING_HG:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Pressure.INCH_OF_MERCURY'):
        return self._.get(f"(A:KOHLSMAN SETTING HG:{self._index},{unit.value})")


# The value for the given altimeter index in millibars.
# IMPORTANT! In the system.cfg file, altimeters are indexed from 0, but the SimVar indexes from 1. So, altimeter 0 in that file is accessed using KOHLSMAN SETTING MB:1, 1 by KOHLSMAN SETTING MB:2, etc...
class _FlightSim_System_KOHLSMAN_SETTING_MB:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Pressure.MILLIBAR'):
        return self._.get(f"(A:KOHLSMAN SETTING MB:{self._index},{unit.value})")


# True if the indexed altimeter is in "Standard" mode, or false otherwise.
# IMPORTANT! In the system.cfg file, altimeters are indexed from 0, but the SimVar indexes from 1. So, altimeter 0 in that file is accessed using KOHLSMAN SETTING STD:1, 1 by KOHLSMAN SETTING STD:2, etc...
class _FlightSim_System_KOHLSMAN_SETTING_STD:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:KOHLSMAN SETTING STD:{self._index},{unit.value})")


# Compass reading.
class _FlightSim_System_MAGNETIC_COMPASS:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:MAGNETIC COMPASS,{unit.value})")


# Position of manual fuel pump handle. 1 is fully deployed.
class _FlightSim_System_MANUAL_FUEL_PUMP_HANDLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:MANUAL FUEL PUMP HANDLE,{unit.value})")


# Overspeed warning state.
class _FlightSim_System_OVERSPEED_WARNING:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:OVERSPEED WARNING,{unit.value})")


# True if panel anti-ice switch is on.
class _FlightSim_System_PANEL_ANTI_ICE_SWITCH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:PANEL ANTI ICE SWITCH,{unit.value})")


# Amount of pitot ice. 100 is fully iced.
class _FlightSim_System_PITOT_ICE_PCT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:PITOT ICE PCT,{unit.value})")


# Pitot heat active.
class _FlightSim_System_PITOT_HEAT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:PITOT HEAT,{unit.value})")


# Pitot heat switch state.
class _FlightSim_System_PITOT_HEAT_SWITCH:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    class Unit(Enum):
        OFF = 0
        ON = 1
        AUTO = 2

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:PITOT HEAT SWITCH:{self._index},{unit.value})")


# Heading indicator (directional gyro) indication.
class _FlightSim_System_PLANE_HEADING_DEGREES_GYRO:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:PLANE HEADING DEGREES GYRO,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Angle.RADIAN', value: str):
        self._.set(f"{value} (>A:PLANE HEADING DEGREES GYRO,{unit.value})")


# Standard Altitude, ie: at a 1013.25 hPa (1 atmosphere) setting.
class _FlightSim_System_PRESSURE_ALTITUDE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.METER'):
        return self._.get(f"(A:PRESSURE ALTITUDE,{unit.value})")


# The current altitude of the cabin pressurization.
class _FlightSim_System_PRESSURIZATION_CABIN_ALTITUDE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.FOOT'):
        return self._.get(f"(A:PRESSURIZATION CABIN ALTITUDE,{unit.value})")


# The set altitude of the cabin pressurization as initialised from the Design Cabin Pressure value in the systems.cfg file. Pressure is converted into an altitude using a standard condition table.
# You can adjust the goal pressure using the PRESSURIZATION_PRESSURE_ALT_INC and PRESSURIZATION_PRESSURE_ALT_DEC events.
class _FlightSim_System_PRESSURIZATION_CABIN_ALTITUDE_GOAL:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.FOOT'):
        return self._.get(f"(A:PRESSURIZATION CABIN ALTITUDE GOAL,{unit.value})")


# The rate at which cabin pressurization changes.
class _FlightSim_System_PRESSURIZATION_CABIN_ALTITUDE_RATE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.FEET_PER_SECOND'):
        return self._.get(f"(A:PRESSURIZATION CABIN ALTITUDE RATE,{unit.value})")


# True if the cabin pressurization dump switch is on.
class _FlightSim_System_PRESSURIZATION_DUMP_SWITCH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:PRESSURIZATION DUMP SWITCH,{unit.value})")


# The difference in pressure between the set altitude pressurization and the current pressurization.
class _FlightSim_System_PRESSURIZATION_PRESSURE_DIFFERENTIAL:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Pressure.POUND_FORCE_PER_SQUARE_FOOT'):
        return self._.get(f"(A:PRESSURIZATION PRESSURE DIFFERENTIAL,{unit.value})")


# True if Rad INS switch on.
class _FlightSim_System_RAD_INS_SWITCH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:RAD INS SWITCH,{unit.value})")


# Selected DME.
class _FlightSim_System_SELECTED_DME:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:SELECTED DME,{unit.value})")


# Smoke system available.
# NOTE: There is no default "smoke system" that this SimVar works on and this is a legacy variable that is available for use should you wish to use it but it affects nothing by default.
class _FlightSim_System_SMOKESYSTEM_AVAILABLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:SMOKESYSTEM AVAILABLE,{unit.value})")


# Set to True to activate the smoke system, if one is available. Please see the notes for SMOKESYSTEM AVAILABLE for more information.
class _FlightSim_System_SMOKE_ENABLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:SMOKE ENABLE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:SMOKE ENABLE,{unit.value})")


# Whether or not the speaker is active.
class _FlightSim_System_SPEAKER_ACTIVE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:SPEAKER ACTIVE,{unit.value})")


# True if stall alarm available.
class _FlightSim_System_STALL_HORN_AVAILABLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:STALL HORN AVAILABLE,{unit.value})")


# Alpha below which the Stall Protection can be disabled. See the [STALL PROTECTION] section for more information.
class _FlightSim_System_STALL_PROTECTION_OFF_LIMIT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:STALL PROTECTION OFF LIMIT,{unit.value})")


# The alpha that the Stall Protection will attempt to reach when triggered. See the [STALL PROTECTION] section for more information.
class _FlightSim_System_STALL_PROTECTION_ON_GOAL:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:STALL PROTECTION ON GOAL,{unit.value})")


# Alpha above which the Stall Protection timer starts. See the [STALL PROTECTION] section for more information.
class _FlightSim_System_STALL_PROTECTION_ON_LIMIT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.RADIAN'):
        return self._.get(f"(A:STALL PROTECTION ON LIMIT,{unit.value})")


# Stall warning state.
class _FlightSim_System_STALL_WARNING:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:STALL WARNING,{unit.value})")


# True if the aircraft structure deice switch is on.
class _FlightSim_System_STRUCTURAL_DEICE_SWITCH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:STRUCTURAL DEICE SWITCH,{unit.value})")


# Vacuum system suction pressure.
class _FlightSim_System_SUCTION_PRESSURE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Pressure.INCH_OF_MERCURY'):
        return self._.get(f"(A:SUCTION PRESSURE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Pressure.INCH_OF_MERCURY', value: str):
        self._.set(f"{value} (>A:SUCTION PRESSURE,{unit.value})")


# Deprecated, do not use!
class _FlightSim_System_SYSTEMS_AVAILABLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.MASK'):
        return self._.get(f"(A:SYSTEMS AVAILABLE,{unit.value})")


# True if the tailhook handle is engaged.
class _FlightSim_System_TAILHOOK_HANDLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:TAILHOOK HANDLE,{unit.value})")


# Percent tail hook extended.
class _FlightSim_System_TAILHOOK_POSITION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:TAILHOOK POSITION,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100', value: str):
        self._.set(f"{value} (>A:TAILHOOK POSITION,{unit.value})")


# Position of tow release handle. 100 is fully deployed.
class _FlightSim_System_TOW_RELEASE_HANDLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:TOW RELEASE HANDLE,{unit.value})")


# True if True Airspeed has been selected.
class _FlightSim_System_TRUE_AIRSPEED_SELECTED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:TRUE AIRSPEED SELECTED,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:TRUE AIRSPEED SELECTED,{unit.value})")


# Turn coordinator ball position.
class _FlightSim_System_TURN_COORDINATOR_BALL:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION'):
        # unit: Position 128 (-127 to 127)
        return self._.get(f"(A:TURN COORDINATOR BALL,{unit.value})")


# Turn coordinator ball position inverted (upside down).
class _FlightSim_System_TURN_COORDINATOR_BALL_INV:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION'):
        # unit: Position 128 (-127 to 127)
        return self._.get(f"(A:TURN COORDINATOR BALL INV,{unit.value})")


# Turn indicator reading.
# NOTE: This is available in multiplayer to all near aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_System_TURN_INDICATOR_RATE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.AngularVelocity.RADIAN_PER_SECOND'):
        return self._.get(f"(A:TURN INDICATOR RATE,{unit.value})")


# True if turn indicator switch is on.
class _FlightSim_System_TURN_INDICATOR_SWITCH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:TURN INDICATOR SWITCH,{unit.value})")


# True if the aircraft windshield deice switch is on.
class _FlightSim_System_WINDSHIELD_DEICE_SWITCH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:WINDSHIELD DEICE SWITCH,{unit.value})")


# Deprecated, do not use!
# Use MAGNETIC_COMPASS instead.
class _FlightSim_System_WISKEY_COMPASS_INDICATION_DEGREES:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Angle.DEGREE'):
        return self._.get(f"(A:WISKEY COMPASS INDICATION DEGREES,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Angle.DEGREE', value: str):
        self._.set(f"{value} (>A:WISKEY COMPASS INDICATION DEGREES,{unit.value})")


# The MacCready setting used to fly an optimal speed between thermals.
class _FlightSim_System_VARIOMETER_MAC_CREADY_SETTING:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Length.METER_PER_SECOND'):
        return self._.get(f"(A:VARIOMETER MAC CREADY SETTING,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Length.METER_PER_SECOND', value: str):
        self._.set(f"{value} (>A:VARIOMETER MAC CREADY SETTING,{unit.value})")


# Variometer rate using Netto (Total Energy - polar sinkRate).
class _FlightSim_System_VARIOMETER_NETTO:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.FEET_PER_SECOND'):
        return self._.get(f"(A:VARIOMETER NETTO,{unit.value})")


# The variometer rate.
class _FlightSim_System_VARIOMETER_RATE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.FEET_PER_SECOND'):
        return self._.get(f"(A:VARIOMETER RATE,{unit.value})")


# Optimal speed to fly between thermals using polar curve and MacCready setting.
class _FlightSim_System_VARIOMETER_SPEED_TO_FLY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.KILOMETER_PER_HOUR'):
        return self._.get(f"(A:VARIOMETER SPEED TO FLY,{unit.value})")


# The glide ratio at optimal speed to fly.
class _FlightSim_System_VARIOMETER_SPEED_TO_FLY_GLIDE_RATIO:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:VARIOMETER SPEED TO FLY GLIDE RATIO,{unit.value})")


# True if the variometer switch is on, false if it is not.
class _FlightSim_System_VARIOMETER_SWITCH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:VARIOMETER SWITCH,{unit.value})")


# The variometer rate using total energy.
class _FlightSim_System_VARIOMETER_TOTAL_ENERGY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Speed.FEET_PER_SECOND'):
        return self._.get(f"(A:VARIOMETER TOTAL ENERGY,{unit.value})")


# The capacity of the indexed water ballast tank.
class _FlightSim_System_WATER_BALLAST_TANK_CAPACITY:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Weight.POUND'):
        return self._.get(f"(A:WATER BALLAST TANK CAPACITY:{self._index},{unit.value})")


# The number of water ballast tank available.
class _FlightSim_System_WATER_BALLAST_TANK_NUMBER:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:WATER BALLAST TANK NUMBER,{unit.value})")


# The quantity of water ballast in the indexed tank.
class _FlightSim_System_WATER_BALLAST_TANK_QUANTITY:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Weight.POUND'):
        return self._.get(f"(A:WATER BALLAST TANK QUANTITY:{self._index},{unit.value})")


# True (1) if a water ballast valve is available, False (0) otherwise.
class _FlightSim_System_WATER_BALLAST_VALVE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:WATER BALLAST VALVE,{unit.value})")


# The flow rate of the water ballast valve.
class _FlightSim_System_WATER_BALLAST_VALVE_FLOW_RATE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.VolumeRate.GALLON_PER_HOUR'):
        return self._.get(f"(A:WATER BALLAST VALVE FLOW RATE,{unit.value})")


# This variable will return 1 (TRUE) if all the ballast tank valves are open, or 0 (FALSE) otherwise.
class _FlightSim_System_WATER_BALLAST_EVERY_VALVE_OPEN:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:WATER BALLAST EVERY VALVE OPEN,{unit.value})")


# Will return true if any interior light is on or false otherwise.
class _FlightSim_System_IS_ANY_INTERIOR_LIGHT_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:IS ANY INTERIOR LIGHT ON,{unit.value})")


# Landing light pitch bank and heading.
#! SIMCONNECT_DATA_XYZ structure
class _FlightSim_System_LANDING_LIGHT_PBH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: ''):
        return self._.get(f"(A:LANDING LIGHT PBH,{unit.value})")


# Light switch state.
# NOTE: This is available in multiplayer to all far aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_System_LIGHT_BEACON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:LIGHT BEACON,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:LIGHT BEACON,{unit.value})")


# Returns true if the target beacon light is functioning or if the switch is ON. Use beacon lightdef index.
class _FlightSim_System_LIGHT_BEACON_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:LIGHT BEACON ON,{unit.value})")


# Vehicle backlights current intensity (0 = off, 1 = full intensity).
class _FlightSim_System_LIGHT_BACKLIGHT_INTENSITY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:LIGHT BACKLIGHT INTENSITY,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100', value: str):
        self._.set(f"{value} (>A:LIGHT BACKLIGHT INTENSITY,{unit.value})")


# Returns true if the target brake light is functioning or if the switch is ON.
class _FlightSim_System_LIGHT_BRAKE_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:LIGHT BRAKE ON,{unit.value})")


# Light switch state.
class _FlightSim_System_LIGHT_CABIN:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:LIGHT CABIN,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:LIGHT CABIN,{unit.value})")


# Returns true if the target cabin light is functioning or if the switch is ON. Use the cabin lightdef index.
class _FlightSim_System_LIGHT_CABIN_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:LIGHT CABIN ON,{unit.value})")


# The current cabin light power setting. Requires the cabin lightdef index.
class _FlightSim_System_LIGHT_CABIN_POWER_SETTING:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:LIGHT CABIN POWER SETTING,{unit.value})")


# Whether or not the Light switch for the Glareshield is enabled.
class _FlightSim_System_LIGHT_GLARESHIELD:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:LIGHT GLARESHIELD,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:LIGHT GLARESHIELD,{unit.value})")


# Returns true if the target glareshield light is functioning or if the switch is ON. Use the glareshield lightdef index.
class _FlightSim_System_LIGHT_GLARESHIELD_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:LIGHT GLARESHIELD ON,{unit.value})")


# The current glareshield light power setting. Requires the glareshield lightdef index.
class _FlightSim_System_LIGHT_GLARESHIELD_POWER_SETTING:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:LIGHT GLARESHIELD POWER SETTING,{unit.value})")


# Vehicle gyrolights current intensity (0 = off, 1 = full intensity).
class _FlightSim_System_LIGHT_GYROLIGHT_INTENSITY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:LIGHT GYROLIGHT INTENSITY,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100', value: str):
        self._.set(f"{value} (>A:LIGHT GYROLIGHT INTENSITY,{unit.value})")


# Returns true if the target navigation light is functioning or if the switch is ON.
class _FlightSim_System_LIGHT_HEAD_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:LIGHT HEAD ON,{unit.value})")


# Vehicle headlights current intensity (0 = off, 1 = full intensity).
class _FlightSim_System_LIGHT_HEADLIGHT_INTENSITY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:LIGHT HEADLIGHT INTENSITY,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100', value: str):
        self._.set(f"{value} (>A:LIGHT HEADLIGHT INTENSITY,{unit.value})")


# Returns true if the target landing light is functioning or if the switch is ON. Use landing lightdef index.
class _FlightSim_System_LIGHT_LANDING_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:LIGHT LANDING ON,{unit.value})")


# Light switch state for landing light.
# NOTE: This is available in multiplayer to all far aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_System_LIGHT_LANDING:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:LIGHT LANDING,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:LIGHT LANDING,{unit.value})")


# Light switch state for logo light.
# NOTE: This is available in multiplayer to all far aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_System_LIGHT_LOGO:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:LIGHT LOGO,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:LIGHT LOGO,{unit.value})")


# Returns true if the target logo light is functioning or if the switch is ON. Use the logo lightdef index.
class _FlightSim_System_LIGHT_LOGO_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:LIGHT LOGO ON,{unit.value})")


# Returns true if the target navigation light is functioning or if the switch is ON. Use navigation lightdef index.
class _FlightSim_System_LIGHT_NAV_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:LIGHT NAV ON,{unit.value})")


# Light switch state for the NAV light.
class _FlightSim_System_LIGHT_NAV:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:LIGHT NAV,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:LIGHT NAV,{unit.value})")


# Bit mask:[index]
class _FlightSim_System_LIGHT_ON_STATES:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.MASK'):
        return self._.get(f"(A:LIGHT ON STATES,{unit.value})")


# Light switch state of the panel light.
class _FlightSim_System_LIGHT_PANEL:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:LIGHT PANEL,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:LIGHT PANEL,{unit.value})")


# Returns true if the target panel light is functioning or if the switch is ON. Use the panel lightdef index.
class _FlightSim_System_LIGHT_PANEL_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:LIGHT PANEL ON,{unit.value})")


# The current panel light power setting. Requires the panel lightdef index.
class _FlightSim_System_LIGHT_PANEL_POWER_SETTING:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:LIGHT PANEL POWER SETTING,{unit.value})")


# Whether or not the Light switch for the Pedestal is enabled.
# NOTE: This is available in multiplayer to all far aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_System_LIGHT_PEDESTRAL:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:LIGHT PEDESTRAL,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:LIGHT PEDESTRAL,{unit.value})")


# Returns true if the target pedestral light is functioning or if the switch is ON. Requires the pedestral lightdef index.
class _FlightSim_System_LIGHT_PEDESTRAL_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:LIGHT PEDESTRAL ON,{unit.value})")


# The current pedestral light power setting. Requires the pedestral lightdef index.
class _FlightSim_System_LIGHT_PEDESTRAL_POWER_SETTING:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT'):
        return self._.get(f"(A:LIGHT PEDESTRAL POWER SETTING,{unit.value})")


# Adjust the potentiometer of the indexed lighting. Index is defined in the appropriate lightdef hashmap setting.
class _FlightSim_System_LIGHT_POTENTIOMETER:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:LIGHT POTENTIOMETER:{self._index},{unit.value})")


# Light switch state for the recognition light.
# NOTE: This is available in multiplayer to all far aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_System_LIGHT_RECOGNITION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:LIGHT RECOGNITION,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:LIGHT RECOGNITION,{unit.value})")


# Returns true if the target recognition light is functioning or if the switch is ON. Use the recognition lightdef index.
class _FlightSim_System_LIGHT_RECOGNITION_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:LIGHT RECOGNITION ON,{unit.value})")


# Same as LIGHT_ON_STATES.
# NOTE: This is available in multiplayer to all far aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_System_LIGHT_STATES:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.MASK'):
        return self._.get(f"(A:LIGHT STATES,{unit.value})")


# Light switch state for the strobe lights.
# NOTE: This is available in multiplayer to all far aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_System_LIGHT_STROBE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:LIGHT STROBE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:LIGHT STROBE,{unit.value})")


# Returns true if the target strobe light is functioning or if the switch is ON. Use the strobe lightdef index.
# NOTE: This is available in multiplayer to all far aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_System_LIGHT_STROBE_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:LIGHT STROBE ON,{unit.value})")


# Light switch state for the taxi light.
# NOTE: This is available in multiplayer to all far aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_System_LIGHT_TAXI:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:LIGHT TAXI,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:LIGHT TAXI,{unit.value})")


# Returns true if the target taxi light is functioning or if the switch is ON. Use taxi lightdef index.
class _FlightSim_System_LIGHT_TAXI_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:LIGHT TAXI ON,{unit.value})")


# Light switch state for the wing lights.
# NOTE: This is available in multiplayer to all far aircraft. See here for more information: Note On SimVars In Multiplayer.
class _FlightSim_System_LIGHT_WING:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:LIGHT WING,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL', value: str):
        self._.set(f"{value} (>A:LIGHT WING,{unit.value})")


# Returns true if the target wing light is functioning or if the switch is ON. Use the wing lightdef index.
class _FlightSim_System_LIGHT_WING_ON:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:LIGHT WING ON,{unit.value})")


# True if instrument lights are set manually.
class _FlightSim_System_MANUAL_INSTRUMENT_LIGHTS:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:MANUAL INSTRUMENT LIGHTS,{unit.value})")


# True if strobe lights are available.
class _FlightSim_System_STROBES_AVAILABLE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:STROBES AVAILABLE,{unit.value})")


# Deprecated, do not use!
class _FlightSim_System_STROBE_FLASH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:STROBE FLASH,{unit.value})")


# Hydraulic system pressure. Indexes start at 1.
class _FlightSim_System_HYDRAULIC_PRESSURE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Pressure.POUND_FORCE_PER_SQUARE_FOOT'):
        return self._.get(f"(A:HYDRAULIC PRESSURE:{self._index},{unit.value})")


# Hydraulic pressure changes will follow changes to this variable. Indexes start at 1.
class _FlightSim_System_HYDRAULIC_RESERVOIR_PERCENT:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:HYDRAULIC RESERVOIR PERCENT:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100', value: str):
        self._.set(f"{value} (>A:HYDRAULIC RESERVOIR PERCENT:{self._index},{unit.value})")


# True if hydraulic switch is on.
class _FlightSim_System_HYDRAULIC_SWITCH:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:HYDRAULIC SWITCH,{unit.value})")


# Percent system functional.
class _FlightSim_System_HYDRAULIC_SYSTEM_INTEGRITY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:HYDRAULIC SYSTEM INTEGRITY,{unit.value})")


# Gauge fail flag.
class _FlightSim_System_PARTIAL_PANEL_ADF:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        OK = 0
        FAIL = 1
        BLANK = 2

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:PARTIAL PANEL ADF,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM', value: str):
        self._.set(f"{value} (>A:PARTIAL PANEL ADF,{unit.value})")


# Gauge fail flag.
class _FlightSim_System_PARTIAL_PANEL_AIRSPEED:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        OK = 0
        FAIL = 1
        BLANK = 2

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:PARTIAL PANEL AIRSPEED,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM', value: str):
        self._.set(f"{value} (>A:PARTIAL PANEL AIRSPEED,{unit.value})")


# Gauge fail flag.
class _FlightSim_System_PARTIAL_PANEL_ALTIMETER:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        OK = 0
        FAIL = 1
        BLANK = 2

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:PARTIAL PANEL ALTIMETER,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM', value: str):
        self._.set(f"{value} (>A:PARTIAL PANEL ALTIMETER,{unit.value})")


# Gauge fail flag.
class _FlightSim_System_PARTIAL_PANEL_ATTITUDE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        OK = 0
        FAIL = 1
        BLANK = 2

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:PARTIAL PANEL ATTITUDE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM', value: str):
        self._.set(f"{value} (>A:PARTIAL PANEL ATTITUDE,{unit.value})")


# Gauge fail flag.
class _FlightSim_System_PARTIAL_PANEL_AVIONICS:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        OK = 0
        FAIL = 1
        BLANK = 2

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:PARTIAL PANEL AVIONICS,{unit.value})")


# Gauge fail flag.
class _FlightSim_System_PARTIAL_PANEL_COMM:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        OK = 0
        FAIL = 1
        BLANK = 2

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:PARTIAL PANEL COMM,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM', value: str):
        self._.set(f"{value} (>A:PARTIAL PANEL COMM,{unit.value})")


# Gauge fail flag.
class _FlightSim_System_PARTIAL_PANEL_COMPASS:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        OK = 0
        FAIL = 1
        BLANK = 2

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:PARTIAL PANEL COMPASS,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM', value: str):
        self._.set(f"{value} (>A:PARTIAL PANEL COMPASS,{unit.value})")


# Gauge fail flag.
class _FlightSim_System_PARTIAL_PANEL_ELECTRICAL:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        OK = 0
        FAIL = 1
        BLANK = 2

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:PARTIAL PANEL ELECTRICAL,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM', value: str):
        self._.set(f"{value} (>A:PARTIAL PANEL ELECTRICAL,{unit.value})")


# Gauge fail flag.
class _FlightSim_System_PARTIAL_PANEL_ENGINE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        OK = 0
        FAIL = 1
        BLANK = 2

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:PARTIAL PANEL ENGINE,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM', value: str):
        self._.set(f"{value} (>A:PARTIAL PANEL ENGINE,{unit.value})")


# Gauge fail flag.
class _FlightSim_System_PARTIAL_PANEL_FUEL_INDICATOR:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        OK = 0
        FAIL = 1
        BLANK = 2

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:PARTIAL PANEL FUEL INDICATOR,{unit.value})")


# Gauge fail flag.
class _FlightSim_System_PARTIAL_PANEL_HEADING:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        OK = 0
        FAIL = 1
        BLANK = 2

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:PARTIAL PANEL HEADING,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM', value: str):
        self._.set(f"{value} (>A:PARTIAL PANEL HEADING,{unit.value})")


# Gauge fail flag.
class _FlightSim_System_PARTIAL_PANEL_NAV:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        OK = 0
        FAIL = 1
        BLANK = 2

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:PARTIAL PANEL NAV,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM', value: str):
        self._.set(f"{value} (>A:PARTIAL PANEL NAV,{unit.value})")


# Gauge fail flag.
class _FlightSim_System_PARTIAL_PANEL_PITOT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        OK = 0
        FAIL = 1
        BLANK = 2

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:PARTIAL PANEL PITOT,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM', value: str):
        self._.set(f"{value} (>A:PARTIAL PANEL PITOT,{unit.value})")


# Gauge fail flag.
class _FlightSim_System_PARTIAL_PANEL_TRANSPONDER:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        OK = 0
        FAIL = 1
        BLANK = 2

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:PARTIAL PANEL TRANSPONDER,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM', value: str):
        self._.set(f"{value} (>A:PARTIAL PANEL TRANSPONDER,{unit.value})")


# Gauge fail flag.
class _FlightSim_System_PARTIAL_PANEL_TURN_COORDINATOR:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        OK = 0
        FAIL = 1
        BLANK = 2

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:PARTIAL PANEL TURN COORDINATOR,{unit.value})")


# Gauge fail flag.
class _FlightSim_System_PARTIAL_PANEL_VACUUM:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        OK = 0
        FAIL = 1
        BLANK = 2

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:PARTIAL PANEL VACUUM,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM', value: str):
        self._.set(f"{value} (>A:PARTIAL PANEL VACUUM,{unit.value})")


# Gauge fail flag.
class _FlightSim_System_PARTIAL_PANEL_VERTICAL_VELOCITY:
    def __init__(self, flightSim):
        self._ = flightSim
    
    class Unit(Enum):
        OK = 0
        FAIL = 1
        BLANK = 2

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:PARTIAL PANEL VERTICAL VELOCITY,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM', value: str):
        self._.set(f"{value} (>A:PARTIAL PANEL VERTICAL VELOCITY,{unit.value})")


# The number of droppable objects at the station number identified by the index.
class _FlightSim_System_DROPPABLE_OBJECTS_COUNT:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:DROPPABLE OBJECTS COUNT:{self._index},{unit.value})")


# The type of droppable object at the station number identified by the index.
class _FlightSim_System_DROPPABLE_OBJECTS_TYPE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.STRING'):
        return self._.get(f"(A:DROPPABLE OBJECTS TYPE:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.STRING', value: str):
        self._.set(f"{value} (>A:DROPPABLE OBJECTS TYPE:{self._index},{unit.value})")


# Descriptive name, used in User Interface dialogs, of a droppable object, identified by index.
class _FlightSim_System_DROPPABLE_OBJECTS_UI_NAME:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.STRING'):
        return self._.get(f"(A:DROPPABLE OBJECTS UI NAME:{self._index},{unit.value})")


# Number of payload stations (1 to 15).
class _FlightSim_System_PAYLOAD_STATION_COUNT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:PAYLOAD STATION COUNT,{unit.value})")


# Descriptive name for payload station.
class _FlightSim_System_PAYLOAD_STATION_NAME:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.STRING'):
        return self._.get(f"(A:PAYLOAD STATION NAME:{self._index},{unit.value})")


# The number of objects at the payload station.
class _FlightSim_System_PAYLOAD_STATION_NUM_SIMOBJECTS:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.NUMBER'):
        return self._.get(f"(A:PAYLOAD STATION NUM SIMOBJECTS:{self._index},{unit.value})")


# Places the named object at the payload station identified by the index (starting from 1). The string is the Container name (refer to the title property of Simulation Object Configuration Files).
class _FlightSim_System_PAYLOAD_STATION_OBJECT:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.STRING'):
        return self._.get(f"(A:PAYLOAD STATION OBJECT:{self._index},{unit.value})")


# Individual payload station weight.
class _FlightSim_System_PAYLOAD_STATION_WEIGHT:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Weight.POUND'):
        return self._.get(f"(A:PAYLOAD STATION WEIGHT:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Weight.POUND', value: str):
        self._.set(f"{value} (>A:PAYLOAD STATION WEIGHT:{self._index},{unit.value})")


# This is the current state of the fuel warning, either on (true) or off (false).
class _FlightSim_System_WARNING_FUEL:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:WARNING FUEL,{unit.value})")


# This is the current state of the left fuel tank warning, either on (true) or off (false).
class _FlightSim_System_WARNING_FUEL_LEFT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:WARNING FUEL LEFT,{unit.value})")


# This is the current state of the right fuel tank warning, either on (true) or off (false).
class _FlightSim_System_WARNING_FUEL_RIGHT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:WARNING FUEL RIGHT,{unit.value})")


# This is the current state of the low height warning, either on (true) or off (false).
class _FlightSim_System_WARNING_LOW_HEIGHT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:WARNING LOW HEIGHT,{unit.value})")


# This is the current state of the oil pressure warning, either on (true) or off (false).
class _FlightSim_System_WARNING_OIL_PRESSURE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:WARNING OIL PRESSURE,{unit.value})")


# This is the current state of the vacuum system warning, either on (true) or off (false).
class _FlightSim_System_WARNING_VACUUM:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:WARNING VACUUM,{unit.value})")


# This is the current state of the left vacuum system warning, either on (true) or off (false).
class _FlightSim_System_WARNING_VACUUM_LEFT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:WARNING VACUUM LEFT,{unit.value})")


# This is the current state of the right vacuum system warning, either on (true) or off (false).
class _FlightSim_System_WARNING_VACUUM_RIGHT:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:WARNING VACUUM RIGHT,{unit.value})")


# This is the current state of the electrical system voltage warning, either on (true) or off (false).
class _FlightSim_System_WARNING_VOLTAGE:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.BOOL'):
        return self._.get(f"(A:WARNING VOLTAGE,{unit.value})")


# Yoke position in horizontal direction.
class _FlightSim_System_YOKE_X_INIDICATOR:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION'):
        # unit: Position (-16K to 0)
        return self._.get(f"(A:YOKE X INIDICATOR,{unit.value})")


# Percent control deflection left/right (for animation).
class _FlightSim_System_YOKE_X_POSITION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION'):
        # unit: Position (-16K to 0)
        return self._.get(f"(A:YOKE X POSITION,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION', value: str):
        # unit: Position (-16K to 0)
        self._.set(f"{value} (>A:YOKE X POSITION,{unit.value})")


# Percent control deflection left/right (for animation). Also includes AP's inputs.
class _FlightSim_System_YOKE_X_POSITION_WITH_AP:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION'):
        # unit: Position (-16K to 0)
        return self._.get(f"(A:YOKE X POSITION WITH AP,{unit.value})")


# Yoke position in vertical direction.
class _FlightSim_System_YOKE_Y_INIDICATOR:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION'):
        # unit: Position (-16K to 0)
        return self._.get(f"(A:YOKE Y INIDICATOR,{unit.value})")


# Percent control deflection fore/aft (for animation).
class _FlightSim_System_YOKE_Y_POSITION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION'):
        # unit: Position (-16K to 0)
        return self._.get(f"(A:YOKE Y POSITION,{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION', value: str):
        # unit: Position (-16K to 0)
        self._.set(f"{value} (>A:YOKE Y POSITION,{unit.value})")


# Percent control deflection fore/aft (for animation). Also includes AP's inputs.
class _FlightSim_System_YOKE_Y_POSITION_WITH_AP:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.POSITION'):
        # unit: Position (-16K to 0)
        return self._.get(f"(A:YOKE Y POSITION WITH AP,{unit.value})")


# Percent door/exit open.
class _FlightSim_System_EXIT_OPEN:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100'):
        return self._.get(f"(A:EXIT OPEN:{self._index},{unit.value})")

    def set(self, unit: 'FlightSim.Unit.Miscellaneous.PERCENT_OVER_100', value: str):
        self._.set(f"{value} (>A:EXIT OPEN:{self._index},{unit.value})")


# Position of exit relative to datum reference point.
class _FlightSim_System_EXIT_POSX:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Length.FOOT'):
        return self._.get(f"(A:EXIT POSX:{self._index},{unit.value})")


# Position of exit relative to datum reference point.
class _FlightSim_System_EXIT_POSY:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Length.FOOT'):
        return self._.get(f"(A:EXIT POSY:{self._index},{unit.value})")


# Position of exit relative to datum reference point.
class _FlightSim_System_EXIT_POSZ:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    def get(self, unit: 'FlightSim.Unit.Length.FOOT'):
        return self._.get(f"(A:EXIT POSZ:{self._index},{unit.value})")


# The exit type.
class _FlightSim_System_EXIT_TYPE:
    def __init__(self, flightSim, index):
        self._ = flightSim
        self._index = index
    
    class Unit(Enum):
        MAIN = 0
        CARGO = 1
        EMERGENCY = 2
        UNKNOWN = 3

    def get(self, unit: 'FlightSim.Unit.Miscellaneous.ENUM'):
        return self._.get(f"(A:EXIT TYPE:{self._index},{unit.value})")


class FlightSim:
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
            FOOT_POUND_PER_SECOND = 'ft lb per second'
    
    
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


    Autopilot: _FlightSim_Autopilot
    Brake: _FlightSim_Brake
    Control: _FlightSim_Control
    Electrics: _FlightSim_Electrics
    Engine: _FlightSim_Engine
    FlightModel: _FlightSim_FlightModel
    Fuel: _FlightSim_Fuel
    Misc: _FlightSim_Misc
    Radio: _FlightSim_Radio
    System: _FlightSim_System

    def __init__(self):
        self.Autopilot = _FlightSim_Autopilot(self)
        self.Brake = _FlightSim_Brake(self)
        self.Control = _FlightSim_Control(self)
        self.Electrics = _FlightSim_Electrics(self)
        self.Engine = _FlightSim_Engine(self)
        self.FlightModel = _FlightSim_FlightModel(self)
        self.Fuel = _FlightSim_Fuel(self)
        self.Misc = _FlightSim_Misc(self)
        self.Radio = _FlightSim_Radio(self)
        self.System = _FlightSim_System(self)
