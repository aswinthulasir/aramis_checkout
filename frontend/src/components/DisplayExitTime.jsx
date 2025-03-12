import axios from "axios";
import { useState } from "react";

const DisplayExitTime = ({ checkIns, checkOuts }) => {
  const [exitTime, setExitTime] = useState(null);

  const calculateExitTime = async () => {
    try {
      const response = await axios.post("http://localhost:5000/api/time/check", {
        user_id: "12345",
        check_ins: checkIns,
        check_outs: checkOuts,
      });
      setExitTime(response.data.exit_time);
    } catch (error) {
      console.error("Error calculating exit time", error);
    }
  };

  return (
    <div>
      <button onClick={calculateExitTime}>Calculate Exit Time</button>
      {exitTime && <h3>Exit Time: {exitTime}</h3>}
    </div>
  );
};

export default DisplayExitTime;
