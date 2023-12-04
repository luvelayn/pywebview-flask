def convert_units(value, from_unit, to_unit):
    conversion_factors = {
        "km": 1000,
        "m": 1,
        "cm": 0.01,
        "mm": 0.001,
        "mile": 1609.34,
        "yard": 0.9144,
        "foot": 0.3048,
        "inch": 0.0254,
    }

    value_m = value * conversion_factors[from_unit]
    converted_value = value_m / conversion_factors[to_unit]
    result = f"{value} {from_unit} = {converted_value} {to_unit}"

    return result
