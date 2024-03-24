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
#! Integer
class _FlightSim_Autopilot_AUTOPILOT_MAX_BANK_ID:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: ''):
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
#! Percent Over 100
# or
# Position
# (16K = down, 0 = up)
class _FlightSim_Control_SPOILERS_HANDLE_POSITION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: ''):
        return self._.get(f"(A:SPOILERS HANDLE POSITION,{unit.value})")

    def set(self, unit: '', value: str):
        self._.set(f"{value} (>A:SPOILERS HANDLE POSITION,{unit.value})")


# Percent left spoiler deflected.
# NOTE: This is available in multiplayer. See here for more information: Note On SimVars In Multiplayer.
#! Percent Over 100
# or
# Position
# (0 = retracted, 16K fully extended)
class _FlightSim_Control_SPOILERS_LEFT_POSITION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: ''):
        return self._.get(f"(A:SPOILERS LEFT POSITION,{unit.value})")


# Percent right spoiler deflected.
# NOTE: This is available in multiplayer. See here for more information: Note On SimVars In Multiplayer.
#! Percent Over 100
# or
# Position (0 = retracted, 16K fully extended)
class _FlightSim_Control_SPOILERS_RIGHT_POSITION:
    def __init__(self, flightSim):
        self._ = flightSim
    
    def get(self, unit: ''):
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


    Autopilot: _FlightSim_Autopilot
    Control: _FlightSim_Control
    Electrics: _FlightSim_Electrics

    def __init__(self):
        self.Autopilot = _FlightSim_Autopilot(self)
        self.Control = _FlightSim_Control(self)
        self.Electrics = _FlightSim_Electrics(self)
