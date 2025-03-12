from flask import Blueprint, request, jsonify
from controllers.time_controller import check_exit_time

time_routes = Blueprint("time_routes", __name__)

@time_routes.route("/check", methods=["POST"])
def calculate_exit_time():
    data = request.json
    user_id = data.get("user_id")
    check_ins = data.get("check_ins")  # List of check-ins
    check_outs = data.get("check_outs")  # List of check-outs

    if not user_id or not check_ins or not check_outs:
        return jsonify({"error": "Invalid input"}), 400

    exit_time = check_exit_time(check_ins, check_outs)
    return jsonify({"exit_time": exit_time})
