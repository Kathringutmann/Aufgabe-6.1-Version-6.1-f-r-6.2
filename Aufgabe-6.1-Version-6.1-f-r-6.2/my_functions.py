def estimate_max_hr(age_years : int , sex : str) -> int:
    """
    See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4124545/ for different formulas
    """
    if sex == "male":
        max_hr_bpm =  223 - 0.9 * age_years
    elif sex == "female":
        max_hr_bpm = 226 - 1.0 *  age_years
    else:
        max_hr_bpm  = int(input("Enter maximum heart rate:"))
    return int(max_hr_bpm)