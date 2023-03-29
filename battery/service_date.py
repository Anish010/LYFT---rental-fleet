def service_date(last_service_date, years_added):
    date_limit_for_service = last_service_date.replace(
        year=last_service_date.year + years_added)
    return date_limit_for_service
