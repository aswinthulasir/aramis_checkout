from datetime import datetime, timedelta

def calculate_total_inside_time(check_ins, check_outs):
    """
    Calculates the total time spent inside the office.
    """
    total_inside_time = timedelta()
    for check_in, check_out in zip(check_ins, check_outs):
        in_time = datetime.strptime(check_in, "%H:%M")
        out_time = datetime.strptime(check_out, "%H:%M")
        total_inside_time += out_time - in_time
    return total_inside_time

def calculate_final_exit_time(check_ins, check_outs):
    """
    Calculates the expected exit time after ensuring 8.5 hours inside the office.
    """
    total_inside_time = calculate_total_inside_time(check_ins, check_outs)
    required_time = timedelta(hours=8, minutes=30)
    remaining_time = required_time - total_inside_time
    last_check_out = datetime.strptime(check_outs[-1], "%H:%M")
    final_exit_time = last_check_out + remaining_time
    return final_exit_time.strftime("%H:%M")

def validate_time_entries(check_ins, check_outs):
    """
    Validates that check-ins and check-outs are in proper format and logically correct.
    """
    if len(check_ins) != len(check_outs):
        return False, "Mismatched check-ins and check-outs."

    for check_in, check_out in zip(check_ins, check_outs):
        try:
            in_time = datetime.strptime(check_in, "%H:%M")
            out_time = datetime.strptime(check_out, "%H:%M")
            if in_time >= out_time:
                return False, "Check-in time must be earlier than check-out time."
        except ValueError:
            return False, "Invalid time format. Use HH:MM."
    
    return True, "Valid time entries."
