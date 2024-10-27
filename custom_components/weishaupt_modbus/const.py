"""Constants."""

from dataclasses import dataclass
from datetime import timedelta

from homeassistant.const import (
    PERCENTAGE,
    UnitOfEnergy,
    UnitOfPower,
    UnitOfTemperature,
    UnitOfTime,
    UnitOfVolumeFlowRate,
)


@dataclass(frozen=True)
class MainConstants:
    """Main constants."""

    DOMAIN = "weishaupt_modbus"
    SCAN_INTERVAL = timedelta(minutes=1)
    UNIQUE_ID = "unique_id"
    APPID = 100
    KENNFELDFILE = "weishaupt_wsb8_kennfeld.json"
    PREFIX = "weishaupt_modbus"


CONST = MainConstants()


@dataclass(frozen=True)
class FormatConstants:
    """Format constants."""

    TEMPERATUR = UnitOfTemperature.CELSIUS
    ENERGY = UnitOfEnergy.KILO_WATT_HOUR
    POWER = UnitOfPower.WATT
    PERCENTAGE = PERCENTAGE
    NUMBER = ""
    STATUS = "Status"
    VOLUMENSTROM = UnitOfVolumeFlowRate.CUBIC_METERS_PER_HOUR
    KENNLINIE = "Stg."
    TIME_MIN = UnitOfTime.MINUTES
    TIME_H = UnitOfTime.HOURS


FORMATS = FormatConstants()


@dataclass(frozen=True)
class TypeConstants:
    """Type constants."""

    SENSOR = "Sensor"
    SENSOR_CALC = "Sensor_Calc"
    SELECT = "Select"
    NUMBER = "Number"
    NUMBER_RO = "Number_RO"


TYPES = TypeConstants()
