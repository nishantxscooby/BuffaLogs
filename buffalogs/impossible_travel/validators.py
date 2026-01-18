from ipaddress import ip_address, ip_network

import pycountry
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_countries_names(values):
    if not isinstance(values, list):
        raise ValidationError(_("Value must be a list."))

    invalid_entries = []

    for value in values:
        if not isinstance(value, str):
            invalid_entries.append(value)
            continue

        value = value.strip()

        if not pycountry.countries.get(
            alpha_2=value.upper()
        ) and not pycountry.countries.get(name=value):
            invalid_entries.append(value)

    if invalid_entries:
        raise ValidationError(
            _("Invalid country identifiers: %(countries)s"),
            params={"countries": ", ".join(map(str, invalid_entries))},
        )


def validate_ips_or_network(values):
    if not isinstance(values, list):
        raise ValidationError(_("Value must be a list."))

    for value in values:
        try:
            if "/" in value:
                ip_network(value, strict=False)
            else:
                ip_address(value)
        except Exception:
            raise ValidationError(
                _("Invalid IP address or network: %(value)s"),
                params={"value": value},
            )


def validate_string_or_regex(value):
    if not isinstance(value, str):
        raise ValidationError(_("Value must be a string."))


def validate_tags(values):
    if not isinstance(values, list):
        raise ValidationError(_("Value must be a list."))

    for value in values:
        if not isinstance(value, str):
            raise ValidationError(_("Each tag must be a string."))


def validate_country_couples_list(values):
    if not isinstance(values, list):
        raise ValidationError(_("Value must be a list."))

    for pair in values:
        if not isinstance(pair, (list, tuple)) or len(pair) != 2:
            raise ValidationError(_("Each entry must be a country pair."))


def validate_alert_query(value):
    if not isinstance(value, dict):
        raise ValidationError(_("Alert query must be a dictionary."))

    return value


def validate_login_query(value):
    if not isinstance(value, dict):
        raise ValidationError(_("Login query must be a dictionary."))

    return value
