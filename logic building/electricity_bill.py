# Electricity bill calculation

def electricity_bill(current_units):
    prev_units = 1700  # assumed previous meter reading
    
    current_consumed = current_units - prev_units

    # Validate meter reading
    if current_consumed < 0:
        print("Invalid meter reading")
        return

    # -------- Without Slab (Flat Rate) --------
    rate_per_unit = 5
    bill_without_slab = current_consumed * rate_per_unit
    print("Bill amount without slab:", bill_without_slab)

    # -------- With Slab --------
    """
    Slab System:
    0–100 units  -> ₹5 per unit
    101–200 units -> ₹7 per unit
    Above 200     -> ₹10 per unit
    Fixed charge  -> ₹100
    """

    if current_consumed <= 100:
        bill_with_slab = current_consumed * 5
    elif current_consumed <= 200:
        bill_with_slab = 100 * 5 + (current_consumed - 100) * 7
    else:
        bill_with_slab = (
            100 * 5 +
            100 * 7 +
            (current_consumed - 200) * 10
        )

    bill_with_slab += 100  # add fixed charge

    print("Bill amount with slab:", bill_with_slab)


# Example call
electricity_bill(1950)

