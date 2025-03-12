import { useState } from "react";
import CheckInForm from "../components/CheckinForm";
import CheckOutForm from "../components/CheckoutForm";
import DisplayExitTime from "../components/DisplayExitTime";

const Home = () => {
  const [checkIns, setCheckIns] = useState([]);
  const [checkOuts, setCheckOuts] = useState([]);

  return (
    <div>
      <h1>Exit Time Calculator</h1>
      <CheckInForm addCheckIn={(time) => setCheckIns([...checkIns, time])} />
      <CheckOutForm addCheckOut={(time) => setCheckOuts([...checkOuts, time])} />
      <DisplayExitTime checkIns={checkIns} checkOuts={checkOuts} />
    </div>
  );
};

export default Home;
