def calculate_oee(demand_annual, production, scheduled_time, oee_loss):
    # Calculate OEE based on the input data
    demand_per_hour = demand_annual / 365 / 24
    production_per_hour = production / scheduled_time
    oee = (production_per_hour - demand_per_hour) / production_per_hour * (1 - oee_loss)
    return oee