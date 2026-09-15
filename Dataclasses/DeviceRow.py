from attr import dataclass


@dataclass
class DeviceRow:
    name_of_station: str
    mac: str
    ip: str
    netmask: str
    gateway: str
    family: str
    dcp_access: str = "unknown"
    vendor: str = "Looking up..."
    ping_status: str = "Unknown"
    ping_ms: str = ""
