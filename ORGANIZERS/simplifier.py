# Simplifies the location data
def simplify_location(location_string: str, locations: list[str]) -> list[str]:
    return [l.upper() for l in locations if l in location_string]

# Simplifies the name data by turning it into a title
def simplify_name(name_string: str) -> str:
    return str(name_string).lower().title()

# Simplifies the school data
def simplify_school(school_string: str, school_tuples: list[tuple[str, ...]]) -> str:
    return next((s[0] for s in school_tuples for spelling in s if spelling in school_string.lower()), None)

# Simplifies the subject data, by turning it into a standardized list
def simplify_subjects(subject_string: str, subjects: list[str]) -> list[str]:
    return [s.upper() for s in subjects if s in subject_string]

# Simplifies the availability data, by turning it into a standardized list
def simplify_availability(availability_string: str, availabilities: list[str]) -> list[str]:
    return [a.upper() for a in availabilities if a in availability_string]

# Simplifies the number
def simplify_number(number_string: str) -> str:
    return str(number_string).replace('385', '0').replace('+', '').replace(' ', '')

# Simplifies the grade
def simplify_grade(grade_string: str) -> str:
    return str(grade_string).replace(' ', '')