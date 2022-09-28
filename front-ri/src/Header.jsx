import React from "react";

const Header = (props) => {
  return (
    <div>
      <button onClick={(e) => props.setmodoAdvanced(false)}>Normal Search</button>
      <button onClick={(e) => props.setmodoAdvanced(true)}>Advanced Search</button>
    </div>
  );
};

export default Header;
