import { useState } from "react";

const CheckInForm = ({ addCheckIn }) => {
  const [checkInTime, setCheckInTime] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    addCheckIn(checkInTime);
    setCheckInTime("");
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="time"
        value={checkInTime}
        onChange={(e) => setCheckInTime(e.target.value)}
        required
      />
      <button type="submit">Add Check-In</button>
    </form>
  );
};

export default CheckInForm;
