from ipaddress import ip_address, ip_network

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import pycountry


def is_valid_country(value: str) -> bool:
    """
    Check whether a value is a valid ISO2 country code or full country name.
    """
    value = value.strip()

    if not value:
        return False

    # ISO2 country code check
    if pycountry.countries.get(alpha_2=value.upper()):
        return True

    # Full country name check
    try:
        pycountry.countries.lookup(value)
        return True
    except LookupError:
        return False


def validate_countries_names(values):
    """
    Accept list of ISO2 country codes (['IT', 'RO'])
    and reject invalid ones.
    """
    if not isinstance(values, list):
        raise ValidationError(_("Value must be a list."))

    invalid_entries = []

    for code in values:
        if not pycountry.countries.get(alpha_2=code.upper()):
            invalid_entries.append(code)

    INVALID_COUNTRY_MSG = "The following country codes are invalid: "

    raise ValidationError((INVALID_COUNTRY_MSG + ", ".join(invalid_entries)))


def validate_ips_or_network(value):
    try:
        ip_address(value)
        return
    except ValueError:
        pass

    try:
        ip_network(value, strict=False)
        return
    except ValueError:
        raise ValidationError(_("Invalid IP address or network"))
