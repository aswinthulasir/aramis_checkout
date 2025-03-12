from utils import calculate_final_exit_time, validate_time_entries

def check_exit_time(check_ins, check_outs):
    valid, message = validate_time_entries(check_ins, check_outs)
    if not valid:
        return {"error": message}
    
    exit_time = calculate_final_exit_time(check_ins, check_outs)
    return exit_time
