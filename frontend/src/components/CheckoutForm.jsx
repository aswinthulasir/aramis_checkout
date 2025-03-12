import { useState } from "react";

const CheckOutForm = ({ addCheckOut }) => {
  const [checkOutTime, setCheckOutTime] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    addCheckOut(checkOutTime);
    setCheckOutTime("");
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="time"
        value={checkOutTime}
        onChange={(e) => setCheckOutTime(e.target.value)}
        required
      />
      <button type="submit">Add Check-Out</button>
    </form>
  );
};

export default CheckOutForm;
